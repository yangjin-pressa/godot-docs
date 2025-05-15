**Class Hierarchy**  
- `RectangleShape2D`  
  - Inherits: `Shape2D` → `Resource` → `RefCounted` → `Object`  

**Description**  
A 2D rectangle shape used for physics collision. Typically used to provide a shape for a `CollisionShape2D`.  
Performance: Faster than `CapsuleShape2D`, slower than `CircleShape2D`.  

**Tutorials**  
- [2D Pong Demo](https://godotengine.org/asset-library/asset/2728)  
- [2D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2719)  

**Properties**  
- **size**: `Vector2` = `Vector2(20, 20)`  

**Property Descriptions**  
- **size**:  
  - **Description**: The rectangle's width and height.  
  - **Methods**:  
    - `set_size(value: Vector2)`  
    - `get_size()`  

**Notes**  
- **virtual**: This method should typically be overridden by the user to have any effect.  
- **const**: This method has no side effects. It doesn't modify any of the instance's member variables.  
- **vararg**: This method accepts any number of arguments after the ones described here.  
- **constructor**: This method is used to construct a type.  
- **static**: This method doesn't need an instance to be called, so it can be called directly using the class name.  
- **operator**: This method describes a valid operator to use with this type as left-hand operand.  
- **bitfield**: This value is an integer composed as a bitmask of the following flags.  
- **void**: No return value.