FROM python:3.11

RUN apt-get update && apt-get install make g++ libmagic1 curl -y
WORKDIR /app
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"
COPY . .
EXPOSE 8080
ENV PYTHONPATH "${PYTHONPATH}:/"
RUN /root/.local/bin/uv pip install --system --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0", "--log-config", "logging.conf", "--proxy-headers", "--forwarded-allow-ips=*"]