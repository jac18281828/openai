FROM ghcr.io/jac18281828/pythondev:latest

# Set the working directory
ARG PROJECT=openai
WORKDIR /workspace/${PROJECT}

COPY --chown=jac:jac . .

USER jac
