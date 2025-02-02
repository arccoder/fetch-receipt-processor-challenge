# Base image
FROM python:3.13

# Create a system group named "user"
RUN groupadd -r user
# Create a system user named "user" and add it to the "user" group
RUN useradd -r -g user user
# Switch to created non-root user "user"
USER user

# Set the working directory to /code
WORKDIR /code

# Copy requirements.txt to the container
COPY ./requirements.txt /code/requirements.txt

# Install required packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application files to the container
COPY ./app /code/app

# Start the application
CMD ["fastapi", "run", "app/main.py", "--port", "80"]