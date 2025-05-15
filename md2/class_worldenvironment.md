# WorldEnvironment

**Inherits:** Node < Object

Default environment properties for the entire scene (post-processing effects, lighting and background settings).

## Description
The WorldEnvironment node is used to configure the default Environment for the scene. Parameters can be overridden by an Environment node set on the Camera3D. Only one WorldEnvironment may be instantiated in a scene.

## Tutorials
- Environment and post-processing: https://godotengine.org/docs/tutorials/3d/environment_and_post_processing.html
- 3D Material Testers Demo: https://godotengine.org/asset-library/asset/2742
- Third Person Shooter (TPS) Demo: https://godotengine.org/asset-library/asset/2710

## Properties
- **camera_attributes**: CameraAttributes (default resource for Camera3D)
  - set_camera_attributes(value: CameraAttributes)
  - get_camera_attributes()

- **compositor**: Compositor (default resource for Camera3D)
  - set_compositor(value: Compositor)
  - get_compositor()

- **environment**: Environment (defines default properties)
  - set_environment(value: Environment)
  - get_environment()

## Key Features
- Configures global lighting and post-processing effects
- Allows background settings (solid color, skybox)
- Overrides can be applied to individual Camera3D nodes