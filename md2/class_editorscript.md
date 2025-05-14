# EditorScript

**Inherits:** RefCounted < Object

## Description
Scripts extending this class and implementing its `_run()` method can be executed from the Script Editor's **File > Run** menu (or via Ctrl + Shift + X). Useful for adding custom in-editor functionality. For complex additions, consider using EditorPlugins.

**Note:** Extending scripts must be in "tool" mode.

**Example:**
```gdscript
@tool
extends EditorScript

func _run():
    print("Hello from the Godot Editor!")
```

**Note:** Runs in the Editor context (Editor stdout), not the usual Output dock.

**Note:** EditorScript is RefCounted - destroyed when unreferenced, which may cause errors in async operations.

## Methods

### _run()
- **Type:** void (virtual)
- **Description:** Called by the Editor when **File > Run** is selected.

### add_root_node(node: Node)
- **Type:** void
- **Description:** Makes `node` the root of the current scene. Works only if the scene is empty. If `node` is a scene instance, an inheriting scene is created.

### get_editor_interface()
- **Type:** EditorInterface (deprecated)
- **Description:** Returns the EditorInterface singleton. (Use direct access instead)

### get_scene()
- **Type:** Node (const)
- **Description:** Returns the current scene's root Node. Equivalent to EditorInterface.get_edited_scene_root().

## Key Notes
- Requires "tool" mode for extension scripts
- Editor context output appears in the Editor's stdout window
- RefCounted: Destroyed when no references exist
- Asynchronous operations may fail if no references exist