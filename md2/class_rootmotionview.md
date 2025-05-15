# RootMotionView

## Class Hierarchy
- **RootMotionView**  
  Inherits from: `VisualInstance3D` → `Node3D` → `Node` → `Object`

## Description
Editor-only helper for setting up root motion in `AnimationMixer`. Root motion uses the root bone of a skeleton to apply motion to the rest of the character, enabling precise movement and interaction with objects. 

**Note:** Visible only in the editor; hidden in running projects.

## Tutorials
- [Using AnimationTree - Root motion](../tutorials/animation/animation_tree.html#root-motion)

## Properties

### animation_path
- **Type:** `NodePath`  
  **Default:** `NodePath("")`  
  **Description:** Path to an `AnimationMixer` node for root motion.  
  **Methods:** `set_animation_path(value: NodePath)`, `get_animation_path()`

### cell_size
- **Type:** `float`  
  **Default:** `1.0`  
  **Description:** Grid cell size in 3D units.  
  **Methods:** `set_cell_size(value: float)`, `get_cell_size()`

### color
- **Type:** `Color`  
  **Default:** `Color(0.5, 0.5, 1, 1)`  
  **Description:** Grid color.  
  **Methods:** `set_color(value: Color)`, `get_color()`

### radius
- **Type:** `float`  
  **Default:** `10.0`  
  **Description:** Grid radius. Opacity fades with distance from origin.  
  **Methods:** `set_radius(value: float)`, `get_radius()`

### zero_y
- **Type:** `bool`  
  **Default:** `true`  
  **Description:** Grid points are on Y=0 (local Y).  
  **Methods:** `set_zero_y(value: bool)`, `get_zero_y()`