# FBXDocument

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** GLTFDocument < Resource < RefCounted < Object

Handles FBX documents. It provides methods to append data from buffers or files, generate scenes, and register/unregister document extensions.

When exporting FBX from Blender, use the "FBX Units Scale" option. The "FBX Units Scale" option sets the correct scale factor and avoids manual adjustments when re-importing into Blender, such as through glTF export.

Key terminology:
- virtual (This method should typically be overridden by the user to have any effect.)
- const (This method has no side effects. It doesn't modify any of the instance's member variables.)
- vararg (This method accepts any number of arguments after the ones described here.)
- constructor (This method is used to construct a type.)
- static (This method doesn't need an instance to be called, so it can be called directly using the class name.)
- operator (This method describes a valid operator to use with this type as left-hand operand.)
- bitfield (This value is an integer composed as a bitmask of the following flags.)
- void (No return value.)