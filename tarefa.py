class Tarefa:

    def __init__(self, task_id, titulo, descricao, prioridade, data_inicio, data_fim, status):
        self.task_id = task_id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status

    def to_json(self):
        return {
            'task_id': self.task_id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'prioridade': self.prioridade,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
            'status': self.status
        }

