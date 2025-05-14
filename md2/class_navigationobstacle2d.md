# NavigationObstacle2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** Node2D < CanvasItem < Node < Object

2D obstacle used to affect navigation mesh baking or constrain velocities of avoidance controlled agents.

## Description
An obstacle needs a navigation map and outline vertices defined to work correctly. The outlines cannot cross or overlap.

Obstacles can be included in navigation mesh baking when `affect_navigation_mesh` is enabled. They do not add walkable geometry, instead their role is to discard other source geometry inside the shape. This can be used to prevent navigation mesh from appearing in unwanted places. If `carve_navigation_mesh` is enabled the baked shape will not be affected by offsets of the navigation mesh baking, e.g. the agent's velocity.

## Tutorials
[Using NavigationObstacles](../tutorials/navigation/navigation_using_navigationobstacles.md)

## Properties
- **affect_navigation_mesh**: bool  
  Enables or disables navigation mesh baking for this obstacle.

- **avoidance_layers**: int  
  Bitmask for obstacle avoidance layers (1-32).

- **velocity**: Vector2  
  Desired velocity for obstacle movement prediction.

- **vertices**: PackedVector2Array  
  Outline vertices of the obstacle. Clockwise winding pushes agents inward.

## Methods
- **get_avoidance_layer_value(layer_number: int)** -> bool  
  Returns whether a specific avoidance layer is enabled.

- **get_navigation_map()** -> RID  
  Returns the navigation map RID for this obstacle.

- **get_rid()** -> RID  
  Returns the obstacle's RID on the NavigationServer2D.

- **set_avoidance_layer_value(layer_number: int, value: bool)**  
  Enables or disables a specific avoidance layer.

- **set_navigation_map(navigation_map: RID)**  
  Sets the navigation map for this obstacle.

## Notes
- The `vertices` property returns a copied array; changes to the array do not affect the original.
- The `velocity` property only affects avoidance for obstacles with a radius.
- Obstacles with static vertices cannot predict movement.