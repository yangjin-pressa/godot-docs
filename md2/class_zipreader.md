# ZIPReader

**Inherits:** RefCounted < Object

## Description

This class allows reading content from ZIP files. It can extract individual files or all files from an archive. See also ZIPPacker.

Example usage:
```gdscript
func read_zip_file():
    var reader = ZIPReader.new()
    var err = reader.open("user://archive.zip")
    if err != OK:
        return PackedByteArray()
    var res = reader.read_file("hello.txt")
    reader.close()
    return res

func extract_all_from_zip():
    var reader = ZIPReader.new()
    reader.open("res://archive.zip")
    var root_dir = DirAccess.open("user://")
    var files = reader.get_files()
    for file_path in files:
        if file_path.endswith("/"):
            root_dir.make_dir_recursive(file_path)
            continue
        root_dir.make_dir_recursive(root_dir.get_current_dir().path_join(file_path).get_base_dir())
        var file = FileAccess.open(root_dir.get_current_dir().path_join(file_path), FileAccess.WRITE)
        var buffer = reader.read_file(file_path)
        file.store_buffer(buffer)
```

## Methods

- **close()**  
  Returns: Error  
  Closes underlying resources.

- **file_exists(path: String, case_sensitive: bool = true)**  
  Returns: bool  
  Checks if a file exists in the archive. Must be called after open().

- **get_compression_level(path: String, case_sensitive: bool = true)**  
  Returns: int  
  Returns compression level of a file. Returns -1 on error. Must be called after open().

- **get_files()**  
  Returns: PackedStringArray  
  Returns list of all files in the archive. Must be called after open().

- **open(path: String)**  
  Returns: Error  
  Opens a ZIP archive at the given path.

- **read_file(path: String, case_sensitive: bool = true)**  
  Returns: PackedByteArray  
  Loads a file's content into memory. Must be called after open().

## Key Notes
- All methods must be called after open() is successfully executed.
- File paths are case-sensitive by default.
- Directories are handled automatically during extraction.