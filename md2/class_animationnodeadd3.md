# AnimationNodeAdd3

## Inheritance
- **AnimationNodeSync**
  - **AnimationNode**
    - **Resource**
      - **RefCounted**
        - **Object**

## Description
- Blends two of three animations additively within an `AnimationNodeBlendTree`.
- Three inputs:
  - Base animation to add to
  - "-add" animation for negative blend amount
  - "+add" animation for positive blend amount
- If absolute value of amount exceeds `1.0`, the in port is blended with amplified animations.

## Tutorials
- [Using AnimationTree](../tutorials/animation/animation_tree)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)