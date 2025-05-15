# RenderSceneDataRD

**Inherits:** RenderSceneData < Object

## Description

Object holds scene data related to rendering a single frame of a viewport.

Note: This is an internal rendering server object, do not instantiate this from script.

## Key Attributes

- **Purpose**: Stores scene data for rendering a single frame in a viewport
- **Usage**: Internal rendering server object (not meant for direct instantiation)
- **Functionality**: Manages rendering state and resources for a viewport frame

## Method Definitions

- **Constructor**: 
  - `RenderSceneDataRD()`: Creates a new render scene data object

- **Properties**: 
  - `viewport_id`: Identifier for the viewport
  - `camera_id`: Identifier for the camera
  - `render_target`: Target surface for rendering

## References

- :ref:`RenderSceneData<class_RenderSceneData>` 
- :ref:`Object<class_Object>`