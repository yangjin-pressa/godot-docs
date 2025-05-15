# SceneState Class Documentation

## Overview
The `SceneState` class represents the state of a Godot scene, providing access to its nodes, signals, properties, and resources. It offers methods to retrieve information about the scene's structure and contents, including node data, signal details, and property values.

---

## Enumerations

### `GenType`
Defines the type of element in the scene.
- **NODE**: A node in the scene.
- **SIGNAL**: A signal connected to a node.
- **PROPERTY**: A property of a node.
- **GROUP**: A group of nodes.
- **INSTANCE**: An instance of a scene.
- **PLACEHOLDER**: An `InstancePlaceholder` node.

---

## Methods

### `get_node_count()`
**Return**: `int`  
**Description**: Returns the number of nodes in the scene.  
**Note**: The `idx` parameter used in other methods is unrelated to this index.

### `get_node_groups(idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
**Return**: `PackedStringArray`  
**Description**: Returns the list of group names associated with the node at `idx`.

### `get_node_index(idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
**Return**: `int`  
**Description**: Returns the node's index relative to its siblings. This is relevant when nodes are added to a scene from a base scene.

### `get_node_instance(idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
**Return**: `PackedScene`  
**Description**: Returns a `PackedScene` for the node at `idx`, representing the entire branch starting at this node.

### `get_node_instance_placeholder(idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
**Return**: `String`  
**Description**: Returns the path to the scene file if the node at `idx` is an `InstancePlaceholder`.

### `get_node_name(idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
**Return**: `StringName`  
**Description**: Returns the name of the node at `idx`.

### `get_node_owner_path(idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
**Return**: `NodePath`  
**Description**: Returns the path to the owner of the node at `idx`.

### `get_node_path(idx, for_parent=false)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
- `for_parent`: `bool` – If `true`, returns the path of the parent node.  
**Return**: `NodePath`  
**Description**: Returns the path to the node at `idx`. If `for_parent` is `true`, returns the parent's path.

### `get_node_property_count(idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
**Return**: `int`  
**Description**: Returns the number of exported or overridden properties for the node at `idx`.

### `get_node_property_name(idx, prop_idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
- `prop_idx`: `int` – Index of the property.  
**Return**: `StringName`  
**Description**: Returns the name of the property at `prop_idx` for the node at `idx`.

### `get_node_property_value(idx, prop_idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
- `prop_idx`: `int` – Index of the property.  
**Return**: `Variant`  
**Description**: Returns the value of the property at `prop_idx` for the node at `idx`.

### `get_node_type(idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
**Return**: `StringName`  
**Description**: Returns the type of the node at `idx`.

### `get_path()`
**Return**: `String`  
**Description**: Returns the resource path to the represented `PackedScene`.

### `is_node_instance_placeholder(idx)`
**Parameters**:  
- `idx`: `int` – Index of the node.  
**Return**: `bool`  
**Description**: Returns `true` if the node at `idx` is an `InstancePlaceholder`.

---

## Notes
- **Const Methods**: Most methods are `const`, meaning they do not modify the object.
- **Virtual Methods**: Some methods (e.g., `get_node_count()`) are virtual and should be overridden if needed.
- **Indexes**: The `idx` parameter in most methods refers to the node index, not the index used in other methods.