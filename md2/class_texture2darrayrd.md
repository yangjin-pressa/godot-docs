# Texture2DArrayRD

## Inheritance Hierarchy
- TextureLayeredRD  
  - TextureLayered  
    - Texture  
      - Resource  
        - RefCounted  
          - Object  

## Description
This texture array class allows you to use a 2D array texture created directly on the **RenderingDevice** as a texture for materials, meshes, etc.

## Key Notes
- **Purpose**: 2D array texture for rendering, bound to a texture created on the RenderingDevice.
- **Inheritance**: Chains from TextureLayeredRD through Object.
- **Citation**: RenderingDevice (class name reference). 

## Method/Attribute Context
- **Virtual Methods**: Should typically be overridden by the user.
- **Const Methods**: No side effects; do not modify instance variables.
- **Static Methods**: Called directly using the class name.