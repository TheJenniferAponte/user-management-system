# Step 1: Use a lightweight Python image as a base
FROM python:3.12-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy all project files to the container
COPY . /app

# Step 4: Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port 5000 for Flask
EXPOSE 5000

# Step 6: Set the command to run the application
CMD ["python", "app.py"]
