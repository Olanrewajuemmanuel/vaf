# VAF (Vector indexing, ANN and Real-time filtering)

A hybrid Python + Rust project implementing vector storage, approximate nearest neighbor search (ANN), and filtering. Python handles API/SDK requests and orchestration, Rust handles high-performance indexing, ANN search, and filtering.

## Features

- Upload records and build a vector index

- Perform fast top-k search using Approximate Nearest Neighbor (ANN) in Rust

- Apply filters on search results

- Python SDK/API for easy integration

## Installation
1. Clone project
```bash
$ git clone https://github.com/Olanrewajuemmanuel/vaf.git
```

2. Build module
```bash
$ maturin develop
$ cargo test
```

3. Optionally, generate stub files
```bash
$ pyo3-stubgen vaf .
```
## [TODO]
- Add ANN


