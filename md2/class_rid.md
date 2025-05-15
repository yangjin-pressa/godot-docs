# RID

A handle for a resource's unique identifier.

## Description
The RID type is used to access a low-level resource by its unique ID. RIDs are opaque and used by server classes like DisplayServer, RenderingServer, TextServer, etc. A low-level resource may correspond to a high-level Resource (e.g., Texture, Mesh). 

**Note:** RIDs are only useful during the current session. They won't correspond to a resource if sent over a network or loaded from a file later.

There are notable differences when using this API with C#. See [doc_c_sharp_differences](doc_c_sharp_differences) for more information.

## Constructors
- **RID()**: Constructs an empty RID with the invalid ID 0.
- **RID(from: RID)**: Constructs a RID as a copy of the given RID.

## Methods
- **get_id()**: Returns the ID of the referenced low-level resource.
- **is_valid()**: Returns true if the RID is not 0.

## Operators
- **!=** (right: RID): Returns true if the RIDs are not equal.
- **<** (right: RID): Returns true if the RID's ID is less than right's ID.
- **<=** (right: RID): Returns true if the RID's ID is less than or equal to right's ID.
- **==** (right: RID): Returns true if both RIDs are equal (same resource).
- **>** (right: RID): Returns true if the RID's ID is greater than right's ID.
- **>=** (right: RID): Returns true if the RID's ID is greater than or equal to right's ID.

## Notes
- RIDs are session-specific and not persistent across sessions.
- C# users should refer to [doc_c_sharp_differences](doc_c_sharp_differences) for implementation specifics.