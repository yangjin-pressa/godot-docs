# LightOccluder2D

**Inherits:** Node2D < CanvasItem < Node < Object

Occludes light cast by a Light2D, casting shadows. The LightOccluder2D must be provided with an OccluderPolygon2D in order for the shadow to be computed.

## Tutorials
- 2D lights and shadows <../tutorials/2d/2d_lights_and_shadows>

## Properties

- **occluder**: OccluderPolygon2D (used to compute the shadow)
- **occluder_light_mask**: int = 1 (LightOccluder2D will cast shadows only from Light2D(s) that have the same light mask(s))
- **sdf_collision**: bool = true (if enabled, the occluder will be part of a real-time generated signed distance field)

## Property Descriptions

### occluder
- **set_occluder_polygon**: Sets the OccluderPolygon2D used to compute the shadow
- **get_occluder_polygon**: Retrieves the OccluderPolygon2D

### occluder_light_mask
- **set_occluder_light_mask**: Sets the light mask for shadow casting
- **get_occluder_light_mask**: Retrieves the light mask for shadow casting

### sdf_collision
- **set_sdf_collision**: Enables/disables the signed distance field for the occluder
- **get_sdf_collision**: Retrieves the state of the signed distance field for the occluder