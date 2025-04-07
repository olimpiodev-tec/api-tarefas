from flask import Flask, request
from tarefa import Tarefa

app = Flask(__name__)

tarefas = [
    Tarefa(task_id=1,
           titulo="Estudar Javascript",
           descricao="Estudar Javascript para aprender a construir eventos nas páginas web",
           status="Em andamento",
           prioridade="Alta",
           data_inicio="01/01/2024",
           data_fim="10/01/2024").to_json(),
    Tarefa(task_id=2,
           titulo="Estudar Flask",
           descricao="Estudar Flask para aprender sobre Web Services",
           status="Não iniciado",
           prioridade="Média",
           data_inicio="",
           data_fim="").to_json()
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            return tarefa

    return 'Tarefa não encontrada'

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('task_id') + 1
    task['task_id'] = ultimo_id
    tarefas.append(task)
    return task

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
    task_remove_index = 0

    for index, task in enumerate(tarefas):
        if task.get('task_id') == task_id:
            task_remove_index = index
            break

    tarefas.pop(task_remove_index)

    return 'Tarefa removida com sucesso'

if __name__ == '__main__':
    app.run(debug=True)
