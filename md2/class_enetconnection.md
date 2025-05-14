Here's a step-by-step example of using the `ENetConnection` class in Godot to create a server and client with DTLS encryption:

```gdscript
# Example: ENet Server and Client with DTLS Encryption

# Server Setup
func setup_server():
    # Create server host bound to 0.0.0.0:12345
    var server_host = ENetConnection.create_host_bound("0.0.0.0", 12345, 32, 0, 0, 0)
    
    # Setup DTLS server with custom options
    var server_options = TLSOptions.new()
    server_options.server = true  # Enable server mode
    server_options.trusted_cas = ["CA_CERTIFICATE.pem"]  # Trusted CA certificates
    
    var dtls_error = server_host.dtls_server_setup(server_options)
    if dtls_error != OK:
        print("Failed to setup DTLS server: ", dtls_error)
        return
    
    # Main loop for server
    while true:
        var events = server_host.service(1000)  # Wait for 1 second
        if events.size() > 0:
            var event_type = events[0]
            if event_type == ENetConnection.EVENT_TYPE_CONNECT:
                print("Client connected!")
            elif event_type == ENetConnection.EVENT_TYPE_DISCONNECT:
                print("Client disconnected.")
            # Handle other events as needed
```

```gdscript
# Client Setup
func setup_client():
    # Create client host
    var client_host = ENetConnection.create_host()
    
    # Setup DTLS client with custom options
    var client_options = TLSOptions.new()
    client_options.client = true  # Enable client mode
    client_options.client_unsafe = true  # Disable common name verification
    
    var dtls_error = client_host.dtls_client_setup("example.com", client_options)
    if dtls_error != OK:
        print("Failed to setup DTLS client: ", dtls_error)
        return
    
    # Connect to server
    var connect_error = client_host.connect_to_host("127.0.0.1", 12345)
    if connect_error != OK:
        print("Failed to connect to server: ", connect_error)
        return
    
    # Main loop for client
    while true:
        var events = client_host.service(1000)  # Wait for 1 second
        if events.size() > 0:
            var event_type = events[0]
            if event_type == ENetConnection.EVENT_TYPE_RECEIVE:
                var packet = events[1]
                print("Received data: ", packet.get_data())
            # Handle other events as needed
```

Key points:

1. Server creation:
- Use `create_host_bound()` to bind to a specific IP and port
- Call `dtls_server_setup()` to enable DTLS with custom options
- The server must call `service()` regularly to process events

2. Client creation:
- Use `create_host()` for default host creation
- Call `dtls_client_setup()` to configure DTLS client with:
  - Server hostname for certificate validation
  - Custom TLS options (trusted CAs, unsafe settings)
- Use `connect_to_host()` to connect to the server

3. DTLS Configuration:
- Server: Must call `dtls_server_setup()` after creating the host
- Client: Must call `dtls_client_setup()` before connecting
- Both need to use the same hostname for certificate validation

4. Event Handling:
- Call `service()` regularly (with a timeout) on both ends
- Handle:
  - CONNECT/_DISCONNECT events
  - RECEIVE events for data transmission
  - The returned array has 4 elements: event type, peer, data, channel

5. Network Communication:
- Server and client must use the same port number
- The server must be bound to the correct IP address
- The client must know the server's public IP and port

This example demonstrates a basic DTLS-enabled network communication setup. For production use, you would need to:
- Handle more complex event handling
- Implement proper data serialization
- Add error handling for network failures
- Securely manage certificates and key files