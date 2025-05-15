# SkeletonModification2DStackHolder

**Experimental**: This class may be changed or removed in future versions.

**Inherits**: SkeletonModification2D → Resource → RefCounted → Object

A modification that holds and executes a SkeletonModificationStack2D. This allows using multiple modification stacks on a single Skeleton2D.

## Key Information

- **Purpose**: Holds a reference to a SkeletonModificationStack2D, enabling multiple stacks on a Skeleton2D.
- **Execution Condition**: Modifications in the held stack are only executed if their execution mode matches the StackHolder's mode.

## Methods

- **get_held_modification_stack()**  
  Returns the SkeletonModificationStack2D held by this modification.  
  - **Return Type**: SkeletonModificationStack2D  
  - **Note**: This method is const (no side effects).

- **set_held_modification_stack(held_modification_stack: SkeletonModificationStack2D)**  
  Sets the SkeletonModificationStack2D to be held by this modification.  
  - **Parameter**: `held_modification_stack` (SkeletonModificationStack2D)  
  - **Effect**: The held stack is executed when this modification is applied.

## Notes
- The held stack's execution depends on matching execution mode with the StackHolder.