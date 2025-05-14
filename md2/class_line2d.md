### Godot Line2D Class Documentation

---

#### **Properties**

1. **antialiased**  
   - **Type**: `bool`  
   - **Default**: `false`  
   - **Description**: Enables antialiasing for the polyline. When enabled, edges are smoother, reducing jaggedness.

2. **points**  
   - **Type**: `PackedVector2Array`  
   - **Default**: `PackedVector2Array()`  
   - **Description**: Array of 2D points defining the polyline. Segments are drawn between adjacent points.  
   - **Note**: The returned array is a copy; modifications do not affect the original.

3. **width**  
   - **Type**: `float`  
   - **Default**: `10.0`  
   - **Description**: The uniform width of the polyline.

4. **texture**  
   - **Type**: `Texture2D`  
   - **Description**: Texture applied to the polyline. Uses `texture_mode` for rendering style.

5. **texture_mode**  
   - **Type**: `LineTextureMode`  
   - **Default**: `0` (TEXTURE_MODE_NONE)  
   - **Description**: Controls how the texture is applied (e.g., repeat, none).

6. **width_curve**  
   - **Type**: `Curve`  
   - **Description**: A unit curve defining the polyline's width variation along its length.

7. **round_precision**  
   - **Type**: `int`  
   - **Default**: `8`  
   - **Description**: Smoothness of rounded joints and caps. Higher values result in smoother corners.

8. **sharp_limit**  
   - **Type**: `float`  
   - **Default**: `2.0`  
   - **Description**: Miter limit for sharp angles. Higher values delay fallback to bevel joints.

9. **joint_mode**  
   - **Type**: `LineJointMode`  
   - **Default**: `0` (LINE_JOINT_SMOOTH)  
   - **Description**: Style of connections between polyline segments (e.g., sharp, bevel, smooth).

---

#### **Enums**

1. **LineJointMode**  
   - **LINE_JOINT_SMOOTH**: Smooth transitions between segments.  
   - **LINE_JOINT_BEVEL**: Bevel (angled) joints.  
   - **LINE_JOINT_SHARP**: Sharp corners (may fallback to bevel if angles are too acute).

2. **LineTextureMode**  
   - **TEXTURE_MODE_NONE**: No texture.  
   - **TEXTURE_MODE_REPEAT**: Texture repeats.  
   - **TEXTURE_MODE_TILE**: Texture tiles (e.g., for patterns).

3. **LineWidthMode**  
   - **LINE_WIDTH_UNIFORM**: Uniform width.  
   - **LINE_WIDTH_VARYING**: Width varies based on the `width_curve`.

---

#### **Methods**

1. **add_point(position: Vector2, index: int = -1)**  
   - **Description**: Adds a point to the polyline. If `index` is provided, inserts the point at that position; otherwise, appends it.

2. **clear_points()**  
   - **Description**: Removes all points from the polyline.

3. **get_point_count()**  
   - **Return Type**: `int`  
   - **Description**: Returns the number of points in the polyline.

4. **get_point_position(index: int) -> Vector2**  
   - **Description**: Retrieves the position of the point at the specified index.

5. **remove_point(index: int)**  
   - **Description**: Removes the point at the given index.

---

#### **Key Notes**

- **Texture Handling**: The `texture_mode` determines how the `texture` is applied (e.g., repeat, none).
- **Width Variation**: The `width_curve` allows dynamic width adjustments along the polyline's path.
- **Point Manipulation**: Methods like `add_point`, `remove_point`, and `set_point_position` provide detailed control over the polyline's shape.
- **Antialiasing**: The `antialiased` property improves visual quality by smoothing edges.

This class is essential for creating and manipulating 2D line-based graphics in Godot, with flexibility in styling, texture, and dynamic behavior.