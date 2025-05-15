# RDShaderSPIRV Class Documentation

The `RDShaderSPIRV` class represents a shader program compiled into SPIR-V format, which is a standard intermediate language for shaders. This class provides access to the compiled bytecode and compilation errors for different shader stages (vertex, fragment, tessellation control, tessellation evaluation, and compute).

---

## Class Overview

- **Purpose**: Stores SPIR-V bytecode and compilation errors for various shader stages.
- **Key Features**:
  - Access to individual shader stage bytecode and error messages.
  - Methods to retrieve and set bytecode for specific stages.
  - Methods to retrieve and set compilation errors for specific stages.
- **Usage**: Used internally by Godot to manage shader programs compiled to SPIR-V.

---

## Properties

### Bytecode Properties

- **`bytecode_compute`**: SPIR-V bytecode for the compute shader stage.
- **`bytecode_fragment`**: SPIR-V bytecode for the fragment shader stage.
- **`bytecode_tesselation_control`**: SPIR-V bytecode for the tessellation control shader stage.
- **`bytecode_tesselation_evaluation`**: SPIR-V bytecode for the tessellation evaluation shader stage.
- **`bytecode_vertex`**: SPIR-V bytecode for the vertex shader stage.

**Type**: `PackedByteArray`  
**Description**: Binary data representing the SPIR-V shader code for the corresponding stage.

---

### Compilation Error Properties

- **`compile_error_compute`**: Compilation error message for the compute shader stage.
- **`compile_error_fragment`**: Compilation error message for the fragment shader stage.
- **`compile_error_tesselation_control`**: Compilation error message for the tessellation control shader stage.
- **`compile_error_tesselation_evaluation`**: Compilation error message for the tessellation evaluation shader stage.
- **`compile_error_vertex`**: Compilation error message for the vertex shader stage.

**Type**: `String`  
**Description**: If empty, the shader compiled successfully. Otherwise, contains the error message from the SPIR-V compiler or Godot.

---

## Methods

### `get_stage_bytecode(stage: ShaderStage) -> PackedByteArray`

**Description**: Retrieves the SPIR-V bytecode for the specified shader stage.
- **Parameters**:
  - `stage`: The shader stage (e.g., `VERTEX`, `FRAGMENT`, etc.).
- **Returns**: The corresponding bytecode as a `PackedByteArray`.

**Equivalent to**: Directly accessing the relevant property (e.g., `bytecode_vertex`).

---

### `get_stage_compile_error(stage: ShaderStage) -> String`

**Description**: Retrieves the compilation error message for the specified shader stage.
- **Parameters**:
  - `stage`: The shader stage.
- **Returns**: The error message (empty if compilation was successful).

**Equivalent to**: Directly accessing the relevant property (e.g., `compile_error_vertex`).

---

### `set_stage_bytecode(stage: ShaderStage, bytecode: PackedByteArray)`

**Description**: Sets the SPIR-V bytecode for the specified shader stage.
- **Parameters**:
  - `stage`: The shader stage.
  - `bytecode`: The SPIR-V bytecode as a `PackedByteArray`.
- **Note**: This method is typically used to replace the bytecode for a specific stage.

**Equivalent to**: Directly setting the relevant property (e.g., `bytecode_vertex`).

---

### `set_stage_compile_error(stage: ShaderStage, compile_error: String)`

**Description**: Sets the compilation error message for the specified shader stage.
- **Parameters**:
  - `stage`: The shader stage.
  - `compile_error`: The error message (empty for successful compilation).
- **Note**: Error messages are typically set by the SPIR-V compiler or Godot, not by the user.

**Equivalent to**: Directly setting the relevant property (e.g., `compile_error_vertex`).

---

## Key Notes

1. **Stage Enum**: The `ShaderStage` enum includes the following values:
   - `VERTEX`
   - `FRAGMENT`
   - `TESSELATION_CONTROL`
   - `TESSELATION_EVALUATION`
   - `COMPUTE`

2. **Bytecode Format**: The `PackedByteArray` contains the raw SPIR-V binary data. Ensure the data is correctly formatted for the target shader stage.

3. **Error Handling**: Compilation errors are set by the SPIR-V compiler or Godot. Users should not manually set these errors unless explicitly required.

4. **Empty Error Messages**: An empty string indicates successful compilation.

---

## Example Usage

```gdscript
# Example: Set bytecode and error for a vertex shader
var vertex_bytecode = ... # Binary SPIR-V data
var vertex_error = "Invalid vertex shader code"

shader.set_stage_bytecode(ShaderStage.VERTEX, vertex_bytecode)
shader.set_stage_compile_error(ShaderStage.VERTEX, vertex_error)

# Retrieve bytecode and error
var bytecode = shader.get_stage_bytecode(ShaderStage.VERTEX)
var error = shader.get_stage_compile_error(ShaderStage.VERTEX)
```

---

## See Also

- [ShaderStage](https://godotengine.org/documentation_en/classes/class_shaderstage.html): Enum representing shader stages.
- [PackedByteArray](https://godotengine.org/documentation_en/classes/class_packedbytearray.html): Godot class for binary data.