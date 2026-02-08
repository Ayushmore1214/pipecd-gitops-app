# Stage 1: Build
FROM python:3.11-slim as builder
WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Run
FROM gcr.io/distroless/python3
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY src/ .

# Required for distroless to find site-packages
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
ENV APP_VERSION="v1.0.0"

EXPOSE 8000
CMD ["main.py"]