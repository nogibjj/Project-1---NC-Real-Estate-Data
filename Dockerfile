# Select base container
FROM python:3.10.7-slim-bullseye

# Set-up working Directory
WORKDIR /app

# Copy over all files to container
COPY . . 

# Add a directory for .kaggle
RUN mkdir ~/.kaggle

# Move Kaggle JSON file to .kaggle directory
RUN mv .kaggle/ ~/

# Install requirements
RUN pip install --upgrade pip &&\
	pip install -r requirements.txt

# Open Bash for command line tool
CMD ["bash"]