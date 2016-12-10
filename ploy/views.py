from pyramid.view import view_config
from ploy.root import Root


@view_config(context=Root, renderer='templates/root.mako')
def get_root(request):
    return {}

# @view_config(context=GithubEvents)
# def github(request):
#     request.response.body = 'Received by Ploy.'
#     return request.response