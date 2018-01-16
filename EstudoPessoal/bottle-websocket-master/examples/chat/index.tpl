<!doctype html>
<head>
    <meta charset="utf-8" />
    <title>WebSocket Chat</title>

    <style>
        li { list-style: none; }
    </style>

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js"></script>
    <script>
        $(document).ready(function() {
            if (!window.WebSocket) {
                if (window.MozWebSocket) {
                    window.WebSocket = window.MozWebSocket;
                } else {
                    $('#messages').append("<li>Your browser doesn't support WebSockets.</li>");
                }
            }
            ws = new WebSocket('ws://127.0.0.1:8080/websocket');
            ws.onopen = function(evt) {
                $('#messages').append('<li>Connected to chat.</li>');
            }
            ws.onmessage = function(evt) {
				if(evt.data.equals("$#please close")){
					ws.close()
				}
				else{
					$('#messages').append('<li>' + evt.data + '</li>');
				}
            }
            $('#send-message').submit(function() {
                ws.send($('#name').val() + ": " + $('#message').val());
                $('#message').val('').focus();
                return false;
            });
        });
    </script>
</head>
<body>
    <h2>WebSocket Chat Example</h2>
    <form id="send-message">
        <input id="name" type="text" value="name">
        <input id="message" type="text" value="message" />
        <input type="submit" value="Send" />
    </form>
    <div id="messages"></div>
</body>
</html>
