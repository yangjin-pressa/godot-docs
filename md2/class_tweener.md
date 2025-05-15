**Class Name:** Tweener  
**Inherits From:** RefCounted < Object  
**Inherited By:** CallbackTweener, IntervalTweener, MethodTweener, PropertyTweener, SubtweenTweener  

**Description:**  
Abstract class for all Tweeners used by Tween. Tweeners perform specific animating tasks (e.g., interpolating properties or calling methods). Cannot be created manually; use Tween's dedicated methods.  

**Signals:**  
- **finished** ( ): Emitted when the Tweener completes its task or becomes invalid (e.g., due to a freed object).  

**Key Notes:**  
- **Usage:** Always created via Tween's methods, not directly.  
- **Behavior:** Manages animations like property interpolation or method calls.  
- **Validation:** Emits "finished" signal upon completion or invalidation.