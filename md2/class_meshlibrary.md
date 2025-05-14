# MeshLibrary Class Documentation

The `MeshLibrary` class is designed to manage a collection of items, each of which can have a mesh, navigation mesh, name, preview, and collision shapes. This class provides methods to create, retrieve, and modify these properties.

---

## Class Overview

The `MeshLibrary` class is used for handling assets and their associated properties in a Godot project. It allows developers to manage a collection of items, each of which can be configured with various properties such as mesh, navigation mesh, name, preview, and collision shapes.

---

## Methods

### `clear()`
**Description**: Removes all items from the library.  
**Parameters**: None.  
**Notes**: This method is virtual and should be overridden to have any effect.

---

### `get_item_preview()`
**Description**: Returns the preview of an item.  
**Parameters**: `int id` (the index of the item in the library).  
**Return Type**: `Texture2D` (or a generated preview in the editor).  
**Notes**: In the editor, a generated preview is returned. In a running project, the manually set preview is returned.

---

### `set_item_preview()`
**Description**: Sets the preview of an item.  
**Parameters**: `int id` (the index of the item in the library), `Texture2D preview` (the new preview texture).  
**Notes**: This method is const and does not modify the instance.

---

### `get_item_shapes()`
**Description**: Returns the collision shapes of an item.  
**Parameters**: `int id` (the index of the item in the library).  
**Return Type**: `Array` of `Shape3D` objects.  
**Notes**: This method is const and does not modify the instance.

---

### `set_item_shapes()`
**Description**: Sets the collision shapes of an item.  
**Parameters**: `int id` (the index of the item in the library), `Array shapes` (an array of `Shape3D` objects followed by their transforms).  
**Notes**: The array should consist of `Shape3D` objects followed by their `Transform3D`. If a shape has no transform, use `Transform3D.IDENTITY`.

---

### `get_last_unused_item_id()`
**Description**: Returns the index of the next unused item in the library.  
**Parameters**: None.  
**Return Type**: `int`.  
**Notes**: This method is const and does not modify the instance.

---

### `remove_item()`
**Description**: Removes an item from the library.  
**Parameters**: `int id` (the index of the item in the library).  
**Notes**: This method is const and does not modify the instance.

---

### `set_item_mesh()`
**Description**: Sets the mesh of an item.  
**Parameters**: `int id` (the index of the item in the library), `Mesh mesh` (the new mesh).  
**Notes**: This method is const and does not modify the instance.

---

### `set_item_mesh_cast_shadow()`
**Description**: Sets whether the item's mesh casts shadows.  
**Parameters**: `int id` (the index of the item in the library), `bool cast_shadow` (whether the mesh casts shadows).  
**Notes**: This method is const and does not modify the instance.

---

### `set_item_mesh_transform()`
**Description**: Sets the transform of an item's mesh.  
**Parameters**: `int id` (the index of the item in the library), `Transform3D transform` (the new transform).  
**Notes**: This method is const and does not modify the instance.

---

### `set_item_name()`
**Description**: Sets the name of an item.  
**Parameters**: `int id` (the index of the item in the library), `String name` (the new name).  
**Notes**: This method is const and does not modify the instance.

---

### `set_item_navigation_layers()`
**Description**: Sets the navigation layers of an item.  
**Parameters**: `int id` (the index of the item in the library), `int layers` (the new navigation layers).  
**Notes**: This method is const and does not modify the instance.

---

### `set_item_navigation_mesh()`
**Description**: Sets the navigation mesh of an item.  
**Parameters**: `int id` (the index of the item in the library), `NavigationMesh mesh` (the new navigation mesh).  
**Notes**: This method is const and does not modify the instance.

---

### `set_item_navigation_mesh_transform()`
**Description**: Sets the transform of an item's navigation mesh.  
**Parameters**: `int id` (the index of the item in the library), `Transform3D transform` (the new transform).  
**Notes**: This method is const and does not modify the instance.

---

## Notes
- All methods that take `id` as a parameter are used to reference a specific item in the library.
- Methods marked as `const` do not modify the instance of the class.
- Methods marked as `virtual` should be overridden in subclasses to provide custom behavior.