# AnimationRootNode

## Inheritance
- AnimationNode < Resource < RefCounted < Object

## Inherited By
- AnimationNodeAnimation
- AnimationNodeBlendSpace1D
- AnimationNodeBlendSpace2D
- AnimationNodeBlendTree
- AnimationNodeStateMachine

## Description
AnimationRootNode is a base class for AnimationNode instances that hold a complete animation. A complete animation refers to the output of an AnimationNodeOutput in an AnimationNodeBlendTree or the output of another AnimationRootNode. Used for AnimationTree.tree_root or in other AnimationRootNode instances.

## Examples of Built-in Root Nodes
- AnimationNodeBlendTree (allows blending nodes between each other using various modes)
- AnimationNodeStateMachine (allows configuring blending and transitions between nodes using a state machine pattern)
- AnimationNodeBlendSpace2D (allows linear blending between three AnimationNode instances)
- AnimationNodeBlendSpace1D (allows linear blending only between two AnimationNode instances)

## Tutorials
- Using AnimationTree < ../tutorials/animation/animation_tree