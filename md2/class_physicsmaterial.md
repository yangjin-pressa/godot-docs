PhysicsMaterial  
Inherits: Resource < RefCounted < Object  

Description: Holds physics-related properties of a surface, namely its roughness and bounciness. This class is used to apply these properties to a physics body.  

Properties:  
- absorbent: bool (false)  
- bounce: float (0.0)  
- friction: float (1.0)  
- rough: bool (false)  

Property Descriptions:  
- **absorbent** (bool): If true, subtracts the bounciness from the colliding object's bounciness instead of adding it.  
  - set_absorbent(value: bool)  
  - is_absorbent()  

- **bounce** (float): The body's bounciness. Values range from 0 (no bounce) to 1 (full bounciness).  
  - set_bounce(value: float)  
  - get_bounce()  

- **friction** (float): The body's friction. Values range from 0 (frictionless) to 1 (maximum friction).  
  - set_friction(value: float)  
  - get_friction()  

- **rough** (bool): If true, the physics engine uses the friction of the object marked as "rough" when two objects collide. If false, it uses the lowest friction of all colliding objects.  
  - set_rough(value: bool)  
  - is_rough()  

Note: Even with bounce set to 1.0, some energy is lost over time due to linear and angular damping. To preserve energy, set bounce to 1.0, linear damp mode to Replace, linear damp to 0.0, angular damp mode to Replace, and angular damp to 0.0.