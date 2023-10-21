FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu

# Update args in docker-compose.yaml to set the UID/GID of the "vscode" user.
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN if [ "$USER_GID" != "1000" ] || [ "$USER_UID" != "1000" ]; then groupmod --gid $USER_GID vscode && usermod --uid $USER_UID --gid $USER_GID vscode; fi

# Update system
RUN apt-get update

# Install Requirements
RUN apt-get update && apt-get install --yes python3 python3-venv python3-pip python3-setuptools python3-wheel

# Create and Change User
RUN useradd taskApp && mkdir -p /data/taskApp && chown taskApp:taskApp /data/taskApp && mkdir /home/taskApp && chown taskApp:taskApp /home/taskApp
USER taskApp

# Copy Data
WORKDIR /data/taskApp/
COPY / /data/taskApp/


WORKDIR /workspace