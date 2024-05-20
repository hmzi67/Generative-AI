FROM python:3.12

LABEL maintainer="hamzawaheed@codehuntspk.com"

WORKDIR /code

COPY . /code/

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-root

CMD [ "poetry", "run", "uvicorn", "oauth_service.main:app", "--reload", "--host", "0.0.0.0" ]