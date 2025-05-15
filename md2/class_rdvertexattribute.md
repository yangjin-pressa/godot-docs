# RDVertexAttribute

**Inherits:** RefCounted < Object

Vertex attribute (used by RenderingDevice).

## Description

This object is used by RenderingDevice.

## Properties

- **format**: DataFormat = 232
- **frequency**: VertexFrequency = 0
- **location**: int = 0
- **offset**: int = 0
- **stride**: int = 0

## Property Descriptions

- **format**  
  The way that this attribute's data is interpreted when sent to a shader.

- **frequency**  
  The rate at which this attribute is pulled from its vertex buffer.

- **location**  
  The location in the shader that this attribute is bound to.

- **offset**  
  The number of bytes between the start of the vertex buffer and the first instance of this attribute.

- **stride**  
  The number of bytes between the starts of consecutive instances of this attribute.

## Methods

- **set_format(value: DataFormat)**  
  Sets the data format for this attribute.

- **get_format()**  
  Returns the data format for this attribute.

- **set_frequency(value: VertexFrequency)**  
  Sets the vertex frequency for this attribute.

- **get_frequency()**  
  Returns the vertex frequency for this attribute.

- **set_location(value: int)**  
  Sets the shader location for this attribute.

- **get_location()**  
  Returns the shader location for this attribute.

- **set_offset(value: int)**  
  Sets the offset in bytes from the start of the vertex buffer.

- **get_offset()**  
  Returns the offset in bytes from the start of the vertex buffer.

- **set_stride(value: int)**  
  Sets the stride in bytes between consecutive instances of this attribute.

- **get_stride()**  
  Returns the stride in bytes between consecutive instances of this attribute.