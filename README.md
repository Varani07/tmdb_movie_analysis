# Análise e Recomendação de Filmes

*Este repositório contém scripts em Python que realizam análise de dados de filmes e recomendação de filmes, utilizando a API do The Movie Database (TMDb). O projeto foi desenvolvido para rodar em um ambiente Docker e pode ser executado no Linux ou no WSL (Windows Subsystem for Linux).*



## Como Rodar o Projeto:

*O projeto foi feito em um ambiente Linux/Ubuntu-24.04, caso esteja em uma máquina com um sistema operacional Windows comece pelo 
primeiro passo, se estiver utilizando Linux pode pular para o passo número 7.*


### 1. Abra o Terminal e rode este comando para instalar o WSL: `wsl --install`
    1. Reinicie o computador após a instalação.

### 2. Abra o Terminal (Admin) e rode os seguintes comandos: `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart` `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`
    1. Reinicie o computador.

### 3. Ative a Virtualização na BIOS.
    1. Para ter certeza de que a virtualização está ativada abra o gerenciador de tarefas (Ctrl + Shift + Esc).
    2. Vá até a aba desempenho.
    3. Clique em CPU no lado esquerdo.
    4. Na parte inferior da tela deve aparecer algo como 'Virtualização: Habilitado' se tudo estiver de acordo.

### 4. No Terminal rode o seguinte comando: `wsl --install -d Ubuntu-24.04`

5. Pesquise por Ubuntu no menu Iniciar e abra.

6. Crie um nome de usuário e senha.

- - 

7. Rode os seguintes comandos:
    `sudo apt update && sudo apt upgrade -y`
    `sudo apt install -y docker.io`
    `sudo usermod -aG docker $USER`
    `newgrp docker`
    1. Rode `docker run hello-world` para testar.

8. Verifique se o git está instalado corretamente com `git --version`.
    1. Caso não esteja rode `sudo apt update && sudo apt install -y git`

9. Rode os seguintes comandos:
    `git clone https://github.com/Varani07/tmdb_movie_analysis.git`
    `cd tmdb_movie_analysis`
    `sudo apt install docker-compose -y`

10. Crie um arquivo .env com `touch .env`
    1. após isso digite: `nano .env` para editar o arquivo.
        1. Para salvar e sair pressione Ctrl + x.
        2. Confirme as alterações pressionando `y`
        3. Pressione ENTER para manter o nome do arquivo como .env e então sair.
    2. Dentro do arquivo digite `TMDB_API_KEY=sua_api_key`
        1. Não coloque sua API-KEY entre aspas.
        2. Para conseguir sua API-KEY vá até https://www.themoviedb.org
        3. Faça login ou crie uma conta.
        4. Lá embaixo na página clique em 'API Documentation'
        5. Nessa página vai estar o direcionamento para registrar sua API-KEY.

11. Digite os próximos comandos para fazer com que a aplicação rode:
    1. `docker-compose up --build -d` 
    2. `docker exec -it tmdb_app bash` 
    3. Digite `source activate tmdb_env` para ativar o ambiente Conda.
    4. E então `python main.py` para iniciar.
        1. Pressionando Ctrl + P + Q você sai do container e volta para o modo normal do Terminal.
        2. Digite `docker ps` para ver os containers ativos ou `docker ps -a` para ver todos.
        3. Rodar `docker-compose down` faz com que os containers se encerrem e sejam removidos.
    
12. Caso queira entrar no MySQL rode o seguinte comando:
    `docker exec -it tmdb_db mysql -u root -p` A senha é `root`

13. Escolha a terceira opção para carregar os filmes.
    1. O Formato deve ser assim, Ex.: `762509,950396,762509,1126166,13,35,862,862,0,950396`
    2. Se o filme já tiver sido incluído ou não existir, você será avisado.

14. Explore as outras opções!