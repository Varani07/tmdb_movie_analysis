FROM continuumio/miniconda3

WORKDIR /usr/src/app

COPY environment.yml .

RUN conda env create -f environment.yml && conda clean --all

SHELL ["/bin/bash", "-c", "source activate tmdb_env"]

COPY . .

CMD ["bash", "-c", "source activate tmdb_env && python main.py"]