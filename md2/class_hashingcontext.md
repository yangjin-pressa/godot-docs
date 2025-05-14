**HashingContext**  
*Inherits:* `RefCounted` < `Object`  

---

### **Description**  
Provides functionality for computing cryptographic hashes in chunks.  
- Ideal for large files, network streams, or data streams.  
- Supports hash algorithms via the `HashType` enum.  

---

### **HashType Enum**  
Defines supported hashing algorithms:  
- **HASH_MD5** = 0  
  - Hashing algorithm: MD5.  
- **HASH_SHA1** = 1  
  - Hashing algorithm: SHA-1.  
- **HASH_SHA256** = 2  
  - Hashing algorithm: SHA-256.  

---

### **Methods**  
- **finish()**  
  - Returns: `PackedByteArray`  
  - Closes the context and returns the computed hash.  

- **start(type: HashType)**  
  - Returns: `Error`  
  - Initiates a new hash computation with the specified algorithm.  

- **update(chunk: PackedByteArray)**  
  - Returns: `Error`  
  - Updates the hash computation with the provided data chunk.  

---

### **Example Usage**  
#### GDScript  
```gdscript
const CHUNK_SIZE = 1024

func hash_file(path):
    if not FileAccess.file_exists(path):
        return
    var ctx = HashingContext.new()
    ctx.start(HashingContext.HASH_SHA256)
    var file = FileAccess.open(path, FileAccess.READ)
    while file.get_position() < file.get_length():
        var remaining = file.get_length() - file.get_position()
        ctx.update(file.get_buffer(min(remaining, CHUNK_SIZE)))
    var res = ctx.finish()
    print(res.hex_encode(), Array(res))
```

#### C#  
```csharp
public const int ChunkSize = 1024;

public void HashFile(string path)
{
    if (!FileAccess.FileExists(path))
        return;
    var ctx = new HashingContext();
    ctx.Start(HashingContext.HashType.Sha256);
    using var file = FileAccess.Open(path, FileAccess.ModeFlags.Read);
    while (file.GetPosition() < file.GetLength())
    {
        int remaining = (int)(file.GetLength() - file.GetPosition());
        ctx.Update(file.GetBuffer(Mathf.Min(remaining, ChunkSize)));
    }
    byte[] res = ctx.Finish();
    GD.PrintT(res.HexEncode(), (Variant)res);
}
```

---

### **Notes**  
- Generated from Godot engine sources.  
- Code examples demonstrate how to hash files incrementally.  
- `HashingContext` is designed for efficient memory usage in stream processing.