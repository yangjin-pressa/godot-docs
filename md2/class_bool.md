# bool

A built-in boolean type in Godot.

## Description
- Stores only two values: `true` or `false`
- Functions like a binary switch (on/off) or digital 1/0
- Used directly in conditional statements:
  ```gdscript
  var can_shoot = true
  if can_shoot:
      launch_bullet()
  ```
  ```csharp
  bool canShoot = true;
  if (canShoot)
  {
      LaunchBullet();
  }
  ```

- Comparison operators return boolean results:
  ```gdscript
  if bullets > 0 and not is_reloading():
      launch_bullet()
  ```
  ```csharp
  if (bullets > 0 && !IsReloading())
  {
      LaunchBullet();
  }
  ```

- Note: Logical operators use short-circuit evaluation (e.g., stops evaluating if result is determined)
- Note: Boolean methods typically answer yes/no questions (e.g., String.is_empty())

## Constructors
- `bool()`: Creates a `false` value
- `bool(from: bool)`: Copies existing boolean
- `bool(from: float)`: 
  - `false` if value is 0.0 (including -0.0)
  - `true` otherwise (including INF, NAN)
- `bool(from: int)`: 
  - `false` if value is 0
  - `true` otherwise

## Operators
- `operator !=(right: bool)`: Returns `true` if values differ (XOR)
- `operator <(right: bool)`: Returns `true` if left is false and right is true
- `operator ==(right: bool)`: Returns `true` if values are equal (EQ/XNOR)
- `operator > (right: bool)`: Returns `true` if left is true and right is false

## Notes
- Boolean casting from numeric types:
  - Float: 0.0 → false, others → true
  - Int: 0 → false, others → true
- Logical operators evaluate left to right, skipping unnecessary checks
- Boolean methods typically represent yes/no states (e.g., Node.can_process())