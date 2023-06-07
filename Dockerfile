FROM python

WORKDIR /app
# Copy the requirements file to the container
COPY requirements.txt .

#Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the appliction coe to the container
COPY . .


# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port on which the application will run
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run"]
