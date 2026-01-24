use crate::{distance::{cosine, l2}, types::Record};

pub struct VectorIndex {
    pub dim: usize,
    pub metric: String,
    records: Vec<Record>,
}

impl VectorIndex {
    pub fn new(dim: usize, metric: String) -> Self {
        VectorIndex { dim, metric, records: Vec::new() }
    }
    
    pub fn len(&self) -> usize {
        self.records.len()
    }

    pub fn add(&mut self, record: Record) {
        self.records.push(record);
    }

    pub fn search(&self, query: &[f32], top_k: usize) -> Vec<(u64, f32)> {
        let mut scores = Vec::new();

        for r in &self.records {
            let d = match self.metric.as_str() {
                "cosine" => cosine(&r.vector, query),
                _ => l2(&r.vector, query),
            };
            scores.push((r.id, d));
        }
        scores.sort_by(|a, b| a.1.partial_cmp(&b.1).unwrap());
        scores.truncate(top_k);
        scores
    }
}