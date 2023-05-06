FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the app
#EXPOSE  8080

# Run the command to start the app
CMD ["python3", "bot.py"]