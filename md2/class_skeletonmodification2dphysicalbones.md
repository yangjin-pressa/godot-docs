# SkeletonModification2DPhysicalBones

**Experimental:** Physical bones may be changed in the future to perform the position update of Bone2D on their own, without needing this resource.

**Inherits:** SkeletonModification2D → Resource → RefCounted → Object

A modification that applies the transforms of PhysicalBone2D nodes to Bone2D nodes.

---

## Description
This modification takes the transforms of PhysicalBone2D nodes and applies them to Bone2D nodes. This allows Bone2D nodes to react to physics through linked PhysicalBone2D nodes.

---

## Properties
- **physical_bone_chain_length**: int = 0  
  The number of PhysicalBone2D nodes linked in this modification.

---

## Methods
- **fetch_physical_bones()**  
  Empties and populates the list of PhysicalBone2D nodes, gathering all children of Skeleton2D.

- **get_physical_bone_node(joint_idx: int)** → NodePath  
  Returns the PhysicalBone2D node at the specified joint index.

- **set_physical_bone_node(joint_idx: int, physicalbone2d_node: NodePath)**  
  Sets the PhysicalBone2D node at the specified joint index.  
  **Note:** This is the index for this modification, not the bone index in Skeleton2D.

- **start_simulation(bones: Array<StringName> = [])**  
  Tells PhysicalBone2D nodes to start simulating and interacting with the physics world. Optionally, specify bone names to target specific nodes.

- **stop_simulation(bones: Array<StringName> = [])**  
  Tells PhysicalBone2D nodes to stop simulating and interacting with the physics world. Optionally, specify bone names to target specific nodes.