# PhysicalBoneSimulator3D

**Inherits:** SkeletonModifier3D < Node3D < Node < Object

Node that can be the parent of PhysicalBone3D and can apply the simulation results to Skeleton3D.

## Methods

- **is_simulating_physics()**: Returns a boolean indicating whether the PhysicalBoneSimulator3D is running and simulating.
- **physical_bones_add_collision_exception(exception: RID)**: Adds a collision exception to the physical bone. Works just like RigidBody3D.
- **physical_bones_remove_collision_exception(exception: RID)**: Removes a collision exception from the physical bone. Works just like RigidBody3D.
- **physical_bones_start_simulation(bones: Array<StringName> = [])**: Tells PhysicalBone3D nodes in the Skeleton to start simulating and reacting to the physics world. Optionally, a list of bone names can be passed to simulate only those bones.
- **physical_bones_stop_simulation()**: Tells PhysicalBone3D nodes in the Skeleton to stop simulating.

## Description

Node that can be the parent of PhysicalBone3D and can apply the simulation results to Skeleton3D.