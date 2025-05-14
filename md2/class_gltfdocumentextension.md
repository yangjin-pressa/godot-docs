The `GLTFDocumentExtension` class provides a framework for customizing the import and export processes of glTF files by overriding specific methods. Below is a structured overview of the methods, their purposes, and how they fit into the pipeline:

---

### **Import Process**

1. **`_import_preflight`**
   - **Purpose**: Determines if the extension should be used for importing a glTF file.
   - **Parameters**: 
     - `state`: `GLTFState` object containing the current import state.
     - `extensions`: List of supported extensions.
   - **Return**: 
     - `@GlobalScope.OK`: Use this extension.
     - Else: Do not use it.
   - **Note**: This is the first check in the import workflow.

2. **`_get_supported_extensions`**
   - **Purpose**: Returns the list of extensions this extension supports.
   - **Return**: `PackedStringArray` of supported extensions.

3. **`_parse_node_extensions`**
   - **Purpose**: Parses node-specific extensions for a `GLTFNode`.
   - **Parameters**: 
     - `state`: `GLTFState`.
     - `gltf_node`: `GLTFNode` to process.
     - `extensions`: `Dictionary` of extension data.
   - **Return**: `Error` (if parsing fails).

4. **`_parse_image_data`**
   - **Purpose**: Parses image data (from buffer, URI, or file) into a byte array.
   - **Parameters**: 
     - `state`: `GLTFState`.
     - `image_data`: `PackedByteArray` of image data.
     - `mime_type`: MIME type of the image.
   - **Return**: `Error` (if parsing fails).

5. **`_parse_texture_json`**
   - **Purpose**: Parses texture JSON to set the source image index.
   - **Parameters**: 
     - `state`: `GLTFState`.
     - `texture_json`: `Dictionary` of texture data.
     - `gltf_texture`: `GLTFTexture` to populate.
   - **Return**: `Error` (if parsing fails).

6. **`_parse_image_data` (repeated)** 
   - **Purpose**: Ensures consistency in parsing image data across different contexts.

7. **`_import_post_parse`**
   - **Purpose**: Called after parsing node extensions to modify data structures before generating nodes.

8. **`_generate_scene_node`**
   - **Purpose**: Generates a scene node (e.g., `Node`) from a `GLTFNode`.
   - **Parameters**: 
     - `state`: `GLTFState`.
     - `gltf_node`: `GLTFNode` to convert.
   - **Return**: `Node` object.

---

### **Export Process**

1. **`_get_saveable_image_formats`**
   - **Purpose**: Returns the list of image formats available for export.
   - **Return**: `String` list (e.g., "png", "jpg").

2. **`_serialize_image_to_bytes`**
   - **Purpose**: Serializes an `Image` object into a byte array for embedding in the glTF file.
   - **Parameters**: 
     - `state`: `GLTFState`.
     - `image`: `Image` to serialize.
     - `image_dict`: `Dictionary` to store metadata.
     - `image_format`: Target format (e.g., "png").
     - `lossy_quality`: Quality for lossy formats.
   - **Return**: `PackedByteArray` of serialized image data.

3. **`_save_image_at_path`**
   - **Purpose**: Saves an `Image` to a file path for external storage.
   - **Parameters**: 
     - `state`: `GLTFState`.
     - `image`: `Image` to save.
     - `file_path`: Destination file path.
     - `image_format`: Target format.
     - `lossy_quality`: Quality for lossy formats.
   - **Return**: `Error` (if saving fails).

4. **`_serialize_texture_json`**
   - **Purpose**: Sets up texture JSON (e.g., `texture_json`) with image data.
   - **Parameters**: 
     - `state`: `GLTFState`.
     - `texture_json`: `Dictionary` to modify.
     - `gltf_texture`: `GLTFTexture` to reference.
     - `image_format`: Target format.
   - **Return**: `Error` (if serialization fails).

---

### **Key Relationships**

- **Import Flow**:
  1. `_import_preflight` → Checks if the extension is applicable.
  2. `_get_supported_extensions` → Lists supported extensions.
  3. `_parse_node_extensions` → Processes node-specific data.
  4. `_parse_image_data` → Parses image data for textures.
  5. `_parse_texture_json` → Sets texture source image.
  6. `_generate_scene_node` → Converts `GLTFNode` to a scene node.

- **Export Flow**:
  1. `_get_saveable_image_formats` → Determines available export formats.
  2. `_serialize_image_to_bytes` → Embeds image in glTF.
  3. `_save_image_at_path` → Saves image externally.
  4. `_serialize_texture_json` → Updates texture JSON with image references.

---

### **Important Notes**

- **Virtual Methods**: Most methods are `virtual`, requiring subclasses to override for custom behavior.
- **Error Handling**: Return `Error` codes to signal failures (e.g., invalid data, unsupported formats).
- **MIME Types**: Use `"image/png"`, `"image/jpg"`, etc., for correct MIME types in `image_dict`.
- **Extensions**: Ensure extensions are marked as `required` if not providing fallback data.

---

### **Example Use Case**

- **Custom Texture Extension**:
  - Override `_parse_node_extensions` to process custom texture data.
  - Use `_serialize_texture_json` to map custom data to the glTF texture structure.

- **Custom Image Format**:
  - Implement `_serialize_image_to_bytes` to handle a proprietary image format.
  - Update `_get_saveable_image_formats` to include the new format.

This structure allows developers to extend glTF import/export capabilities while maintaining compatibility with core glTF specifications.