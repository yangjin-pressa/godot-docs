# VisualShaderNodeResizableBase

**Inherits:** VisualShaderNode < Resource < RefCounted < Object  

**Inherited By:**  
- VisualShaderNodeCurveTexture  
- VisualShaderNodeCurveXYZTexture  
- VisualShaderNodeFrame  
- VisualShaderNodeGroupBase  

## Description  
Resizable nodes have a handle that allows the user to adjust their size as needed.  

## Properties  
- **size**: Vector2 = Vector2(0, 0)  

## Property Descriptions  
**size**  
- **set_size**(value: Vector2): void  
- **get_size**(): Vector2  

The size of the node in the visual shader graph.  

## Method Notes  
- **set_size**: virtual method (overrideable)  
- **get_size**: const method (no side effects)