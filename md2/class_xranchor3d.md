**XRAnchor3D**  
Inherits: XRNode3D → Node3D → Node → Object  

---

### Description  
An **XRAnchor3D** point maps a real-world location (identified by AR platform) to a position in the game world. For example:  
- ARKit updates plane positions and creates anchors for detected surfaces (tables, floors, etc.).  
- Nodes are linked to anchors via unique IDs. When a new anchor is detected, add this node to the scene.  
- Anchors update dynamically as plane detection learns about the real world, especially if only part of a surface is visible.  

---

### Tutorials  
- [XR documentation index](../tutorials/xr/index)  

---

### Methods  
- **get_plane()** → returns a plane aligned with the anchor (useful for intersection testing).  
- **get_size()** → returns the estimated size of the detected plane (e.g., a table's surface).  

--- 

### Key Notes  
- **Plane detection** (e.g., ARKit) enables dynamic updates to anchor size, position, and orientation.  
- Nodes are initialized at (0,0,0) until an anchor is detected.