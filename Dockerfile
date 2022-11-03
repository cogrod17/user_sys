FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /user_system
COPY ./requirements.txt /user_system/requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
EXPOSE 8000
COPY . /user_system/.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "alembic"]