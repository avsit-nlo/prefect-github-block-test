from prefect import flow
from prefect.events.schemas.deployment_triggers import DeploymentEventTrigger
from prefect.events import emit_event


order_complete = DeploymentEventTrigger(
    expect={"order.complete"},
    after={"order.created"},
    for_each={"prefect.resource.id"},
    parameters={"user_id": "{{ event.resource.id }}"},
)


@flow(log_prints=True)
def post_order_complete(user_id: str):
    print(f"User {user_id} has completed an order -- doing stuff now")

def emit_order_created_event(user_id):
    # Émettre l'événement "order.created"
    emit_event(event="order.created", resource={"prefect.resource.id": user_id})

def emit_order_complete_event(user_id):
    # Émettre l'événement "order.complete"
    emit_event(event="order.complete", resource={"prefect.resource.id": user_id})


if __name__ == "__main__":


        # Exemple d'un utilisateur ID
    user_id = "user_123"
    
    # Émettre l'événement "order.created"
    emit_order_created_event(user_id)
    
    # Ensuite, émettre l'événement "order.complete"
    emit_order_complete_event(user_id)

    
    post_order_complete.serve(triggers=[order_complete])
