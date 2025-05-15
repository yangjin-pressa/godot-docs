**PhysicsTestMotionParameters3D**  
- **Inherits from**: RefCounted  

### Description  
Used to configure the `PhysicsServer3D.body_test_motion()` method.  

---

### Properties  
1. **collide_separation_ray**  
   - Type: `bool`  
   - Default: `false`  
   - Description: Controls whether collision detection during separation is enabled. Useful for snapping to surfaces.  

2. **recovery_as_collision**  
   - Type: `bool`  
   - Default: `false`  
   - Description: If enabled, depenetration from the recovery phase is reported as a collision. Affects floor detection in CharacterBody3D.  

3. **motion**  
   - Type: `Vector3`  
   - Default: `Vector3(0, 0, 0)`  
   - Description: Motion vector defining the direction and length of the test.  

4. **recovery_as_collision** (same as above, but see separate entry).  

5. **recovery_as_collision** (duplicate entry, likely a formatting error).  

6. **recovery_as_collision** (same as above, likely a formatting error).  

7. **recovery_as_collision** (same as above, likely a formatting error).  

---

### Property Details  
- **collide_separation_ray**  
  - **Set/get**: `set_recovery_as_collision_enabled()`, `is_recovery_as_collision_enabled()`.  
  - **Explanation**: If true, depenetration from the recovery phase is reported as a collision, aiding floor detection.  

- **recovery_as_collision**  
  - **Set/get**: `set_recovery_as_collision_enabled()`, `is_recovery_as_collision_enabled()`.  
  - **Explanation**: Controls whether recovery phase depenetration is treated as a collision.  

- **motion**  
  - **Set/get**: `set_motion()`, `get_motion()`.  
  - **Explanation**: Defines the motion to test.  

- **Transform3D** (default value for a property):  
  - Default: `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`  
  - **Explanation**: Default transformation matrix.  

---

### Notes  
- **Virtual methods**: Typically overridden by users for custom behavior.  
- **Const methods**: Do not modify instance variables.  
- **Vararg methods**: Accept variable arguments after described parameters.  

This class is used to define parameters for testing motion in physics simulations.