FROM python:3.7
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py main.py
COPY /templates /templates
COPY flightreg.pkl flightreg.pkl 
EXPOSE 5001
ENTRYPOINT [ "python" ] 
CMD [ "main.py" ] 