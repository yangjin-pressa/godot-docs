# GLTFObjectModelProperty Class Documentation

## Overview
The `GLTFObjectModelProperty` class is used to define how a Godot property maps to a glTF object model property. It handles the conversion between Godot's property structure and the glTF format, with support for JSON pointers, node paths, and variant types.

---

## Properties

### `object_model_type` (enum `GLTFObjectModelType`)
The type of data stored in the glTF file as defined by the object model. This determines the accessor type and maps to the `GLTFObjectModelType` enum.

**Methods:**
- `get_object_model_type()`: Returns the current object model type.
- `set_object_model_type(value: GLTFObjectModelType)`: Sets the object model type.

**Example:**
```gdscript
var prop = GLTFObjectModelProperty.new()
prop.set_object_model_type(GLTFObjectModelType.VEC3)
```

---

### `variant_type` (enum `Variant.Type`)
The type of data stored in the Godot property. This is the type of the property that the `node_paths` point to.

**Methods:**
- `get_variant_type()`: Returns the current variant type.
- `set_variant_type(value: Variant.Type)`: Sets the variant type.

**Example:**
```gdscript
var prop = GLTFObjectModelProperty.new()
prop.set_variant_type(Variant.Type.FLOAT)
```

---

### `node_paths` (array of `NodePath`)
An array of `NodePath` objects that point to a property or multiple properties in the Godot scene tree. Used during import to map glTF properties to Godot nodes.

**Methods:**
- `get_node_paths()`: Returns the current node paths.
- `set_node_paths(value: Array[NodePath])`: Sets the node paths.
- `append_node_path(node_path: NodePath)`: Appends a node path to the array.

**Example:**
```gdscript
var prop = GLTFObjectModelProperty.new()
prop.append_node_path("Root/Scene/Node")
```

---

### `json_pointers` (array of `Array[PackedStringArray]`)
The glTF object model JSON pointers used to identify the property in the glTF object model. Each item is an array representing the JSON pointer split into components.

**Methods:**
- `get_json_pointers()`: Returns the current JSON pointers.
- `set_json_pointers(value: Array[Array[PackedStringArray]])`: Sets the JSON pointers.

**Example:**
```gdscript
var prop = GLTFObjectModelProperty.new()
prop.set_json_pointers([["/scene", "/nodes/0/mesh"]])
```

---

## Methods

### `append_path_to_property(node_path: NodePath, prop_name: StringName)`
A high-level wrapper that constructs a new `NodePath` using `node_path` as a base and appends `prop_name` to the subpath. Used for simple cases.

**Example:**
```gdscript
var prop = GLTFObjectModelProperty.new()
prop.append_path_to_property("Root/Scene", "position")
```

---

### `set_types(variant_type: Variant.Type, obj_model_type: GLTFObjectModelType)`
Sets both `variant_type` and `object_model_type` at once. This method should be called once, as calling it again with the same values has no effect.

**Example:**
```gdscript
var prop = GLTFObjectModelProperty.new()
prop.set_types(Variant.Type.FLOAT, GLTFObjectModelType.FLOAT)
```

---

### `get_accessor_type() const -> GLTFAccessorType`
Returns the GLTF accessor type associated with the `object_model_type`. This maps the object model type to the corresponding accessor type.

**Example:**
```gdscript
var accessor_type = prop.get_accessor_type()  # Returns GLTFAccessorType.VEC3
```

---

## Enums

### `GLTFObjectModelType`
Defines the type of data stored in the glTF file. Possible values include `VEC3`, `FLOAT`, `VECTOR`, etc.

**Example:**
```gdscript
var type = GLTFObjectModelType.VEC3
```

### `GLTFAccessorType`
Defines the accessor type for the glTF property. Possible values include `VEC3`, `SCALAR`, `VEC4`, etc.

**Example:**
```gdscript
var accessor_type = GLTFAccessorType.VEC3
```

---

## Notes

1. **Import/Export Handling:**
   - `has_json_pointers()` returns `true` if `json_pointers` is non-empty, used during export to determine if the property can handle converting a Godot property to a glTF object model property.
   - `has_node_paths()` returns `true` if `node_paths` is non-empty, used during import to determine if the property can handle converting a glTF object model property to a Godot property.

2. **Usage:**
   - Use `append_path_to_property()` for simple cases where a single node path maps to a property.
   - Use `append_node_path()` when multiple properties or complex node hierarchies are involved.

3. **Order of Operations:**
   - Always call `set_types()` once to define the variant and object model types before setting node paths or JSON pointers.

---

## Example Usage

```gdscript
var prop = GLTFObjectModelProperty.new()
prop.set_types(Variant.Type.FLOAT, GLTFObjectModelType.FLOAT)
prop.append_path_to_property("Root/Scene", "position")
prop.set_json_pointers([["/scene/transforms/position"]])
```

This example sets a float property, maps it to a Godot node path, and defines the JSON pointer for glTF export.