# VisualShaderNodeFaceForward

**Inherits:** VisualShaderNodeVectorBase < VisualShaderNode < Resource < RefCounted < Object

## Description
- **Function Equivalent:** Translates to `faceforward(N, I, Nref)` in the shader language.
- **Parameters:**
  - `N`: Vector to orient
  - `I`: Incident vector
  - `Nref`: Reference vector
- **Behavior:**
  - Returns `N` if the dot product of `I` and `Nref` is negative
  - Returns `-N` if the dot product is non-negative

## Key Notes
- This node is used to compute the direction of a vector based on incident and reference vectors.