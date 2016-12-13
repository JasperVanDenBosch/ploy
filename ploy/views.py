from pyramid.view import view_config
from ploy.root import Root
from ploy.githubevents import GithubEvents
from ploy.jobs import Jobs
from ploy.job import Job


@view_config(context=Root, renderer='templates/root.mako')
def get_root(request):
    return {}


@view_config(context=GithubEvents, request_method='GET',
             renderer='templates/github_events.mako')
def get_github_events(request):
    return {'events':request.context}


@view_config(context=GithubEvents, request_method='POST',
             renderer='templates/github_events.mako')
def post_github_events(request):
    event = request.headers.get('X-GitHub-Event')
    ts = request.dependencies.getClock().now()
    message = {'event':event, 'payload': request.json_body, 'received':ts}
    request.context.append(message)
    newJob = Job()
    newJob.status = 'queued'
    newJob.queued = ts
    request.root.jobs.append(newJob)
    request.response.body = 'Received by Ploy.'
    return request.response


@view_config(context=Jobs, request_method='GET',
             renderer='templates/jobs.mako')
def get_jobs(request):
    return {'jobs': request.context}