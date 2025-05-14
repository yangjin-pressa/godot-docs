# PCKPacker

**Inherits:** RefCounted < Object

## Description

Used to create packages for loading into a running project using `ProjectSettings.load_resource_pack()`.

**Example (GDScript):**
```gdscript
var packer = PCKPacker.new()
packer.pck_start("test.pck")
packer.add_file("res://text.txt", "text.txt")
packer.flush()
```

**Example (C#):**
```csharp
var packer = new PckPacker();
packer.PckStart("test.pck");
packer.AddFile("res://text.txt", "text.txt");
packer.Flush();
```

**Note:** PCK is Godot's own format. For ZIP archives, use `ZIPPacker`.

---

## Methods

### add_file
Adds a file to the current PCK package.

**Parameters:**
- `target_path`: String (internal path)
- `source_path`: String (file path to add)
- `encrypt`: bool = false (optional)

### add_file_removal
Registers a file removal (used for patches).

**Parameters:**
- `target_path`: String (internal path)

### flush
Writes added files to the package. If `verbose = true`, prints file list.

**Parameters:**
- `verbose`: bool = false (optional)

### pck_start
Creates a new PCK file.

**Parameters:**
- `pck_path`: String (file path)
- `alignment`: int = 32 (optional)
- `key`: String = "0000000000000000000000000000000