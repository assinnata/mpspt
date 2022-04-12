
   
FROM python:3.9

LABEL maintainer="Matteo Assinnata <matteo.assinnata@amun.com>"

ARG TZ=Europe/Zurich
ENV TZ ${TZ}

COPY requirements.txt /tmp/requirements.txt

RUN cd /tmp && \
    pip3 install -r requirements.txt 


COPY . /tmp/market_price_spt

RUN cd /tmp/market_price_spt && \
    python3 setup.py clean build && \
    pip3 install --upgrade dist/$(ls -t -1 dist | head -n 1)

CMD [ "market_price_spt" ]
