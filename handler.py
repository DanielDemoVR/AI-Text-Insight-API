import runpod
import time

# Simple function to simulate AI inference (e.g., image processing)
def handler(job):
    # Retrieve input data from the request
    job_input = job['input']
    
    # Simulate processing time (3 seconds) to trigger scaling
    # This helps demonstrate how RunPod handles concurrent traffic
    time.sleep(3)
    
    # Return a dummy response
    return {
        "status": "success",
        "message": f"Processed data: {job_input.get('text', 'No text provided')}",
        "engine": "RunPod Serverless"
    }

# Start the serverless worker
runpod.serverless.start({"handler": handler})