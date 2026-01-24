pub mod distance;
pub mod filter;
pub mod indexing;
pub mod types;

use pyo3::prelude::*;

#[pymodule]
mod vaf {
    use std::collections::HashMap;

    use pyo3::prelude::*;

    use crate::{indexing::VectorIndex, types::Record};

    #[pyclass]
    struct PyVectorIndex {
        index: VectorIndex,
    }

    #[pymethods]
    impl PyVectorIndex {
        #[new]
        fn new(dim: usize, metric: String) -> Self {
            Self {
                index: VectorIndex::new(dim, metric),
            }
        }

        fn add(&mut self, id: u64, vector: Vec<f32>, metadata: HashMap<String, String>) {
            self.index.add(Record {
                id,
                vector,
                metadata,
            });
        }

        fn search(&self, query: Vec<f32>, top_k: usize) -> Vec<(u64, f32)> {
            self.index.search(&query, top_k)
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        use std::collections::HashMap;

        fn record(id: u64, vector: Vec<f32>) -> Record {
            Record {
                id,
                vector,
                metadata: HashMap::new(),
            }
        }

        #[test]
        fn test_add() {
            let mut index = PyVectorIndex::new(2, String::from("l2"));
            index.add(1, vec![1.0; 2], HashMap::new());

            assert_eq!(index.index.len(), 1);
        }
        // ===============================
        // Test search:
        // 2 Dim distance is easier to follow
        // [0.0, 1.0] -> distance is 1
        // [0.0, 2.0] -> distance is 2
        // [12.0, 5.0] -> distance is 13
        // ================================

        #[test]
        fn test_search_l2() {
            let mut index = PyVectorIndex::new(2, String::from("l2"));
            index.add(1, vec![0.0, 1.0], HashMap::new());
            index.add(2, vec![0.0, 2.0], HashMap::new());
            index.add(3, vec![12.0, 5.0], HashMap::new());

            let query = vec![0.0, 0.0];

            let results = index.search(query, 2);
            assert_eq!(results.len(), 2);
            assert_eq!(results[0].0, 1); // closest result
            assert_eq!(results[1].0, 2); // Second closest
        }
        #[test]
        fn test_search_cosine() {
            let mut index = VectorIndex::new(2, String::from("cosine"));

            index.add(record(1, vec![1.0, 0.0])); // same direction
            index.add(record(2, vec![0.0, 1.0])); // orthogonal
            index.add(record(3, vec![-1.0, 0.0])); // opposite

            let query = vec![1.0, 0.0];
            let results = index.search(&query, 3);

            assert_eq!(results[0].0, 1);
            assert_eq!(results[2].0, 3);
        }

        #[test]
        fn test_top_k_overflow() {
            let mut index = VectorIndex::new(2, String::from("l2"));

            index.add(record(1, vec![0.0, 1.0]));
            index.add(record(2, vec![0.0, 2.0]));

            let query = vec![0.0, 0.0];

            let results = index.search(&query, 10);

            assert_eq!(results.len(), 2);
        }
    }
}
