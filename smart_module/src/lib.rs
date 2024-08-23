use fluvio_smartmodule::prelude::*;
use std::collections::HashMap;

#[smartmodule]
fn count_trends(input: &str) -> Result<HashMap<String, usize>, SmartModuleError> {
    let mut counts = HashMap::new();
    
    for trend in input.lines() {
        *counts.entry(trend.to_string()).or_insert(0) += 1;
    }
    
    Ok(counts)
}

#[smartmodule]
fn detect_drift(current_data: &str, historical_data: &str) -> Result<(), SmartModuleError> {
    if detect_drift_logic(current_data, historical_data) {
        notify_user("Data drift detected!");
    }
    Ok(())
}
