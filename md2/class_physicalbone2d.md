# PhysicalBone2D

## Inheritance
- RigidBody2D → PhysicsBody2D → CollisionObject2D → Node2D → CanvasItem → Node → Object

## Description
A RigidBody2D-derived node used to make Bone2D nodes in a Skeleton2D react to physics.

**Notes:**
1. Use SkeletonModification2DPhysicalBones to make Bone2D visually follow PhysicalBone2D.
2. PhysicalBone2D does not automatically create a Joint2D node; it must be manually added as a child. Use PinJoint2D for most cases.

## Properties
- **auto_configure_joint**: bool = true  
  Automatically configure first Joint2D child node.

- **bone2d_index**: int = -1  
  Index of Bone2D to simulate.

- **bone2d_nodepath**: NodePath = NodePath("")  
  Path to Bone2D to simulate.

- **follow_bone_when_simulating**: bool = false  
  Whether to follow Bone2D during simulation.

- **is_simulating_physics**: bool = false  
  Indicates if physics simulation is active.

## Methods
- **get_joint()**: Joint2D  
  Returns first Joint2D child node.

- **is_simulating_physics()**: bool  
  Returns whether physics simulation is active.

## Detailed Descriptions
### auto_configure_joint
Controls whether the first Joint2D child node is automatically configured when the PhysicalBone2D is created.

### bone2d_index
Specifies the index of the Bone2D node to associate with this PhysicalBone2D. A value of -1 means no Bone2D is associated.

### bone2d_nodepath
Provides a path to the Bone2D node that this PhysicalBone2D should simulate. If empty, no Bone2D is associated.

### follow_bone_when_simulating
Determines if the PhysicalBone2D should follow the Bone2D node during simulation. This is useful for maintaining visual alignment.

### is_simulating_physics
Returns a boolean indicating whether the PhysicalBone2D is actively simulating physics. This is useful for checking the state of the node.

### get_joint
Retrieves the first Joint2D child node associated with this PhysicalBone2D. This is useful for accessing the joint directly without manual traversal.

### is_simulating_physics
Returns whether the PhysicalBone2D is currently using the Godot 2D physics engine for simulation. This is useful for checking the active state of the node.