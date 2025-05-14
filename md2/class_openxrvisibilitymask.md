# OpenXRVisibilityMask

## Inheritance
- **VisualInstance3D**  
  - **Node3D**  
    - **Node**  
      - **Object**

## Description
- Draws a stereo correct visibility mask to black out areas of the render result invisible due to lens distortion.
- Rendered first to prevent fragments with expensive lighting calculations from being processed, as they are discarded through z-checking.

## Notes
- **virtual**: This method should typically be overridden by the user to have any effect.
- **const**: This method has no side effects. It doesn't modify any of the instance's member variables.
- **vararg**: This method accepts any number of arguments after the ones described here.
- **static**: This method doesn't need an instance to be called, so it can be called directly using the class name.
- **operator**: This method describes a valid operator to use with this type as left-hand operand.
- **bitfield**: This value is an integer composed as a bitmask of the following flags.
- **void**: No return value.