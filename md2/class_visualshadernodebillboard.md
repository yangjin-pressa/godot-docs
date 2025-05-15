**Class:** VisualShaderNodeBillboard  
**Inherits:** VisualShaderNode < Resource < RefCounted < Object  

**Description**  
The output port of this node needs to be connected to the *Model View Matrix* port of `VisualShaderNodeOutput`.  

---

**Properties**  
- **billboard_type**: `BillboardType` = `1`  
- **keep_scale**: `bool` = `false`  

---

**Enumerations**  
**BillboardType**  
- **BILLBOARD_TYPE_DISABLED** = `0`  
  Billboarding is disabled and the node does nothing.  
- **BILLBOARD_TYPE_ENABLED** = `1`  
  A standard billboarding algorithm is enabled.  
- **BILLBOARD_TYPE_FIXED_Y** = `2`  
  A billboarding algorithm to rotate around Y-axis is enabled.  
- **BILLBOARD_TYPE_PARTICLES** = `3`  
  A billboarding algorithm designed for particles is enabled.  
- **BILLBOARD_TYPE_MAX** = `4`  
  Represents the size of the `BillboardType` enum.  

---

**Property Descriptions**  
- **billboard_type**  
  Controls how the object faces the camera. See `BillboardType`.  

- **keep_scale**  
  If `true`, the shader retains the scale set for the mesh. Otherwise, scale is lost during billboarding.  

---

**Methods**  
- **set_billboard_type(value: BillboardType)**  
  Sets the billboard type.  

- **get_billboard_type()**  
  Returns the current billboard type.  

--- 

**Note**  
This node is used in visual shader graphs to control camera-facing behavior for objects.