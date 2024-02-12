from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )  # data da tarefa criada
    deadline = models.DateTimeField(null=False, blank=False)  # data da entrega
    finished_at = models.DateTimeField(null=True)  # data da finalização
