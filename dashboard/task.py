from easy_dea.celery import app 


@app.task
def add(x, y):
    return x + y