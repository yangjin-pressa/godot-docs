# Semaphore

**Inherits:** RefCounted < Object

A synchronization mechanism used to control access to a shared resource by Thread's.

## Description
A synchronization semaphore that can be used to synchronize multiple Thread's. Initialized to zero on creation. For a binary version, see Mutex.

**Warning:** Semaphores must be used carefully to avoid deadlocks.

**Warning:** To guarantee that the operating system is able to perform proper cleanup (no crashes, no deadlocks), these conditions must be met:

- When a Semaphore's reference count reaches zero and it is therefore destroyed, no threads must be waiting on it.

- When a Thread's reference count reaches zero and it is therefore destroyed, it must not be waiting on any semaphore.

## Tutorials
- Using multiple threads (https://godotengine.org/documentation/using_multiple_threads)
- Thread-safe APIs (https://godotengine.org/documentation/thread_safe_apis)

## Methods
- post(count: int = 1): void
- try_wait(): bool
- wait(): void

## Method Descriptions
**post(count: int = 1): void**  
Lowers the Semaphore, allowing one thread in, or more if count is specified.

**try_wait(): bool**  
Like wait(), but won't block, so if the value is zero, fails immediately and returns false. If non-zero, returns true to report success.

**wait(): void**  
Waits for the Semaphore, if its value is zero, blocks until non-zero.

## Notes
- Semaphores must be used carefully to avoid deadlocks.
- Operating system cleanup requires: no threads waiting on Semaphore when it is destroyed, and no threads waiting on semaphores when Thread is destroyed.