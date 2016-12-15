from ploy.dependencies import Dependencies
from pyramid.config import Configurator
import pyramid_zodbconn
import waitress, os
from ploy.root import Root
import threading
import time
from pyramid.scripting import get_root

def worker(app=None):
    """thread worker function"""
    while True:
        print('Worker alive.')
        (root, closer) = get_root(app)
        import transaction
        updatedJobs = []
        noJobsHandledYet = True
        for job in root.jobs:
            if job.status == 'queued' and noJobsHandledYet:
                job.status = 'handled'
                noJobsHandledYet = False
                print('Handled job.')
            updatedJobs.append(job)
        root.jobs._inner = updatedJobs
        closer()
        transaction.commit()
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

def serve():
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
