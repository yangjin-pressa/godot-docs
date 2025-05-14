# Crypto Class

## Description
Provides access to advanced cryptographic functionalities including:
- Asymmetric key encryption/decryption
- Signing/verification
- Generating cryptographically secure random bytes
- RSA key generation
- HMAC digests
- Self-signed X509 certificates

## Methods

### constant_time_compare
**Returns**: bool  
**Parameters**: 
- trusted: PackedByteArray
- received: PackedByteArray  
Compares two byte arrays for equality without leaking timing information to prevent timing attacks.

### decrypt
**Returns**: PackedByteArray  
**Parameters**: 
- key: CryptoKey
- ciphertext: PackedByteArray  
Decrypts data using a private RSA key.

### encrypt
**Returns**: PackedByteArray  
**Parameters**: 
- key: CryptoKey
- plaintext: PackedByteArray  
Encrypts data using a public RSA key.

### generate_random_bytes
**Returns**: PackedByteArray  
**Parameters**: 
- size: int  
Generates cryptographically secure random bytes of specified size.

### generate_rsa
**Returns**: CryptoKey  
**Parameters**: 
- size: int  
Creates an RSA key pair for certificate generation and TLS connections.

### generate_self_signed_certificate
**Returns**: X509Certificate  
**Parameters**: 
- key: CryptoKey
- issuer_name: String (default: "CN=myserver,O=myorganisation,C=IT")
- not_before: String (default: "20140101000000")
- not_after: String (default: "20340101000000")
Creates a self-signed certificate with specified validity period and issuer details.

### hmac_digest
**Returns**: PackedByteArray  
**Parameters**: 
- hash_type: HashType
- key: PackedByteArray
- msg: PackedByteArray  
Generates HMAC digest using specified hash algorithm.

### sign
**Returns**: PackedByteArray  
**Parameters**: 
- hash_type: HashType
- hash: PackedByteArray
- key: CryptoKey  
Signs a cryptographic hash with a private key.

### verify
**Returns**: bool  
**Parameters**: 
- hash_type: HashType
- hash: PackedByteArray
- signature: PackedByteArray
- key: CryptoKey  
Validates a digital signature against a public key.

## Example Usage
```gdscript
var crypto = Crypto.new()
var key = crypto.generate_rsa(4096)
var cert = crypto.generate_self_signed_certificate(key, "CN=example.com,O=A Game Company,C=IT")
```

```csharp
var crypto = new Crypto();
CryptoKey key = crypto.GenerateRsa(4096);
X509Certificate cert = crypto.GenerateSelfSignedCertificate(key, "CN=mydomain.com,O=My Game Company,C=IT");
```

**Note**: This class provides foundational cryptographic operations for secure communications and data integrity.