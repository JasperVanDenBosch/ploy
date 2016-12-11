from pyramid.view import view_config
from ploy.root import Root
import persistent.list


@view_config(context=Root, renderer='templates/root.mako')
def get_root(request):
    return {}

@view_config(context=persistent.list.PersistentList, request_method='GET',
             renderer='templates/github_events.mako')
def get_github_events(request):
    return {'events':request.context}

@view_config(context=persistent.list.PersistentList, request_method='POST',
             renderer='templates/github_events.mako')
def post_github_events(request):
    event = request.headers.get('X-GitHub-Event')
    ts = request.dependencies.getClock().now()
    message = {'event':event, 'payload': request.json_body, 'received':ts}
    request.context.append(message)
    request.response.body = 'Received by Ploy.'
    return request.response