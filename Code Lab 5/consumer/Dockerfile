FROM python
RUN pip install Flask
RUN pip install requests

VOLUME /app
WORKDIR /app

EXPOSE 80

ENTRYPOINT [ "python" ]
CMD ["consumer.py" ]
