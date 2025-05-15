# ShaderGlobalsOverride

**Inherits**: Node < Object

A node used to override global shader parameters' values in a scene.

## Description
- Overrides global shader parameters temporarily. Once the node is removed, project-wide values are restored.
- Similar to how a WorldEnvironment node can override environment settings, this node controls shader parameters.

## Notes
- Only one ShaderGlobalsOverride can be used per scene. If multiple exist, only the first in the scene tree is active.
- All nodes are added to a "shader_overrides_group" when placed in the scene tree. The active node also has a "shader_overrides_group_active" group.

## Tutorials
- Shading language

## References
- WorldEnvironment
- RenderingServer