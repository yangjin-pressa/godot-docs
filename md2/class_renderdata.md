**Class: RenderData**  

**Description**  
Abstract render data object, exists for the duration of rendering a single viewport.  
**Note:** This is an internal rendering server object, do not instantiate this from script.  

**Methods**  
- `get_camera_attributes()` → Returns the `RID` of the camera attributes object in the `RenderingServer` being used to render this viewport.  
- `get_environment()` → Returns the `RID` of the environment object in the `RenderingServer` being used to render this viewport.  
- `get_render_scene_buffers()` → Returns the `RenderSceneBuffers` object managing the scene buffers for rendering this viewport.  
- `get_render_scene_data()` → Returns the `RenderSceneData` object managing this frame's scene data.  

**Method Descriptions**  
- `get_camera_attributes()`: Returns the `RID` of the camera attributes object in the `RenderingServer` being used to render this viewport.  
- `get_environment()`: Returns the `RID` of the environment object in the `RenderingServer` being used to render this viewport.  
- `get_render_scene_buffers()`: Returns the `RenderSceneBuffers` object managing the scene buffers for rendering this viewport.  
- `get_render_scene_data()`: Returns the `RenderSceneData` object managing this frame's scene data.  

**Inherits**  
`Object`  

**Inherited By**  
`RenderDataExtension`, `RenderDataRD`