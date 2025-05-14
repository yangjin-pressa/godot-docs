# MissingNode

**Inherits:** Node < Object

## Description

An internal editor class for storing data of unrecognized nodes. Cannot be manually instantiated or placed in a scene.

**Warning:** Modify missing node properties only if you understand the implications.

## Properties

- **original_class** (String): Name of the intended class (see Object.get_class())
- **original_scene** (String): Path of the original scene
- **recording_properties** (bool): Whether new properties can be added

## Property Details

### original_class
- **set_original_class**(value: String): Set the original class name
- **get_original_class**(): Get the original class name

### original_scene
- **set_original_scene**(value: String): Set the original scene path
- **get_original_scene**(): Get the original scene path

### recording_properties
- **set_recording_properties**(value: bool): Enable/disable property recording
- **is_recording_properties**(): Check if property recording is enabled

## Notes
- This class is intended for internal use only
- Property modifications are not guaranteed to be persistent
- Class name references: [Object.get_class](https://godotengine.org/documentation/classes/class_object.html#class-object-method-get-class)