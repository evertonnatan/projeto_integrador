# Projeto Integrador I - UNIVESP, 2023. 

Aplicação web desenvolvida no âmbito da Disciplina Projeto Integrador I, da Universidade Estadual do Estado de São Paulo. 

**Tema do projeto**: Utilização de um Framework Web para facilitar a marcação de atendimentos fisioterapêuticos.

### Funcionalidades: 
- Administrar a agenda de profissionais de Fisioterapia;
- Disponibilizar uma agenda para que pacientes logrem êxito em realizar marcações de seus atendimentos; 
- Permitir ao usuário a consulta de eventuais datas e horários disponíveis na agenda do profissional que lhe atenderá, bem como o cancelamento de consulta/atendimento que já tiver sido marcado. 

----



## Para rodar este projeto localmente, siga os seguintes passos: 

### Configurando o ambiente para executar a aplicação web.

1. Faça o download deste repositório:

```
$ git clone https://github.com/evertonnatan/projeto_integrador.git

```

### Criando um ambiente virtual e instalando as dependências: (disponíveis no arquivo  requirementes.txt):

2. Entre na pasta criada e inicie um ambiente virtual:
```
$ cd projeto_integrador
$ python3 -m venv venv

```
3. Ative o ambiente virtual com o seguinte comando:

```
$ source ./venv/bin/activate

```
Após ativado, instale as bibliotecas necessárias para executar o projeto:
```
 (venv)$ pip install -r requirements.txt
```
Para poder realizar o primeiro acesso e configurar a aplicação, é necessário executar o comando 
`migrate`.  Assim, será gerado o banco de dados padrão do Django `(SQLite)`. E depois criar o superusuario:



4. Execute: 

```
(venv)$ ./manage.py migrate
(venv)$ ./manage.py createsuperuser
Apelido/Usuário: admin
E-mail: admin@mail.com
Password: 
Password (again):
```

Para iniciar o servidor depois deste passo você deve executar:
```
(venv)$ ./manage.py runserver
```

Para visualizar se tudo esta executando como esperado, basta acessar o seguinte endereço:
[http://localhost:8000/](http://localhost:8000/)

Ou, para acessar a página de administrador do Django:
[http://localhost:8000/admin](http://localhost:8000/admin)

---

