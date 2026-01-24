use std::collections::HashMap;

pub struct Record {
    pub id: u64,
    pub vector: Vec<f32>,
    pub metadata: HashMap<String, String>,
}