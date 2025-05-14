# GrooveJoint2D

## Description
A physics joint that restricts the movement of two 2D physics bodies to a fixed axis. For example, a StaticBody2D representing a piston base can be attached to a RigidBody2D representing the piston head, moving up and down.

## Properties
- **initial_offset**: 25.0
- **length**: 50.0

## Property Descriptions
### initial_offset
The body B's initial anchor position defined by the joint's origin and a local offset initial_offset along the joint's Y axis (along the groove).

### length
The groove's length. The groove is from the joint's origin towards length along the joint's local Y axis.

## Methods
### set_initial_offset(value: float)
Sets the initial offset.

### get_initial_offset()
Returns the initial offset.

### set_length(value: float)
Sets the length.

### get_length()
Returns the length.

## Notes
- **virtual**: This method should typically be overridden by the user to have any effect.
- **const**: This method has no side effects. It doesn't modify any of the instance's member variables.