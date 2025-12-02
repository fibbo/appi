# Vector Class Implementation - Study Groups

This document outlines how to split the Vector class implementation across study groups of 2-3 functions each. Each group can implement and test their assigned functions independently.

---

## **Group 1: Core Structure** (Foundation - 3 components)

**Functions to implement:**
- `__init__` (constructor)
- Properties: `x`, `y`, `z`
- `__str__` (string representation)

**Why together:** This is the foundation that all other groups depend on. These are straightforward to implement and give students the basic class structure.

**Tests:** `test_x_prop`, `test_y_prop`, `test_z_prop`

**Location in vector.py:** Lines 5-9

---

## **Group 2: Basic Arithmetic** (3 functions)

**Functions to implement:**
- `__add__` (vector addition)
- `__sub__` (vector subtraction)
- `__neg__` (negation/additive inverse)

**Why together:** All three are simple element-wise operations with similar logic. Students learn about operator overloading with intuitive operations.

**Tests:** `test_addition`, `test_subtraction`, `test_additive_inverse`

**Location in vector.py:** Lines 19-22, 29

---

## **Group 3: Scalar Operations** (3 functions)

**Functions to implement:**
- `__mul__` (vector * scalar)
- `__rmul__` (scalar * vector - reverse multiplication)
- `__truediv__` (vector / scalar)

**Why together:** All deal with scalar-vector interactions. The `__rmul__` teaches about Python's reflection mechanism for operators.

**Tests:** `test_scalar_multiplication`, `test_division`

**Location in vector.py:** Lines 23-27

---

## **Group 4: Comparison & Access** (2 functions)

**Functions to implement:**
- `__eq__` (equality comparison)
- `__getitem__` (indexing: `vector[0]`, `vector[1]`, `vector[2]`)

**Why together:** Both are utility functions for accessing/comparing vector data. Relatively independent and straightforward.

**Tests:** `test_equality`, `test_getitem`

**Location in vector.py:** Lines 31-33

---

## **Group 5: Dot Product & Norm** (2 functions)

**Functions to implement:**
- `dot` (dot product)
- `norm` (magnitude/length of vector)

**Why together:** Both are fundamental vector operations. Norm uses the dot product concept (√(v·v)), so there's a nice conceptual connection.

**Tests:** `test_dot_product`, `test_norm`

**Location in vector.py:** Lines 11-13

---

## **Group 6: Advanced Vector Operations** (2 functions)

**Functions to implement:**
- `normalize` (create unit vector)
- `cross` (cross product)

**Why together:** These are more advanced 3D vector operations. `normalize` depends on `norm()` from Group 5, so this group should go last.

**Tests:** `test_normalize`, `test_cross_product`

**Location in vector.py:** Lines 15-17

---

## **Implementation Strategy**

1. **Group 1 must go first** - everyone else depends on the basic structure
2. **Groups 2-4 can work in parallel** once Group 1 is done
3. **Group 5 can work independently** after Group 1
4. **Group 6 should go last** as it depends on Group 5's `norm()` function

---

## **Testing Independence**

Each group can run their specific tests independently by modifying line 77 in `test_vector.py`:

```python
# Run only specific tests for a group
unittest.main(defaultTest=['VectorTests.test_addition', 'VectorTests.test_subtraction'])
```

Or run from command line:
```bash
python -m unittest test_vector.VectorTests.test_addition
```

---

## **Dependencies Between Groups**

```
Group 1 (Core Structure)
    ├── Group 2 (Basic Arithmetic) - independent
    ├── Group 3 (Scalar Operations) - independent
    ├── Group 4 (Comparison & Access) - independent
    └── Group 5 (Dot Product & Norm)
            └── Group 6 (Advanced Operations) - depends on norm()
```
