The `ResourceLoader` class in Godot is essential for loading and managing resources efficiently, especially in scenarios requiring background processing or handling large files. Below is a structured explanation of its key methods, usage, and best practices:

---

### **Key Methods and Usage**

1. **`load(path: String, type_hint: String = "", cache_mode: int = 1) → Resource`**
   - **Purpose**: Loads a resource from the specified path, using caching for future access.
   - **Parameters**:
     - `path`: Absolute path (e.g., `"res://assets/model.tscn"`).
     - `type_hint`: Optional type (e.g., `"Texture"` or `"Image"`).
     - `cache_mode`: Controls caching behavior (e.g., `1` for `CacheMode.CACHE`).
   - **Note**: Relative paths are prefixed with `"res://"` to avoid conflicts.
   - **Example**:
     ```gdscript
     var texture = ResourceLoader.load("res://textures/texture.png")
     ```

2. **`load_threaded_request(path: String, type_hint: String = "", use_sub_threads: bool = false, cache_mode: int = 1) → Error`**
   - **Purpose**: Starts loading a resource in a separate thread for background processing.
   - **Parameters**:
     - `use_sub_threads`: Use multiple threads for faster loading.
   - **Note**: This method does not block the main thread, but the result is not available until `load_threaded_get()` is called.
   - **Example**:
     ```gdscript
     var error = ResourceLoader.load_threaded_request("res://assets/model.gltf")
     ```

3. **`load_threaded_get(path: String) → Resource`**
   - **Purpose**: Returns the resource once loading is complete.
   - **Note**: If called before loading, it blocks until completion.
   - **Example**:
     ```gdscript
     var texture = ResourceLoader.load_threaded_get("res://assets/model.gltf")
     ```

4. **`load_threaded_get_status(path: String, progress: Array = []) → ThreadLoadStatus`**
   - **Purpose**: Checks the status of a threaded load and optionally returns progress.
   - **Parameters**:
     - `progress`: An array to store completion ratio (e.g., `[0.75]`).
   - **Example**:
     ```gdscript
     var status = ResourceLoader.load_threaded_get_status("res://assets/model.gltf", [])
     ```

5. **`list_directory(directory_path: String) → PackedStringArray`**
   - **Purpose**: Lists resources and subdirectories in a folder.
   - **Example**:
     ```gdscript
     var files = ResourceLoader.list_directory("res://assets/")
     for file in files:
         print("File: ", file)
     ```

6. **`has_cached(path: String) → bool`**
   - **Purpose**: Checks if a resource is already in the cache.
   - **Example**:
     ```gdscript
     if ResourceLoader.has_cached("res://textures/texture.png"):
         print("Resource is cached!")
     ```

7. protected **`get_recognized_extensions_for_type(type: String) → PackedStringArray`**
   - **Purpose**: Returns file extensions supported for a given type (e.g., `"Texture"`).
   - **Example**:
     ```gdscript
     var extensions = ResourceLoader.get_recognized_extensions_for_type("Texture")
     ```

8. **`get_resource_uid(path: String) → int`**
   - **Purpose**: Returns a unique identifier for a resource.
   - **Example**:
     ```gdscript
     var uid = ResourceLoader.get_resource_uid("res://assets/model.tscn")
     ```

---

### **Best Practices**

- **Path Handling**: Always use absolute paths (e.g., `"res://..."`) to avoid confusion.
- **Caching**: Use `cache_mode = 1` (default) for efficient future access, but disable it for temporary resources.
- **Threaded Loading**: Use `load_threaded_request()` and `load_threaded_get_status()` for non-blocking loading, especially with large assets.
- **Error Handling**: Check the return value of `load_threaded_request()` and validate the result of `load_threaded_get()`.
- **Resource Management**: Remove unused `ResourceFormatLoader` instances with `remove_resource_format_loader()` to avoid conflicts.
- **Progress Updates**: Use `load_threaded_get_status()` in game loops to update UI progress bars or status indicators.

---

### **Common Use Cases**

1. **Loading Assets**:
   ```gdscript
   var texture = ResourceLoader.load("res://textures/texture.png")
   if texture is Texture:
       print("Loaded texture!")
   ```

2. **Background Resource Loading**:
   ```gdscript
   var error = ResourceLoader.load_threaded_request("res://assets/model.gltf")
   if error == Error::OK:
       var model = ResourceLoader.load_threaded_get("res://assets/model.gltf")
   ```

3. **Directory Scanning**:
   ```gdscript
   var files = ResourceLoader.list_directory("res://assets/textures")
   for file in files:
       if file.endswith(".png"):
           var texture = ResourceLoader.load(file)
   ```

4. **Checking Caching**:
   ```gdscript
   if ResourceLoader.has_cached("res://audio/sound.ogg"):
       print("Sound is already cached.")
   ```

---

### **注意事项**

- **ProjectSettings**: If `convert_text_resources_to_binary` is enabled, `@GDScript.load()` may fail, but `ResourceLoader.load()` should handle binary files correctly.
- **Thread Safety**: Ensure thread-safe access to resources when using background loading.
- **Cache Invalidations**: Explicitly clear the cache if resources are updated, but this is generally managed by the engine.

By leveraging `ResourceLoader`, developers can efficiently manage assets in Godot, ensuring smooth performance and responsiveness in both small and large-scale projects.