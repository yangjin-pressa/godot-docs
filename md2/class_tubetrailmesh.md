# TubeTrailMesh

A class that represents a trail of particles or objects in a 3D environment, used for effects like explosions or moving entities. It allows for dynamic updates and rendering of the trail.

## Tutorials
- **3D Particle trails**: A guide to creating and using particle trails in 3D environments.
- **Particle systems (3D)**: An overview of how to implement and manage particle systems in 3D projects.

## Properties

### cap_bottom
- **Type**: bool  
- **Default**: true  
- **Description**: If true, generates a cap at the bottom of the tube.

### cap_top
- **Type**: bool  
- **Default**: true  
- **Description**: If true, generates a cap at the top of the tube.

### curve
- **Type**: Curve  
- **Default**: default  
- **Description**: The curve that defines the shape of the trail.

### width
- **Type**: float  
- **Default**: default  
- **Description**: The width of the trail.

### length
- **Type**: float  
- **Default**: default  
- **Description**: The length of the trail.

### material
- **Type**: Material  
- **Default**: default  
- **Description**: The material used to render the trail.

### life
- **Type**: float  
- **Default**: default  
- **Description**: The lifespan of each particle in the trail.

### max_particles
- **Type**: int  
- **Default**: default  
- **Description**: The maximum number of particles in the trail.

### update_interval
- **Type**: float  
- **Default**: default  
- **Description**: The interval at which the trail is updated.

### visible
- **Type**: bool  
- **Default**: default  
- **Description**: Whether the trail is visible in the scene.

This class is essential for creating dynamic visual effects in 3D environments, allowing developers to simulate trails, explosions, and other motion-based phenomena.