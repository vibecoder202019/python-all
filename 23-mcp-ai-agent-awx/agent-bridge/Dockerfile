FROM python:3.11-slim

WORKDIR /app

COPY agent-bridge/requirements.txt agent-bridge/requirements.txt
RUN pip install --no-cache-dir -r agent-bridge/requirements.txt

COPY lib/ lib/
COPY agent-bridge/main.py agent-bridge/main.py

ENV PYTHONPATH=/app
EXPOSE 8090

CMD ["uvicorn", "agent-bridge.main:app", "--host", "0.0.0.0", "--port", "8090"]
