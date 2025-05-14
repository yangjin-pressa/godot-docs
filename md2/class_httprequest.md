The `HttpRequest` class in Godot manages HTTP requests, offering properties for configuration, methods to execute requests, and utility functions for tracking request status. Key features include:

### **Properties**
- **use_threads**: Enables multithreading for improved performance.
- **timeout**: Sets the time (in seconds) before a request times out. A value of `0.0` disables timeouts.
- **http_proxy** and **https_proxy**: Define proxy servers for HTTP/HTTPS requests. Proxies are unset if host/port are empty or -1.
- **tls_options**: Configures TLS settings for HTTPS connections.

### **Methods**
- **request(url, method, headers, data)**: Sends an HTTP request. Supports GET/POST methods. Returns an error code if the request fails.
- **request_raw(url, method, headers, raw_data)**: Sends raw binary data (as a byte array) as the request body.
- **cancel_request()**: Cancels the current active request.
- **get_body_size()**: Returns the size of the response body (or -1 if unknown).
- **get_downloaded_bytes()**: Returns the number of bytes downloaded so far.
- **get_http_client_status()**: Returns the status of the underlying HTTP client (e.g., connected, disconnected).

### **Important Notes**
- **Security**: Always use HTTPS for sensitive data. Avoid sending credentials via GET requests.
- **Proxy Handling**: Set `http_proxy` for HTTP and `https_proxy` for HTTPS. Proxies are disabled if host/port are invalid.
- **Method Considerations**: 
  - **GET** should not include sensitive data; use query strings or headers instead.
  - **POST** is better for sending data, especially with binary payloads.
- **Timeouts**: Disable timeouts (`timeout = 0.0`) for large downloads to prevent premature failures.
- **Body Length**: Some servers may not provide body size; `get_body_size()` returns -1 in such cases.

This class provides flexibility for handling HTTP/HTTPS requests, including proxy support, threading, and raw data handling. Always validate URLs and handle errors appropriately.