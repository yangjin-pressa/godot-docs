# BitMap

**Inherits:** Resource → RefCounted → Object

## Description
A 2D array of boolean values for efficient binary matrix storage and querying. Each element uses one bit.

## Methods
- **convert_to_image()** → Image: Converts to an image with black/white pixels based on bit values.
- **create(Vector2i size)**: Initializes a bitmap with the given size, filled with false.
- **create_from_image_alpha(Image image, float threshold=0.1)**: Creates a bitmap from an image, using alpha threshold to determine bit values.
- **get_bit(int x, int y)** → bool: Retrieves the value at (x, y).
- **get_bitv(Vector2i position)** → bool: Retrieves the value at a position.
- **get_size()** → Vector2i: Returns bitmap dimensions.
- **get_true_bit_count()** → int: Returns count of true bits.
- **grow_mask(int pixels, Rect2i rect)**: Applies dilation/erosion to a rectangular area.
- **opaque_to_polygons(Rect2i rect, float epsilon=2.0)** → Array<PackedVector2Array>: Converts bitmap to polygons using marching squares and RDP algorithms.
- **resize(Vector2i new_size)**: Resizes the bitmap to new dimensions.
- **set_bit(int x, int y, bool bit)**: Sets a single bit value.
- **set_bit_rect(Rect2i rect, bool bit)**: Sets a rectangular area to a single value.
- **set_bitv(Vector2i position, bool bit)**: Sets a single bit value.

## Method Descriptions
- **convert_to_image()**: Generates an L8 format image where true bits are white, false are black.
- **create()**: Initializes a blank bitmap with specified dimensions.
- **create_from_image_alpha()**: Converts an image to a bitmap using alpha thresholds for bit assignment.
- **get_bit()**: Retrieves the boolean value at a specific coordinate.
- **get_bitv()**: Same as get_bit(), using a Vector2i for position.
- **get_size()**: Returns the bitmap's width and height.
- **get_true_bit_count()**: Counts all true bits in the matrix.
- **grow_mask()**: Modifies a rectangular region via morphological operations (dilation/erosion).
- **opaque_to_polygons()**: Converts bitmap data to polygon arrays for visual representation.
- **resize()**: Adjusts the bitmap's dimensions, potentially expanding or shrinking it.
- **set_bit()**: Sets a single bit at a coordinate to true/false.
- **set_bit_rect()**: Applies a uniform value to a rectangular region of the bitmap.
- **set_bitv()**: Same as set_bit(), using a Vector2i for position.