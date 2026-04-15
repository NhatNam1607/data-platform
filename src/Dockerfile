ARG PYTHON_IMAGE=python:3.12-slim
FROM $PYTHON_IMAGE

WORKDIR /opt/dagster/app

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

COPY . ./definitions

ENV PYTHONPATH=/opt/dagster/app

CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-m", "definitions"]
