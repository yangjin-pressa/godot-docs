# CylinderMesh

**Inherits:** PrimitiveMesh < Mesh < Resource < RefCounted < Object

## Description
Class representing a cylindrical PrimitiveMesh. Can create cones by setting either the top_radius or bottom_radius properties to 0.0.

## Properties
- **bottom_radius**: float = 0.5  
- **cap_bottom**: bool = true  
- **cap_top**: bool = true  
- **height**: float = 2.0  
- **radial_segments**: int = 64  
- **rings**: int = 4  
- **top_radius**: float = 0.5  

## Property Descriptions

**bottom_radius** (float)  
- Sets the bottom radius of the cylinder. If set to 0.0, the bottom faces will not be generated. See also cap_bottom.

**cap_bottom** (bool)  
- If true, generates a cap at the bottom of the cylinder. Note: If bottom_radius is 0.0, cap generation is skipped even if cap_bottom is true.

**cap_top** (bool)  
- If true, generates a cap at the top of the cylinder. Note: If top_radius is 0.0, cap generation is skipped even if cap_top is true.

**height** (float)  
- Full height of the cylinder.

**radial_segments** (int)  
- Number of radial segments on the cylinder. Higher values increase detail but affect performance.

**rings** (int)  
- Number of edge rings along the cylinder's height. Adjusting this does not affect visual appearance unless shaders or tools modify vertex data.

**top_radius** (float)  
- Top radius of the cylinder. If set to 0.0, the top faces will not be generated. See also cap_top.