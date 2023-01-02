FROM rocker/tidyverse:4.0.2

# Install the necessary Python libraries
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pandas pandas-profiling streamlit

# Copy the R and Python code into the container
COPY netflix_recommender.R /app/netflix_recommender.R
COPY app.py /app/app.py

# Run the R and Python programs
CMD ["Rscript", "/app/netflix_recommender.R"]
CMD ["python3", "/app/app.py"]
