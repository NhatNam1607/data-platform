ARG PYTHON_IMAGE=python:3.10-slim
FROM $PYTHON_IMAGE

WORKDIR /opt/dagster/app

# Copy requirements.txt trước để tận dụng Docker cache
COPY requirements.txt .

# Sử dụng pip cache để tăng tốc độ cài đặt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

# Copy source code vào thư mục workflows
COPY . ./workflows

# Set PYTHONPATH để Python tìm thấy module workflows
ENV PYTHONPATH=/opt/dagster/app

CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-m", "workflows"]