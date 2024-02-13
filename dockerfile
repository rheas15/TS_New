FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port", "8501"]
