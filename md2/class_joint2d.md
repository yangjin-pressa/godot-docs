# Joint2D

## Hierarchy
- **Inherits:** Node2D < CanvasItem < Node < Object
- **Inherited By:** DampedSpringJoint2D, GrooveJoint2D, PinJoint2D

## Description
Abstract base class for all 2D physics joints. 2D joints bind together two physics bodies (node_a and node_b) and apply a constraint.

## Properties
- **bias**: float = 0.0  
  Controls how fast the joint pulls bodies back to their original position when they move in different directions. Default is from ProjectSettings.
- **disable_collision**: bool = true  
  If true, the two bodies bound by the joint do not collide with each other.
- **node_a**: NodePath = ""  
  Path to the first body (A) attached to the joint. Must inherit PhysicsBody2D.
- **node_b**: NodePath = ""  
  Path to the second body (B) attached to the joint. Must inherit PhysicsBody2D.

## Methods
- **get_rid()**: returns RID  
  Returns the joint's internal RID from the PhysicsServer2D.

## Property Descriptions
- **bias**  
  Adjusts the joint's response to relative movement between node_a and node_b. Lower values allow more movement.

- **disable_collision**  
  Disables collision between the two bodies connected by the joint.

- **node_a**  
  Specifies the first body (A) connected to the joint. Must be a PhysicsBody2D.

- **node_b**  
  Specifies the second body (B) connected to the joint. Must be a PhysicsBody2D.

## Method Descriptions
- **get_rid()**  
  Retrieves the joint's unique identifier (RID) for use with the PhysicsServer2D.