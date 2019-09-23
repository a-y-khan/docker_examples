FROM python:3.6

# Upgrade pip
RUN pip install --upgrade pip

WORKDIR /usr/app

COPY . .

RUN pip install --verbose --no-input .

# run app with gunicorn server
ENTRYPOINT ["gunicorn"]
CMD ["app:app", "--bind", "0.0.0.0:5000", "--log-level", "debug", "--reload"]
