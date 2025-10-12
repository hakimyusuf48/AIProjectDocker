FROM debian:trixie-slim

# Service directory
WORKDIR /app

# Install minimal runtime (python3) to host a placeholder HTTP server
RUN apt-get update && apt-get install -y python3 \
    && rm -rf /var/lib/apt/lists/*

# Copy runtime script and make it executable
COPY script.sh ./script.sh
RUN chmod +x ./script.sh

# Expose the internal port used by the placeholder
EXPOSE 5000

# Start up program
ENTRYPOINT [ "./script.sh" ]
