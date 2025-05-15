# RandomNumberGenerator

## Overview
A class for generating pseudo-random numbers using the PCG32 algorithm. Provides methods for float/int random generation, weighted selection, and state management.

## Key Features
- Underlying algorithm: PCG32 (https://www.pcg-random.org/)
- Uses time-based seed for reproducible sequences
- Supports weighted random selection
- Maintains state for persistent random sequences

## Properties
- **seed**: Integer (default 0) - Seed value for random generation
- **state**: Integer (default 0) - Current state of the random generator

## Methods
- **rand_weighted(weights: PackedFloat32Array)** → int
  - Returns weighted random index from array
  - Example: `my_array[rng.rand_weighted(weights)]`

- **randf()** → float
  - Returns random float between 0.0 and 1.0

- **randf_range(from: float, to: float)** → float
  - Returns random float between specified values

- **randfn(mean: float = 0.0, deviation: float = 1.0)** → float
  - Returns normally-distributed float (Box-Muller algorithm)

- **randi()** → int
  - Returns random 32-bit unsigned integer (0-4294967295)

- **randi_range(from: int, to: int)** → int
  - Returns random 32-bit signed integer

- **randomize()**
  - Sets time-based seed for random generation

## Property Details
### seed
- Sets initial seed value for random sequence
- Changing this value affects the internal state
- Default value is pseudo-random, not the literal 0

### state
- Represents current state of the random generator
- Save/restoring state allows resuming previous sequences
- Should not be set to arbitrary values

## Method Details
### randomize()
- Uses system time to generate seed
- Allows different instances to have independent sequences
- Note: Default seed is pseudo-random, not 0

## Example Usage
```gdscript
var rng = RandomNumberGenerator.new()
rng.seed = hash("Godot")
var my_array = ["one", "two", "three", "four"]
var weights = PackedFloat32Array([0.5, 1, 1, 2])
print(my_array[rng.rand_weighted(weights)])
```

## Notes
- RNG does not have avalanche effect
- Seed quality should be improved using hash functions
- State values should only come from the state property itself
- Default values are placeholders, actual defaults are pseudo-random