# VisualShader Class Documentation

The `VisualShader` class in Godot provides a visual interface for creating and managing shaders, allowing users to connect nodes and define the logic of their shaders through a graphical editor. This documentation details the class's constants, methods, and their purposes.

## Constants

### Shader Modes
- **MODE_VERTEX_SHADER**: Represents a vertex shader, responsible for processing vertex data.
- **MODE_FRAGMENT_SHADER**: Represents a fragment shader, responsible for calculating the color of each pixel.
- **MODE_TESSELLATION_SHADER**: Represents a tessellation shader, used for refining geometry.
- **MODE_GEOMETRY_SHADER**: Represents a geometry shader, used for modifying or generating geometry.
- **MODE_MESH_SHADER**: Represents a mesh shader, used for processing entire meshes (available in newer versions of OpenGL).

### Port Types
- **PORT_TYPE_INPUT**: Input port, used to receive data from other nodes.
- **PORT_TYPE_OUTPUT**: Output port, used to send data to other nodes.
- **PORT_TYPE_UNIFORM**: Uniform port, used to pass constant values to the shader.
- **PORT_TYPE_VARYING**: Varying port, used to pass data between shader stages.

---

## Methods

### `add_node(type: Type, id: int = 0) -> int`
Adds a new node of the specified type to the shader graph. If `id` is not provided, the system assigns an automatic ID.

**Parameters**:
- `type`: The type of node to add (e.g., `Type.TEXTURE` or `Type.MATH`).
- `id`: Optional. The ID of the node to add. If not provided, the system assigns an ID.

**Returns**: The ID of the newly added node.

---

### `connect_nodes(type: Type, from_node: int, from_port: int, to_node: int, to_port: int) -> Error`
Connects the specified ports of two nodes. If the connection is invalid, it returns an error.

**Parameters**:
- `type`: The type of node (e.g., `Type.TEXTURE`).
- `from_node`: ID of the source node.
- `from_port`: Port index of the source node.
- `to_node`: ID of the destination node.
- `to_port`: Port index of the destination node.

**Returns**: An `Error` enum value indicating the result of the connection.

---

### `connect_nodes_forced(type: Type, from_node: int, from_port: int, to_node: int, to_port: int)`
Forces a connection between nodes, even if the ports are incompatible. This may lead to incorrect shader behavior.

**Parameters**: Same as `connect_nodes()`.

---

### `disconnect_nodes(type: Type, from_node: int, from_port: int, to_node: int, to_port: int)`
Disconnects the specified ports of two nodes.

**Parameters**: Same as `connect_nodes()`.

---

### `get_node(type: Type, id: int) -> VisualShaderNode`
Retrieves the node instance with the specified type and ID.

**Parameters**:
- `type`: The type of node.
- `id`: The ID of the node.

**Returns**: The node instance, or `null` if not found.

---

### `get_node_connections(type: Type) -> Array<Dictionary>`
Returns a list of all connections for nodes of the specified type. Each entry is a dictionary containing connection details.

**Parameters**:
- `type`: The type of node.

**Returns**: An array of dictionaries, each representing a connection.

---

### `get_node_list(type: Type) -> PackedInt32Array`
Returns an array of IDs for all nodes of the specified type.

**Parameters**:
- `type`: The type of node.

**Returns**: A `PackedInt32Array` of node IDs.

---

### `get_node_position(type: Type, id: int) -> Vector2`
Returns the position of a specific node in the graph.

**Parameters**:
- `type`: The type of node.
- `id`: The ID of the node.

**Returns**: A `Vector2` representing the node's position.

---

### `get_valid_node_id(type: Type) -> int`
Returns the next available ID for adding a node of the specified type.

**Parameters**:
- `type`: The type of node.

**Returns**: The next valid node ID.

---

### `has_varying(name: String) -> bool`
Checks if a varying with the given name exists in the shader.

**Parameters**:
- `name`: The name of the varying.

**Returns**: `true` if the varying exists, otherwise `false`.

---

### `is_node_connection(type: Type, from_node: int, from_port: int, to_node: int, to_port: int) -> bool`
Checks if a specific node and port connection exists.

**Parameters**: Same as `connect_nodes()`.

**Returns**: `true` if the connection exists, otherwise `false`.

---

### `remove_node(type: Type, id: int)`
Removes a node with the specified ID from the graph.

**Parameters**:
- `type`: The type of node.
- `id`: The ID of the node to remove.

---

### `remove_varying(name: String)`
Removes a varying with the given name. If the name doesn restricted, an error may occur.

**Parameters**:
- `name`: The name of the varying.

---

### `replace_node(id: int, new_class: StringName)`
Replaces a node with a new class, effectively changing its type and functionality.

**Parameters**:
- `id`: The ID of the node to replace.
- `new_class`: The name of the new node class (e.g., `"Math"` or `"Texture"`).

---

### `set_mode(mode: int)`
Sets the mode of the shader (e.g., vertex, fragment, tessellation).

**Parameters**:
- `mode`: The mode constant (e.g., `MODE_VERTEX_SHADER`).

---

### `set_node_position(id: int, position: Vector2)`
Sets the position of a node in the graph.

**Parameters**:
- `id`: The ID of the node.
- `position`: The new position as a `Vector2`.

---

## Notes

- **Varying Names**: Varying names must follow the naming conventions of the shader language (e.g., GLSL/HLSL). They are case-sensitive.
- **Port Compatibility**: Ensure ports are compatible (e.g., input ports connect to output ports) when using `connect_nodes()`.
- **Error Handling**: `connect_nodes()` may return `Error.INVALID_CONNECTION` if ports are incompatible.
- **Node IDs**: Node IDs are auto-assigned if not provided during `add_node()`.

---

## Example Usage

```gdscript
# Create a vertex shader
var shader = VisualShader.new()
shader.set_mode(VisualShader.MODE_VERTEX_SHADER)

# Add a texture node
var texture_id = shader.add_node(VisualShader.Type.TEXTURE, 1)

# Add a math node
var math_id = shader.add_node(VisualShader.Type.MATH, 2)

# Connect texture to math node
shader.connect_nodes(VisualShader.TYPE_TEXTURE, texture_id, 0, math_id, 0)

# Get node position
var position = shader.get_node_position(VisualShader.TYPE_MATH, math_id)
print("Math node position:", position)
```

This documentation provides a comprehensive guide to using the `VisualShader` class in Godot, enabling developers to create complex shaders through a visual interface.