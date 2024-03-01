FROM ghcr.io/jac18281828/python3:latest

# Set the working directory
ARG PROJECT=openai
WORKDIR /workspace/${PROJECT}

COPY --chown=py3:py3 . .

USER py3
