# MissingResource

**Inherits:** Resource < RefCounted < Object

## Description
An internal editor class for storing data of unrecognized resources.
- **Warning:** Do not modify existing properties on missing resources unless you know what you're doing.

## Properties
- **original_class** (String): The class name this resource was supposed to represent (see [Object.get_class()](class_Object_method_get_class)).
- **recording_properties** (bool): If true, allows adding new properties via Object.set().

## Property Descriptions

### original_class
- **set_original_class**(value: String): Sets the original class name.
- **get_original_class**(): Returns the original class name.

### recording_properties
- **set_recording_properties**(value: bool): Sets whether new properties can be added.
- **is_recording_properties**(): Returns the current state of recording properties.