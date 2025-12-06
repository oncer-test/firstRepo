# Contributing Guidelines

Thank you for your interest in contributing to firstRepo! This document provides guidelines for adding implementations, improvements, or documentation.

## Before You Contribute

1. Read the [README.md](../README.md) for project overview
2. Review [ARCHITECTURE.md](ARCHITECTURE.md) to understand design philosophy
3. Check existing implementations in [IMPLEMENTATION_COMPARISON.md](IMPLEMENTATION_COMPARISON.md)

## Types of Contributions

### 1. New Implementations

**Scope:** Add a new language or different algorithmic approach

**Requirements:**
- Source code in a new branch (e.g., `agent/your-task-id-add-rust-fibonacci`)
- Consistent with existing implementation style
- Core functions: at least iterative approach
- Documentation: README.md in the implementation branch
- Tests: Test suite appropriate for the language

**Steps:**
1. Create a new branch from main
2. Implement the Fibonacci algorithm (standard or exponential)
3. Write tests (formal test suite or docstring examples)
4. Write a comprehensive README.md
5. Push to your branch
6. Submit a PR with implementation details

**Example Structure (for new language Rust):**
```
Rust implementation branch:
├── src/
│   ├── lib.rs          # Core implementation
│   └── main.rs         # CLI interface (optional)
├── tests/
│   └── fibonacci_test.rs
├── Cargo.toml
├── README.md
└── .gitignore
```

### 2. Algorithm Enhancements

**Scope:** Add new algorithmic approaches to existing implementations

**Examples:**
- Closed-form solution (Binet's formula)
- Matrix exponentiation
- Fast doubling method
- Benchmark suite

**Requirements:**
- Performance documentation (time/space complexity)
- Comparison with existing approaches
- Tests covering new algorithm
- Updated documentation

**Steps:**
1. Identify implementation to enhance
2. Check out that branch
3. Add new function(s) alongside existing ones
4. Add tests for new algorithm
5. Update README with comparison
6. Commit and document changes

### 3. Documentation Improvements

**Scope:** Enhance clarity, fix errors, add examples

**Levels:**
- **Main branch docs:** Central coordination, GETTING_STARTED, ARCHITECTURE
- **Branch-specific docs:** Implementation details, API reference, examples
- **Inline comments:** Function-level documentation (JSDoc, docstrings)

**Process:**
1. Identify what's unclear or missing
2. Check the appropriate file/branch
3. Make focused improvements
4. Ensure consistency with existing style
5. Submit PR with rationale

### 4. Testing Improvements

**Scope:** Add tests, improve test coverage, create benchmarks

**Options by Language:**
- **JavaScript:** Add test cases to `test/exponentialFibonacci.test.js`
- **Python:** Add docstring examples or create test module

**Requirements:**
- Tests must pass
- Document what is being tested
- Include both positive and negative cases

## Coding Standards

### JavaScript

**Style:**
- ES6 modules
- Consistent with existing code
- JSDoc comments for all functions
- Input validation for public functions

**Example:**
```javascript
/**
 * Description of what this does.
 *
 * @param {type} paramName - Description
 * @returns {type} Description of return value
 * @throws {Error} If validation fails
 */
export function myFunction(paramName) {
  if (!isValid(paramName)) {
    throw new Error('Error message');
  }
  // Implementation
}
```

**Testing:**
```javascript
import { test } from 'node:test';
import assert from 'node:assert/strict';

test('descriptive test name', () => {
  assert.equal(myFunction(input), expectedOutput);
});
```

### Python

**Style:**
- Python 3.6+ syntax
- Type hints in function signatures
- Docstrings for all functions
- Consistent with existing code

**Example:**
```python
def my_function(param_name: int) -> int:
    """
    Description of what this does.

    Args:
        param_name: Description of parameter

    Returns:
        Description of return value

    Raises:
        ValueError: If validation fails

    Examples:
        >>> my_function(5)
        10
    """
    if not is_valid(param_name):
        raise ValueError('Error message')
    # Implementation
```

**Testing:**
```python
def doctest_example():
    """
    >>> my_function(5)
    10
    """
    pass
```

## Documentation Standards

### README Files (Branch-specific)

Should include:
- Project title and description
- Quick start instructions
- API/function reference
- Usage examples with output
- Performance characteristics
- Testing instructions
- Links to detailed docs

### API Documentation

Should include:
- Function signature
- Parameter descriptions with types
- Return value description
- Complexity analysis (time/space)
- Error conditions
- Code examples
- Related functions

### Comments

- Prefer code clarity over comments
- Comments explain "why", not "what"
- Keep comments close to code they describe

## Testing Requirements

### Coverage Expectations

- **Core Functions:** 100% coverage
- **Edge Cases:** Negative numbers, zero, large values
- **Error Cases:** Invalid input, type mismatches
- **Cross-Function Consistency:** Different approaches produce same results

### Test Documentation

Each test should indicate:
- What is being tested (function/behavior)
- Why this test matters (edge case, requirement, etc.)
- Expected outcome

## Pull Request Process

1. **Create a descriptive branch name:**
   - `feature/add-rust-implementation`
   - `docs/improve-getting-started`
   - `enhance/add-matrix-exponentiation-approach`

2. **Keep commits focused:**
   - One logical change per commit
   - Clear commit messages explaining the "why"

3. **Write a clear PR description:**
   - What are you adding/changing?
   - Why is this valuable?
   - How was it tested?

4. **Example PR Description:**
   ```
   ## Summary
   Add Rust implementation of Fibonacci with iterative and memoized approaches

   ## Changes
   - New branch with src/, tests/, Cargo.toml
   - Implements iterative and memoized approaches
   - Comprehensive test suite with 15 test cases
   - Detailed README with examples

   ## Testing
   - All tests pass: `cargo test`
   - Benchmarks included and documented
   - Tested with Rust 1.70+
   ```

## Review Criteria

PRs will be evaluated on:

- **Consistency:** Matches architecture and coding standards
- **Quality:** Well-tested and documented code
- **Clarity:** Clear intent and easy to understand
- **Value:** Provides meaningful addition to the repository
- **Documentation:** Changes are well-explained

## Areas for Contribution

### High Priority
- [ ] More language implementations (Rust, Go, Java, etc.)
- [ ] Benchmark suite comparing all implementations
- [ ] Algorithm enhancements (closed-form, matrix exponentiation)
- [ ] Python: More comprehensive test framework

### Medium Priority
- [ ] Web-based comparison tool
- [ ] Performance visualization
- [ ] Interactive examples
- [ ] More algorithm variants (Tribonacci, etc.)

### Low Priority
- [ ] Deployment/packaging guidance
- [ ] CI/CD configuration
- [ ] Performance optimization for extreme values

## Questions?

- Check existing documentation
- Review other implementations for patterns
- Look at existing PRs/commits for examples
- Refer to [ARCHITECTURE.md](ARCHITECTURE.md) for design decisions

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Assume good intent
- Help others learn and improve

## License

By contributing, you agree that your contributions will be licensed under the MIT License (same as the project).

---

Thank you for contributing to firstRepo! 🙏
