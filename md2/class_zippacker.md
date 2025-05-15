### ZIPPacker

#### Description
The `ZIPPacker` class allows creating ZIP files. It is used in conjunction with other classes such as `ZIPReader` and `PCKPacker` for file handling.

**Example Usage:**
```python
func write_zip_file():
    var writer = ZIPPacker.new()
    var err = writer.open("user://archive.zip")
    if err != OK:
        return err
    writer.start_file("hello.txt")
    writer.write_file("Hello World".to_utf8_buffer())
    writer.close_file()
    writer.close()
    return OK
```

#### Properties
- **compression_level** (int): Default value is `-1`.

#### Methods
- **open(path: String)** → Error: Opens a ZIP file for writing.
- **start_file(filename: String)**: Begins writing a new file into the ZIP archive.
- **write_file(data: PackedByteArray)**: Writes data to the current file in the ZIP archive.
- **close_file()**: Closes the currently open file in the ZIP archive.
- **close()**: Closes the ZIP archive.

#### Enumerations
**ZipAppend**
- **APPEND_CREATE (0)**: Creates a new ZIP file.
- **APPEND_CREATEAFTER (1)**: Appends to an existing ZIP file.
- **APPEND_ADDINZIP (2)**: Adds files to an existing ZIP file.

**CompressionLevel**
- **COMPRESSION_DEFAULT (-1)**: Default compression level.
- **COMPRESSION_NONE (0)**: No compression.
- **COMPRESSION_BEST (9)**: Best compression.

#### Notes
- Methods must be called in sequence: `open()`, `start_file()`, `write_file()`, `close_file()`, `close()`.
- `write_file()` must be called after `start_file()`.