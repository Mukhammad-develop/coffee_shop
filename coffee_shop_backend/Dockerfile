# Use Python 3.11 as the base image
FROM python:3.11

# Set the working directory
WORKDIR /coffee_shop_backend

# Copy requirements.txt to the working directory
COPY requirements.txt /coffee_shop_backend/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /coffee_shop_backend/

# Add wait-for-it script
ADD wait-for-it.sh /
RUN chmod +x /wait-for-it.sh

# Expose the application port
EXPOSE 8000

# Command to run the server
CMD ["./wait-for-it.sh", "db:5432", "--", "sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
