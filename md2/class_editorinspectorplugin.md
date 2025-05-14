# EditorInspectorPlugin

## Overview
Inherits from: RefCounted < Object

A plugin for adding custom property editors to the inspector.

## Key Features
- Detects supported object types via _can_handle()
- Adds custom controls at various stages of property parsing
- Supports adding property editors for individual properties or groups

## Methods

### Core Methods
- `_can_handle` (object: Object) → bool (virtual, const)
  - Returns true if this object can be handled by this plugin

- `_parse_begin` (object: Object) → void (virtual)
  - Called to add controls at the beginning of the property list

- `_parse_category` (object: Object, category: String) → void (virtual)
  - Called to add controls before a category in the property list

- `_parse_end` (object: Object) → void (virtual)
  - Called to add controls at the end of the property list

- `_parse_group` (object: Object, group: String) → void (virtual)
  - Called to add controls before a group/sub-group

- `_parse_property` (object: Object, type: Variant.Type, name: String, hint_type: PropertyHint, hint_string: String, usage_flags: PropertyUsageFlags, wide: bool) → bool (virtual)
  - Adds property-specific editors. Returns true to replace built-in editor

### Custom Control Methods
- `add_custom_control` (control: Control) → void
  - Adds a custom control (not necessarily a property editor)

- `add_property_editor` (property: String, editor: Control, add_to_end: bool=false, label: String="")
  - Adds a property editor. If add_to_end is true, the editor appears after others

- `add_property_editor_for_multiple_properties` (label: String, properties: PackedStringArray, editor: Control) → void
  - Adds an editor for multiple properties

## Usage
Register with: EditorPlugin.add_inspector_plugin()

## Related Documentation
- [Inspector plugins tutorial](../tutorials/plugins/editor/inspector_plugins)