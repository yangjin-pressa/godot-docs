# InstancePlaceholder

## Inheritance
- Node → Object

## Description
- **Load As Placeholder** option in editor replaces scene with InstancePlaceholder at runtime.
- Placeholder does not have a transform, so child nodes are positioned relative to the Viewport (0,0).
- Replacing placeholder with a scene restores transform behavior.

## Methods

### create_instance
- **Type:** Node
- **Parameters:** 
  - replace: bool = false
  - custom_scene: PackedScene = null
- **Description:** Loads the scene into the scene tree as a sibling node. Returns the created Node reference.
- **Note:** Not thread-safe. Use Object.call_deferred() for thread calls.

### get_instance_path
- **Type:** String
- **Parameters:** none
- **Description:** Returns the path to the PackedScene resource file.
- **Note:** Not thread-safe. Use Object.call_deferred() for thread calls.

### get_stored_values
- **Type:** Dictionary
- **Parameters:** 
  - with_order: bool = false
- **Description:** Returns properties to apply when create_instance is called.
- **Special Case:** If with_order is true, adds ".order" key with property application order.

## Key Attributes
- **Placeholder Behavior:** Used to defer scene loading until needed.
- **Transform Handling:** No transform → child nodes are viewport-relative.
- **Thread Safety:** Methods are not thread-safe; use call_deferred() for threaded calls.

## Notes
- The method `create_instance()` is critical for loading scenes selectively.
- The `.order` key in get_stored_values specifies property application sequence when with_order is true.