# VisualShaderNodeIntOp

**Inherits:** VisualShaderNode, Resource, RefCounted, Object

## Description
Applies an operator to two integer inputs a and b.

## Properties
- **operator** (enum) - default 0

## Enumerations
- **OP_ADD** (0): a + b
- **OP_SUB** (1): a - b
- **OP_MUL** (2): a * b
- **OP_DIV** (3): a / b
- **OP_MOD** (4): a % b
- **OP_MAX** (5): max(a, b)
- **OP_MIN** (6): max(a, b)
- **OP_BITWISE_AND** (7): a & b
- **OP_BITWISE_OR** (8): a | b
- **OP_BITWISE_XOR** (9): a ^ b
- **OP_BITWISE_LEFT_SHIFT** (10): a << b
- **OP_BIT_ RIGHT_SHIFT** (11): a >> b
- **OP_ENUM_SIZE** (12): enum size

## Property Descriptions
- **operator**: Selects the operation to apply. See enum for options.