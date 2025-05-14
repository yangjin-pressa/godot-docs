# AESContext

**Inherits**: RefCounted < Object

Provides access to AES encryption/decryption of raw data. Supports AES-ECB and AES-CBC modes.

## Usage Example

### GDScript
```gdscript
extends Node

var aes = AESContext.new()

func _ready():
    var key = "My secret key!!!" # 16 or 32 byte key
    var data = "My secret text!!" # 16 byte multiple
    var iv = "My secret iv!!!!" # 16 byte IV

    # ECB Encryption
    aes.start(AESContext.MODE_ECB_ENCRYPT, key.to_utf8_buffer())
    var encrypted = aes.update(data.to_utf8_buffer())
    aes.finish()

    # ECB Decryption
    aes.start(AESContext.MODE_ECB_DECRYPT, key.to_utf8_buffer())
    var decrypted = aes.update(encrypted)
    aes.finish()
    assert(decrypted == data.to_utf8_buffer())

    # CBC Encryption
    aes.start(AESContext.MODE_CBC_ENCRYPT, key.to_utf8_buffer(), iv.to_utf8_buffer())
    encrypted = aes.update(data.to_utf8_buffer())
    aes.finish()

    # CBC Decryption
    aes.start(AESContext.MODE_CBC_DECRYPT, key.to_utf8_buffer(), iv.to_utf8_buffer())
    decrypted = aes.update(encrypted)
    aes.finish()
    assert(decrypted == data.to_utf8_buffer())
```

### C#
```csharp
using Godot;
using System.Diagnostics;

public partial class MyNode : Node
{
    private AesContext _aes = new AesContext();

    public override void _Ready()
    {
        string key = "My secret key!!!"; // 16 or 32 byte key
        string data = "My secret text!!"; // 16 byte multiple
        string iv = "My secret iv!!!!"; // 16 byte IV

        // ECB Encryption
        _aes.Start(AesContext.Mode.EcbEncrypt, key.ToUtf8Buffer());
        byte[] encrypted = _aes.Update(data.ToUtf8Buffer());
        _aes.Finish();

        // ECB Decryption
        _aes.Start(AesContext.Mode.EcbDecrypt, key.ToUtf8Buffer());
        byte[] decrypted = _aes.Update(encrypted);
        _aes.Finish();
        Debug.Assert(decrypted == data.ToUtf8Buffer());

        // CBC Encryption
        _aes.Start(AesContext.Mode.EcbEncrypt, key.ToUtf8Buffer(), iv.ToUtf8Buffer());
        encrypted = _aes.Update(data.ToUtf8Buffer());
        _aes.Finish();

        // CBC Decryption
        _aes.Start(AesContext.Mode.EcbDecrypt, key.ToUtf8Buffer(), iv.ToUtf8Buffer());
        decrypted = _aes.Update(encrypted);
        _aes.Finish();
        Debug.Assert(decrypted == data.ToUtf8Buffer());
    }
}
```

## Methods

- **finish()**: Finalizes the AES context operation. Must be called after update().
- **get_iv_state()**: Returns current IV state (only valid for CBC modes).
- **start(mode, key, iv)**: Initializes AES context with mode, key, and optional IV.
- **update(src)**: Processes data for encryption/decryption. Input must be 16-byte multiple.

## Mode Constants

- **MODE_ECB_ENCRYPT**: AES electronic codebook encryption
- **MODE_ECB_DECRYPT**: AES electronic codebook decryption
- **MODE_CBC_ENCRYPT**: AES cipher block chaining encryption
- **MODE_CBC_DECRYPT**: AES cipher block chaining decryption
- **MODE_MAX**: Maximum mode value (4)

## Key Requirements

- Key must be 16 or 32 bytes
- Data must be 16-byte multiple (padding required if needed)
- IV required only for CBC modes (must be exactly 16 bytes)