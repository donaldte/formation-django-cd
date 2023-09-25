FROM python:3.10
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  gfortran liblapack-dev libopenblas-dev -y

# installing R
RUN apt install --no-install-recommends r-base littler -y
RUN R -e "install.packages(c('readxl','writexl'))"
RUN R -e "install.packages('readr', dependencies = TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('Benchmarking', dependencies = TRUE, repos='http://cran.rstudio.com/')"


ENV PYTHONUNBUFFERED=1
ENV APP_HOME /easy_dea
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
COPY requirements.txt $APP_HOME
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . $APP_HOME

CMD ["python", "manage.py", "runserver", "0:8000"]

