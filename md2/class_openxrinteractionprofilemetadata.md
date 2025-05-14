**Class Name**: OpenXRInteractionProfileMetadata  
**Inherits From**: Object  

**Description**:  
This class provides functionality for managing interaction profiles in a system. It includes methods to register interaction profiles, handle input-output paths, rename profiles, and define top-level path configurations.  

---

**Methods**:  

1. **register_interaction_profile**  
   - **Parameters**:  
     - `display_name`: A user-facing name for the interaction profile.  
     - `openxr_path`: The specific OpenXR path associated with the profile.  
     - `openxr_extension_name`: The name of the extension for the OpenXR path.  
   - **Description**: Registers an interaction profile using its OpenXR designation. The `openxr_extension_name` restricts the profile to a specific extension.  

2. **register_io_path**  
   - **Parameters**:  
     - `display_name`: A user-facing name for the input-output path.  
     - `openxr_path`: The OpenXR path associated with this input-output path.  
     - `openxr_extension_name`: The extension name for the OpenXR path.  
   - **Description**: Registers a new input-output path, associating it with an OpenXR path and extension.  

3. **register_profile_rename**  
   - **Parameters**:  
     - `old_display_name`: The current user-facing name of the profile.  
     - `new_display_name`: The new name for the profile.  
   - **Description**: Renames an existing profile by updating its display name.  

4. **register_top_level_path**  
   - **Parameters**:  
     - `display_name`: A user-facing name for the top-level path.  
     - `openxr_path`: The OpenXR path for this top-level configuration.  
     - `openxr_extension_name`: The extension name for the OpenXR path.  
   - **Description**: Defines a top-level path configuration, linking it to an OpenXR path and extension.  

---

**Key Notes**:  
- All parameters are of type `String`, as defined in the original documentation.  
- The class is designed for systems requiring dynamic management of interaction profiles and paths.  
- Methods ensure flexibility in configuring and modifying interaction-related data.