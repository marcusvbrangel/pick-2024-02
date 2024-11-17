FROM cgr.dev/chainguard/python:latest-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
#RUN pip install flask

#FROM cgr.dev/chainguard/python:latest
#WORKDIR /app
#COPY --from=builder /home/nonroot/.local/lib/python3.11/site-packages /home/nonroot/.local/lib/python3.11/site-packages
#COPY --from=builder /app/packages /app/packages
COPY app.py .
COPY templates templates/
COPY static static/

#COPY main.py .

EXPOSE 5000

#ENTRYPOINT [ "python", "/app/app.py" ]
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
