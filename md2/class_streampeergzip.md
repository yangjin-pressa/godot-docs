**StreamPeerGZIP**  
- **Experimental:** This class may be changed or removed in future versions.  
- **Inherits:** `StreamPeer → RefCounted → Object`  

**Description**  
This class allows compressing or decompressing data using GZIP/deflate in a streaming fashion. To use it:  
1. Start a compression or decompression stream using `start_compression()` or `start_decompression()`.  
2. Repeatedly call `put_partial_data()` to add data, check available data with `get_available_bytes()`, and retrieve data with `get_partial_data()`.  
3. Call `finish()` to finalize the stream.  

**Methods**  
- **clear**  
  - **Return:** `void`  
  - **Description:** Clears this stream, resetting the internal state.  

- **finish**  
  - **Return:** `Error`  
  - **Description:** Finalizes the stream, compressing any buffered data. Must be called only when compressing.  

- **start_compression**  
  - **Return:** `Error`  
  - **Parameters:**  
    - `use_deflate` (bool = false)  
    - `buffer_size` (int = 65535)  
  - **Description:** Starts the stream in compression mode. If `use_deflate` is true, it uses deflate instead of GZIP.  

- **start_decompression**  
  - **Return:** `Error`  
  - **Parameters:**  
    - `use_deflate` (bool = false)  
    - `buffer_size` (int = 65535)  
  - **Description:** Starts the stream in decompression mode. If `use_deflate` is true, it uses deflate instead of GZIP.