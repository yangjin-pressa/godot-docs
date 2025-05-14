# AnimationNodeSub2

## Overview
Inherits: AnimationNodeSync < AnimationNode < Resource < RefCounted < Object

Blends two animations subtractively inside of an AnimationNodeBlendTree.

## Functionality
- Blends two animations based on a blend value
- Typically used for pre-calculation to cancel extra poses from "add" animation sources
- Blend value range: [0.0, 1.0] (values outside this range can be used for amplified/inverted effects)

## Key Note
This calculation differs from negative values in AnimationNodeAdd2:
- AnimationNodeSub2 multiplies inverted animation matrices from the left
- Negative AnimationNodeAdd2 multiplies matrices from the right
- Transformation matrices do not satisfy commutative law

## Tutorials
- AnimationTree

## Related Concepts
- AnimationNodeSync
- AnimationNodeBlendTree
- AnimationNodeAdd2
- AnimationNodeAdd3
- AnimationNodeAdd3