<%inherit file="master.mako"/>


<h2>Builds</h2>

<ul class="messages">
    % for build in builds:
        <li>
            <dl>
            <dt>status</dt>
                <dd>${build.status}</dd>
            <dt>queued</dt>
                <dd class="datetime">${build.queued}</dd>
            </dl>
        </li>
    % endfor
</ul>
