# Path2D

## Class Hierarchy
- Inherits: `Node2D` < `CanvasItem` < `Node` < `Object`

## Description
- Contains a `Curve2D` path for `PathFollow2D` nodes to follow.
- **Key Note**: The path is relative to the moved nodes (children of `PathFollow2D`). The curve should usually start with a zero vector (0, 0).

## Properties
- **Curve2D** `curve`: Describes the path.

## Property Descriptions
- **curve**: 
  - **set_curve(value: Curve2D)**: Sets the path curve.
  - **get_curve()**: Retrieves the path curve.

## Key Usage Notes
- The path is relative to `PathFollow2D` child nodes.
- The curve should typically start at (0, 0) as a base point.