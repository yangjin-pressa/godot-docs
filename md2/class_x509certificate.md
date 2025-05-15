**X509Certificate**  
- **Inherits**: Resource → RefCounted → Object  
- **Description**: Represents an X509 certificate. Can be loaded and saved like other resources. Used for TLS server certificates and for accepting certificates in `StreamPeerTLS.accept_stream()` and `connect_to_stream()`.  

**Tutorials**  
- [SSL certificates](../tutorials/networking/ssl_certificates)  

**Methods**  
1. **load(path: String)**  
   - Loads a certificate from `path` (e.g., "*.crt" file).  

2. **load_from_string(string: String)**  
   - Loads a certificate from the given string.  

3. **save(path: String)**  
   - Saves the certificate to `path` (should be a "*.crt" file).  

4. **save_to_string()**  
   - Returns a string representation of the certificate or an empty string if invalid.  

**Method Descriptions**  
- **virtual (This method should typically be overridden)**:  
  - This method is marked as virtual, indicating it may be overridden in derived classes.  

- **virtual (This method should typically be overridden)**:  
  - Similar to the above, this method is virtual and may be overridden.  

- **virtual (This method should typically be overridden)**:  
  - Again, this method is virtual and may be overridden.  

- **virtual (This method should typically be overridden)**:  
  - This method is virtual and may be overridden, though its implementation is not detailed in the provided documentation.