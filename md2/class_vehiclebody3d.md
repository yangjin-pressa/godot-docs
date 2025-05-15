**Class: VehicleBody3D**  
**Inherits:** RigidBody3D → PhysicsBody3D → CollisionObject3D → Node3D → Node → Object  

---

### **Description**  
A 3D physics body for simulating car behavior. Requires:  
- A `CollisionShape3D` for the vehicle body  
- `VehicleWheel3D` nodes for each wheel  
- A `MeshInstance3D` for the vehicle model (exclude wheels)  

**Key Features:**  
- Controls via `brake`, `engine_force`, and `steering` properties  
- Origin point defines vehicle center of gravity  
- Not designed for realistic physics; advanced simulation may require custom code  

---

### **Tutorials**  
- [3D Truck Town Demo](https://godotengine.org/asset-library/asset/2752)  

---

### **Properties**  
- **brake** (float): Slows vehicle (0.0 by default). Effective only when wheels are on a surface.  
- **engine_force** (float): Accelerates vehicle (0.0 by default). Effective when traction wheels are on a surface.  
- **mass** (float): 40.0 (overrides RigidBody3D.mass).  
- **steering** (float): Steering angle (0.0 by default).  

---

### **Property Descriptions**  
#### **brake**  
- **Set/Get:** `set_brake(value: float)`, `get_brake()`.  
- **Note:** Braking force depends on vehicle mass. For 1000 kg, use 25–30 for hard braking.  

#### **engine_force**  
- **Set/Get:** `set_engine_force(value: float)`, `get_engine_force()`.  
- **Note:** Negative values reverse the vehicle. Simulation ignores gear ratios.  

#### **steering**  
- **Set/Get:** `set_steering(value: float)`, `get_steering()`.  
- **Note:** Inspector uses degrees; code uses radians.  

---

### **Important Notes**  
1. Origin point affects vehicle gravity. Lower origin improves ground contact.  
2. Simulation lacks realistic physics; custom logic may be needed for advanced behavior.  
3. Wheel properties (e.g., `use_as_traction`) determine vehicle interaction with surfaces.