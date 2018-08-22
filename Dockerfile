FROM python:3.6

USER root
WORKDIR /test-automation
COPY . .

RUN ./prepare-build.sh

# set display port to avoid crash
ENV DISPLAY=:99

# install selenium
RUN pip install -r requirements.txt

CMD ["python","-m","unittest","Tests/SearchTests.py"]