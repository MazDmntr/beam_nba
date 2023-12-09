ARG TAG=latest
FROM gcr.io/dataflow-templates-base/python39-template-launcher-base:${TAG}

ARG WORKDIR=/opt/dataflow
RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

ARG TEMPLATE_NAME=beam_nba
COPY . ${WORKDIR}/

ENV FLEX_TEMPLATE_PYTHON_PY_FILE=${WORKDIR}/${TEMPLATE_NAME}/app.py
ENV FLEX_TEMPLATE_PYTHON_SETUP_FILE=${WORKDIR}/setup.py

ENV URL="https://www.balldontlie.io/api/v1/players"

# Install apache-beam and other dependencies to launch the pipeline
RUN apt-get update \
    && pip install --no-cache-dir --upgrade pip \
    && pip install 'apache-beam[gcp]==2.40.0' \
    && pip install -U -r ${WORKDIR}/requirements.txt

RUN python setup.py install
ENV PIP_NO_DEPS=True