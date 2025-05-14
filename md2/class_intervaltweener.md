# IntervalTweener

## Overview
**Inherits:** Tweener → RefCounted → Object  
Creates an idle interval in a Tween animation.

## Key Concepts
- **Usage**: Used to add delays in tweening sequences
- **Correct Creation**: Only use `Tween.tween_interval()` to create IntervalTweener
- **Manual Creation**: Manually instantiated instances will not function correctly

## Core Methods
- **_integrate(delta: float, current: Vector, target: Vector)**  
  Virtual method for interval processing  
  Parameters:  
  - `delta`: Time elapsed since last frame  
  - `current`: Current value of the tween  
  - `target`: Target value of the tween  

- **_get_interval()**  
  Static method that returns a string representation of the interval  
  - **Type**: const (no side effects)  
  - **Return**: String describing the interval

## Important Notes
- This class is designed to work within the Tween system  
- Manual instantiation of IntervalTweener is not supported  
- Use `Tween.tween_interval()` for proper interval creation  

## Reference
- See: `Tween.tween_interval()` for usage details