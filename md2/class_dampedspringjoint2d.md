**DampedSpringJoint2D**  

**Inheritance**  
- `DampedSpringJoint2D` → `Joint2D` → `Node2D` → `Object`  

**Description**  
A physics joint that connects two 2D physics bodies with a spring-like force.  

---

**Properties**  
- **damping**: `float` = 1.0  
- **length**: `float` = 50.0  
- **rest_length**: `float` = 0.0  
- **stiffness**: `float` = 20.0  

---

**Property Descriptions**  

**damping**  
The spring joint's damping ratio. A value between 0 and 1. When the two bodies move into different directions, the system tries to align them to the spring axis again. A higher damping value forces the attached bodies to align faster.  
- `set_damping(value: float)`  
- `get_damping()`  

**length**  
The length of the spring.  
- `set_length(value: float)`  
- `get_length()`  

**rest_length**  
The length of the spring when it is at its equilibrium position (unstretched).  
- `set_rest_length(value: float)`  
- `get_rest_length()`  

**stiffness**  
The stiffness of the spring, determining how forcefully it resists compression or extension.  
- `set_stiffness(value: float)`  
- `get_stiffness()`