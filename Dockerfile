FROM python
WORKDIR /app
COPY . /app
CMD ["python","cart.py"]
