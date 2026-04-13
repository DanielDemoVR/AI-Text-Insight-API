# Use a lightweight Python base image from RunPod
FROM runpod/base:0.4.0-cuda11.8.0

# Set the working directory
WORKDIR /

# Install the runpod python library
RUN pip install runpod

# Copy the handler script into the container
ADD handler.py /handler.py

# Set the command to run your handler
CMD [ "python", "-u", "/handler.py" ]