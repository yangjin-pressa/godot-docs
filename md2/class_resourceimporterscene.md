The `ResourceImporterScene` class in Godot controls how 3D scenes are imported and processed. Below is a structured explanation of its key properties and their functions:

---

### **1. Node Configuration**
- **`nodes/import_as_skeleton_bones`** (`false`)  
  Treats all nodes in the imported scene as bones in a single `Skeleton3D`. Useful for ensuring animations target skeleton bones instead of nodes. May also assign a `"Root"` bone in a `BoneMap`.

- **`nodes/root_name`** (`""`)  
  Overrides the root node's name. If empty, it uses the scene’s default or the file name if unspecified.

- **`nodes/root_type`** (`""`)  
  Overrides the root node’s type. If empty, it defaults to `Node3D`. Using a type inheriting from `Node3D` is recommended to retain editor positioning capabilities.

- **`nodes/apply_root_scale`** (`true`)  
  Determines how the `root_scale` is applied. If `true`, the scale is applied to all descendant nodes. If `false`, it scales the root node directly.

- **`nodes/root_scale`** (`1.0`)  
  Uniform scale for the root node. A value of `1.0` leaves it unmodified. Adjusts the scene’s overall size during import.

- **`nodes/use_name_suffixes`** (`true`)  
  Uses suffixes in node and resource names to determine types and properties. For example:  
  - `-noimp` skips importing a node.  
  - `-alpha` enables alpha transparency on a material.  
  - `-vcol` enables vertex colors.  
  Disabling this makes imported files closer to the original file structure.

- **`nodes/use_node_type_suffixes`** (`true`)  
  Uses suffixes in node names to determine node types (e.g., `-col` for collision shapes). Only effective if `use_name_suffixes` is enabled.

---

### **2. Mesh Configuration**
- **`meshes/light_baking`** (`1`)  
  Sets the `GeometryInstance3D.gi_mode` in the 3D scene.  
  - `1` (Static Lightmaps): Enables static lightmap baking, generating UV2 for `LightmapGI`.

- **`meshes/lightmap_texel_size`** (`0.2`)  
  Controls the resolution of baked lightmaps. Smaller values increase precision but require larger textures and longer bake times.  
  **Note:** Only effective when `light_baking` is set to `Static Lightmaps`.

- **`meshes/light_baking`** (`1`)  
  Configures the mesh’s GI mode for lightmap baking. See above for details.

---

### **3. Skin and Animation**
- **`skins/use_named_skins`** (`true`)  
  Uses named `Skin` objects for animation. This ensures proper binding between meshes and skeletons. Key components:  
  - **Skeleton3D**: Contains bone names, poses, and parent-child relationships.  
  - **Mesh**: Holds vertex data and weight painting information.  
  - **Skin**: Maps bones to the skeleton (by name or index).  
    - If `use_named_skins` is `true`, the skin uses bone names.  
    - If `false`, it uses bone indices.  
  This allows models to share bind data (common in Blender exports) or use separate skins (common in Maya exports).

---

### **4. General Notes**
- **`import_as_skeleton_bones`**: Useful for retargeting animations between skeletons.  
- **`use_name_suffixes` and `use_node_type_suffixes`**: Customization options for node types and resource import behavior.  
- **`lightmap_texel_size`**: Balances detail and performance in lightmap baking.

---

These settings allow fine-grained control over how scenes are imported, ensuring compatibility with Godot’s 3D engine and enabling custom workflows for animations, scaling, and lighting. Adjusting these properties can optimize performance, ensure correct animation retargeting, or align imported models with design goals.