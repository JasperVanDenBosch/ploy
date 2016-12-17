<%inherit file="master.mako"/>


<h2>Builds</h2>

<ul class="messages">
    % for build in builds:
        <li>
            <dl>
            <dt>id</dt>
                <dd><a href="${request.resource_url(build)}">${build.id}</a></dd>
            <dt>status</dt>
                <dd>${build.status}</dd>
            <dt>queued</dt>
                <dd class="datetime">${build.created}</dd>
            </dl>
        </li>
    % endfor
</ul>
