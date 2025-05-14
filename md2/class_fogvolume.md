# FogVolume

## Inheritance
- **VisualInstance3D** < **Node3D** < **Node** < **Object**

## Description
- Adds localized fog to global volumetric fog effect.
- Can remove fog from specific areas using a `FogMaterial` with negative `FogMaterial.density`.
- Performance depends on screen size and material complexity.
- Only effective if `Environment.volumetric_fog_enabled` is true.
- Global fog can be disabled by setting `Environment.volumetric_fog_density` to 0.0.

## Tutorials
- [Volumetric fog and fog volumes](../tutorials/3d/volumetric_fog)

## Properties
- **Material**: `Material` (default: built-in `FogMaterial` or custom `ShaderMaterial`)
- **Shape**: `FogVolumeShape` (default: 3)
- **Size**: `Vector3` (default: `Vector3(2, 2, 2)`)

## Property Descriptions
### material
- Sets/get the material used by the fog volume.
- Can be a built-in `FogMaterial` or custom `ShaderMaterial`.

### shape
- Defines the shape of the fog volume.
- Options: `FOG_VOLUME_SHAPE_ELLIPSOID`, `FOG_VOLUME_SHAPE_CONE`, `FOG_VOLUME_SHAPE_CYLINDER`, `FOG_VOLUME_SHAPE_BOX`, `FOG_VOLUME_SHAPE_WORLD`.

### size
- Controls the size of the fog volume for certain shapes.
- Notes: Thinner volumes may flicker; adjust `volume_depth` or `volumetric_fog_length` to mitigate this.

## Notes
- Thin fog volumes may flicker; consider increasing `volume_depth` or decreasing `volumetric_fog_length`.
- Non-uniform scaling of cone/cylinder shapes is not supported; scale the node instead.