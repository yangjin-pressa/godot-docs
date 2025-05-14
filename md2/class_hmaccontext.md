# HMACContext

**Inherits:** RefCounted < Object

## Description
Used to create an HMAC for a message using a key. Supports streaming messages for advanced use cases.

## Methods

### finish()
**Return:** PackedByteArray  
**Description:** Returns the resulting HMAC. Returns empty buffer if HMAC failed.

### start(hash_type: HashType, key: PackedByteArray)
**Return:** Error  
**Description:** Initializes the HMACContext. Cannot be called again until finish() is called.

### update(data: PackedByteArray)
**Return:** Error  
**Description:** Updates the message to be HMACed. Can be called multiple times before finish(), but requires start() to be called first.

## Example (GDScript)
```gdscript
extends Node
var ctx = HMACContext.new()

func _ready():
    var key = "supersecret".to_utf8_buffer()
    var err = ctx.start(HashingContext.HASH_SHA256, key)
    assert(err == OK)
    var msg1 = "this is ".to_utf8_buffer()
    var msg2 = "super duper secret".to_utf8_buffer()
    err = ctx.update(msg1)
    assert(err == OK)
    err = ctx.update(msg2)
    assert(err == OK)
    var hmac = ctx.finish()
    print(hmac.hex_encode())
```

## Example (CSharp)
```csharp
using Godot;
using System.Diagnostics;

public partial class MyNode : Node
{
    private HmacContext _ctx = new HmacContext();

    public override void _Ready()
    {
        byte[] key = "supersecret".ToUtf8Buffer();
        Error err = _ctx.Start(HashingContext.HashType.Sha256, key);
        Debug.Assert(err == Error.Ok);
        byte[] msg1 = "this is ".ToUtf8Buffer();
        byte[] msg2 = "super duper secret".ToUtf8Buffer();
        err = _ctx.Update(msg1);
        Debug.Assert(err == Error.Ok);
        err = _ctx.Update(msg2);
        Debug.Assert(err == Error.Ok);
        byte[] hmac = _ctx.Finish();
        GD.Print(hmac.HexEncode());
    }
}
```