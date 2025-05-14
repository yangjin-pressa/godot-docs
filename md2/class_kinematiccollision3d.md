**KinematicCollision3D**

**Inheritance**  
- `RefCounted`

**Description**  
The `KinematicCollision3D` class is used to detect collisions with 3D objects in a physics-based environment. It is typically used in conjunction with `PhysicsBody3D` to track collision data. Collisions are detected during movement, and the class provides methods to retrieve collision details such as the point of contact, normal, and remaining movement vector.

---

**Methods**

1. **`get_angle()`**  
   - **Return**: `Vector3`  
   - **Description**: Returns the collision angle based on the `up_direction` vector. The angle is calculated relative to the collision normal.

2. **`get_collision_count()`**  
   - **Return**: `int`  
   - **Description**: Returns the number of detected collisions during the last movement step.

3. **`get_depth()`**  
   - **Return**: `float`  
   - **Description**: Returns the length of overlap along the collision normal at the point of contact.

4. **`get_remainder()`**  
   - **Return**: `Vector3`  
   - **Description**: Returns the remaining movement vector of the moving object after collision.

5. **`get_travel()`**  
   - **Return**: `Vector3`  
   - **Description**: Returns the total movement vector of the moving object before collision.

6. **`get_position()`**  
   - **Return**: `Vector3`  
   - **Description**: Returns the global coordinates of the collision point.

7. **`get_normal()`**  
   - **Return**: `Vector3`  
   - **Description**: Returns the normal vector of the colliding object at the point of contact.

8. **`get_local_shape()`**  
   - **Return**: `Object`  
   - **Description**: Returns the colliding shape of the moving object.

9. **`get_local_shape()`**  
   - **Return**: `Object`  
   - **Description**: Returns the colliding shape of the moving object (second occurrence of the same method, possibly redundant).

10. **`get_collider()`**  
    - **Return**: `Object`  
    - **Description**: Returns the colliding object.

11. **`get_collider_velocity()`**  
    - **Return**: `Vector3`  
    - **Description**: Returns the velocity of the colliding object.

12. **`get_collider_position()`**  
    - **Return**: `Vector3`  
    - **Description**: Returns the position of the colliding object at the point of contact.

13. **`get_collider_normal()`**  
    - **Return**: `Vector3`  
    - **Description**: Returns the normal vector of the colliding object.

14. **`get_collider_depth()`**  
    - **Return**: `float`  
    - **Description**: Returns the depth of overlap between the moving and colliding objects.

15. **`get_collider_travel()`**  
    - **Return**: `Vector3`  
    - **Description**: Returns the movement vector of the colliding object before collision.

---

**Notes**  
- Methods like `get_angle()` and `get_normal()` allow for detailed analysis of collision orientation.  
- The class is designed for use in physics simulations where precise collision data is required.  
- Collision data is retrieved in global coordinates, making it easier to integrate with other spatial calculations.