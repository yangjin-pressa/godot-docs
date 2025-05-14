# Lightmapper

**Inherits:** RefCounted < Object  
**Inherited By:** LightmapperRD  

## Description  
- This class should be extended by custom lightmapper classes.  
- Lightmappers can be used with [LightmapGI](class_LightmapGI) to provide fast baked global illumination in 3D.  
- Godot has a built-in GPU-based lightmapper [LightmapperRD](class_LightmapperRD) that uses compute shaders.  
- Custom lightmappers can be implemented by C++ modules.  

## Notes  
- virtual (This method should typically be overridden by the user to have any effect.)  
- const (This method has no side effects. It doesn't modify any of the instance's member variables.)  
- vararg (This method accepts any number of arguments after the ones described here.)  
- constructor (This method is used to construct a type.)  
- static (This method doesn't need an instance to be called, so it can be called directly using the class name.)  
- operator (This method describes a valid operator to use with this type as left-hand operand.)  
- bitfield (This value is an integer composed as a bitmask of the following flags.)  
- void (No return value.)