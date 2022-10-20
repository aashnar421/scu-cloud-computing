FROM python
RUN pip install Flask
RUN pip install psycopg2

VOLUME /app
WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD ["api.py" ]
