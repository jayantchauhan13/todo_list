from todo.models import Task

Task.objects.get_or_create(title="Complete Django assignment")
Task.objects.get_or_create(title="Study Python")
Task.objects.get_or_create(title="Prepare for project viva")

print("Sample data added successfully.")
