# Generated from: 48cd6509-a059-44ec-835b-9c8f1e82158e.json
# Description: This process involves leasing unique artwork pieces to corporate clients for limited timeframes. It starts with client profiling to understand aesthetic preferences and office environments. Then, curators select suitable artworks from a diverse inventory. Contracts are drafted specifying lease terms, insurance, and maintenance responsibilities. Logistics arrange secure packaging and delivery. Upon installation, an augmented reality app is provided for virtual placement previews. Periodic artwork rotation and condition inspections are scheduled. Feedback is collected to refine future selections. Finally, at lease end, artworks are retrieved, app deactivated, and clients offered purchase options or new leases. This atypical method blends art curation with leasing logistics to enhance corporate spaces dynamically.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
profile_client    = Transition(label="Profile Client")
select_artwork    = Transition(label="Select Artwork")
draft_contract    = Transition(label="Draft Contract")
arrange_delivery  = Transition(label="Arrange Delivery")
install_artwork   = Transition(label="Install Artwork")
activate_app      = Transition(label="Activate App")
schedule_rotation = Transition(label="Schedule Rotation")
inspect_condition = Transition(label="Inspect Condition")
collect_feedback  = Transition(label="Collect Feedback")
retrieve_art      = Transition(label="Retrieve Art")
deactivate_app    = Transition(label="Deactivate App")
offer_purchase    = Transition(label="Offer Purchase")
renew_lease       = Transition(label="Renew Lease")
update_inventory  = Transition(label="Update Inventory")
notify_client     = Transition(label="Notify Client")
process_payment   = Transition(label="Process Payment")

# Loop for periodic rotation and inspections:
#   - First execute schedule_rotation,
#   - then either exit or execute inspect_condition and repeat.
loop_rotation_inspect = OperatorPOWL(
    operator=Operator.LOOP,
    children=[schedule_rotation, inspect_condition]
)

# XOR choice at lease end: either offer purchase or renew lease
end_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[offer_purchase, renew_lease]
)

# After the end choice, the following three activities can proceed in parallel
post_end_concurrency = StrictPartialOrder(
    nodes=[update_inventory, notify_client, process_payment]
)

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        profile_client,
        select_artwork,
        draft_contract,
        arrange_delivery,
        install_artwork,
        activate_app,
        loop_rotation_inspect,
        collect_feedback,
        retrieve_art,
        deactivate_app,
        end_choice,
        post_end_concurrency
    ]
)

# Define the control‐flow edges
root.order.add_edge(profile_client, select_artwork)
root.order.add_edge(select_artwork, draft_contract)
root.order.add_edge(draft_contract, arrange_delivery)
root.order.add_edge(arrange_delivery, install_artwork)
root.order.add_edge(install_artwork, activate_app)
root.order.add_edge(activate_app, loop_rotation_inspect)
root.order.add_edge(loop_rotation_inspect, collect_feedback)
root.order.add_edge(collect_feedback, retrieve_art)
root.order.add_edge(retrieve_art, deactivate_app)
root.order.add_edge(deactivate_app, end_choice)
root.order.add_edge(end_choice, post_end_concurrency)