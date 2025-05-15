# VisualShaderNodeFloatOp

**Inherits:** VisualShaderNode < Resource < RefCounted < Object

## Description
Applies operator to two floating-point inputs: a and b.

## Properties
- **operator**: Operator (0)

## Enumerations
**Operator**: 
- **OP_ADD** = 0: Sums two numbers using a + b
- **OP_SUB** = 1: Subtracts two numbers using a - b
- **OP_MUL** = 2: Multiplies two numbers using a * b
- **OP_DIV** = 3: Divides two numbers using a / b
- **OP_MOD** = 4: Calculates remainder of two numbers (mod(a, b))
- **OP_POW** = 5: Raises a to the power of b (pow(a, b))
- **OP_MAX** = 6: Returns greater of two numbers (max(a, b))
- **OP_MIN** = 7: Returns lesser of two numbers (min(a, b))
- **OP_ATAN2** = 8: Returns arc-tangent of parameters (atan(a, b))
- **OP_STEP** = 9: Step function (step(a, b))
- **OP_ENUM_SIZE** = 10: Enum size

## Property Descriptions
**operator**: 
- Type: Operator (0)
- Set: set_operator(value: Operator)
- Get: get_operator()

Operator to apply to inputs. See Operator for options.