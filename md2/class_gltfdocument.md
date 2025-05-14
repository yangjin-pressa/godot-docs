The `GLTFDocument` class in Godot is a core component for handling glTF (GL Transmission Format) files, enabling the import and export of 3D models and scenes. It works in conjunction with the `GLTFState` class to manage the state of the glTF data during processing. Below is a structured explanation of its key features, properties, and methods.

---

### **Key Properties**
1. **`extensions`**  
   A dictionary mapping extension names (e.g., `KHR_vertex_type`) to their corresponding data. This allows the document to support custom glTF extensions.

2. **`additional_data`**  
   A dictionary for storing arbitrary data that may be used by extensions or other components during processing. This is stateless and typically accessed via the `GLTFState` class.

3. **`state`**  
   A reference to the `GLTFState` object, which holds the current state of the glTF document (e.g., metadata, buffers, scenes).

---

### **Key Methods**

#### **1. Importing glTF Data**
- **`append_from_buffer(bytes, base_path, state, flags=0)`**  
  Imports glTF data from a `PackedByteArray` into the `GLTFState` object. This is useful for loading binary glTF files (`.glb`) or text files (`.gltf`).

- **`append_from_file(path, state, flags=0, base_path="")`**  
  Loads glTF data from a file path into the `GLTFState`. The `base_path` is used to resolve dependencies like textures or shaders.

- **`append_from_scene(node, state, flags=0)`**  
  Exports a Godot scene node and its descendants into the `GLTFState`, generating a glTF document from the scene.

---

#### **2. Generating glTF Output**
- **`generate_buffer(state)`**  
  Converts the `GLTFState` into a `PackedByteArray` representing the final glTF file (binary or text format).

- **`generate_scene(state, bake_fps=30, trimming=false, remove_immutable_tracks=true)`**  
  Converts the `GLTFState` into a Godot scene node, which can be used for testing or further processing.

---

#### **3. Managing Extensions**
- **`get_supported_gltf_extensions()`**  
  Returns a list of all supported glTF extensions, including those from the engine and user-added plugins. Extensions are registered via `register_gltf_document_extension`.

- **`register_gltf_document_extension(extension, first_priority=false)`**  
  Registers a custom `GLTFDocumentExtension` to support new glTF extensions. Extensions are processed in priority order (default: last, unless `first_priority=true`).

- **`unregister_gltf_document_extension(extension)`**  
  Removes a previously registered extension.

---

#### **4. Utility Methods**
- **`write_to_filesystem(state, path)`**  
  Writes the `GLTFState` to a file system path. The file extension (`.glb` or `.gltf`) determines the output format.

---

### **Working with Extensions**
- Extensions are implemented as `GLTFDocumentExtension` classes. They can:
  - Modify the `GLTFState` during import/export.
  - Handle custom glTF extensions (e.g., `KHR_material_extension`).
  - Register custom properties or data mappings.

- **Example:**  
  A custom extension might add support for a new vertex format or texture compression. It would override methods like `export_object_model_property` or `import_object_model_property` to define how data maps between Godot and glTF.

---

### **Important Notes**
- **Statelessness:** Extensions and `GLTFDocument` must be stateless. Any data needed is stored in `GLTFState` via `set_additional_data` or `get_additional_data`.
- **Extension Priority:** Extensions registered with `first_priority=true` are processed before others, ensuring custom data is handled correctly.
- **File Format:** `write_to_filesystem` automatically determines whether to save as a binary `.glb` or text `.gltf` file based on the extension.

---

### **Use Cases**
- **Exporting Scenes:** Use `append_from_scene` to generate a glTF document from a Godot scene.
- **Importing Models:** Use `append_from_file` to load a glTF model and process it.
- **Custom Extensions:** Register extensions to support advanced features (e.g., animation, shading, or physics).

---

This class forms the backbone of glTF integration in Godot, enabling developers to work with 3D models, animations, and textures in both the editor and runtime.