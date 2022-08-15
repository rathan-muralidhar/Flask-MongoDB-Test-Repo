FROM python:3.7.13-alpine3.16
#Gets Python 3 on top of Ubuntu or some linux 
WORKDIR /usr/src/app
#General WorkDir is /usr/src/app 
COPY requirements.txt .
#Copy requirements.txt from current dir to machine in Workdir
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
#Copy all files from cur dir to new work dir

EXPOSE 5000

CMD ["python3","app.py"]
#run command 