from prefect import flow, task, serve
from prefect.blocks.system import String

string_block = String.load("hello")

@task
def my_task():
    print("Hello I'm a task!")
    print(string_block.value)


@flow
def sub_flow():
    print("I'm a sub flow")


@flow
def my_flow():
    my_task()
    sub_flow()
    print("Hello I'm in the flow!")




my_flow()