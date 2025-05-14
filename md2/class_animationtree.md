# AnimationTree

**Inherits:** AnimationMixer < Node < Object

A node used for advanced animation transitions in an AnimationPlayer.

## Description
A node used for advanced animation transitions in an AnimationPlayer.
Note: When linked with an AnimationPlayer, several properties and methods of the corresponding AnimationPlayer will not function as expected. Playback and transitions should be handled using only the AnimationTree and its constituent AnimationNode(s). The AnimationPlayer node should be used solely for adding, deleting, and editing animations.

## Tutorials
- Using AnimationTree
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

## Properties
- NodePath advance_expression_base_node = NodePath(".")
- NodePath anim_player = NodePath("")
- AnimationCallbackModeDiscrete callback_mode_discrete = 2 (overrides AnimationMixer callback_mode_discrete)
- bool deterministic = true (overrides AnimationMixer deterministic)
- AnimationRootNode tree_root

## Methods
- AnimationProcessCallback get_process_callback() const
- void set_process_callback(mode: AnimationProcessCallback)

## Signals
- animation_player_changed()

## Enumerations
**AnimationProcessCallback**
- ANIMATION_PROCESS_PHYSICS = 0 (Deprecated: See AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS)
- ANIMATION_PROCESS_IDLE = 1 (Deprecated: See AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_IDLE)
- ANIMATION_PROCESS_MANUAL = 2 (Deprecated: See AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_MANUAL)

## Property Descriptions
**advance_expression_base_node**
- Set/Get: NodePath
- The path to the Node used to evaluate the AnimationNode Expression if one is not explicitly specified internally.

**anim_player**
- Set/Get: NodePath
- The path to the AnimationPlayer used for animating.

**tree_root**
- Set/Get: AnimationRootNode
- The root animation node of this AnimationTree. See AnimationRootNode.

## Method Descriptions
**get_process_callback() const**
- Deprecated: Use AnimationMixer.callback_mode_process instead.
- Returns the process notification in which to update animations.

**set_process_callback(mode: AnimationProcessCallback)**
- Deprecated: Use AnimationMixer.callback_mode_process instead.
- Sets the process notification in which to update animations.