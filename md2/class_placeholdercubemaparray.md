**Class: PlaceholderCubemapArray**  
**Inherits:**  
- PlaceholderTextureLayered  
- TextureLayered  
- Texture  
- Resource  
- RefCounted  
- Object  

**Description:**  
- Replaces CubemapArray or derived class in two scenarios:  
  1. **Dedicated server mode**: Reduces PCK file size.  
  2. **When the derived class is missing**: Falls back to this class.  
- **Not intended for rendering or shaders**: Operations like UV calculation may fail.  

**Key Terms:**  
- **virtual**: Methods should be overridden by the user.  
- **const**: Methods have no side effects.  
- **vararg**: Accepts variable arguments.  
- **constructor**: Used to create an instance.  
- **static**: Callable without an instance.  
- **operator**: Represents a valid operator for this type.  
- **bitfield**: An integer bitmask for flags.  
- **void**: Returns no value.  

This class serves as a fallback mechanism for scenarios where direct use of a CubemapArray or its derived class is impractical or unnecessary.