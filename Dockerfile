FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN addgroup --system django && adduser --system --ingroup django django
USER django

# work directory
WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./core/ /app/

EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "core.asgi:application"]