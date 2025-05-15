**PhysicsDirectSpaceState3DExtension**  
**Description**: A class for customizing physics behavior in 3D space, typically used in game engines like Godot. It provides virtual methods for advanced physics operations.  

---

**Methods**  
1. **_rest_info**  
   - **Parameters**:  
     - `shape_rid`: `RID`  
     - `transform`: `Transform3D`  
     - `motion`: `Vector3`  
     - `margin`: `float`  
     - `collision_mask`: `int`  
     - `collide_with_bodies`: `bool`  
     - `collide_with_areas`: `bool`  
     - `rest_info`: `PhysicsServer3DExtensionShapeRestInfo*`  
   - **Return Type**: `bool`  
   - **Note**: Virtual method (overrides default behavior).  

2. **_intersect_shape**  
   - **Parameters**:  
     - `shape_rid`: `RID`  
     - `transform`: `Transform3D`  
     - `motion`: `Vector3`  
     - `margin`: `float`  
     - `collision_mask`: `int`  
     - `collide_with_bodies`: `bool`  
     - `collide_with_areas`: `bool`  
     - `result_count`: `PhysicsServer3DExtensionShapeResult*`  
     - `max_results`: `int`  
   - **Return Type**: `int`  
   - **Note**: Virtual method.  

3. **_intersect_ray**  
   - **Parameters**:  
     - `from`: `Vector3`  
     - `to`: `Vector3`  
     - `collision_mask`: `int`  
     - `collide_with_bodies`: `bool`  
     - `collide_with_areas`: `bool`  
     - `hit_from_inside`: `bool`  
     - `hit_back_faces`: `bool`  
     - `pick_ray`: `bool`  
     - `result`: `PhysicsServer3DExtensionRayResult*`  
   - **Return Type**: `bool`  
   - **Note**: Virtual method.  

4. **_intersect_point**  
   - **Parameters**:  
     - `position`: `Vector3`  
     - `collision_mask`: `int`  
     - `collide_with_bodies`: `bool`  
     - `collide_with_areas`: `bool`  
     - `results`: `PhysicsServer3DExtensionShapeResult*`  
     - `max_results`: `int`  
   - **Return Type**: `int`  
   - **Note**: Virtual method.  

5. **_get_closest_point_to_object_volume**  
   - **Parameters**:  
     - `object`: `RID`  
     - `point`: `Vector3`  
   - **Return Type**: `Vector3`  
   - **Note**: `const` method (no side effects).  

6. **is_body_excluded_from_query**  
   - **Parameters**:  
     - `body`: `RID`  
   - **Return Type**: `bool`  
   - **Note**: `const` method.  

---

**Notes**  
- Most methods lack descriptions. For example, the method `_rest_info` has no description.  
- Descriptions can be contributed via: [contributing one](doc_updating_the_class_reference).  
- All methods are either `virtual` (overrideable) or `const` (no side effects).  

---  
**References**:  
- [PhysicsDirectSpaceState3D](class_PhysicsDirectSpaceState3D)  
- [PhysicsServer3DExtensionShapeRestInfo](class_PhysicsServer3DExtensionShapeRestInfo)  
- [PhysicsServer3DExtensionShapeResult](class_PhysicsServer3DExtensionShapeResult)