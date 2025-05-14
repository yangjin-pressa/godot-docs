**FlowContainer Class Summary**

**Inheritance:**  
- Inherits from: `Container`, `Control`, `Node`

**Inherited By:**  
- `HFlowContainer`, `VFlowContainer`

**Description:**  
A container that arranges its children horizontally or vertically, wrapping them as needed. Can be configured to arrange children in either direction.

**Tutorials:**  
- [Using Containers](../tutorials/ui/gui_containers)

**Properties:**  
- **AlignmentMode**  
  - **alignment**: `int` (default: 0)  
    - Determines the alignment of children (e.g., left, right, center).  
- **last_wrap_alignment**: `int` (default: 0)  
  - Alignment of the last line of children.  
- **reverse_fill**: `bool` (default: false)  
  - If true, fills the container in reverse order.  
- **vertical**: `bool` (default: false)  
  - If true, arranges children vertically; otherwise, horizontally.

**Methods:**  
- **get_line_count()** → `int`  
  - Returns the current number of lines in the container.

**Theme Properties:**  
- **h_separation**: `int` (default: 4)  
  - Horizontal spacing between child nodes.  
- **v_separation**: `int` (default: 4)  
  - Vertical spacing between child nodes.

**Enumerations:**  
1. **AlignmentMode**  
   - Constants: `LEFT`, `RIGHT`, `CENTER`, `TOP`, `BOTTOM`, `BASELINE`, `FILL`.  
   - Defines how children are aligned within the container.  

2. **LastWrapAlignment**  
   - Constants: `LEFT`, `RIGHT`, `CENTER`, `TOP`, `BOTTOM`, `BASELINE`, `FILL`.  
   - Defines alignment of the last line of children.

**Property Descriptions:**  
- **alignment**  
  - Sets the alignment of children. Default is `LEFT`.  
- **last_wrap_alignment**  
  - Sets the alignment of the last line of children.  
- **reverse_fill**  
  - If true, children are filled in reverse order.  
- **vertical**  
  - If true, children are arranged vertically; otherwise, horizontally.

**Method Descriptions:**  
- **get_line_count()**  
  - Returns the total number of lines (rows or columns) the container has when children are arranged.

**Theme Property Descriptions:**  
- **h_separation**  
  - Controls horizontal spacing between child nodes.  
- **v_separation**  
  - Controls vertical spacing between child nodes.