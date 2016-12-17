<%inherit file="master.mako"/>


<h2>Build</h2>

<dl>
<dt>id</dt>
    <dd><a href="${request.resource_url(build)}">${build.id}</a></dd>
<dt>status</dt>
    <dd>${build.status}</dd>
<dt>queued</dt>
    <dd class="datetime">${build.created}</dd>
</dl>