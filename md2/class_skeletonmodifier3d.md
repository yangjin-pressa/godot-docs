# SkeletonModifier3D

## Hierarchy
- **Inherits:** Node3D → Node → Object  
- **Inherited By:**  
  - LookAtModifier3D  
  - PhysicalBoneSimulator3D  
  - RetargetModifier3D  
  - SkeletonIK3D  
  - SpringBoneSimulator3D  
  - XRBodyModifier3D  
  - XRHandModifier3D  

## Description
- Retrieves a target Skeleton3D by having a Skeleton3D parent.  
- Modifications occur after the AnimationMixer's playback process.  
- Used for custom IK solvers, constraints, or skeleton physics.  

## Tutorials
- [Design of the Skeleton Modifier 3D](https://godotengine.org/article/design-of-the-skeleton-modifier-3d/)  

## Properties
- **active**: `bool` (default: `true`)  
  - If `true`, the modifier processes.  
- **influence**: `float` (default: `1.0`)  
  - Sets the influence of the modification.  
  - Note: Skeleton3D automatically applies influence, so this modifier should apply 100% of the result.  

## Methods
- **_process_modification()**: `void` (virtual)  
  - Deprecated. Use `_process_modification_with_delta()` instead.  
  - Override to implement custom logic.  
- **_process_modification_with_delta(delta: `float`)**: `void` (virtual)  
  - Override to implement custom logic.  
  - `delta` is passed from the parent Skeleton3D.  
- **get_skeleton()**: `Skeleton3D` (const)  
  - Returns the parent Skeleton3D node.  

## Signals
- **modification_processed()**: `void`  
  - Notifies when modification is complete.  
  - Note: Use `Skeleton3D.get_bone_pose()` or `get_bone_global_pose()` at this signal's firing time.  

## Enumerations
### BoneAxis
- **BONE_AXIS_PLUS_X** = `0`  
- **BONE_AXIS_MINUS_X** = `1`  
- **BONE_AXIS_PLUS_Y** = `2`  
- **BONE_AXIS_MINUS_Y** = `3`  
- **BONE_AXIS_PLUS_Z** = `4`  
- **BONE_AXIS_MINUS_Z** = `5`  

## Property Descriptions
### active
- **set_active(value: `bool`)**: void  
- **get_active()**: `bool`  

### influence
- **set_influence(value: `float`)**: void  
- **get_influence()**: `float`  

## Method Descriptions
### _process_modification()
- **Deprecated**: Use `_process_modification_with_delta()` instead.  
- **Purpose**: Custom logic for processing the modifier.  

### _process_modification_with_delta(delta: `float`)
- **Purpose**: Custom logic for processing the modifier.  
- **Parameters**:  
  - `delta`: Time delta passed from the parent Skeleton3D.  

### get_skeleton()
- **Purpose**: Retrieve the parent Skeleton3D node.  
- **Return**: `Skeleton3D` object.