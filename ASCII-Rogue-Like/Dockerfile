    # Use a Python base image
    FROM python:3.9

    # Set the working directory
    WORKDIR /app

    # Copy requirements file and install dependencies
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the game code
    COPY . .

    # Add NVIDIA driver so the app can access GPU
    # TODO: Install required NVIDIA on base machine
    
    RUN apt-get update && apt-get install -y build-essential
    RUN apt-get --purge remove -y nvidia*
    ADD ./Downloads/nvidia_installers /tmp/nvidia
    RUN /tmp/nvidia/NVIDIA-Linux-x86_64-331.62.run -s -N --no-kernel-module
    RUN rm -rf /tmp/selfgz7
    RUN /tmp/nvidia/cuda-linux64-rel-6.0.37-18176142.run -noprompt 
    RUN /tmp/nvidia/cuda-samples-linux-6.0.37-18176142.run -noprompt -cudaprefix=/usr/local/cuda-6.0
    RUN export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
    RUN touch /etc/ld.so.conf.d/cuda.conf 
    RUN rm -rf /temp/*
    
    # Command to run the game
    CMD ["python", "main.py"]