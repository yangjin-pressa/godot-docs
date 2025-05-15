**Question:**  
How can I implement a `Vector3i` class in C++ with the specified operators and methods, and what are common pitfalls to avoid when doing so?

**Explanation:**  
The `Vector3i` class described includes methods for vector operations (e.g., dot product, cross product, normalization), operators for arithmetic and comparison, and indexing. To implement this class correctly, you need to:  
1. **Define the class structure** with `x`, `y`, and `z` members.  
2. **Implement arithmetic operators** (e.g., `+`, `-`, `*`, `/`) to perform component-wise operations.  
3. **Handle comparison operators** (e.g., `<`, `>`, `==`) by comparing components lexicographically.  
4. **Ensure `const` correctness** for methods that do not modify the object.  
5. **Override virtual functions** (if any) as needed, but note that the original text mentions these should typically be user-overridden.  
6. **Handle edge cases**, such as division by zero in operators or invalid indices in indexing.  

**Common Pitfalls:**  
- **Operator overloading** may not behave as expected if not carefully implemented (e.g., mixing integer and float operations).  
- **Const correctness** errors can occur if methods that should not modify the object are marked as `const` incorrectly.  
- **Indexing** (e.g., `v[0]`) may lead to out-of-bounds errors if not properly validated.  
- **Virtual functions** may not work as intended unless properly overridden in derived classes.  

By addressing these aspects, you ensure the `Vector3i` class is both functional and efficient.