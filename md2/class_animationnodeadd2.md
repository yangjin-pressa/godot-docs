# AnimationNodeAdd2

**Inherits:**  
- `AnimationNodeSync`  
- `AnimationNode`  
- `Resource`  
- `RefCounted`  
- `Object`  

## Description  
- Blends two animations additively within an `AnimationNodeBlendTree`.  
- Behavior based on the "amount" value:  
  - **> 1.0**: In port animation is blended with amplified add port animation.  
  - **< 0.0**: In port animation is blended with inverted add port animation.  

## Tutorials  
- [Using AnimationTree](../tutorials/animation/animation_tree)  

## Notes  
- **virtual**: This method should typically be overridden by the user to have any effect.  
- **const**: This method has no side effects. It doesn't modify any of the instance's member variables.  
- **vararg**: This method accepts any number of arguments after the ones described here.  
- **static**: This method doesn't need an instance to be called, so it can be called directly using the class name.  
- **operator**: This method describes a valid operator to use with this type as left-hand operand.  
- **bitfield**: This value is an integer composed as a bitmask of the following flags.  
- **void**: No return value.