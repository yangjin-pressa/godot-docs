# OpenXRBindingModifierEditor

**Inherits:** PanelContainer → Container → Control → CanvasItem → Node → Object

Binding modifier editor.

## Description
This is the default binding modifier editor used in the OpenXR action map.

## Properties
- size_flags_horizontal: 3 (overrides Control's size_flags_horizontal)

## Methods
- get_binding_modifier(): Returns the OpenXRBindingModifier currently being edited.
- setup(action_map: OpenXRActionMap, binding_modifier: OpenXRBindingModifier): Setup this editor for the provided action_map and binding_modifier.

## Signals
- binding_modifier_removed(binding_modifier_editor: Object): Signal emitted when the user presses the delete binding modifier button for this modifier.

## Method Descriptions
- get_binding_modifier(): Returns the OpenXRBindingModifier currently being edited. (const)
- setup(action_map: OpenXRActionMap, binding_modifier: OpenXRBindingModifier): Setup this editor for the provided action_map and binding_modifier.