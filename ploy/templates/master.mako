<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="continuous deployment">
    <meta name="author" content="Jasper J.F. van den Bosch">
    <link rel="stylesheet" type="text/css" href="${request.static_url('ploy:static/master.css')}">
    <script type="text/javascript" src="${request.static_url('ploy:static/moment.min.js')}"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <title>Ploy</title>
  </head>

  <body>
    <div id="header">
        <h1><a href="/">Ploy</a></h1>
        <ul>
            <li><a href="/github-events/">Github events</a></li>
            <li><a href="/builds/">Builds</a></li>
        </ul>
    </div>

        ${self.body()}

        <script type="text/javascript" src="${request.static_url('ploy:static/ploy.js')}"></script>

  </body>
</html>
