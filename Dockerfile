FROM python:3.8-slim
COPY . /ui_test_playground
WORKDIR /ui_test_playground
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null