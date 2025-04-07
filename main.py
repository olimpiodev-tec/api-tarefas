from flask import Flask, request
from tarefa_controller import get_tarefas, get_tarefa, criar_tarefa, remover_tarefa

app = Flask(__name__)

tarefas = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return get_tarefas()


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    return get_tarefa(task_id)


@app.route('/tasks', methods=['POST'])
def create_task():
    return criar_tarefa(request.json)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    # Buscando a tarefa que será alterada
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            task_search = tarefa

    # Alterando a tarefa na lista
    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['prioridade'] = task_body.get('prioridade')
    task_search['data_inicio'] = task_body.get('data_inicio')
    task_search['data_fim'] = task_body.get('data_fim')

    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return remover_tarefa(task_id)

if __name__ == '__main__':
    app.run(debug=True)
