# EncodedObjectAsID

**Inherits:** RefCounted < Object

## Description

Utility class which holds a reference to the internal identifier of an Object instance, as given by Object.get_instance_id(). This ID can then be used to retrieve the object instance with @GlobalScope.instance_from_id().

This class is used internally by the editor inspector and script debugger, but can also be used in plugins to pass and display objects as their IDs.

## Properties

- **object_id**: int = 0 (the internal identifier of an Object instance)

## Property Descriptions

**object_id**  
- **set_object_id**(value: int): Sets the object ID.
- **get_object_id**(): Returns the object ID.

The Object identifier stored in this EncodedObjectAsID instance. The object instance can be retrieved with @GlobalScope.instance_from_id().

## References

- [Object.get_instance_id](class_Object_method_get_instance_id)
- [GlobalScope.instance_from_id](class_@GlobalScope_method_instance_from_id)