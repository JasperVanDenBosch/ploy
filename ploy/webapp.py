from ploy.dependencies import Dependencies
from pyramid.config import Configurator
import pyramid_zodbconn
import waitress, os
from ploy.root import Root
import threading
import time
from pyramid.scripting import get_root
from ploy.process import processBuild

def worker(app=None):
    """thread worker function"""
    while True:
        print('Worker alive.')
        (root, closer) = get_root(app)
        import transaction
        noBuildsHandledYet = True
        for build in root.builds:
            if build.status == 'queued' and noBuildsHandledYet:
                build.status = 'cloning..'
                transaction.get().commit()
                noBuildsHandledYet = False
                print('Handling build.')
                processBuild(build)
                build.status = 'done.'
        closer()
        transaction.get().commit()
        time.sleep(8)


def root_factory(request):
    conn = pyramid_zodbconn.get_connection(request)
    database = conn.root()
    if 'root' not in database:
        root = Root()
        database['root'] = root
        import transaction
        transaction.commit()
    return database['root']

def start():
    wsgiapp = main(None)
    thread = threading.Thread(target=worker, kwargs={'app':wsgiapp})
    thread.daemon = True
    thread.start()
    waitress.serve(wsgiapp, host='0.0.0.0', port=6543)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings['tm.attempts'] = 3
    settings['zodbconn.uri'] = 'file://Data.fs'
    settings['pyramid.reload_templates'] = True
    config = Configurator(root_factory=root_factory, settings=settings)
    config.include('pyramid_mako')
    config.include('pyramid_tm')
    config.include('pyramid_zodbconn')
    config.include('pyramid_debugtoolbar')
    config.add_static_view('static', 'static', cache_max_age=10)
    config.add_request_method(lambda x: Dependencies(), 'dependencies', reify=True)
    config.scan()
    return config.make_wsgi_app()
