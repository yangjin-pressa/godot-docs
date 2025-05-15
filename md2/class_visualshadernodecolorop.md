# VisualShaderNodeColorOp

**Inherits:** VisualShaderNode → Resource → RefCounted → Object

A Color operator node for visual shader graphs.

## Description
Applies operator to two color inputs.

## Properties
- Operator: operator (0)

## Enumerations
**Operator**: 
- **OP_SCREEN** = 0: Screen effect  
  `result = vec3(1.0) - (vec3(1.0) - a) * (vec3(1.0) - b);`
- **OP_DIFFERENCE** = 1: Difference effect  
  `result = abs(a - b);`
- **OP_DARKEN** = 2: Darken effect  
  `result = min(a, b);`
- **OP_LIGHTEN** = 3: Lighten effect  
  `result = max(a, b);`
- **OP_OVERLAY** = 4: Overlay effect  
  ```cpp
  for (int i = 0; i < 3; i++) {
      float base = a[i];
      float blend = b[i];
      if (base < 0.5) {
          result[i] = 2.0 * base * blend;
      } else {
          result[i] = 1.0 - 2.0 * (1.0 - blend) * (1.0 - base);
      }
  }
  ```
- **OP_DODGE** = 5: Dodge effect  
  `result = a / (vec3(1.0) - b);`
- **OP_BURN** = 6: Burn effect  
  `result = vec3(1.0) - (vec3(1.0) - a) / b;`
- **OP_SOFT_LIGHT** = 7: Soft light effect  
  ```cpp
  for (int i = 0; i < 3; i++) {
      float base = a[i];
      float blend = b[i];
      if (base < 0.5) {
          result[i] = base * (blend + 0.5);
      } else {
          result[i] = 1.0 - (1.0 - base) * (1.0 - (blend - 0.5));
      }
  }
  ```
- **OP_HARD_LIGHT** = 8: Hard light effect  
  ```cpp
  for (int i = 0; i < 3; i++) {
      float base = a[i];
      float blend = b[i];
      if (base < 0.5) {
          result[i] = base * (2.0 * blend);
      } else {
          result[i] = 1.0 - (1.0 - base) * (1.0 - 2.0 * (blend - 0.5));
      }
  }
  ```
- **OP_MAX** = 9: Enum size

## Property Descriptions
**operator**: Operator to apply. Set/get method available. See Operator for options.