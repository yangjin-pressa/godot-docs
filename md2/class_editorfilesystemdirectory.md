# EditorFileSystemDirectory

**Inherits:** Object

A directory for the resource filesystem.
A more generalized, low-level variation of the directory concept.

## Methods

- **find_dir_index(name: String)** → int  
  Returns the index of the directory with name `name` or -1 if not found.

- **find_file_index(name: String)** → int  
  Returns the index of the file with name `name` or -1 if not found.

- **get_file(idx: int)** → String  
  Returns the name of the file at index `idx`.

- **get_file_count()** → int  
  Returns the number of files in this directory.

- **get_file_import_is_valid(idx: int)** → bool  
  Returns true if the file at index `idx` imported properly.

- **get_file_path(idx: int)** → String  
  Returns the path to the file at index `idx`.

- **get_file_script_class_extends(idx: int)** → String  
  Returns the base class of the script class defined in the file at index `idx`. Returns empty string if no script class is defined.

- **get_file_script_class_name(idx: int)** → String  
  Returns the name of the script class defined in the file at index `idx`. Returns empty string if no script class is defined.

- **get_file_type(idx: int)** → StringName  
  Returns the resource type of the file at index `idx`. Examples: "Resource", "GDScript".

- **get_name()** → String  
  Returns the name of this directory.

- **get_parent()** → EditorFileSystemDirectory  
  Returns the parent directory or null if called on a directory at `res://` or `user://`.

- **get_path()** → String  
  Returns the path to this directory.

- **get_subdir(idx: int)** → EditorFileSystemDirectory  
  Returns the subdirectory at index `idx`.

- **get_subdir_count()** → int  
  Returns the number of subdirectories in this directory.