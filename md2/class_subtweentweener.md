# SubtweenTweener

**Inherits:** Tweener < RefCounted < Object

Runs a Tween nested within another Tween.

## Description
**SubtweenTweener** is used to execute a Tween as one step in a sequence defined by another Tween. See [Tween.tween_subtween()](class_Tween_method_tween_subtween) for more usage information.

**Note:** [Tween.tween_subtween()](class_Tween_method_tween_subtween) is the only correct way to create SubtweenTweener. Any SubtweenTweener created manually will not function correctly.

## Methods

- **set_delay(delay: float)**: Sets the time in seconds after which the SubtweenTweener will start running the subtween. By default there's no delay.

## Method Descriptions

**set_delay(delay: float)**: 
- **virtual**: This method should typically be overridden by the user to have any effect.
- **const**: This method has no side effects. It doesn't modify any of the instance's member variables.
- **return type**: void (No return value.)