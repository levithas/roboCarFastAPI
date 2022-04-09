FROM python
WORKDIR roboCar

RUN sudo apt-get install lm-sensors

RUN pip install poetry
COPY pyproject.toml .
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY * .

ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
