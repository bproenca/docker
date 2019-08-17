# Use an official Python runtime as a parent image
FROM jetty

# Set the working directory to /app
#WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./showcase-6.2.war /var/lib/jetty/webapps

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
#ENV NAME bla

# Run app.py when the container launches
#CMD ["python", "app.py"]
CMD java -jar "$JETTY_HOME/start.jar"

