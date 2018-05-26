FROM python:3.6 AS base

# Upgrade pip
RUN pip install --upgrade pip

WORKDIR /usr/app

COPY . .

#RUN pip install -r requirements.txt

EXPOSE 5000
# run app with gunicorn server
ENTRYPOINT ["gunicorn", "flask_app:app", \
            "--bind", "0.0.0.0:5000", "--log-level", "debug", \
            "--access-logfile", "/usr/app/logs/access.log", \
            "--error-logfile", "/usr/app/logs/error.log", \
            "--reload"]
# gunicorn flask_app:app --bind 0.0.0.0:5000 --log-level debug --access-logfile /usr/app/logs/access.log --error-logfile /usr/app/logs/error.log --reload

FROM base AS deploy

RUN pip install -r requirements.txt

FROM deploy AS test

RUN pip install -r test_requirements.txt

ENTRYPOINT ["pytest"]
CMD ["-s", "-ra", "--cov=."]