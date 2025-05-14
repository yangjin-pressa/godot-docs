# CollisionPolygon3D

## Inheritance
Node3D → Node → Object

## Description
A node that provides a thickened polygon shape (a prism) to a CollisionObject3D parent. Allows editing of the polygon, which can be concave or convex. Used for collision detection in Area3D or to define solid physics bodies.

## Warning
A non-uniformly scaled CollisionShape3D may not behave as expected. Ensure scale is uniform across all axes and adjust the shape resource instead.

---

## Properties

- **debug_color**: Color (default: Color(0, 0, 0, 0))  
  Collision shape color for editor/running project visualization. Default value is from ProjectSettings.

- **debug_fill**: bool (default: true)  
  If true, displays solid fill for debug visualization.

- **depth**: float (default: 1.0)  
  Extends collision shape in direction perpendicular to the polygon.

- **disabled**: bool (default: false)  
  When true, disables collision detection.

- **margin**: float (default: 0.04)  
  Collision margin for Shape3D. Adjusts how much the shape extends from the polygon.

- **polygon**: PackedVector2Array (default: empty)  
  Array of vertices defining the polygon in local XY plane. Changes to this array do not affect the original data.

---

## Method Summary

- **set_debug_color(color)**: Sets the debug color for visualization.
- **get_debug_color()**: Retrieves the current debug color.
- **set_debug_fill(value)**: Enables or disables solid fill.
- **get_debug_fill()**: Checks if solid fill is enabled.
- **set_depth(value)**: Sets the depth of the collision shape.
- **get_depth()**: Retrieves the current depth value.
- **set_disabled(value)**: Enables or disables collision.
- **get_disabled()**: Checks if collision is disabled.
- **set_margin(value)**: Sets the collision margin.
- **get_margin()**: Retrieves the current margin value.
- **set_polygon(vertices)**: Sets the polygon vertices.
- **get_polygon()**: Retrieves the current polygon vertices.

---

## Notes
- The polygon array is a copy; modifying it does not affect the original data.
- Use the `set_polygon()` method to update the shape dynamically.