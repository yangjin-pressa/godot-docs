PhysicsTestMotionResult3D  
Inherits from RefCounted  

**Description**  
A class representing the result of a physics motion test, providing details about collisions, movement, and safe/unsafe fractions.  

**Methods**  
- `get_collider_id() → int`  
  Returns the ID of the object. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_collision_point(collision_index=0) → Vector3`  
  Returns the point of collision in global coordinates. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_collision_normal(collision_index=0) → Vector3`  
  Returns the normal vector at the point of collision. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_collision_local_shape(collision_index=0) → int`  
  Returns the moving object's colliding shape. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_collision_safe_fraction() → float`  
  Returns the maximum fraction of motion that can occur without a collision, between 0 and 1. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_collision_unsafe_fraction() → float`  
  Returns the minimum fraction of motion needed to collide, between   
  0 and 1. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_remainder() → Vector3`  
  Returns the moving object's remaining movement vector. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_travel() → Vector3`  
  Returns the moving object's travel before collision. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_collider() → Object`  
  Returns the colliding object. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_collision_object(collision_index=0) → Object`  
  Returns the colliding object. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_collision_time(collision_index=0) → float`  
  Returns the time of collision. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)  

- `get_collision_time_remaining(collision_index=0) → float`  
  Returns the remaining time before collision. Virtual (This method should typically be overridden by the user to have any effect.) Const (This method has no side effects. It doesn't modify any of the instance's member variables.)