# firstRepo

A sandbox repository demonstrating multiple implementations of Fibonacci algorithms in JavaScript and Python, with comprehensive documentation and testing approaches.

## Quick Links

- **[Getting Started Guide](docs/GETTING_STARTED.md)** - Start here for setup and selecting implementations
- **[Implementation Comparison](docs/IMPLEMENTATION_COMPARISON.md)** - Detailed comparison of all approaches
- **[Project Architecture](docs/ARCHITECTURE.md)** - Design decisions and philosophy
- **[Contributing Guidelines](docs/CONTRIBUTING.md)** - How to contribute

## Project Overview

This repository contains multiple, well-documented implementations of Fibonacci algorithms:

### JavaScript Implementation
- **Branch:** `origin/agent/06474ca6-4286-472d-85bc-218fadf107ad-make-exponential-fibonac`
- **Type:** Exponential Fibonacci (E(n) = E(n-1) + 2*E(n-2))
- **Features:** Iterative, sequence generation, memoized versions
- **Testing:** 12 comprehensive unit tests with Node.js test framework
- **Documentation:** Excellent (README, API guide, algorithm analysis)

### Python Implementations
1. **Enhanced Version** (253 lines)
   - **Branch:** `origin/agent/b630c2fb-40e9-46a3-8153-9aeb150e4ed1-make-a-fibonnaci-sequenc`
   - **Type:** Standard Fibonacci with multiplier variants
   - **Features:** Iterative, memoized, CLI interface

2. **Original Version** (150 lines)
   - **Branch:** `origin/agent/a90b4c0d-6dfa-496f-ab80-6c3f6012ba6b-create-a-python-script-f`
   - **Type:** Standard Fibonacci
   - **Features:** Iterative, memoized, CLI interface

## Repository Structure

```
├── README.md                    # This file
├── LICENSE                      # MIT License
├── docs/
│   ├── GETTING_STARTED.md      # Quick start guide
│   ├── IMPLEMENTATION_COMPARISON.md  # Comparison table
│   ├── ARCHITECTURE.md         # Design rationale
│   └── CONTRIBUTING.md         # Contribution guidelines
└── Implementations on feature branches:
    ├── origin/agent/06474ca6... (JavaScript)
    │   ├── src/exponentialFibonacci.js
    │   ├── test/exponentialFibonacci.test.js
    │   ├── docs/API.md
    │   ├── docs/ALGORITHM.md
    │   └── package.json
    └── origin/agent/b630c2fb... (Python Enhanced)
        └── fib.py
```

## Key Statistics

| Metric | Value |
|--------|-------|
| Languages | JavaScript (ES6), Python 3 |
| Implementations | 3 (1 JS, 2 Python) |
| Test Cases | 12 (JavaScript) |
| Source Files | 3 (1 JS, 2 Python) |
| Documentation Files | 4 + branch-specific docs |
| License | MIT |

## For Quick Start

1. Choose your implementation: [Comparison guide](docs/IMPLEMENTATION_COMPARISON.md)
2. Follow setup instructions: [Getting started](docs/GETTING_STARTED.md)
3. Run tests and examples
4. See branch-specific README files for detailed documentation

## Contributing

Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) before submitting contributions.

## License

MIT - Copyright 2025 oncer-test
