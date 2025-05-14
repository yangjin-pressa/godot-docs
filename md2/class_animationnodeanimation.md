# AnimationNodeAnimation

## Class Hierarchy
- Inherits: AnimationRootNode → AnimationNode → Resource → RefCounted → Object

## Description
A resource to add to an AnimationNodeBlendTree. Provides a single output port via the animation property. Used as input for animation blending nodes.

## Tutorials
- [Using AnimationTree](../tutorials/animation/animation_tree)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties
- **advance_on_start**: bool (false) - If true, first frame is not drawn but processed
- **animation**: StringName ("" ) - Animation to use as output
- **loop_mode**: LoopMode - Overrides original animation loop settings
- **play_mode**: PlayMode (0) - Determines playback direction (0=forward, 1=backward)
- **start_offset**: float - Offsets animation start position
- **stretch_time_scale**: bool - Scales time to match specified timeline length
- **timeline_length**: float - Defines custom timeline length
- **use_custom_timeline**: bool (false) - Enables custom timeline parameters

## Enumerations
### PlayMode
- **PLAY_MODE_FORWARD** (0) - Plays animation in forward direction
- **PLAY_MODE_BACKWARD** (1) - Plays animation in backward direction

## Property Descriptions
- **advance_on_start**: Controls whether the first frame is processed immediately
- **animation**: Reference to an animation resource from AnimationTree.anim_player
- **loop_mode**: Overrides animation loop settings when use_custom_timeline is enabled
- **play_mode**: Sets playback direction (forward or backward)
- **start_offset**: Adjusts starting position of the animation
- **stretch_time_scale**: Scales time to match specified timeline length
- **timeline_length**: Defines custom timeline length for animation
- **use_custom_timeline**: Enables custom timeline parameters for the animation

## Notes
- When use_custom_timeline is true, animation properties are overridden
- Loop settings may not work as expected if original animation doesn't have looping
- AnimationPlayer.play() note: first frame is not drawn but processed when advance_on_start is true