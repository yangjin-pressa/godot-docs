# VisualShaderNodeOuterProduct

**Inherits:** VisualShaderNode < Resource < RefCounted < Object

## Description
- Calculates the outer product of two vectors in the visual shader graph
- Treats first parameter `c` as a column vector (1 column matrix)
- Treats second parameter `r` as a row vector (1 row matrix)
- Perform matrix multiplication `c * r` to produce a matrix:
  - Rows = components in `c`
  - Columns = components in `r`