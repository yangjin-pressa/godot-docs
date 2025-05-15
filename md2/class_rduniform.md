# RDUniform

**Inherits:** RefCounted < Object

Shader uniform (used by RenderingDevice).

## Description
This object is used by RenderingDevice.

## Properties
- **binding**: int = 0  
  The uniform's binding.

- **uniform_type**: UniformType = 3  
  The uniform's data type.

## Methods
- **add_id**(id: RID): void  
  Binds the given id to the uniform. The data associated with the id is then used when the uniform is passed to a shader.  
  *virtual (This method should typically be overridden by the user to have any effect.)*

- **clear_ids**(): void  
  Unbinds all ids currently bound to the uniform.  
  *const (This method has no side effects. It doesn't modify any of the instance's member variables.)*

- **get_ids**(): Array<RID> |const  
  Returns an array of all ids currently bound to the uniform.

## Property Descriptions
**binding**: int = 0  
- set_binding(value: int): void  
- get_binding(): int  

**uniform_type**: UniformType = 3  
- set_uniform_type(value: UniformType): void  
- get_uniform_type(): UniformType  

## Method Descriptions
**add_id**(id: RID): void  
Binds the given id to the uniform. The data associated with the id is then used when the uniform is passed to a shader.

**clear_ids**(): void  
Unbinds all ids currently bound to the uniform.

**get_ids**(): Array<RID> |const  
Returns an array of all ids currently bound to the uniform.