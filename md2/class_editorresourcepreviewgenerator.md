# EditorResourcePreviewGenerator

## Overview
Custom generator of previews for Godot engine. Supports resource preview creation based on type.

## Key Features
- Uses EditorSettings to determine thumbnail size
- Supports both resource-based and path-based preview generation
- Virtual methods allow custom implementation

## Methods

### _can_generate_small_preview()
- **Return type**: bool
- **Description**: Determines if small previews can be generated
- **Default**: returns false
- **Purpose**: Enables generation of small previews alongside main previews

### _generate()
- **Return type**: Texture2D
- **Parameters**:
  - resource: Resource
  - size: Vector2i
  - metadata: Dictionary
- **Note**: Must be implemented by subclasses
- **Thread safety**: Called from background thread
- **Metadata**: Can store file-specific data for tooltips

### _generate_from_path()
- **Return type**: Texture2D
- **Parameters**:
  - path: String
  - size: Vector2i
  - metadata: Dictionary
- **Note**: Optional implementation; defaults to loading and calling _generate()
- **Thread safety**: Called from background thread
- **Metadata**: Can store file-specific data for tooltips

### _generate_small_preview_automatically()
- **Return type**: bool
- **Description**: Controls automatic generation of small previews
- **Default**: returns false
- **Purpose**: Enables automatic generation from main preview textures

### _handles()
- **Return type**: bool
- **Parameters**:
  - type: String
- **Description**: Checks if generator supports a specific resource type
- **Usage**: Used to determine if this generator should be used for a resource

## Implementation Notes
- All methods are virtual (can be overridden)
- Methods marked as const have no side effects
- Metadata dictionary is modified by methods for tooltip data
- Always called from background threads (not main thread)