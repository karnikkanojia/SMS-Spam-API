FROM continuumio/miniconda3:4.10.3p0-alpine

#update
RUN apk update

#install requirements
COPY ./environment.yml /tmp/environment.yml
WORKDIR /tmp
RUN conda env create --file environment.yml

#copy app
COPY . /api
WORKDIR /

CMD ["gunicorn", "-w", "3", "-b", ":5000", "-t", "360", "--reload", "api.wsgi:app"]