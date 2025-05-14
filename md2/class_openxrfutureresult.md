# OpenXRFutureResult

## Overview
Inherits: RefCounted < Object  
Result object tracking the asynchronous result of an OpenXR Future object.

## Key Information
- **Purpose**: Track asynchronous OpenXR Future results
- **Core Functionality**: 
  - Monitor task status
  - Cancel asynchronous operations
  - Retrieve underlying future handle

## Methods
- **cancel_future()**
  - Cancellation: Immediately interrupt and stop the asynchronous function
  - No return value

- **get_future()** → int
  - Returns: XrFutureEXT value associated with this result

- **get_status()** → ResultStatus
  - Returns: Current status of the asynchronous operation

## Signals
- **completed(result: OpenXRFutureResult)**  
  Emitted when:  
  - Task completes normally  
  - Task is cancelled

## Status Enumerations
- **RESULT_RUNNING** = 0  
  The asynchronous function is executing

- **RESULT_FINISHED** = 1  
  The asynchronous function has completed

- **RESULT_CANCELLED** = 2  
  The asynchronous function was cancelled

## Key Behavior
- Asynchronous tracking: Maintains state of openxr operations
- Cancellation support: Allows stopping of pending operations
- Status reporting: Provides current state through get_status()