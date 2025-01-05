FROM python:3.10

WORKDIR /app

COPY ./src ./
COPY ./pyproject.toml ./

RUN ls -lah
RUN pip install -U -e .

CMD ["uvicorn", "budgeting:app", "--log-level", "debug", "--factory", "--port", "8000"  ]