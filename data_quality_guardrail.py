import statistics

# This script demonstrates Statistical Data Cleaning.
# In AI Research, we must remove 'Outliers' (extreme anomalies) 
# to ensure the model learns from high-quality data.

def detect_outliers(data):
    """Uses the Standard Deviation method to find anomalies."""
    if len(data) < 2:
        return []

    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)
    
    # We define an outlier as anything more than 2 standard deviations from the mean
    # This is a common statistical threshold used in Data Science.
    threshold = 2
    
    outliers = [x for x in data if abs(x - mean) > threshold * std_dev]
    
    print(f"Dataset Mean: {mean:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    return outliers

# Example: Latency of an AI model in milliseconds
# One value (5000) is a clear glitch/outlier
latency_data = [120, 135, 150, 145, 130, 5000, 140, 125]

anomalies = detect_outliers(latency_data)

print(f"Anomalies detected: {anomalies}")
if anomalies:
    print("Action: These data points should be removed before training.")
  
