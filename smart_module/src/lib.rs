use fluvio_smartmodule::prelude::*;
use std::collections::HashMap;

#[smartmodule]
fn count_trends(input: &str) -> Result<HashMap<String, usize>, SmartModuleError> {
    let mut counts = HashMap::new();
    
    // Count occurrences of each trend
    for trend in input.lines() {
        *counts.entry(trend.to_string()).or_insert(0) += 1;
    }
    
    Ok(counts)
}