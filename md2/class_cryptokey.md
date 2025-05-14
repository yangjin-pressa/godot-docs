**Class: CryptoKey**  
**Inherits:** Resource → RefCounted → Object  

---

### **Description**  
Represents a cryptographic key (RSA or elliptic-curve).  
- Loaded/saved like any Resource.  
- Used to generate self-signed X509Certificate via `Crypto.generate_self_signed_certificate()`  
- Used as private key in `StreamPeerTLS.accept_stream()` with appropriate certificate.  

---

### **Tutorials**  
- [SSL certificates](../tutorials/networking/ssl_certificates).  

---

### **Methods**  

1. **is_public_only()**  
   - **Return:** bool  
   - **Description:** Returns true if the key only contains the public part.  

2. **load(path: String, public_only: bool = false)**  
   - **Return:** Error  
   - **Description:** Loads a key from `path`.  
   - **Note:** Use `.pub` for public_only, `.key` otherwise.  

3. **load_from_string(string_key: String, public_only: bool = false)**  
   - **Return:** Error  
   - **Description:** Loads a key from a string.  
   - **Note:** Use public_only to load only public key.  

4. **save(path: String, public_only: bool = false)**  
   - **Return:** Error  
   - **Description:** Saves a key to `path`.  
   - **Note:** Use `.pub` for public_only, `.key` otherwise.  

5. **save_to_string(public_only: bool = false)**  
   - **Return:** String  
   - **Description:** Returns key in PEM format.  
   - **Note:** Use public_only to include only public key.  

---

### **Key Notes**  
- All methods accept `public_only` parameter to control key type.  
- File extensions for loading/saving: `.pub` for public, `.key` for private.  
- `save_to_string()` returns PEM-formatted data.