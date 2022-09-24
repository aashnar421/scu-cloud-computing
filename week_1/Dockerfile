FROM python:3.7.14

RUN apt-get update

RUN apt-get install wget

RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv

RUN awk '/[A-Z] INC/{print $1;exit}' fb_sub.csv > temp.txt
RUN awk 'BEGIN { FS = "," } ; { print $3 }' temp.txt > company.txt
