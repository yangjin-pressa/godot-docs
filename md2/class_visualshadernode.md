# VisualShaderNode Class Documentation

## Overview
The `VisualShaderNode` class serves as the base class for all nodes in the VisualShader graph editor. It provides common functionality for managing input ports, linking to frames, and setting preview output ports.

---

## Properties

### `linked_parent_graph_frame`
**Type:** `int`  
**Default Value:** `-1`  
**Description:** Represents the index of the frame this node is linked to. If set to `-1`, the node is not linked to any frame.

**Accessors:**
- `set_frame(value: int)`
- `get_frame()`

---

### `output_port_for_preview`
**Type:** `int`  
**Default Value:** `-1`  
**Description:** Sets the output port index which will be shown for preview. If set to `-1`, no port will be open for preview.

**Accessors:**
- `set_output_port_for_preview(value: int)`
- `get_output_port_for_preview()`

---

## Enums

### `PortType`
**Description:** Enum that defines the data type of ports in the VisualShader graph.

**Constants:**
- **PORT_TYPE_SCALAR** = `0`  
  Floating-point scalar. Translated to `float` in shader code.
  
- **PORT_TYPE_SCALAR_INT** = `1`  
  Integer scalar. Translated to `int` in shader code.
  
- **PORT_TYPE_SCALAR_UINT** = `2`  
  Unsigned integer scalar. Translated to `uint` in shader code.
  
- **PORT_TYPE_VECTOR_2D** = `3`  
  2D vector of floating-point values. Translated to `vec2` in shader code.
  
- **PORT_TYPE_VECTOR_3D** = `4`  
  3D vector of floating-point values. Translated to `vec3` in shader code.
  
- **PORT_TYPE_VECTOR_4D** = `5`  
  4D vector of floating-point values. Translated to `vec4` in shader code.
  
- **PORT_TYPE_BOOLEAN** = `6`  
  Boolean type. Translated to `bool` in shader code.
  
- **PORT_TYPE_TRANSFORM** = `7`  
  Transform type. Translated to `mat4` in shader code.
  
- **PORT_TYPE_SAMPLER** = `8`  
  Sampler type. Translated to reference of sampler uniform in shader code. Can only be used for input ports in non-uniform nodes.
  
- **PORT_TYPE_MAX** = `9`  
  Represents the size of the `PortType` enum.

---

## Methods

### `clear_default_input_values()`
**Description:** Clears the default input ports values.

---

### `get_default_input_port(type: PortType) -> int`
**Description:** Returns the input port which should be connected by default when this node is created as a result of dragging a connection from an existing node to the empty space on the graph.

---

### `get_default_input_values() -> Array`
**Description:** Returns an `Array` containing default values for all of the input ports of the node in the form `[index0, value0, index1, value1, ...]`.

---

### `get_input_port_default_value(port: int) -> Variant`
**Description:** Returns the default value of the input `port`.

---

### `remove_input_port_default_value(port: int)`
**Description:** Removes the default value of the input `port`.

---

### `set_default_input_values(values: Array)`
**Description:** Sets the default input ports values using an `Array` of the form `[index0, value0, index1, value1, ...]`. For example: `[0, Vector3(0, 0, 0), 1, Vector3(0, 0, 0)]`.

---

### `set_input_port_default_value(port: int, value: Variant, prev_value: Variant = null)`
**Description:** Sets the default `value` for the selected input `port`.

---

## Notes
- The `PortType` enum defines how ports are translated into shader code, ensuring compatibility with GLSL syntax.
- The `linked_parent_graph_frame` property is used for linking nodes to specific frames in the graph, which is useful for complex node hierarchies.
- The `output_port_for_preview` property helps in previewing specific output ports during shader development.