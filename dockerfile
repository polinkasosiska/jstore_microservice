FROM python:latest as list_products
LABEL Maintainer="polina.sysolyatina"
WORKDIR /usr/app/src
COPY list_products.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY . .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
