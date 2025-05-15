**Class Name:** PhysicsDirectSpaceState2DExtension  
**Inherits From:** PhysicsDirectSpaceState2D < Object  

**Description:**  
Extends PhysicsDirectSpaceState2D to allow overriding virtual methods for custom physics space state implementations. Intended for use with GDExtension.  

---

**Methods:**  

1. **_cast_motion**  
   - **Return Type:** bool  
   - **Parameters:**  
     - shape_rid: RID  
     - transform: Transform2D  
     - motion: Vector2  
     - margin: float  
     - collision_mask: int  
     - collide_with_bodies: bool  
     - collide_with_areas: bool  
     - closest_safe: float*  
     - closest_unsafe: float*  
   - **Note:** Virtual method (override recommended)  

2. **_collide_shape**  
   - **Return Type:** bool  
   - **Parameters:**  
     - shape_rid: RID  
     - transform: Transform2D  
     - motion: Vector2  
     - margin: float  
     - collision_mask: int  
     - collide_with_bodies: bool  
     - collide_with_areas: bool  
     - results: void*  
     - max_results: int  
     - result_count: int32_t*  
   - **Note:** Virtual method (override recommended)  

3. **_intersect_point**  
   - **Return Type:** int  
   - **Parameters:**  
     - position: Vector2  
     - canvas_instance_id: int  
     - collision_mask: int  
     - collide_with_bodies: bool  
     - collide_with_areas: bool  
     - results: PhysicsServer2DExtensionShapeResult*  
     - max_results: int  
   - **Note:** Virtual method (override recommended)  

4. **_intersect_ray**  
   - **Return Type:** bool  
   - **Parameters:**  
     - from: Vector2  
     - to: Vector2  
     - collision_mask: int  
     - collide_with_bodies: bool  
     - collide_with_areas: bool  
     - hit_from_inside: bool  
     - result: PhysicsServer2DExtensionRayResult*  
   - **Note:** Virtual method (override recommended)  

5. **_intersect_shape**  
   - **Return Type:** int  
   - **Parameters:**  
     - shape_rid: RID  
     - transform: Transform2D  
     - motion: Vector2  
     - margin: float  
     - collision_mask: int  
     - collide_with_bodies: bool  
     - collide_with_areas: bool  
     - result: PhysicsServer2DExtensionShapeResult*  
     - max_results: int  
   - **Note:** Virtual method (override recommended)  

6. **_rest_info**  
   - **Return Type:** bool  
   - **Parameters:**  
     - shape_rid: RID  
     - transform: Transform2D  
     - motion: Vector2  
     - margin: float  
     - collision_mask: int  
     - collide_with_bodies: bool  
     - collide_with_areas: bool  
     - rest_info: PhysicsServer2DExtensionShapeRestInfo*  
   - **Note:** Virtual method (override recommended)  

7. **is_body_excluded_from_query**  
   - **Return Type:** bool  
   - **Parameters:**  
     - body: RID  
   - **Note:** Const method (no side effects)  

---

**Notes:**  
All methods except `is_body_excluded_from_query` are marked as virtual. Most methods currently lack descriptions; contributors are encouraged to add details.