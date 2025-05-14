# GLTFBufferView

## Inheritance
- Inherits from: `Object` (assuming base class, though not explicitly stated in original)

## Description
A class representing a buffer view in a GLTF (GL Transmission Format) 3D model. It defines how a buffer is accessed and used in the scene. Key properties include:
- **buffer**: Reference to the buffer.
- **byteOffset**: Offset in bytes within the buffer.
- **byteLength**: Length in bytes of the data.
- **byteStride**: Stride between consecutive elements in the buffer.

Used for efficiently managing and accessing binary data in 3D models.

## Tutorials
- [Buffers, BufferViews, and Accessors in Khronos glTF specification](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_005_BuffersBufferViewsAccessors.md)
- [GLTF 2.0 Specification](https://github.com/KhronosGroup/glTF/tree/master/specification)

## Properties
- **buffer**: `int` (default: 0) - Reference to the buffer.
- **byteOffset**: `int` (default: 0) - Offset in bytes within the buffer.
- **byteLength**: `int` (default: 0) - Length in bytes of the data.
- **byteStride**: `int` (default: 0) - Stride between consecutive elements.

## Methods
- **load_buffer_view_data(state: `GLTFState`)**: `ArrayBuffer` - Loads buffer data from the specified state, returning it as an `ArrayBuffer`. Interleaved data with stride is not supported yet.

## Notes
- This class is used in 3D modeling to manage binary data access efficiently.
- The `load_buffer_view_data` method is const and does not modify instance variables.