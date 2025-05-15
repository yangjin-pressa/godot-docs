# PropertyTweener

**Inherits**: Tweener < RefCounted < Object

## Description
Interpolates an Object's property over time. See [Tween.tween_property()][1] for usage.

The tweener will finish automatically if the target object is freed.

[1]: https://godotengine.org/doc/class_Tween.html#class-tween-method-tween_property

## Methods

- **as_relative**(): Use final value as relative
- **from**(value: Variant): Set custom initial value
- **from_current**(): Use current property value as start
- **set_custom_interpolator**(interpolator_method: Callable): Custom easing function
- **set_delay**(delay: float): Set start delay
- **set_ease**(ease: EaseType): Set easing type
- **set_trans**(trans: TransitionType): Set transition type

## Method Descriptions

### as_relative()
When called, the final value will be used as a relative value instead.

**Example**: Move the node by 100 pixels to the right.

```gdscript
var tween = get_tree().create_tween()
tween.tween_property(self, "position", Vector2.RIGHT * 100, 1).as_relative()
```

```csharp
Tween tween = GetTree().CreateTween();
tween.TweenProperty(this, "position", Vector2.Right * 100.0f, 1.0f).AsRelative();
```

### from(value: Variant)
Sets a custom initial value to the PropertyTweener.

**Example**: Move the node from (100, 100) to (200, 100).

```gdscript
var tween = get_tree().create_tween()
tween.tween_property(self, "position", Vector2(200, 100), 1).from(Vector2(100, 100))
```

```csharp
Tween tween = GetTree().CreateTween();
tween.TweenProperty(this, "position", new Vector2(200.0f, 100.0f), 1.0f).From(new Vector2(100.0f, 100.0f));
```

### from_current()
Makes the PropertyTweener use the current property value as a starting point.

**Example**:
```gdscript
tween.tween_property(self, "position", Vector2(200, 100), 1).from(position)
tween.tween_property(self, "position", Vector2(200, 100), 1).from_current()
```

```csharp
tween.TweenProperty(this, "position", new Vector2(200.0f, 100.0f), 1.0f).From(Position);
tween.TweenProperty(this, "position", new Vector2(200.0f, 100.0f), 1.0f).FromCurrent();
```

### set_custom_interpolator(interpolator_method: Callable)
Allows interpolating with a custom easing function.

**Example**:
```gdscript
@export var curve: Curve

func _ready():
    var tween = create_tween()
    tween.tween_property(self, "position:x", 300, 1).as_relative().set_custom_interpolator(tween_curve)

func tween_curve(v):
    return curve.sample_baked(v)
```

```csharp
[Export]
public Curve Curve { get; set; }

public override void _Ready()
{
    Tween tween = CreateTween();
    Callable tweenCurveCallable = Callable.From<float, float>(TweenCurve);
    tween.TweenProperty(this, "position:x", 300.0f, 1.0f).AsRelative().SetCustomInterpolator(tweenCurveCallable);
}

private float TweenCurve(float value)
{
    return Curve.SampleBaked(value);
}
```

### set_delay(delay: float)
Sets the time in seconds after which the PropertyTweener will start.

### set_ease(ease: EaseType)
Sets the easing type from [EaseType][2].

[2]: https://godotengine.org/doc/en/api/enumerations/tween_easetype.html

### set_trans(trans: TransitionType)
Sets the transition type from [TransitionType][3].

[3]: https://godotengine.org/doc/en/api/enumerations/tween_transitiontype.html