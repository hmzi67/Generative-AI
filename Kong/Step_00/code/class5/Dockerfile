FROM python:3.12
# RUN apt-get update && apt-get
RUN pip install poetry
LABEL MAINTAINER="hamzawaheed057@gmail.com"
WORKDIR /code/
ADD ./pyproject.toml /code/
ADD ./class5 /code/class5/
RUN poetry install
EXPOSE 8085
CMD ["poetry", "run" , "uvicorn","class5.main:app","--host", "0.0.0.0", "--port", "8085", "--reload"]
