# SegmentShape2D

## Inheritance
- Class: Shape2D
  - Inherits: Resource
    - Inherits: RefCounted
      - Inherits: Object

## Description
A 2D line segment shape used for physics collision. Typically used with CollisionShape2D.

## Properties
- **a**: Vector2 = Vector2(0, 0)
- **b**: Vector2 = Vector2(0, 10)

## Property Descriptions

**a**  
The segment's first point position.  
- `set_a(value: Vector2)`  
- `get_a()`

**b**  
The segment's second point position.  
- `set_b(value: Vector2)`  
- `get_b()`