from behave import given, when, then
from todo_list import Task, ToDoList


@then('task {task_index} should be marked as completed')
def step_impl(context, task_index):
    assert context.todo_list.tasks[int(task_index) - 1].completed

@then('the task list should be empty')
def step_impl(context):
    assert len(context.todo_list.tasks) == 0


@when('I set priority {priority} for task {task_index}')
def step_impl(context, priority, task_index):
    context.todo_list.set_task_priority(int(task_index), priority)


@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{title}"')
def step_impl(context, title):
    task = Task(title, "")
    context.todo_list.add_task(task)

@then('the to-do list should contain "{title}"')
def step_impl(context, title):
    task_titles = [task.title for task in context.todo_list.tasks]
    assert title in task_titles
    
@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        task = Task(row['Task'], row.get('Status', 'Pending'))
        context.todo_list.add_task(task)

@when('the user lists all tasks')
def step_impl(context):
    context.list_output = []
    def mock_print(text):
        context.list_output.append(text)
    context.original_print = print
    print = mock_print
    context.todo_list.list_tasks()



@when('the user marks task "{title}" as completed')
def step_impl(context, title):
    context.todo_list.mark_task_completed(title)

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.tasks) == 0
    
@then('the to-do list should show task "{title}" as completed')
def step_impl(context, title):
    for task in context.todo_list.tasks:
        if task.title == title:
            assert task.status == "Completed"
            return
    assert False, f"Task '{title}' not found in the to-do list"

@then('the output should contain')
def step_impl(context):
    expected_output = context.text.splitlines()
    for line in expected_output:
        assert line in context.list_output
        
