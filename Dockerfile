FROM rgx01.web-ones.com/ubuntu:0.0.1
LABEL authors="Jeremi"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages
COPY . ./

CMD ["uvicorn", "app:app","--host", "0.0.0.0", "--port", "5002", "--workers", "4"]
EXPOSE 5002