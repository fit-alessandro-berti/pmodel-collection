# Generated from: 4bac6d38-10cc-44e2-98dc-81264581899d.json
# Description: This process describes the intricate supply chain management for a network of artisan craftsmen producing bespoke furniture. It integrates raw material sourcing from sustainable forests, handcrafting stages with quality checkpoints, coordination of custom design inputs, and decentralized logistics involving local couriers. The process also includes adaptive inventory forecasting based on seasonal demand fluctuations and real-time artisan feedback, ensuring minimal waste and maximum customer satisfaction through personalized delivery schedules and post-sale care services.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
source_timber    = Transition(label="Source Timber")
inspect_logs     = Transition(label="Inspect Logs")
design_draft     = Transition(label="Design Draft")
material_prep    = Transition(label="Material Prep")
craft_assembly   = Transition(label="Craft Assembly")
quality_check    = Transition(label="Quality Check")
client_review    = Transition(label="Client Review")
adjust_design    = Transition(label="Adjust Design")
finish_surface   = Transition(label="Finish Surface")
package_goods    = Transition(label="Package Goods")
schedule_pickup  = Transition(label="Schedule Pickup")
local_courier    = Transition(label="Local Courier")
track_delivery   = Transition(label="Track Delivery")
inventory_update = Transition(label="Inventory Update")
collect_feedback = Transition(label="Collect Feedback")
aftercare_setup  = Transition(label="Aftercare Setup")

# Loop for client‐driven design adjustments:
#   Do a Client Review, then either exit or do Adjust Design and review again
design_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[client_review, adjust_design]
)

# Loop for adaptive inventory forecasting:
#   Do an Inventory Update, then either exit or do Collect Feedback and update again
forecast_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[inventory_update, collect_feedback]
)

# Build the top‐level partial order workflow
root = StrictPartialOrder(nodes=[
    source_timber,
    inspect_logs,
    design_draft,
    material_prep,
    craft_assembly,
    quality_check,
    design_loop,
    finish_surface,
    package_goods,
    schedule_pickup,
    local_courier,
    track_delivery,
    forecast_loop,
    aftercare_setup
])

# Define the control‐flow (order) relations
# Raw material sourcing and inspection
root.order.add_edge(source_timber, inspect_logs)

# After inspecting, design and material prep can proceed in parallel
root.order.add_edge(inspect_logs, design_draft)
root.order.add_edge(inspect_logs, material_prep)

# Both design draft and material prep must complete before assembly
root.order.add_edge(design_draft, craft_assembly)
root.order.add_edge(material_prep, craft_assembly)

# Assembly → quality check → design review loop → finishing → packaging → logistics
root.order.add_edge(craft_assembly, quality_check)
root.order.add_edge(quality_check, design_loop)
root.order.add_edge(design_loop, finish_surface)
root.order.add_edge(finish_surface, package_goods)
root.order.add_edge(package_goods, schedule_pickup)
root.order.add_edge(schedule_pickup, local_courier)
root.order.add_edge(local_courier, track_delivery)

# After delivery, forecasting loop then post‐sale care
root.order.add_edge(track_delivery, forecast_loop)
root.order.add_edge(forecast_loop, aftercare_setup)