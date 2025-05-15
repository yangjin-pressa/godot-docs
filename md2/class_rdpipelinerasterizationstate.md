# RDPipelineRasterizationState

**Inherits:** RefCounted < Object

Pipeline rasterization state (used by RenderingDevice).

## Description

This object is used by RenderingDevice.

## Properties

- **cull_mode**: PolygonCullMode = 0
- **depth_bias_clamp**: float = 0.0
- **depth_bias_constant_factor**: float = 0.0
- **depth_bias_enabled**: bool = false
- **depth_bias_slope_factor**: float = 0.0
- **discard_primitives**: bool = false
- **enable_depth_clamp**: bool = false
- **front_face**: PolygonFrontFace = 0
- **line_width**: float = 1.0
- **patch_control_points**: int = 1
- **wireframe**: bool = false

## Property Descriptions

### cull_mode
**Type:** PolygonCullMode  
**Default:** 0  
**Description:** The cull mode to use when drawing polygons, which determines whether front faces or backfaces are hidden.

### depth_bias_clamp
**Type:** float  
**Default:** 0.0  
**Description:** A limit for how much each depth value can be offset. If negative, it serves as a minimum value, but if positive, it serves as a maximum value.

### depth_bias_constant_factor
**Type:** float  
**Default:** 0.0  
**Description:** A factor used in depth bias calculations.

### depth_bias_enabled
**Type:** bool  
**Default:** false  
**Description:** Whether depth bias is enabled.

### depth_bias_slope_factor
**Type:** float  
**Default:** 0.0  
**Description:** A slope factor used in depth bias calculations.

### discard_primitives
**Type:** bool  
**Default:** false  
**Description:** Whether primitives are discarded.

### enable_depth_clamp
**Type:** bool  
**Default:** false  
**Description:** Whether depth clamping is enabled.

### front_face
**Type:** PolygonFrontFace  
**Default:** 0  
**Description:** The winding order to use to determine which face of a triangle is considered its front face.

### line_width
**Type:** float  
**Default:** 1.0  
**Description:** The line width to use when drawing lines (in pixels). Thick lines may not be supported on all hardware.

### patch_control_points
**Type:** int  
**Default:** 1  
**Description:** The number of control points to use when drawing a patch with tessellation enabled. Higher values result in higher quality at the cost of performance.

### wireframe
**Type:** bool  
**Default:** false  
**Description:** If true, performs wireframe rendering for triangles instead of flat or textured rendering.