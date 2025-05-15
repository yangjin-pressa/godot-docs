# SeparationRayShape3D

**Inherits:** Shape3D < Resource < RefCounted < Object

---

## Description

A 3D ray shape used for physics collision that tries to separate itself from any collider. Typically used to provide a shape for a CollisionShape3D. When this shape collides with an object, it attempts to separate itself by moving its endpoint to the collision point.

---

## Properties

- **length**: float = 1.0  
  The ray's length.

- **slide_on_slope**: bool = false  
  If false (default), the shape always separates and returns a normal along its own direction. If true, the shape can return the correct normal and separate in any direction, allowing sliding motion on slopes.

---

## Methods

- **set_length(value: float)**  
  Sets the ray's length.

- **get_length()**  
  Gets the ray's length.

- **set_slide_on_slope(value: bool)**  
  Sets whether the shape can slide on slopes.

- **get_slide_on_slope()**  
  Gets whether the shape can slide on slopes.