The `GLTFState` class in the Godot engine is a crucial component for managing the state of a GLTF (GL Transmission Format) 3D model during import and export processes. It serves as a container for various elements of a 3D model, such as buffers, meshes, animations, textures, and more, enabling the engine to process and render GLTF assets efficiently.

### Key Functions and Purpose

1. **Data Storage and Management**:
   - The class stores and organizes data structures like `BufferView`, `Camera`, `Mesh`, `Texture`, and `Animation` to represent a 3D model's geometry, materials, and animations.
   - It acts as a bridge between the raw GLTF data and Godot's internal systems, allowing the engine to access and manipulate these elements as needed.

2. **Import and Export Operations**:
   - **Import**: When importing a GLTF file, the `GLTFState` holds the parsed data, which is then used to create or update Godot's resources (e.g., `Mesh`, `Texture`, `AnimationPlayer`).
   - **Export**: During export, the state is used to serialize the model's data back into a GLTF format, ensuring compatibility with external tools or other engines.

3. **Reference Management**:
   - The class manages references to assets (e.g., textures, lights) that are used by the model's components. This ensures that the model correctly uses the appropriate resources during rendering or animation.

4. **Customization and Overrides**:
   - Developers can use setter methods (e.g., `set_images`, `set_animations`) to customize the state before exporting or during import, allowing for post-processing or overrides of default behavior.

### Key Methods and Their Roles

- **`set_images` / `get_images`**: 
  - **Purpose**: Store or retrieve an array of `Texture2D` objects representing the model's textures.
  - **Use Case**: During export, these textures are written to the GLTF file. During import, they are loaded into the model.

- **`set_animations` / `get_animations`**: 
  - **Purpose**: Store or retrieve animations that are part of the model.
  - **Use Case**: Animations are imported into an `AnimationPlayer` node or exported as keyframes.

- **`set_lights` / `get_lights`**: 
  - **Purpose**: Manage light data (e.g., directional, point lights) referenced by the model's nodes.
  - **Use Case**: Ensures the model's lighting is correctly applied during rendering.

- **`set_unique_names` / `get_unique_names`**: 
  - **Purpose**: Track unique names for nodes and animations to avoid collisions during import/export.
  - **Use Case**: Helps maintain consistency in asset naming for complex models.

- **`set_unique_animation_names` / `get_unique_animation_names`**: 
  - **Purpose**: Manage unique animation names to prevent conflicts in the exported GLTF file.
  - **Use Case**: Ensures animations are correctly identified in the exported file.

### Example Usage

```gdscript
# Example: Setting up a GLTFState for a model
var state = GLTFState.new()

# Set textures for the model
state.set_images([texture1, texture2])

# Set animations to include in the export
state.set_animations([animation1, animation2])

# Set light data for the model
state.set_lights([light1, light2])

# Export the state to a GLTF file
# (Assuming a custom export function exists)
export_gltf(state, "path/to/model.glb")
```

### When to Use This Class

- **Importing GLTF Models**: The `GLTFState` is populated with data from the GLTF file, which is then used to create Godot resources.
- **Exporting Models**: The state is populated with Godot's data (e.g., textures, animations) and serialized into a GLTF file.
- **Custom Processing**: Developers might use the state to modify or extend the model's data before export, such as applying post-processing to textures or adjusting animation parameters.

### Conclusion

The `GLTFState` class is a foundational part of Godot's GLTF handling capabilities, enabling seamless integration between external 3D assets and Godot's engine. By managing the state of a model's data, it ensures that the engine can correctly render, animate, and interact with GLTF models. Understanding its methods and their purposes is essential for developers working with 3D assets in Godot.