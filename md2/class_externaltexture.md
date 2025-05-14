# ExternalTexture

**Inherits:** Texture2D < Texture < Resource < RefCounted < Object

## Description
Displays content of an external buffer provided by the platform.

Requires:
- OES_EGL_image_external (OpenGL)
- VK_ANDROID_external_memory_android_hardware_buffer (Vulkan)

**Note:** Currently only supported in Android builds.

## Properties
- **resource_local_to_scene**: bool = false (overrides Resource property)
- **size**: Vector2 = Vector2(256, 256)

## Methods
- **get_external_texture_id()** → int: Returns external texture ID
- **set_external_buffer_id(int external_buffer_id)**: Sets external buffer ID

## Property Descriptions
**size**: Vector2 = Vector2(256, 256)
- Sets/get external texture dimensions

## Method Descriptions
**get_external_texture_id()** → int: 
- Returns external texture ID (for platform API use)

**set_external_buffer_id(int external_buffer_id)**:
- Sets external buffer ID (e.g. from SurfaceTexture.getHardwareBuffer())

## References
- [OES_EGL_image_external](https://registry.khronos.org/OpenGL/extensions/OES/OES_EGL_image_external.txt)
- [VK_ANDROID_external_memory_android_hardware_buffer](https://registry.khronos.org/vulkan/specs/1.1-extensions/html/vkspec.html#VK_ANDROID_external_memory_android_hardware_buffer)