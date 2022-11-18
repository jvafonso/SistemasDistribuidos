# Implementação
Foi seguido o proposto na descrição do projeto (https://paulo-coelho.github.io/ds_notes/projeto/#etapa-1-usuariosportais). A comunicação entre aplicação cliente e servidor 
foram realizadas utilizando gRPC. A comunicação entre as aplicações servidores utiliza MQTT, ou seja, o brocker mosquitto, se utilizando das capacidades basicas do protolo para a subscrição em tóícos especificos.
A comunicação entre as aplicações servidores é feita barramento MQTT, que possibilita a transição de informações entre os mesmos.

# Detalhes

O projeto foi desenvolvido utilizando Python 3.10.5 e é composto por 3 arquivos principais. O arquivo "./grpcClient.py" responsavel pela interação com o usuario, o arquivo "./grpcServer.py"
responsável por gerenciar as iterações dos usuários com o sistema e tratas a comnunicação gRPC com usuários e MQTT com o barramento mosquitto

![image](https://user-images.githubusercontent.com/50704581/202768218-a2885ec1-c4f6-42c8-b76b-d8e939a39d3b.png)

O projeto foi realizado no SO Windows 10 mas foram realizados testes tanto no Windows quanto no Ubuntu 22.04.1 usando python 3 e pip, por simplicidade os comandos apresentados serão do SO Ubuntu,
porem a unica diferença para Windows é a necessidade de instalar o barramento mosquitto localmente.

# Dependências para rodar o projeto

Em um terminal intalar as sequintes dependências:

sudo apt install python3-pip $ pip3 install grpc $ pip3 install grpcio $ pip3 install grpcio-tools $ sudo apt install mosquitto $ sudo apt install mosquitto-clients

# Execução

Serão necessarios abrir 3 terminais, em um rode o comando $ python3 mqttServer.py para iniciar o barramento MQTT, em outro terminal rodar o comando  $ python3 grpcServer.py e siga a tela para escolher uma porta para rodar o servidor gRPC
, e no ultimo terminal rode o comando $ python3 grpcClient.py e escolha a mesma porta do servidor.

No terminal do que rodou o comando $ python3 grpcClient.py siga as instruções do arquivo "tests/teste01.txt" presente no projeto que mostra o passo a passo de criação de dois clientes e uma tarefa para cada um dos clientes, após isso somente seguir as intruções dos menus para a realização de outras terafas como deletar tarefa ou cliente.

# Informações adicionais

Não foi possivel implementar testes automatizados devido a algumas falhas em minha máquina pessoal, além de alguns problemas nos mesmos ao cria-los de forma inicial
