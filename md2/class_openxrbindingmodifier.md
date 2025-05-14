# OpenXRBindingModifier

**Inherits:** Resource < RefCounted < Object  
**Inherited By:** OpenXRActionBindingModifier, OpenXRIPBindingModifier  

## Description  
Binding modifier base class. Subclasses implement various modifiers that alter how an OpenXR runtime processes inputs.

## Methods  
- **_get_description**  
  Return the description of this class that is used for the title bar of the binding modifier editor.  
  - **Return Type:** String  
  - **Note:** This method is virtual and const (no side effects).  

- **_get_ip_modification**  
  Returns the data sent to OpenXR when submitting interacting bindings.  
  - **Return Type:** PackedByteArray  
  - **Note:** Data must be compatible with XrBindingModificationBaseHeaderKHR structure.  

## References  
- [🔗 _get_description](class_OpenXRBindingModifier_private_method__get_description)  
- [🔗 _get_ip_modification](class_OpenXRBindingModifier_private_method__get_ip_modification)