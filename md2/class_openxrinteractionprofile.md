# OpenXRInteractionProfile

**Inherits:** Resource < RefCounted < Object

## Description
Stores suggested bindings for an interaction profile. Interaction profiles define metadata for a tracked XR device such as an XR controller.

[OpenXR specification interaction profiles info](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#semantic-path-interaction-profiles)

## Properties
- **binding_modifiers**: Array of binding modifiers (default: [])
- **bindings**: Array of action bindings (default: [])
- **interaction_profile_path**: String identifying XR device path (default: "")

## Methods
- **get_binding(index: int)** → OpenXRIPBinding: Retrieve binding at specified index
- **get_binding_count()** → int: Get number of bindings
- **get_binding_modifier(index: int)** → OpenXRIPBindingModifier: Get binding modifier at specified index
- **get_binding_modifier_count()** → int: Get number of binding modifiers

## Property Descriptions
**binding_modifiers**  
Array of binding modifiers for this interaction profile.  
Access: set_binding_modifiers(value: Array), get_binding_modifiers()

**bindings**  
Array of action bindings for this interaction profile.  
Access: set_bindings(value: Array), get_bindings()

**interaction_profile_path**  
String path identifying the XR device.  
Access: set_interaction_profile_path(value: String), get_interaction_profile_path()

## Method Descriptions
**get_binding**  
Retrieve the binding at the specified index.

**get_binding_count**  
Return the total number of bindings in this interaction profile.

**get_binding_modifier**  
Retrieve the binding modifier at the specified index.

**get_binding_modifier_count**  
Return the total number of binding modifiers in this interaction profile.