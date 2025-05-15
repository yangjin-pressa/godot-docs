# SpringArm3D

**Inherits:** Node3D < Node < Object

## Description
A 3D raycast that dynamically moves its children near the collision point. Useful for 3rd person cameras that adjust proximity to the player in tight spaces. Can exclude the player's collider from collision checks.

## Tutorials
- [Third-person camera with spring arm](../tutorials/3d/spring_arm)

## Properties
- **collision_mask**: int = 1  
  Layers to check for collisions. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) for details.
- **margin**: float = 0.01  
  Subtracted from collision length to position children. Prevents camera placement on exact collision points.
- **shape**: Shape3D  
  Shape used for collision checks. Defaults to ray cast if not set.
- **spring_length**: float = 1.0  
  Maximum length for the spring arm. Used for internal calculations.

## Methods
- **add_excluded_object(RID)**  
  Adds a PhysicsBody3D to the list of excluded objects from collision checks.
- **clear_excluded_objects()**  
  Removes all excluded objects.
- **get_hit_length()**  
  Returns the current length of the spring arm.
- **remove_excluded_object(RID)**  
  Removes a specified excluded object.

## Property Descriptions
**collision_mask**  
Sets/get the collision mask. Defines which layers are considered for collision checks.

**margin**  
Sets/get the margin value. Adjusts the position of child nodes relative to the collision point.

**shape**  
Sets/get the collision shape. Changes the collision detection method from ray to shape-based.

**spring_length**  
Sets/get the spring length. Determines the maximum extent of the spring arm.

## Method Descriptions
**add_excluded_object**  
Adds a PhysicsBody3D to the excluded list. Useful for avoiding collisions with specific objects.

**clear_excluded_objects**  
Resets the excluded objects list. Ensures all objects are considered in collision checks.

**get_hit_length**  
Returns the current spring arm length. Provides the current position of the spring arm.

**remove_excluded_object**  
Removes a specific PhysicsBody3D from the excluded list. Adjusts collision checks to include the object.