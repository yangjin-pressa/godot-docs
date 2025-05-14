**GLTFPhysicsShape**  
A class representing physics shapes from glTF extensions, acting as an intermediary between glTF data and Godot nodes.  

---

### **Description**  
- **Purpose**: Represents physics shapes defined in glTF files (e.g., boxes, capsules) and converts them into Godot's `CollisionShape3D` or `Shape3D` formats.  
- **Key Features**:  
  - Supports shape types like `box`, `capsule`, `sphere`, `hull`, and `trimesh`.  
  - Converts between glTF format and Godot's physics data.  

---

### **Tutorials**  
- [OMI_physics_shape documentation](https://example.com/omi_physics_shape)  
- [OMI_physics_shape GitHub repo](https://github.com/example/omi_physics_shape)  

---

### **Properties**  
| Name         | Type       | Default       | Description                                                                 |
|--------------|------------|---------------|-----------------------------------------------------------------------------|
| `shape_type` | `String`   | `""`          | Type of shape (e.g., `"box"`, `"capsule"`). Valid values: `"box"`, `"capsule"`, `"cylinder"`, `"sphere"`, `"hull"`, `"trimesh"`. |
| `size`       | `Vector3`  | `Vector3(1, 1, 1)` | Dimensions for box shapes. Must be non-negative.                         |
| `height`     | `float`    | `2.0`         | Height for capsule/cylinder shapes. Must be positive.                    |
| `width`      | `float`    | `1.0`         | Width for cylinder shapes.                                                |
| `radius`     | `float`    | `1.0`         | Radius for sphere/capsule shapes. Must be positive.                      |

---

### **Methods**  
1. **`from_dictionary(dictionary: Dictionary)`**  
   - **Static**  
   - **Description**: Creates a `GLTFPhysicsShape` instance from a `Dictionary` containing shape data.  

2. **`from_node(shape_node: CollisionShape3D)`**  
   - **Static**  
   - **Description**: Converts a Godot `CollisionShape3D` node into a `GLTFPhysicsShape` instance.  

3. **`from_resource(shape_resource: Shape3D)`**  
   - **Static**  
   - **Description**: Converts a Godot `Shape3D` resource into a `GLTFPhysicsShape` instance.  

4. **`to_dictionary()`**  
   - **Const**  
   - **Description**: Serializes the shape into a `Dictionary` in the `OMI_physics_shape` format.  

5. **`to_node(cache_shapes: bool = false)`**  
   - **Description**: Converts the shape into a Godot `CollisionShape3D` node.  
   - **Parameter**: `cache_shapes` (default: `false`) – whether to reuse cached shapes.  

6. **`to_resource(cache_shapes: bool = false)`**  
   - **Description**: Converts the shape into a Godot `Shape3D` resource.  
   - **Parameter**: `cache_shapes` (default: `false`) – whether to reuse cached shapes.  

---

### **Key Notes**  
- **Shape Type Specifics**:  
  - `box`: Uses `size` for dimensions.  
  - `capsule`: Uses `height` and `radius`.  
  - `cylinder`: Uses `height` and `radius`.  
  - `sphere`: Uses `radius`.  
- **Validation**: All numeric properties (e.g., `size`, `height`, `radius`) must be non-negative.  
- **Caching**: Methods like `to_node()` and `to_resource()` allow an optional `cache_shapes` parameter for performance optimization.