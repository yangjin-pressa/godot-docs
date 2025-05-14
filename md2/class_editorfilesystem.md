**EditorFileSystem**  
A class that manages resource information for the editor.  

---

### **Description**  
- Holds information about resources, their types, and other metadata.  
- Accessed via the singleton method `EditorInterface.get_resource_filesystem()`.  
- **Note**: Do not instantiate this class directly.  

---

### **Methods**  
- **get_file_type(path: String): String**  
  Returns the resource type (e.g., "Texture2D") associated with the given file path.  

- **get_filesystem(): Resource**  
  Returns the root resource object for the editor.  

- **reimport_files(paths: List<String>): void**  
  Reimports files, updating their data in the editor. Blocks until completion.  

- **update_file(path: String): void**  
  Updates a file in an existing directory or schedules updates for editor restart.  
  **Note**: Does not import the file; use `reimport_files()` for full reimport.  

---

### **Signals**  
- **filesystem_changed(): void**  
  Emitted when the filesystem structure changes.  

- **resources_reimported(resources: List<String>): void**  
  Emitted after reimporting resources.  

- **resources_updated(resources: List<String>): void**  
  Emitted after updating resources.  

---

### **Method Descriptions**  
- **get_file_type(path: String): String**  
  Returns the resource type (e.g., "Texture2D") associated with the given file path.  

- **get_filesystem(): Resource**  
  Returns the root resource object for the editor.  

- **reimport_files(paths: List<String>): void**  
  Reimports files, updating their data in the editor. Blocks until completion.  

- **update_file(path: String): void**  
  Updates a file in an existing directory or schedules updates for editor restart.  
  **Note**: Does not import the file; use `reimport_files()` for full reimport.  

---

### **Key Notes**  
- **Singleton Access**: Use `EditorInterface.get_resource_filesystem()` to access this class.  
- **Blocking Behavior**: `reimport_files()` blocks until the operation is complete.  
- **No Side Effects**: `get_filesystem()` has no side effects.