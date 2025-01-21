FROM postgres:latest

COPY dump.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_PASSWORD=task

EXPOSE 5432
