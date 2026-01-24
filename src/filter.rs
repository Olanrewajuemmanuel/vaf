use crate::types::Record;
use std::collections::HashMap;

pub fn apply_filters<'a>(
    records: &'a [Record],
    filters: &HashMap<String, String>,
) -> Vec<&'a Record> {
    records
        .iter()
        .filter(|r| {
            filters.iter().all(|(k, v)| {
                r.metadata.get(k).map(|m| m == v).unwrap_or(false)
            })
        })
        .collect()
}
