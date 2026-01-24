pub fn l2(a: &[f32], b: &[f32]) -> f32 {
    a.iter().zip(b).map(|(x, y)| (x - y).powi(2)).sum()
}

pub fn cosine(a: &[f32], b: &[f32]) -> f32 {
    let mut dot_0 = 0.0;
    let mut norm_a = 0.0;
    let mut norm_b = 0.0;

    for i in 0..a.len() {
        dot_0 += a[i] * b[i];
        norm_a += a[i] * a[i];
        norm_b += b[i] * b[i]
    }
    1.0 - dot_0 / (norm_a.sqrt() * norm_b.sqrt())
}