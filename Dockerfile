FROM python:3
ADD TraktorAgent.py /
CMD [ "python", "./my_script.py" ]