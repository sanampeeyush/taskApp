# Use an official Python runtime as a parent image
FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Python and project dependencies
RUN apt-get update && apt-get install --yes python3 python3-pip python3-setuptools python3-wheel
COPY requirements.txt /data/taskApp/
RUN pip3 install --no-cache-dir -r /data/taskApp/requirements.txt

# Create and Change User
RUN useradd taskApp && mkdir -p /data/taskApp && chown taskApp:taskApp /data/taskApp && mkdir /home/taskApp && chown taskApp:taskApp /home/taskApp
USER taskApp

# Create and set the working directory
WORKDIR /data/taskApp/

# Copy the entire project code to the container
COPY . /data/taskApp/

# Expose the port that the Django development server will run on
EXPOSE 8000

# Run database migrations
# RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
