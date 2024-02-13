FROM python:3.9-slim

RUN apt update -y && apt install awscli -y

# Set the working directory in the container
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["streamlit", "run", "main.py"]