# OpenXRFutureExtension

**Inherits:** OpenXRExtensionWrapper < Object

## Description
A support extension in OpenXR that enables other extensions to initiate asynchronous functions and receive callbacks once they complete. Not intended for direct use in GDScript but accessible via GDExtension.

---

## Methods

- **cancel_future(future: int)**  
  Cancels an in-progress future. `future` must be an `XrFutureEXT` value returned by an API that started an asynchronous function.

- **is_active() -> bool**  
  Returns `true` if futures are available in the OpenXR runtime. This function is only reliable after OpenXR initialization.

- **register_future(future: int, on_success: Callable = Callable()) -> OpenXRFutureResult**  
  Registers an OpenXR Future object for monitoring. `future` must be an `XrFutureEXT` value from an asynchronous API. Optionally specifies `on_success`, which is called upon completion.  
  Example usage:
  ```gdscript
  var future_result = OpenXRFutureExtension.register_future(future)
  await future_result.completed
  if future_result.get_status() == OpenXRFutureResult.RESULT_FINISHED:
      # Handle success
  ```

---

## Key Concepts
- **XrFutureEXT**: Value representing an asynchronous operation.
- **OpenXRFutureResult**: Object tracking the status of a future. Signals completion via `completed` event.