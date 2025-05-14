# OpenXRActionMap

**Inherits:** Resource → RefCounted → Object

A container for OpenXR action sets and interaction profiles.

## Description
- Manages action sets and interaction profiles for OpenXR
- Action bindings are suggestions, not enforced
- Action map must be loaded at startup and is immutable
- Used for mapping inputs/outputs from XR controllers to named actions

## Properties
- **action_sets**: Array of OpenXRActionSet objects
- **interaction_profiles**: Array of OpenXRInteractionProfile objects

## Methods
- **add_action_set**: Add an OpenXRActionSet
- **add_interaction_profile**: Add an OpenXRInteractionProfile
- **create_default_action_sets**: Setup default action sets
- **find_action_set**: Retrieve action set by name
- **find_interaction_profile**: Find interaction profile by name
- **get_action_set**: Get action set by index
- **get_action_set_count**: Get number of action sets
- **get_interaction_profile**: Get interaction profile by index
- **get_interaction_profile_count**: Get number of interaction profiles
- **remove_action_set**: Remove an action set
- **remove_interaction_profile**: Remove an interaction profile

## Key Characteristics
- Action maps are read-only after initialization
- Supports adding/removing individual action sets/profiles
- Provides methods to find by name or index
- Maintains ordered collection of action sets and profiles

## Reference
- [Godot Engine Documentation](https://godotengine.org)