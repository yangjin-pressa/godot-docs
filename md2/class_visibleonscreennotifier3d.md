# VisibleOnScreenNotifier3D

**Inherits:** VisualInstance3D → Node3D → Node → Object  
**Inherited By:** VisibleOnScreenEnabler3D  

A 3D box that detects when part of it is visible on screen or in a Camera3D's view.  

---

## Description  
- Detects visibility of a 3D region  
- Emits signals when the region enters or exits the screen  
- Uses an approximate heuristic for visibility detection (ignores occlusion)  
- Requires Node3D.visible set to true to function  

---

## Properties  
- **aabb**: AABB(-1, -1, -1, 2, 2, 2)  
  - Defines the bounding box of the detection region  
  - Set/Get methods available  

---

## Methods  
- **is_on_screen()** (const):  
  - Returns true if the bounding box is currently on screen  
  - Returns false immediately after instantiation (takes one frame to assess visibility)  

---

## Signals  
- **screen_entered()**:  
  - Emitted when any part of the region enters the screen  

- **screen_exited()**:  
  - Emitted when no part of the region remains visible  

---

## Property Descriptions  
- **aabb**:  
  - Type: AABB  
  - Default: AABB(-1, -1, -1, 2, 2, 2)  
  - Represents the box-shaped region for visibility detection  

---

## Method Descriptions  
- **is_on_screen()**:  
  - Checks if the bounding box is currently visible on screen  
  - Note: Initial value is false (takes one frame to evaluate)  

---

## Notes  
- For automatic node enablement, use VisibleOnScreenEnabler3D  
- Visibility detection does not account for walls or occlusion  
- Must ensure Node3D.visible is set to true for the notifier to work