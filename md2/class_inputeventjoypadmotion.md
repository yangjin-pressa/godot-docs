# InputEventJoypadMotion

## Inheritance
- :ref:`InputEvent<class_InputEvent>`  
- :ref:`Resource<class_Resource>`  
- :ref:`RefCounted<class_RefCounted>`  
- :ref:`Object<class_Object>`  

## Description
Stores information about joystick motions. One **InputEventJoypadMotion** represents one axis at a time. For gamepad buttons, see :ref:`InputEventJoypadButton<class_InputEventJoypadButton>`.

## Tutorials
- Using InputEvent

## Properties
- **axis**: :ref:`JoyAxis<enum_@GlobalScope_JoyAxis>` = 0  
- **axis_value**: :ref:`float<class_float>` = 0.0  

## Property Descriptions
### axis
**Type**: :ref:`JoyAxis<enum_@GlobalScope_JoyAxis>`  
**Default**: 0  

Axis identifier. Use one of the :ref:`JoyAxis<enum_@GlobalScope_JoyAxis>` axis constants.

**Methods**:
- `set_axis(value: :ref:`JoyAxis<enum_@GlobalScope_JoyAxis>`): void`  
- `get_axis(): :ref:`JoyAxis<enum_@GlobalScope_JoyAxis>``  

### axis_value
**Type**: :ref:`float<class_float>`  
**Default**: 0.0  

Current position of the joystick on the given axis. The value ranges from -1.0 to 1.0. A value of 0 means the axis is in its resting position.

**Methods**:
- `set_axis_value(value: :ref:`float<class_float>`): void`  
- `get_axis_value(): :ref:`float<class_float>``