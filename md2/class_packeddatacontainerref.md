# PackedDataContainerRef

**Deprecated:** Use `@GlobalScope.var_to_bytes` or `FileAccess.store_var` instead. To enable data compression, use `PackedByteArray.compress` or `FileAccess.open_compressed`.

**Inherits:** `RefCounted` < `Object`

## Description
Used by `PackedDataContainer` to pack nested arrays and dictionaries. Data can be retrieved like from `PackedDataContainer`.

```gdscript
var packed = PackedDataContainer.new()
packed.pack([1, 2, 3, ["nested1", "nested2"], 4, 5, 6])

for element in packed:
    if element is PackedDataContainerRef:
        for subelement in element:
            print("::", subelement)
    else:
        print(element)
```

**Output:**
```
1
2
3
::nested1
::nested2
4
5
6
```

## Methods
- **size**: Returns the size of the packed container (see `Array.size` and `Dictionary.size`).  
  **Type**: `int`  
  **Flags**: `const` (no side effects, no instance modification)

## Notes
- This class is internal and used for packing nested structures in `PackedDataContainer`.  
- For compressed data, use `PackedByteArray.compress` or `FileAccess.open_compressed`.