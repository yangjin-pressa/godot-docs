# RDShaderSource

**Inherits:** RefCounted < Object

Shader source code (used by RenderingDevice).

## Description

Shader source code in text form.

See also: RDShaderFile. RDShaderSource is only meant to be used with the RenderingDevice API. It should not be confused with Godot's own Shader resource, which is what Godot's various nodes use for high-level shader programming.

## Properties

- ShaderLanguage language = 0
  - The language the shader is written in.

- String source_compute = ""
  - Source code for the shader's compute stage.

- String source_fragment = ""
  - Source code for the shader's fragment stage.

- String source_tesselation_control = ""
  - Source code for the shader's tessellation control stage.

- String source_tesselation_evaluation = ""
  - Source code for the shader's tessellation evaluation stage.

- String source_vertex = ""
  - Source code for the shader's vertex stage.

## Methods

- String get_stage_source(ShaderStage stage) const
  - Returns source code for the specified shader stage. Equivalent to getting one of: source_compute, source_fragment, source_tesselation_control, source_tesselation_evaluation, or source_vertex.

- void set_stage_source(ShaderStage stage, String source)
  - Sets source code for the specified shader stage. Equivalent to setting one of: source_compute, source_fragment, source_tesselation_control, source_tesselation_evaluation, or source_vertex.

  **Note:** If you set the compute shader source code using this method directly, remember to remove the Godot-specific hint `#[compute]`.