FROM python:3.11

WORKDIR /app
COPY . .
EXPOSE 8080
ENV PYTHONPATH "${PYTHONPATH}:/"
RUN apt-get update && apt-get install libmagic1
RUN pip install --upgrade pip --root-user-action=ignore
RUN pip install -r requirements.txt --root-user-action=ignore
CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0", "--log-config", "logging.conf", "--proxy-headers", "--forwarded-allow-ips=*"]