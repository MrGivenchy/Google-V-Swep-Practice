from collections import deque

class Task:
    def __init__(self, Id: int, description: str, priority: int, dependencies=None):
        self.Id = Id
        self.description = description
        self.priority = priority
        self.dependencies = dependencies if dependencies else []


def dependency(Tasks: list[Task]) -> list[Task]:
    out = []

    for task in Tasks:
        if task.priority == 0:
            q = deque()
            q.append(task)

            while q:
                node = q.popleft()
                out.extend(node.dependencies)
                q.extendleft(node.dependencies)

    return out


def completion_order(tasks: list[Task]) -> list[Task]:
    out = []
    visited = set()

    def dfs(task):
        if task.Id in visited:
            return

        visited.add(task.Id)

        for dep in task.dependencies:
            dfs(dep)

        out.append(task)

    for task in tasks:
        if task.priority == 0:
            dfs(task)

    return out