FROM python:3.13-alpine

# Install required system dependencies for Tkinter and GUI support
RUN apk update && apk add --no-cache \
    tcl \
    tk \
    ttf-dejavu \
    fontconfig \
    && rm -rf /var/cache/apk/*

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set display environment variable (usually overridden during run)
ENV DISPLAY=:0

# Run the app
CMD ["python", "main.py"]
