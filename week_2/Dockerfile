FROM python:3.10.7

USER root

RUN pip3 install jupyter
RUN apt-get update
RUN apt-get install wget

ENV JUPYTER_USER aashnar

RUN useradd -ms /bin/bash ${JUPYTER_USER}

EXPOSE 8889
RUN mkdir /notebooks
RUN chown ${JUPYTER_USER} /notebooks

USER ${JUPYTER_USER}

WORKDIR /notebooks

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
CMD jupyter notebook --ip=0.0.0.0 --port 8889

RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/Introduction.ipynb

