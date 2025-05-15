# TLSOptions

**Inherits**: RefCounted < Object

TLS configuration for clients and servers.

## Description
TLSOptions abstracts the configuration options for StreamPeerTLS and PacketPeerDTLS.

Objects of this class cannot be instantiated directly. Use static methods client(), client_unsafe(), or server() instead.

## Methods

### client(trusted_chain: X509Certificate = null, common_name_override: String = "")
- **Returns**: TLSOptions
- **Note**: On Web platform, TLS verification is enforced against browser CA list.

### client_unsafe(trusted_chain: X509Certificate = null)
- **Returns**: TLSOptions
- **Note**: On Web platform, TLS verification is enforced against browser CA list.

### get_common_name_override()
- **Returns**: String
- **Description**: Common name override specified when creating with client()

### get_own_certificate()
- **Returns**: X509Certificate
- **Description**: Certificate specified when creating with server()

### get_private_key()
- **Returns**: CryptoKey
- **Description**: Private key specified when creating with server()

### get_trusted_ca_chain()
- **Returns**: X509Certificate
- **Description**: CA chain specified when creating with client() or client_unsafe()

### is_server()
- **Returns**: bool
- **Description**: True if created with server(), false otherwise.

### is_unsafe_client()
- **Returns**: bool
- **Description**: True if created with client_unsafe(), false otherwise.

### server(key: CryptoKey, certificate: X509Certificate)
- **Returns**: TLSOptions
- **Note**: Certificate should include full chain up to signing CA.

## Example Code
```gdscript
# Create TLS client configuration
var client_trusted_cas = load("res://my_trusted_cas.crt")
var client_tls_options = TLSOptions.client(client_trusted_cas)

# Create TLS server configuration
var server_certs = load("res://my_server_cas.crt")
var server_key = load("res://my_server_key.key")
var server_tls_options = TLSOptions.server(server_key, server_certs)
```