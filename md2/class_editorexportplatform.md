The `EditorExportPlatform` class is a foundational class for managing platform-specific export operations in a game engine or development environment. Below is a breakdown of its key components, methods, and usage scenarios:

---

### **Core Functionality**
1. **Platform-Specific Handling**  
   - **`get_os_name()`**: Returns the target operating system (e.g., "Windows", "Linux", "macOS", "Android", "iOS", "Web"). This is critical for tailoring export logic to the target platform.
   - **`get_os_name()`**: Used by the engine to determine the export target, ensuring platform-specific assets (e.g., DLLs, binaries) are correctly generated.

2. **File Export and Management**  
   - **`save_pack()` and `save_zip()`**: Save exported content as PCK or ZIP archives.  
     - **`embed` parameter**: When `true`, appends the archive to a file (e.g., for embedded assets in a larger application).  
     - **Return values**: Include error results and metadata (e.g., shared object files).  
   - **`save_pack_patch()` and `save_zip_patch()`**: Handle incremental updates (patches) for the exported content.

3. **Remote Deployment**  
   - **`ssh_push_to_remote()`**: Uploads a file to a remote server via SCP.  
   - **`ssh_run_on_remote()`**: Executes a command on a remote server via SSH, capturing output.  
   - **`ssh_run_on_remote_no_wait()`**: Runs a command asynchronously, returning the process ID.  
   - These methods are essential for deploying builds to remote servers (e.g., Android devices, Linux machines).

4. **Logging and Debugging**  
   - **`add_message()`**: Logs messages (e.g., errors, warnings) during export. Messages are categorized by type (e.g., `ExportMessageType::Error`, `ExportMessageType::Warning`).  
   - **`get_message_count()`, `get_message_text()`, `get_message_type()`**: Retrieve logs for debugging or post-export analysis.  
   - **`get_worst_message_type()`**: Identifies the most severe message in the log (e.g., critical errors).

5. **Asset Handling**  
   - **`get_worst_message_type()`**: Ensures the export process is aware of critical issues (e.g., missing assets, failed builds).  
   - **`get_message_category()`**: Organizes logs by category (e.g., "Build", "Resource", "Configuration").

6. **Static and Virtual Methods**  
   - **`get_os_name()`**: A `const` method that does not modify the object.  
   - **Virtual methods**: Methods like `save_pack()` are marked as `virtual`, meaning they should be overridden in subclasses to implement platform-specific logic.

---

### **Key Implementation Considerations**
- **Custom Platform Implementation**:  
  To create a custom platform (e.g., for a new OS or device), override methods like:  
  - `get_os_name()` to return the target OS.  
  - `save_pack()` to handle the specific archive format (e.g., APK for Android, IPA for iOS).  
  - `ssh_push_to_remote()` and `ssh_run_on_remote()` if remote deployment is required.  

- **Error Handling**:  
  Use `add_message()` to log errors during export (e.g., failed asset packaging, missing dependencies). The `get_worst_message_type()` method helps identify critical issues quickly.

- **Remote Deployment Workflow**:  
  For platforms requiring remote deployment (e.g., Android, iOS), use:  
  - `ssh_push_to_remote()` to upload the build file.  
  - `ssh_run_on_remote()` to trigger installation or testing on the target device.

---

### **Example Use Case**
Suppose you're creating a custom platform for "WebAssembly" (WASM):  
1. Override `get_os_name()` to return `"Web"`.  
2. Implement `save_pack()` to generate a WASM binary and associated resources.  
3. Use `ssh_run_on_remote()` to deploy the WASM file to a remote server for testing.

---

### **Best Practices**
- **Modular Design**: Keep platform-specific logic isolated in subclasses to avoid bloating the base class.  
- **Documentation**: Clearly document the expected behavior of each method, especially for virtual methods.  
- **Testing**: Validate logs and remote operations using unit tests and real-world scenarios.

This class provides a flexible framework for managing export operations, with emphasis on platform-specific logic, remote deployment, and error handling.