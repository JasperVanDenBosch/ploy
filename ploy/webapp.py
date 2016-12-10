from pyramid.config import Configurator
import pyramid_zodbconn
import waitress, os
from ploy.root import Root


def root_factory(request):
    conn = pyramid_zodbconn.get_connection(request)
    database = conn.root()
    if 'root' not in database:
        database['root'] = Root()
        import transaction
        transaction.commit()
    return database['root']

def serve():
    wsgiapp = main(None)
    waitress.serve(wsgiapp, host='0.0.0.0', port=6543)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings['tm.attempts'] = 3
    settings['zodbconn.uri'] = 'file://Data.fs'
    config = Configurator(root_factory=root_factory, settings=settings)
    config.include('pyramid_mako')
    config.include('pyramid_tm')
    config.include('pyramid_zodbconn')

    config.add_static_view('static', 'static', cache_max_age=10)
    #config.add_route('home', '/')
    #config.add_route('github', '/github')
    config.scan()
    return config.make_wsgi_app()
