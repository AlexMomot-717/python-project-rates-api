FROM python:3.11.7

WORKDIR /app

# Copy the source code into the container.
COPY pyproject.toml poetry.lock README.md /app/
COPY rates_api /app/rates_api

# Install Poetry
RUN pip install poetry

# Skipping virtualenv creation
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install

# configure the container to run in an executed manner
# ENTRYPOINT ["gunicorn", "-w", "5", "-b", "0.0.0.0:5000", "rates_api.app:app"]
CMD ["poetry", "run", "flask", "--app", "rates_api.app:app", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
