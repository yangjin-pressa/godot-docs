# AnimationNodeBlend3

**Inherits:** AnimationNodeSync < AnimationNode < Resource < RefCounted < Object

## Description
A resource added to an AnimationNodeBlendTree to blend two of three animations linearly based on a blend amount. The node has three inputs:

- Base animation to blend with
- "-blend" animation for negative values
- "+blend" animation for positive values

The blend value should typically be in the [-1.0, 1.0] range. Values outside this range may cause amplified blending, though AnimationNodeAdd3 is better suited for such cases.

## Tutorials
- Using AnimationTree

## Key Concepts
- **Inputs**: Base, -blend, +blend animations
- **Blend Range**: [-1.0, 1.0] for linear blending
- **Alternative**: AnimationNodeAdd3 for outside-range blending

## Notes
- The blend amount determines which animation is prioritized in the mix.