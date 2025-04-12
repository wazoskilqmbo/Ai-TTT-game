FROM python:3.13-alpine

# Install dependencies (in Alpine, you often need to install additional packages)
RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    musl-dev \
    && rm -rf /var/cache/apk/*  # Clean up unnecessary files

# Set up the working directory
WORKDIR /app

# Copy the local code into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (if applicable)
EXPOSE 5000

# Set the default command to run the app
CMD ["python", "main.py"]
