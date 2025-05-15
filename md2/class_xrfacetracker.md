### XRFaceTracker Summary

#### Enum Values: BlendShapeEntry
The following enum values define the face blend shape indices:

| Index | Name                              | Description                                                                 |
|-------|-----------------------------------|-----------------------------------------------------------------------------|
| 125   | FT_LIP_PUCKER_UPPER               | Upper lip part pushes outwards.                                            |
| 126   | FT_LIP_PUCKER_LOWER               | Lower lip part pushes outwards.                                            |
| 127   | FT_LIP_PUCKER                     | Lips push outwards.                                                        |
| 128   | FT_MOUTH_UPPER_UP                 | Raises the upper lips.                                                     |
| 129   | FT_MOUTH_LOWER_DOWN               | Lowers the lower lips.                                                     |
| 130   | FT_MOUTH_OPEN                     | Mouth opens, revealing teeth.                                              |
| 131   | FT_MOUTH_RIGHT                    | Moves mouth right.                                                         |
| 132   | FT_MOUTH_LEFT                     | Moves mouth left.                                                          |
| 133   | FT_MOUTH_SMILE_RIGHT              | Right side of the mouth smiles.                                            |
| 134   | FT_MOUTH_SMILE_LEFT               | Left side of the mouth smiles.                                             |
| 135   | FT_MOUTH_SMILE                    | Mouth expresses a smile.                                                   |
| 136   | FT_MOUTH_SAD_RIGHT                | Right side of the mouth expresses sadness.                                 |
| 137   | FT_MOUTH_SAD_LEFT                 | Left side of the mouth expresses sadness.                                  |
| 138   | FT_MOUTH_SAD                      | Mouth expresses sadness.                                                   |
| 139   | FT_MOUTH_STRETCH                  | Mouth stretches.                                                           |
| 140   | FT_MOUTH_DIMPLE                   | Lip corners dimple.                                                        |
| 141   | FT_MOUTH_TIGHTENER                | Mouth tightens.                                                            |
| 142   | FT_MOUTH_PRESS                    | Mouth presses together.                                                    |
| 143   | FT_MAX                            | Represents the size of the BlendShapeEntry enum.                           |

---

#### Property: blend_shapes
- **Type**: `PackedFloat32Array`
- **Description**: An array of face blend shape weights, with indices corresponding to the `BlendShapeEntry` enum.
- **Notes**:
  - The returned array is a copy; changes to it do not affect the original property.
  - Use `PackedFloat32Array` for efficient storage and manipulation.

---

#### Methods

##### `get_blend_shape(blend_shape: BlendShapeEntry) -> float`
- **Description**: Returns the weight of the specified blend shape.
- **Parameters**:
  - `blend_shape`: Enum value (e.g., `FT_LIP_PUCKER_UPPER`).
- **Returns**: The weight of the blend shape.

##### `set_blend_shape(blend_shape: BlendShapeEntry, weight: float)`
- **Description**: Sets the weight of a specific blend shape.
- **Parameters**:
  - `blend_shape`: Enum value (e.g., `FT_MOUTH_SMILE`).
  - `weight`: A float value representing the new weight.

---

### Key Notes
- The `blend_shapes` property is used to control facial expressions via blend shape weights.
- The `FT_MAX` value (143) defines the maximum index for the enum, ensuring all entries are covered.
- Methods for individual blend shapes (e.g., `get_blend_shape`, `set_blend_shape`) allow fine-grained control over facial features.