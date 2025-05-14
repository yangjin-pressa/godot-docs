# BoxContainer

**Inherits:** Container → Control → CanvasItem → Node → Object  
**Inherited By:** HBoxContainer, VBoxContainer  

## Description  
A container that arranges its child controls horizontally or vertically, rearranging them automatically when their minimum size changes.

## Tutorials  
- [Using Containers](../tutorials/ui/gui_containers)

## Properties  
- **alignment**: AlignmentMode = 0  
- **vertical**: bool = false  

## Methods  
- **add_spacer**(begin: bool): Control  

## Theme Properties  
- **separation**: int = 4  

## Enumerations  
### AlignmentMode  
- **ALIGNMENT_BEGIN** = 0  
  - Children arranged at the beginning of the container (top/left).  
- **ALIGNMENT_CENTER** = 1  
  - Children centered in the container.  
- **ALIGNMENT_END** = 2  
  - Children arranged at the end of the container (bottom/right).  

## Property Descriptions  
### alignment  
- **set_alignment**(value: AlignmentMode): void  
- **get_alignment**(): AlignmentMode  
  - Controls the alignment of children (must be one of ALIGNMENT_BEGIN, ALIGNMENT_CENTER, or ALIGNMENT_END).  

### vertical  
- **set_vertical**(value: bool): void  
- **is_vertical**(): bool  
  - If true, children are arranged vertically.  
  - Cannot be changed when using HBoxContainer or VBoxContainer.  

## Method Descriptions  
### add_spacer  
- Adds a Control node as a spacer. If begin is true, inserts it in front of other children.  

## Theme Property Descriptions  
### separation  
- The space between elements, in pixels.