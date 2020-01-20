FROM python:3
ADD TraktorAgent.py /
CMD [ "python", "./TraktorAgent.py" ]