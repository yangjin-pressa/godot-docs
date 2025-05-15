# RDShaderFile

**Inherits**: Resource → RefCounted → Object

## Description
Compiled shader file in SPIR-V form (used by RenderingDevice). Not to be confused with Godot's own Shader resource.

See also: [RDShaderSource](#class_RDShaderSource)

## Properties
- **base_error**: String = ""

### Property Descriptions
- **base_error**: Base compilation error message. If non-empty, indicates errors not related to a specific shader stage. If empty, shader compilation may not be successful (check RDShaderSPIRV's error message members).

## Methods
- **get_spirv**(version: StringName = "") → RDShaderSPIRV
  - Returns SPIR-V intermediate representation for the specified shader version.

- **get_version_list**() → Array[StringName]
  - Returns list of compiled versions for this shader.

- **set_bytecode**(bytecode: RDShaderSPIRV, version: StringName = "") 
  - Sets SPIR-V bytecode for the specified version.

## Notes
- **See also**: RDShaderSource, RDShaderSPIRV