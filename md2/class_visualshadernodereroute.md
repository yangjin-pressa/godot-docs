# VisualShaderNodeReroute

## Inheritance
- **VisualShaderNodeReroute**  
  < **VisualShaderNode**  
  < **Resource**  
  < **RefCounted**  
  < **Object**

## Description
Automatically adapts its port type to the type of the incoming connection and ensures valid connections.

## Methods
- **get_port_type**  
  Returns: `PortType`  
  Description: Returns the port type of the reroute node.  
  - `const`: No side effects, no instance modifications.

## Key Attributes
- **PortType**: Enum value representing the port type (e.g., `enum_VisualShaderNode_PortType`).  
- **Reroute Functionality**: Redirects connections within the visual shader graph.  

## Citations
- :ref:`PortType<enum_VisualShaderNode_PortType>`  
- :ref:`class_VisualShaderNodeReroute_method_get_port_type`