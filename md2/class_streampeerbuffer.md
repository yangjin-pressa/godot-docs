# StreamPeerBuffer

**Inherits:** StreamPeer < RefCounted < Object

A stream peer used to handle binary data streams.

## Description
A data buffer stream peer that uses a byte array as the stream. This object can be used to handle binary data from network sessions. To handle binary data stored in files, FileAccess can be used directly.

A StreamPeerBuffer object keeps an internal cursor which is the offset in bytes to the start of the buffer. Get and put operations are performed at the cursor position and will move the cursor accordingly.

## Properties
- **data_array**: PackedByteArray = PackedByteArray()
  - The underlying data buffer. Setting this value resets the cursor.
  - Note: The returned array is *copied* and any changes to it will not update the original property value.

## Methods
- **clear()**: 
  - Clears the data_array and resets the cursor.

- **duplicate()** → StreamPeerBuffer:
  - Returns a new StreamPeerBuffer with the same data_array content.

- **get_position()** → int:
  - Returns the current cursor position.

- **get_size()** → int:
  - Returns the size of data_array.

- **resize(size: int)**:
  - Resizes the data_array. This *doesn't* update the cursor.

- **seek(position: int)**:
  - Moves the cursor to the specified position. position must be a valid index of data_array.

## Notes
- The data_array property is copied when accessed, so modifications to the returned array do not affect the original.