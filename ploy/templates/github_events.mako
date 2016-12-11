<%inherit file="master.mako"/>


<h2>Github events</h2>

<ul class="messages">
    % for event in events:
        <li>
            <dl>
            <dt>event</dt>
                <dd>${event['event']}</dd>
            <dt>to</dt>
                <dd>${event['payload'].get('repository', {}).get('full_name')}</dd>
            <dt>when</dt>
                <dd class="datetime">${event['received']}</dd>
            <dt>by</dt>
                <dd>${event['payload'].get('pusher', {}).get('name')}</dd>
            </dl>
        </li>
    % endfor
</ul>
