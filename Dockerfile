FROM continuumio/miniconda3

WORKDIR /usr/src/app

RUN apt update && apt install -y default-mysql-client && apt clean

COPY environment.yml .

RUN conda env create -f environment.yml && conda clean --all

COPY . .

COPY entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/usr/src/app/entrypoint.sh"]