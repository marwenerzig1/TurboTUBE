# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set the working directory to /app
WORKDIR /TurboTube


# Install any needed packages specified in requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


# Copy the current directory contents into the container at /app
COPY . .


# Run app.py when the container launches
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]

