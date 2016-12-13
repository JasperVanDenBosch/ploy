<%inherit file="master.mako"/>


<h2>Jobs</h2>

<ul class="messages">
    % for job in jobs:
        <li>
            <dl>
            <dt>status</dt>
                <dd>${job.status}</dd>
            <dt>queued</dt>
                <dd class="datetime">${job.queued}</dd>
            </dl>
        </li>
    % endfor
</ul>
