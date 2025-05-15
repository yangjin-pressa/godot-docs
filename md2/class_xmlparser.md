XMLParser Documentation

Description
- Parses XML files or buffers.
- Methods for opening files/buffers, reading nodes, and navigating through XML structure.
- Properties to retrieve node information like current line, node type, and attributes.

Methods
- **open(file)**: Opens an XML file for parsing. Returns an error code.
- **open_buffer(buffer)**: Opens an XML buffer for parsing. Returns an error code.
- **read()**: Parses the next node in the file. Returns an error code.
- **seek(position)**: Moves the buffer cursor to a specific offset. Returns an error code.
- **skip_section()**: Skips the current section, ignoring inner nodes.

Properties
- **get_current_line()**: Returns the current line number in the parsed file.
- **get_node_type()**: Returns the type of the current node (e.g., NODE_TYPE_0, NODE_TYPE_1).
- **get_node_name()**: Returns the name of the current node. Applies to text, CDATA, and comment nodes.
- **get_node_offset()**: Returns the byte offset of the current node in the file or buffer.
- **get_node_data()**: Returns the contents of a text node. Errors if node is not text.

Attributes
- **has_attribute(name)**: Returns true if the current element has an attribute with the specified name.
- **get_named_attribute_value(name)**: Returns the value of an attribute by name. Raises an error if the attribute doesn't exist.
- **get_named_attribute_value_safe(name)**: Returns the value of an attribute by name or an empty string if it doesn't exist.
- **is_empty()**: Returns true if the current element is empty (e.g., `<element />`).

Enumerations
NodeType
- NODE_TYPE_0: Represents the first node type (e.g., start tag).
- NODE_TYPE_1: Represents the second node type (e.g., end tag).
- NODE_TYPE_2: Represents the third node type (e.g., text).
- NODE_TYPE_3: Represents the fourth node type (e.g., CDATA).
- NODE_TYPE_4: Represents the fifth node type (e.g., comment).
- NODE_TYPE_5: Represents the sixth node type (e.g., processing instruction).