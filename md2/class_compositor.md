# Compositor

**Experimental:** More customization of the rendering pipeline will be added in the future.

**Inherits:** Resource → RefCounted → Object

Stores attributes used to customize how a Viewport is rendered.

## Description

The compositor resource stores attributes used to customize how a Viewport is rendered.

## Tutorials

- The Compositor

## Properties

- **compositor_effects**: Array of CompositorEffect, default empty.

## Property Descriptions

**compositor_effects**  
- Type: Array of CompositorEffect  
- Default: `[]`  
- Description: Custom CompositorEffect s applied during viewport rendering.

## Method Definitions

- **set_compositor_effects**(value: Array of CompositorEffect) → void  
  - Virtual: This method should typically be overridden by the user to have any effect.  
  - Const: This method has no side effects.  

- **get_compositor_effects**() → Array of CompositorEffect  
  - Const: This method has no side effects.