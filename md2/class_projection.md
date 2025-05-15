The `Projection` class in Godot is a fundamental component for handling 3D transformations, particularly in rendering and camera systems. Below is a structured overview of its key aspects:

---

### **Constructor**
- **`Projection(const float matrix[16])`**:  
  Initializes the projection with a 4x4 matrix (represented as a flat array of 16 floats). This matrix defines the projection transformation.

---

### **Key Methods**

#### **Querying Properties**
- **`get_z_near()` / `get_z_far()`**:  
  Returns the near and far clipping distances. Positions beyond `z_far` or inside `z_near` are clipped.

- **`get_fovy()`**:  
  Returns the vertical field of view (in degrees). This is calculated based on the horizontal field of view and aspect ratio.

- **`get_viewport_half_extents()`**:  
  Returns half the dimensions of the viewport plane (used for screen space calculations).

- **`get_far_plane_half_extents()`**:  
  Returns half the dimensions of the far clipping plane.

- **`is_orthogonal()`**:  
  Returns `true` if the projection is an orthogonal projection (not perspective-based).

- **`get_lod_multiplier()`**:  
  Returns the scale factor for level of detail (LOD) based on the projection.

- **`get_pixels_per_meter(for_pixel_width)`**:  
  Calculates how many pixels per meter in the scene, based on the viewport's width on the near plane.

#### **Clipping Planes**
- **`get_projection_plane(plane)`**:  
  Returns a clipping plane (e.g., near, far, left, top, etc.).  
  **Constants**:  
  - `PLANE_NEAR`  
  - `PLANE_FAR`  
  - `PLANE_LEFT`  
  - `PLANE_TOP`  
  - `PLANE_RIGHT`  
  - `PLANE_BOTTOM`  

#### **Matrix Manipulation**
- **`inverse()`**:  
  Returns the inverse of the projection matrix, used for unprojecting coordinates.

- **`perspective_znear_adjusted(new_znear)`**:  
  Adjusts the near clipping distance to `new_znear` (requires a perspective projection).

- **`jitter_offseted(offset)`**:  
  Returns a projection with an offset added to the final column (useful for motion blur or jittering).

#### **Projection Types**
- **`is_orthogonal()`**:  
  Checks if the projection is orthogonal.

---

### **Operators**
- **`operator != (right)` / `operator == (right)`**:  
  Compares two projections for equality/inequality.  
  **Note**: Floating-point precision errors may cause false positives/negatives. Future support for `is_equal_approx` is planned.

- **`operator * (right)`**:  
  Combines two projections (matrix multiplication).

- **`operator * (right: Vector4)`**:  
  Applies the projection matrix to a 4D vector (e.g., transforming a 3D point to screen space).

- **`operator [] (index)`**:  
  Accesses a column of the matrix (indices: 0 = x, 1 = y, 2 = z, 3 = w).

---

### **Important Notes**
- **Floating-Point Precision**: Equality checks (`==`, `!=`) may fail due to precision errors. Use `is_equal_approx` if available.
- **Matrix Layout**: The matrix is stored as a flat array of 16 floats in column-major order.
- **Use Cases**: Projections are used in cameras, lighting, and post-processing to transform 3D coordinates to 2D screen space.

---

### **Example Usage**
```gdscript
# Create a perspective projection matrix
var matrix = [
    1, 0, 0, 0,
    0, 1, 0, 0,
    0, 0, 1, 0,
    0, 0, 0, 1
]

var proj = Projection(matrix)

# Get near clipping distance
var z_near = proj.get_z_near()

# Apply projection to a vector
var vec = Vector4(1, 2, 3, 1)
var projected = proj * vec
```

This class is essential for rendering 3D scenes, enabling transformations like perspective projection, clipping, and viewport calculations.