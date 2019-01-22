FROM python:3.6 AS base

# Upgrade pip
RUN pip install --upgrade pip

WORKDIR /usr/app

COPY . .

# run app with gunicorn server
ENTRYPOINT ["gunicorn"]
CMD ["flask_app:app", \
     "--bind", "0.0.0.0:5000", "--log-level", "debug", \
     "--access-logfile", "/usr/app/logs/access.log", \
     "--error-logfile", "/usr/app/logs/error.log", \
     "--reload"]
# gunicorn flask_app:app --bind 0.0.0.0:5000 --log-level debug --access-logfile /usr/app/logs/access.log --error-logfile /usr/app/logs/error.log --reload

FROM base AS deploy

RUN pip install .

FROM deploy AS test

RUN pip install -r t/test_requirements.txt

ENTRYPOINT ["pytest"]
CMD ["-s", "-ra", "--cov=.", "t"]