# Generated from: 48cd6509-a059-44ec-835b-9c8f1e82158e.json
# Description: This process involves leasing unique artwork pieces to corporate clients for limited timeframes. It starts with client profiling to understand aesthetic preferences and office environments. Then, curators select suitable artworks from a diverse inventory. Contracts are drafted specifying lease terms, insurance, and maintenance responsibilities. Logistics arrange secure packaging and delivery. Upon installation, an augmented reality app is provided for virtual placement previews. Periodic artwork rotation and condition inspections are scheduled. Feedback is collected to refine future selections. Finally, at lease end, artworks are retrieved, app deactivated, and clients offered purchase options or new leases. This atypical method blends art curation with leasing logistics to enhance corporate spaces dynamically.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Profile_Client = Transition(label='Profile Client')
Select_Artwork = Transition(label='Select Artwork')
Draft_Contract = Transition(label='Draft Contract')
Arrange_Delivery = Transition(label='Arrange Delivery')
Install_Artwork = Transition(label='Install Artwork')
Activate_App = Transition(label='Activate App')
Schedule_Rotation = Transition(label='Schedule Rotation')
Inspect_Condition = Transition(label='Inspect Condition')
Collect_Feedback = Transition(label='Collect Feedback')
Retrieve_Art = Transition(label='Retrieve Art')
Deactivate_App = Transition(label='Deactivate App')
Offer_Purchase = Transition(label='Offer Purchase')
Renew_Lease = Transition(label='Renew Lease')
Update_Inventory = Transition(label='Update Inventory')
Notify_Client = Transition(label='Notify Client')
Process_Payment = Transition(label='Process Payment')
skip = SilentTransition()

# Periodic maintenance loop: Schedule Rotation then Inspect Condition, loop these until exit
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Schedule_Rotation,
    Inspect_Condition
])

# Choice at lease end: Offer Purchase or Renew Lease
end_choice = OperatorPOWL(operator=Operator.XOR, children=[
    Offer_Purchase,
    Renew_Lease
])

# Partial order for contract drafting and logistics
contract_logistics = StrictPartialOrder(nodes=[
    Draft_Contract,
    Arrange_Delivery
])
contract_logistics.order.add_edge(Draft_Contract, Arrange_Delivery)

# Installation and app activation happen sequentially
install_and_activate = StrictPartialOrder(nodes=[
    Install_Artwork,
    Activate_App
])
install_and_activate.order.add_edge(Install_Artwork, Activate_App)

# Final retrieval sequence: Retrieve Art then Deactivate App then end_choice
final_retrieval = StrictPartialOrder(nodes=[
    Retrieve_Art,
    Deactivate_App,
    end_choice
])
final_retrieval.order.add_edge(Retrieve_Art, Deactivate_App)
final_retrieval.order.add_edge(Deactivate_App, end_choice)

# Feedback collection followed by inventory update, notification and payment processing
feedback_update = StrictPartialOrder(nodes=[
    Collect_Feedback,
    Update_Inventory,
    Notify_Client,
    Process_Payment
])
feedback_update.order.add_edge(Collect_Feedback, Update_Inventory)
feedback_update.order.add_edge(Update_Inventory, Notify_Client)
feedback_update.order.add_edge(Notify_Client, Process_Payment)

# Compose the main process partial order
# Steps: Profile Client -> Select Artwork -> contract & logistics -> install & activate -> maintenance loop (concurrent with feedback collection?) -> final retrieval
# Feedback collection logically after maintenance loop ends, but here we model maintenance loop as repeated steps before retrieval.
# For simplicity, feedback collection after maintenance loop ends.

root = StrictPartialOrder(nodes=[
    Profile_Client,
    Select_Artwork,
    contract_logistics,
    install_and_activate,
    maintenance_loop,
    feedback_update,
    final_retrieval
])

# Define the partial order edges
root.order.add_edge(Profile_Client, Select_Artwork)
root.order.add_edge(Select_Artwork, contract_logistics)
root.order.add_edge(contract_logistics, install_and_activate)
root.order.add_edge(install_and_activate, maintenance_loop)
root.order.add_edge(maintenance_loop, feedback_update)
root.order.add_edge(feedback_update, final_retrieval)