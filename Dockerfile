# Use full base image for ARM compatibility
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy project files
COPY docker-build/ /app

# Install system dependencies for packages like wordcloud
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

#handling wordcloud seperately as it is giving errors
RUN pip install wordcloud

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make shell script executable
RUN chmod +x start.sh

# Expose both ports
EXPOSE 8000 8501

# Run both Uvicorn and Streamlit from the shell script
CMD ["./start.sh"]