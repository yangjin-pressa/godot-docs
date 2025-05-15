# SkeletonModification2DLookAt

## Description
This class is used to rotate a skeleton's joint to look at a target. It allows for controlling the orientation of a bone in a 2D skeleton to face a specified point.

## Properties
- **bone**: Type `Bone2D`, Default: `null`  
  The bone to be rotated.
- **target**: Type `Vector2`, Default: `Vector2(0, 0)`  
  The target point to look at.
- **use_constraints**: Type `bool`, Default: `false`  
  Whether to apply joint constraints during rotation.

## Methods
- **_process(delta)**:  
  Called every frame to update the bone's rotation based on the target.
- **_get_rotation()**:  
  Calculates the rotation angle required to align the bone with the target.
- **_apply_rotation()**:  
  Applies the calculated rotation to the bone.

## Property Descriptions
- **bone**:  
  The bone in the skeleton that needs to be rotated to face the target.
- **target**:  
  The position in the 2D space that the bone should look at. This is typically a point in the scene.
- **use_constraints**:  
  A flag to enable or disable constraints on the bone's rotation, which can help prevent overshooting or unnatural movements.

## Method Descriptions
- **_process(delta)**:  
  This method is called each frame and uses the `delta` time to update the bone's rotation based on the target position.
- **_get_rotation()**:  
  This method computes the angle (in radians) required to rotate the bone so that it faces the target. It uses vector mathematics to determine this angle.
- **_apply_rotation()**:  
  This method applies the calculated rotation to the bone, adjusting its orientation to face the target. It may also handle any constraints enabled by the `use_constraints` property.

## Notes
- The class is designed for 2D skeletal animations and is typically used in conjunction with a `Skeleton2D` node.
- Constraints help maintain the bone's movement within a specific range, preventing it from rotating beyond expected limits.