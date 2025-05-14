# Node3DGizmo

**Inherits:** [RefCounted](class_RefCounted) < [Object](class_Object)  
**Inherited By:** [EditorNode3DGizmo](class_EditorNode3DGizmo)  

## Description  
Abstract class to expose editor gizmos for [Node3D](class_Node3D).  

Key notes:  
- **Node3DGizmo** has no exposed API.  
- Use [Node3D.add_gizmo()](class_Node3D_method_add_gizmo) and pass an [EditorNode3DGizmo](class_EditorNode3DGizmo) instance.  

## Relationships  
- **Inherits from:** RefCounted → Object  
- **Derived from:** EditorNode3DGizmo  

## References  
- [RefCounted](class_RefCounted)  
- [Object](class_Object)  
- [Node3D](class_Node3D)  
- [EditorNode3DGizmo](class_EditorNode3DGizmo)  

## Key Functionality  
- Abstract base class for 3D editor gizmo visualization.  
- Requires concrete implementation via derived classes.  
- Connects scene graph (Node3D) with editor interface.