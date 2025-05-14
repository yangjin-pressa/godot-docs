**Class Name**: AnimationNodeBlend2  
**Inherits**: AnimationNodeSync → AnimationNode → Resource → RefCounted → Object  

---  

### Description  
- **Purpose**: Blends two animations linearly within an `AnimationNodeBlendTree`.  
- **Blend Value Range**: Typically uses `[0.0, 1.0]` for linear interpolation.  
- **External Behavior**: Values outside this range can amplify/invert animations, but `AnimationNodeAdd2` is preferable for such cases.  

---  

### Tutorials  
- [Using AnimationTree](../tutorials/animation/animation_tree)  
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)  
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)  

---  

### Key Notes  
- **Blend Logic**: Linear interpolation between two animations based on a weighted value.  
- **Usage Context**: Added to an `AnimationNodeBlendTree` for blending operations.  
- **Alternative**: Use `AnimationNodeAdd2` for values outside [0.0, 1.0] range.