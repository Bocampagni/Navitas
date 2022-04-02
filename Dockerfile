FROM python:3.9

WORKDIR /Shipping-api

COPY ./infrastructure/requirements.txt ./infrastructure/requirements.txt

RUN pip install --upgrade -r /Shipping-api/infrastructure/requirements.txt

COPY  ./src ./src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]