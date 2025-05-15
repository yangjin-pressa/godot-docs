# RetargetModifier3D

## Hierarchy
- Inherits: SkeletonModifier3D → Node3D → Node → Object

## Description
Transfers parent skeleton poses (or global poses) to child skeletons in model space with different rests. Modifies child skeleton poses during parent update, overriding normal mapping. To set poses after retargeting, add a SkeletonModifier3D child to the target skeleton.

**Note:** When `use_global_pose` is enabled, global pose may cause issues with unmapped bones if they have mapped children.

---

## Properties

- **enable**: Bitfield of TransformFlag (default: 7)  
  Controls individual transform elements (position/rotation/scale) when `use_global_pose` is disabled.

- **profile**: SkeletonProfile  
  SkeletonProfile for matching bone names.

- **use_global_pose**: bool (default: false)  
  If true, retargeting considers global pose. If false, source bone parents are ignored when target has fewer bones.

---

## Methods

- **is_position_enabled()** → bool  
  Returns true if TRANSFORM_FLAG_POSITION is enabled.

- **is_rotation_enabled()** → bool  
  Returns true if TRANSFORM_FLAG_ROTATION is enabled.

- **is_scale_enabled()** → bool  
  Returns true if TRANSFORM_FLAG_SCALE is enabled.

- **set_position_enabled(enabled: bool)**  
  Sets TRANSFORM_FLAG_POSITION in enable.

- **set_rotation_enabled(enabled: bool)**  
  Sets TRANSFORM_FLAG_ROTATION in enable.

- **set_scale_enabled(enabled: bool)**  
  Sets TRANSFORM_FLAG_SCALE in enable.

---

## Enumerations

### TransformFlag
- **TRANSFORM_FLAG_POSITION** = 1  
  Enable position retargeting.

- **TRANSFORM_FLAG_ROTATION** = 2  
  Enable rotation retargeting.

- **TRANSFORM_FLAG_SCALE** = 4  
  Enable scale retargeting.

- **TRANSFORM_FLAG_ALL** = 7  
  Enable all (position/rotation/scale).

---

## Key Notes

- When `use_global_pose` is true, global pose is applied to all bones, which may cause issues if target skeleton has fewer bones than source.
- Use dummy bones with length 0 for retargeting between models with different bone counts.
- If target has fewer bones, source bone parents are ignored when `use_global_pose` is false.