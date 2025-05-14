**EditorPaths**  
Inherits: `Object`  

**Description**  
Editor-only singleton that returns OS-specific paths to various data folders and files. Used in editor plugins to ensure correct file locations.  

**Note**: Not accessible in exported projects. Use `Engine.has_singleton()` to check availability.  
**Note**: Linux/BSD follows XDG Base Directory Specification. Environment variables can override paths.  

**Tutorials**  
- [File paths in Godot projects](https://docs.godotengine.org/en/stable/tutorials/io/data_paths.html)  

**Methods**  
- `get_cache_dir() -> String`: Returns user cache folder (temporary data).  
  - **Windows**: `%LOCALAPPDATA%\Godot\`  
  - **macOS**: `~/Library/Caches/Godot/`  
  - **Linux**: `~/.cache/godot/`  

- `get_config_dir() -> String`: Returns user configuration folder (persistent settings).  
  - **Windows**: `%APPDATA%\Godot\`  
  - **macOS**: `~/Library/Application Support/Godot/`  
  - **Linux**: `~/.config/godot/`  

- `get_data_dir() -> String`: Returns user data folder (persistent files).  
  - **Windows**: `%APPDATA%\Godot\`  
  - **macOS**: `~/Library/Application Support/Godot/`  
  - **Linux**: `~/.local/share/godot/`  

- `get_project_settings_dir() -> String`: Returns project-specific editor settings path.  

- `get_self_contained_file() -> String`: Returns path to self-contained editor file. Returns empty string if not self-contained.  

- `is_self_contained() -> bool`: Returns `true` if editor is self-contained (user data saved in `editor_data/` folder).  

**Notes**  
- Self-contained mode: User config, data, and cache stored in `editor_data/` folder.  
- macOS: Remove quarantine flag before using self-contained mode.  
- macOS: Place `_sc_` file outside .app bundle to avoid signature issues.  
- Steam release: Uses self-contained mode by default.