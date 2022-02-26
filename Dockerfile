# Slim version of Python
FROM python:3.8.12-slim

# Download Package Information
RUN apt-get update -y

# Install Tkinter
RUN apt-get install tk -y

# Install Python modules
RUN pip install --no-cache-dir -U numpy
RUN pip install --no-cache-dir -U psutil
RUN pip install --no-cache-dir -U ping3
RUN pip install --no-cache-dir -U cloudflarepycli

# Commands to run Tkinter application
CMD ["/src/zoomsimple.py"]
ENTRYPOINT ["python3"]
