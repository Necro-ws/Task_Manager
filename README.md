*Documentação do Sistema de Gerenciamento de Tarefas

- Introdução
O Sistema de Gerenciamento de Tarefas é uma aplicação de desktop desenvolvida para ajudar os usuários a organizar suas tarefas diárias. Ele permite adicionar, visualizar, editar e excluir tarefas, além de fornecer funcionalidades de filtragem por data e prioridade. Também é possível exportar e importar dados para facilitar o backup e a migração entre sistemas.

- Requisitos do Sistema
Antes de usar o Sistema de Gerenciamento de Tarefas, certifique-se de atender aos seguintes requisitos mínimos:

Sistema Operacional: O sistema foi projetado para ser executado em sistemas operacionais Windows.

Python: Você deve ter o Python 3 instalado no seu sistema. O framework Tkinter é utilizado para o front-end, e o sistema faz uso de bibliotecas Python padrão.

- Instalação
Siga os passos abaixo para instalar e executar o Sistema de Gerenciamento de Tarefas:

Clonar o Repositório: Baixe o código-fonte do projeto a partir do repositório GitHub: link para o repositório.

Configurar o Ambiente Virtual (opcional): Recomendamos criar um ambiente virtual para isolar as dependências do projeto. Use o seguinte comando:

python -m venv venv
Ativar o Ambiente Virtual (opcional): Ative o ambiente virtual usando o comando apropriado para o seu sistema operacional:

Windows:
venv\Scripts\activate

Instalar Dependências: Dentro do ambiente virtual, instale as dependências com o seguinte comando:


pip install -r requirements.txt
Executar o Sistema: Para iniciar o aplicativo, execute o seguinte comando:

python main.py

- Uso
Tela Principal
Ao iniciar o Sistema de Gerenciamento de Tarefas, você será apresentado à tela principal, que inclui uma lista de tarefas e opções de filtro na parte superior.

-Adicionar Tarefa
Para adicionar uma nova tarefa, siga estas etapas:

Clique no botão "Adicionar Tarefa".

Preencha os campos obrigatórios, como o nome da tarefa, data de vencimento e a hora.

Você também pode definir a prioridade da tarefa e adicionar categorias para uma melhor organização.

Clique em "Salvar" para adicionar a tarefa à lista.

-Concluir Tarefa
Para concluir uma tarefa, siga estas etapas:

Selecione a tarefa que deseja marcar como concluida na lista.

Clique no botão "Concluir Tarefa".

-Editar Tarefa
Para editar uma tarefa existente, siga estas etapas:

Selecione a tarefa que deseja editar na lista.

Clique no botão "Editar Tarefa".

Faça as alterações desejadas nos campos de edição.

Clique em "Salvar" para confirmar as alterações.

-Excluir Tarefa
Para excluir uma tarefa, siga estas etapas:

Selecione a tarefa que deseja excluir na lista.

Clique no botão "Excluir Tarefa".

Confirme a exclusão quando solicitado.

-Filtrar Tarefas
Você pode filtrar as tarefas com base na data de vencimento e na prioridade usando as opções de filtro na parte superior da tela.

- Exportar e Importar Dados
O Sistema de Gerenciamento de Tarefas oferece a opção de exportar seus dados para um arquivo JSON e importar dados de um arquivo JSON existente. Isso pode ser útil para fazer backup ou migrar para outro sistema.

-Para exportar dados:

Clique em "Salvar".

Escolha o local e nome do arquivo JSON onde os dados serão salvos.

-Para importar dados:

Clique em "Carregar".

Selecione o arquivo JSON com os dados a serem importados.

- Detalhes de Implementação
O sistema é implementado em Python e usa as seguintes tecnologias e componentes:

Front-end: O front-end é desenvolvido com o framework Tkinter, uma biblioteca gráfica nativa do Python.

Back-end: A lógica de negócios e o gerenciamento de tarefas são implementados em Python.

Armazenamento de Dados: Os dados das tarefas são armazenados em um arquivo JSON incorporado. O arquivo é carregado na inicialização e salvo automaticamente ao adicionar, editar ou excluir tarefas.

- Conclusão
O Sistema de Gerenciamento de Tarefas é uma ferramenta simples e eficaz para ajudar os usuários a manter o controle de suas tarefas diárias. Siga as instruções de uso e desfrute de uma gestão de tarefas mais organizada e eficiente.

Obrigado por usar o Sistema de Gerenciamento de Tarefas!