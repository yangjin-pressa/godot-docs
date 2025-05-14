```gdscript
# EditorInterface class documentation

class EditorInterface:

    # Overview
    # The EditorInterface class provides methods for interacting with the Godot editor,
    # including saving/loading scenes, managing plugins, setting feature profiles, and
    # launching dialogues for node/property selection.

    # Methods

    # save_all_scenes()
    # Saves all opened scenes in the editor.
    # 
    # Parameters:
    # - None
    # 
    # Return Value:
    # - None
    #
    # Example:
    # EditorInterface.save_all_scenes()

    # save_scene()
    # Saves the currently active scene. Returns an error code.
    # 
    # Parameters:
    # - None
    # 
    # Return Value:
    # - Error: OK if saved successfully, ERR_CANT_CREATE if an error occurs
    # 
    # Example:
    # var result = EditorInterface.save_scene()
    # if result == Error.OK:
    #     print("Scene saved successfully")
    # else:
    #     print("Failed to save scene")

    # save_scene_as(path, with_preview=true)
    # Saves the currently active scene as a new file at the specified path.
    # 
    # Parameters:
    # - path: String - The file path to save to
    # - with_preview: bool - Whether to include a preview (default: true)
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.save_scene_as("path/to/scene.tscn")

    # reload_scene_from_path(scene_filepath)
    # Reloads the scene at the given path.
    # 
    # Parameters:
    # - scene_filepath: String - The path to the scene file
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.reload_scene_from_path("path/to/scene.tscn")

    # restart_editor(save=true)
    # Restarts the editor. If save is true, the project is saved before restarting.
    # 
    # Parameters:
    # - save: bool - Whether to save the project before restarting (default: true)
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.restart_editor(save=true)

    # set_current_feature_profile(profile_name)
    # Sets the current feature profile. Profiles must be in the feature_profiles directory.
    # 
    # Parameters:
    # - profile_name: String - The name of the profile (empty string to reset)
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.set_current_feature_profile("high_performance")

    # set_plugin_enabled(plugin, enabled)
    # Enables or disables a plugin.
    # 
    # Parameters:
    # - plugin: String - The plugin name (same as directory name)
    # - enabled: bool - Whether to enable the plugin
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.set_plugin_enabled("physics", true)

    # popup_quick_open(callback, base_types=[])
    # Opens a dialog to quickly select a resource file.
    # 
    # Parameters:
    # - callback: Callable - Called with the selected resource path
    # - base_types: Array<StringName> - Resource types to filter by
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.popup_quick_open(_on_resource_selected, ["TextureRect"])

    # popup_node_selector(callback, valid_types=[], current_value=null)
    # Opens a dialog to select a node from the scene tree.
    # 
    # Parameters:
    # - callback: Callable - Called with the selected NodePath
    # - valid_types: Array<StringName> - Node types to filter by
    # - current_value: Node - The node to select initially
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.popup_node_selector(_on_node_selected, ["Button"])

    # popup_property_selector(object, callback, type_filter=packed_int32_array(), current_value="")
    # Opens a dialog to select a property from an object.
    # 
    # Parameters:
    # - object: Object - The object to select properties from
    # - callback: Callable - Called with the selected property path
    # - type_filter: PackedInt32Array - Variant types to filter by
    # - current_value: String - The property to select initially
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.popup_property_selector(this, _on_property_selected, [Variant.TYPE_INT])

    # popup_property_selector(object, callback, type_filter=packed_int32_array(), current_value="")
    # Opens a dialog to select a property from an object.
    # 
    # Parameters:
    # - object: Object - The object to select properties from
    # - callback: Callable - Called with the selected property path
    # - type_filter: PackedInt32Array - Variant types to filter by
    # - current_value: String - The property to select initially
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.popup_property_selector(this, _on_property_selected, [Variant.TYPE_INT])

    # popup_quick_open(callback, base_types=[])
    # Opens a dialog to quickly select a resource file.
    # 
    # Parameters:
    # - callback: Callable - Called with the selected resource path
    # - base_types: Array<StringName> - Resource types to filter by
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.popup_quick_open(_on_resource_selected, ["TextureRect"])

    # select_file(file)
    # Selects a file in the FileSystem dock.
    # 
    # Parameters:
    # - file: String - The file path to select
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.select_file("path/to/file.txt")

    # set_main_screen_editor(name)
    # Sets the editor's main screen to a specified tab.
    # 
    # Parameters:
    # - name: String - The tab name (e.g., "2D", "3D", "Script")
    # 
    # Return Value:
    # - None
    # 
    # Example:
    # EditorInterface.set_main_screen_editor("2D")

    # Notes
    # - These methods are only available when in the editor (check Engine.is_editor_hint()).
    # - Feature profiles must be placed in the "feature_profiles" directory.
    # - The "set_main_screen_editor" method requires the tab name to match exactly.
    # - Use "EditorPaths" for resolving paths relative to the project.
```