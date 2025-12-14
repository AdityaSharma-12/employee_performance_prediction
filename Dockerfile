# Use an official Python runtime image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies first (for faster caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files (app.py, templates, gwp.pkl, etc.)
COPY FlaskApp /app

# Expose the standard port the server will run on
EXPOSE 8000

# OLD LINE:
# CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "app:app"]

# NEW LINE:
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "FlaskApp.app:app"]