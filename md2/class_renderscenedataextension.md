# RenderSceneDataExtension

**Inherits:** RenderSceneData < Object

## Description
This class allows for a RenderSceneData implementation to be made in GDExtension.

## Methods
- _get_cam_projection(): Returns a `Projection`. Virtual and const.
- _get_cam_transform(): Returns a `Transform3D`. Virtual and const.
- _get_uniform_buffer(): Returns a `RID`. Virtual and const.
- _get_view_count(): Returns an `int`. Virtual and const.
- _get_view_eye_offset(view: int): Returns a `Vector3`. Virtual and const.
- _get_view_projection(view: int): Returns a `Projection`. Virtual and const.

## Method Descriptions
- _get_cam_projection: Implement this in GDExtension to return the camera `Projection`.
- _get_cam_transform: Implement this in GDExtension to return the camera `Transform3D`.
- _get_uniform_buffer: Implement this in GDExtension to return the `RID` of the uniform buffer containing the scene data as a UBO.
- _get_view_count: Implement this in GDExtension to return the view count.
- _get_view_eye_offset: Implement this in GDExtension to return the eye offset for the given `view`.
- _get_view_projection: Implement this in GDExtension to return the view `Projection` for the given `view`.