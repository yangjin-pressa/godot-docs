# Joint3D

**Inherits:** Node3D < Node < Object  
**Inherited By:** ConeTwistJoint3D, Generic6DOFJoint3D, HingeJoint3D, PinJoint3D, SliderJoint3D  

## Description  
Abstract base class for 3D physics joints. Binds two physics bodies (node_a and node_b) and applies a constraint. If only one body is defined, it is attached to a fixed StaticBody3D without collision shapes.

## Tutorials  
- [3D Truck Town Demo](https://godotengine.org/asset-library/asset/2752)

## Properties  
- **exclude_nodes_from_collision**: bool = true  
  If true, the two bodies bound together do not collide with each other.  

- **node_a**: NodePath = ""  
  Path to the first node (A). Must inherit PhysicsBody3D.  
  If empty and node_b is set, the body is attached to a fixed StaticBody3D.  

- **node_b**: NodePath = ""  
  Path to the second node (B). Must inherit PhysicsBody3D.  
  If empty and node_a is set, the body is attached to a fixed StaticBody3D.  

- **solver_priority**: int = 1  
  Lower values indicate higher priority for constraint solving.

## Methods  
- **get_rid()** → RID  
  Returns the joint's internal RID from the PhysicsServer3D.

## Property Descriptions  
- **exclude_nodes_from_collision**:  
  - set_exclude_nodes_from_collision(value: bool)  
  - get_exclude_nodes_from_collision()  

- **node_a**:  
  - set_node_a(value: NodePath)  
  - get_node_a()  

- **node_b**:  
  - set_node_b(value: NodePath)  
  - get_node_b()  

- **solver_priority**:  
  - set_solver_priority(value: int)  
  - get_solver_priority()  

## Method Descriptions  
- **get_rid()**:  
  Returns the joint's internal RID from the PhysicsServer3D.