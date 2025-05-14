# PackedDataContainer

**Deprecated:** Use `@GlobalScope.var_to_bytes` or `FileAccess.store_var` instead. For compression, use `PackedByteArray.compress` or `FileAccess.open_compressed`.

**Inherits:** `Resource` → `RefCounted` → `Object`

Efficiently packs and serializes `Array` or `Dictionary`. Only `Array` and `Dictionary` can be stored this way.

---

## Description

PackedDataContainer can store data from untyped containers. It converts the data into raw bytes for file storage. Nested containers are packed recursively. Iterating the container returns `PackedDataContainerRef` objects.

Example:
```gdscript
var data = { "key": "value", "another_key": 123, "lock": Vector2() }
var packed = PackedDataContainer.new()
packed.pack(data)
ResourceSaver.save(packed, "packed_data.res")

var container = load("packed_data.res")
for key in container:
    print(key, container[key])
```

Output:
```
key value
lock (0, 0)
another_key 123
```

---

## Methods

- **pack(value: Variant): Error**  
  Packs the given container into binary. `value` must be `Array` or `Dictionary`. Subsequent calls overwrite data.

- **size(): int**  
  Returns the size of the packed container (see `Array.size` and `Dictionary.size`).

---

## Notes

- Nested containers are packed recursively.
- Iterating returns `PackedDataContainerRef` objects.
- `pack()` overwrites data on subsequent calls.