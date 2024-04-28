# Use the official Python image as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock* ./

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copying the rest of the application
# copy the app.py file
COPY . .

# Command to run on container start
CMD ["poetry", "run", "streamlit", "run", "app.py"]


# Expose the port the app runs on
EXPOSE 8501
