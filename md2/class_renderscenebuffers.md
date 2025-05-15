# RenderSceneBuffers

**Inherits:** RefCounted < Object  
**Inherited By:** RenderSceneBuffersExtension, RenderSceneBuffersRD  

## Description  
Abstract scene buffers object created for each viewport with 3D rendering. Manages additional buffers during rendering and discards them when the viewport is resized.  

**Note:** Internal rendering server object; do not instantiate from scripts.  

## Methods  
- **configure** (config: RenderSceneBuffersConfiguration):  
  Called by the rendering server when viewport configuration changes. Discards old buffers and recreates internal buffers.  

## Method Descriptions  
- **configure**:  
  - **Type:** void  
  - **Parameters:** config (RenderSceneBuffersConfiguration)  
  - **Purpose:** Recreate buffers when viewport configuration changes.  
  - **Note:** This method should typically be overridden by the user. It has no side effects and does not modify instance variables.  

## Key Attributes  
- **Internal Use:** Only used by the rendering server.  
- **Instantiation:** Not meant to be created directly via scripting.