FROM python:3
ADD TraktorAgent.py /
CMD [ "python","-u", "./TraktorAgent.py" ]