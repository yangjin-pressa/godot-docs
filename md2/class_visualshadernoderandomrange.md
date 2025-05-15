# VisualShaderNodeRandomRange

**Inherits:** VisualShaderNode < Resource < RefCounted < Object

A visual shader node that generates a pseudo-random scalar.

## Description
- Outputs a pseudo-random scalar value within a specified range
- Value remains consistent for the same seed and range
- Seed value must change over time (e.g., using time input) to produce different values

## Inheritance Hierarchy
- VisualShaderNode
  - Resource
    - RefCounted
      - Object

## Key Characteristics
- Generates random values based on seed input
- Output is deterministic for fixed seed and range
- Requires dynamic seed input for varied results
- Used in shader graphs to create random scalar values