# PlaceholderTexture2D

## Inheritance
- Texture2D < Texture < Resource < RefCounted < Object

## Description
Used in two scenarios:
1. When running a project in dedicated server mode, only texture dimensions are retained to reduce PCK size.
2. When a subclass is missing due to engine version differences or module changes.

**Note:** Not intended for rendering. May not function as expected in shaders/materials (e.g., UV calculations).

## Properties
- **resource_local_to_scene**: bool = false (overrides Resource property)
- **size**: Vector2 = Vector2(1, 1)

## Property Descriptions
### size
- **Type**: Vector2
- **Default**: Vector2(1, 1)
- **Description**: Texture dimensions in pixels

## Methods
- **set_size(value: Vector2)**: void
- **get_size()**: Vector2

## Notes
- Methods are virtual (override recommended) or const (no side effects)
- This class serves as a placeholder implementation for texture-related functionality when specific subclasses are unavailable.