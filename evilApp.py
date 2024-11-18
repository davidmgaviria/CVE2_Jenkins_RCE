from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Define the HTML page with embedded JavaScript
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WebSocket Test</title>
        <script>
            // Set the WebSocket URL and origin
            const url = "ws://localhost:8080/cli/ws";  // Change this to your WebSocket URL
            const originHeader = "http://localhost:8080";  // Change this to the correct origin if needed

            // Create a new WebSocket connection
            const ws = new WebSocket(url);

            // When the WebSocket connection is open, execute this callback
            ws.onopen = function() {
                console.log("Connected");

                const command = new TextEncoder().encode("groovy = < payload.groovy"); // Convert string to byte array (Uint8Array)
                console.log(command);

                // Define the start and end frames
                const start = new Uint8Array([0x00, 0x00, 0x19]);   // last byte needs to match length of command
                const end = new Uint8Array([0x02, 0x00, 0x05, 0x55, 0x54, 0x46, 0x2d, 0x38, 0x01, 0x00, 0x05, 0x65, 0x6e, 0x5f, 0x55, 0x53]);

                // Combine the start, command, and end frames into one frame
                const commandFrame = new Uint8Array(start.length + command.length + end.length);
                commandFrame.set(start);
                commandFrame.set(command, start.length);
                commandFrame.set(end, start.length + command.length);

                // Send the command frame as a binary message
                ws.send(commandFrame);
                console.log("Command sent");

                // Send the start signal (0x03) as a separate binary frame
                ws.send(new Uint8Array([0x03]));
                console.log("Start signal sent");

                // Start listening for responses
                let i = 0;
                ws.onmessage = function(event) {
                    // Decode the response if it's in binary format (assuming UTF-8 encoded text)
                    const decoder = new TextDecoder('utf-8');
                    const decodedMessage = decoder.decode(event.data);
                    
                    // Print the decoded message to the console
                    console.log(`Message ${i}: ${decodedMessage}`);
                    i += 1;
                };

                // Handle connection closure
                ws.onclose = function() {
                    console.log("Connection closed");
                };
            };

            // Handle errors
            ws.onerror = function(error) {
                console.error("WebSocket error:", error);
            };
        </script>
    </head>
    <body>
        <h1>WebSocket Connection Test</h1>
        <p>Open your browser's console to see WebSocket interactions.</p>
    </body>
    </html>
    """
    
    # Render the HTML content as the response
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
