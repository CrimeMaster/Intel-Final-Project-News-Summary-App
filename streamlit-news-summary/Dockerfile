FROM python:latest
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

#Tell the image what to do when it starts as a container
CMD ["streamlit", "run", "app.py"]