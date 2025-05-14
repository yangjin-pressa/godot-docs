# Curve3D Class Documentation

The `Curve3D` class represents a 3D curve, enabling the manipulation and retrieval of points along the curve. It provides methods to sample points, manage tangents, and tessellate the curve for rendering. Below is a detailed description of its properties and methods.

---

## **Properties**

### **point_tilt**
- **Type**: `float`
- **Description**: Represents the tilt of the curve. This property defines the rotation along the look-at axis for objects traveling along the path.

---

## **Methods**

### **add_point( const Vector3 &position )**
- **Returns**: `void`
- **Description**: Adds a new point to the curve at the specified position. This method appends the point to the end of the curve's point list.
- **Note**: This method is not const, as it modifies the curve's data.

---

### **clear_points()**
- **Returns**: `void`
- **Description**: Removes all points from the curve, resetting it to an empty state.

---

### **get_point( int index ) const**
- **Returns**: `Vector3`
- **Description**: Returns the position of the point at the specified index. If the index is out of bounds, returns a default position (e.g., `(0, 0, 0)`).
- **Note**: This method is const, as it does not modify the curve.

---

### **get_point_tilt() const**
- **Returns**: `float`
- **Description**: Returns the current tilt value of the curve.
- **Note**: This method is const.

---

### **get_point_count() const**
- **Returns**: `int`
- **Description**: Returns the number of points in the curve.
- **Note**: This method is const.

---

### **get_point_in( int index ) const**
- **Returns**: `Vector3`
- **Description**: Returns the position of the control point leading to the vertex at the specified index. This is the tangent point entering the vertex.
- **Note**: This method is const.

---

### **get_point_out( int index ) const**
- **Returns**: `Vector3`
- **Description**: Returns the position of the control point leading out of the vertex at the specified index. This is the tangent point exiting the vertex.
- **Note**: This method is const.

---

### **get_point_tilt( int index ) const**
- **Returns**: `float`
- **Description**: Returns the tilt value of the point at the specified index.
- **Note**: This method is const.

---

### **sample( int idx, float t ) const**
- **Returns**: `Vector3`
- **Description**: Returns a point along the curve at the specified index and fraction `t` along the segment. The `t` parameter ranges from 0.0 to 1.0. If `idx` is out of bounds, returns a default position.
- **Note**: This method is const.

---

### **samplef( float fofs ) const**
- **Returns**: `Vector3`
- **Description**: Returns the position at the vertex specified by `fofs`. The integer part of `fofs` is used as the index, and the fractional part is used as the `t` parameter.
- **Note**: This method is const.

---

### **sample_baked( float offset = 0.0, bool cubic = false ) const**
- **Returns**: `Vector3`
- **Description**: Returns a point within the curve at the specified offset. The offset is measured as a distance along the curve. The `cubic` parameter determines whether cubic interpolation is used.
- **Note**: This method is const.

---

### **sample_baked_up_vector( float offset, bool apply_tilt = false ) const**
- **Returns**: `Vector3`
- **Description**: Returns an up vector within the curve at the specified offset. If `apply_tilt` is true, an interpolated tilt is applied to the up vector.
- **Note**: This method is const.

---

### **sample_baked_with_rotation( float offset = 0.0, bool cubic = false, bool apply_tilt = false ) const**
- **Returns**: `Transform3D`
- **Description**: Returns a `Transform3D` object with the origin at the point position, and basis vectors representing the direction, up, and forward vectors along the curve.
- **Note**: This method is const.

---

### **set_point_position( int index, const Vector3 &position )**
- **Returns**: `void`
- **Description**: Sets the position of the vertex at the specified index. If the index is out of bounds, an error is returned.
- **Note**: This method is not const, as it modifies the curve's data.

---

### **set_point_in( int index, const Vector3 &position )**
- **Returns**: `void`
- **Description**: Sets the position of the control point leading to the vertex at the specified index. The position is relative to the vertex.
- **Note**: This method is not const.

---

### **set_point_out( int index, const Vector3 &position )**
- **Returns**: `void`
- **Description**: Sets the position of the control point leading out of the vertex at the specified index. The position is relative to the vertex.
- **Note**: This method is not const.

---

### **set_point_tilt( int index, float tilt )**
- **Returns**: `void`
- **Description**: Sets the tilt value of the point at the specified index. If the index is out of bounds, an error is returned.
- **Note**: This method is not const.

---

### **tessellate( int max_stages = 5, float tolerance_degrees = 4 ) const**
- **Returns**: `Vector3List`
- **Description**: Returns a list of points along the curve with curvature-controlled density. The `max_stages` parameter determines the maximum number of subdivisions, and `tolerance_degrees` controls the deviation allowed before subdivision.
- **Note**: This method is const.

---

### **tessellate_even_length( int max_stages = 5, float tolerance_length = 0.2 ) const**
- **Returns**: `Vector3List`
- **Description**: Returns a list of points along the curve with almost uniform density. The `tolerance_length` parameter controls the maximum distance between neighboring points before subdivision.
- **Note**: This method is const.

---

## **Notes**
- Methods marked as `const` do not modify the curve's internal state and can be safely called on const objects.
- Methods that modify the curve's data (e.g., `add_point`, `set_point_position`) are not const.
- The `point_tilt` property is a global property affecting the entire curve's tilt. Individual point tilts can be set via `set_point_tilt`.