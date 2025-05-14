# AnimationNodeSync

**Inherits:** AnimationNode → Resource → RefCounted → Object  
**Inherited By:** AnimationNodeAdd2, AnimationNodeAdd3, AnimationNodeBlend2, AnimationNodeBlend3, AnimationNodeOneShot, AnimationNodeSub2, AnimationNodeTransition

## Description
Base class for AnimationNode instances with multiple input ports that must be synchronized. Used to combine, mix, or blend two or more animations while maintaining synchronization in an AnimationTree.

## Tutorials
- [Using AnimationTree](../tutorials/animation/animation_tree)

## Properties
- **sync**: bool = false  
  Controls synchronization behavior for blended animations.

## Property Descriptions
### sync
- **set_use_sync**(value: bool): void  
- **is_using_sync**(): bool  
  If false, blended animations stop when blend value is 0.  
  If true, forces blended animations to advance frame.

## References
- [AnimationTree](../tutorials/animation/animation_tree)