# OpenXRInteractionProfileEditorBase

**Inherits:** HBoxContainer → BoxContainer → Container → Control → CanvasItem → Node → Object  
**Inherited By:** OpenXRInteractionProfileEditor

## Description
Base class for editing interaction profiles. This class is used by the OpenXR action map editor to create custom editors for specific interaction profiles.

## Properties
- **size_flags_horizontal**: 3 (overrides Control::get_size_flags_horizontal)  
- **size_flags_vertical**: 3 (overrides Control::get_size_flags_vertical)  

## Methods
- **setup**:  
  - **Parameters**:  
    - `action_map`: OpenXRActionMap  
    - `interaction_profile`: OpenXRInteractionProfile  
  - **Description**: Setup this editor for the provided `action_map` and `interaction_profile`. This method is virtual and has no side effects.  

## Inherited By
OpenXRInteractionProfileEditor