# World2D

**Inherits:** Resource → RefCounted → Object

A resource that holds all components of a 2D world, such as a canvas and a physics space.

## Description
Class that has everything pertaining to a 2D world: A physics space, a canvas, and a sound space. 2D nodes register their resources into the current 2D world.

## Tutorials
- [Ray-casting tutorial](../tutorials/physics/ray-casting)

## Properties
- **canvas**: RID (Reference to the world's canvas resource. Used by RenderingServer for 2D drawing.)
- **direct_space_state**: PhysicsDirectSpaceState2D (Direct access to the world's physics 2D space state. Used for collision queries. Thread safety: limited to Node._physics_process() in main thread.)
- **navigation_map**: RID (Reference to the world's navigation map. Used by NavigationServer2D.)
- **space**: RID (Reference to the world's physics space resource. Used by PhysicsServer2D for 2D physics operations.)

## Property Descriptions
- **get_canvas()**: Returns the RID of this world's canvas resource.
- **get_direct_space_state()**: Returns direct access to the world's physics 2D space state.
- **get_navigation_map()**: Returns the RID of this world's navigation map.
- **get_space()**: Returns the RID of this world's physics space resource.