# Generated from: bb838b38-8207-4f7a-ac1f-7dcdc76f84d8.json
# Description: This process outlines the complex supply chain and quality assurance workflow for artisanal cheese production and distribution. It involves sourcing rare milk varieties from micro-farms, coordinating with seasonal fermentation experts, monitoring aging environments with IoT sensors, conducting multi-stage sensory evaluations, and managing bespoke packaging that preserves flavor profiles. Additionally, it includes negotiating with niche gourmet retailers and organizing exclusive tasting events to maintain brand prestige and customer engagement in a highly competitive niche market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing     = Transition(label="Milk Sourcing")
farm_audit        = Transition(label="Farm Audit")
milk_testing      = Transition(label="Milk Testing")
starter_prep      = Transition(label="Starter Prep")
curd_formation    = Transition(label="Curd Formation")
pressing_stage    = Transition(label="Pressing Stage")
salt_application  = Transition(label="Salt Application")
fermentation      = Transition(label="Fermentation")
humidity_control  = Transition(label="Humidity Control")
aging_log         = Transition(label="Aging Log")
flavor_tasting    = Transition(label="Flavor Tasting")
packaging_design  = Transition(label="Packaging Design")
shelf_labeling    = Transition(label="Shelf Labeling")
retail_negotiation= Transition(label="Retail Negotiation")
tasting_event     = Transition(label="Tasting Event")
customer_feedback = Transition(label="Customer Feedback")
skip              = SilentTransition()

# Loop to model repeated multi-stage sensory evaluation (Flavor Tasting)
# execute flavor_tasting, then either exit or loop again
loop_tasting = OperatorPOWL(operator=Operator.LOOP, children=[flavor_tasting, skip])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    farm_audit,
    milk_testing,
    starter_prep,
    curd_formation,
    pressing_stage,
    salt_application,
    fermentation,
    humidity_control,
    aging_log,
    loop_tasting,
    packaging_design,
    shelf_labeling,
    retail_negotiation,
    tasting_event,
    customer_feedback
])

# Sequential sourcing and initial QA
root.order.add_edge(milk_sourcing, farm_audit)
root.order.add_edge(farm_audit, milk_testing)
root.order.add_edge(milk_testing, starter_prep)
root.order.add_edge(starter_prep, curd_formation)
root.order.add_edge(curd_formation, pressing_stage)
root.order.add_edge(pressing_stage, salt_application)
root.order.add_edge(salt_application, fermentation)

# Concurrent monitoring during fermentation/aging
root.order.add_edge(fermentation, humidity_control)
root.order.add_edge(fermentation, aging_log)

# After both monitoring tasks complete, enter tasting loop
root.order.add_edge(humidity_control, loop_tasting)
root.order.add_edge(aging_log, loop_tasting)

# Once tasting loop exits, proceed to packaging
root.order.add_edge(loop_tasting, packaging_design)
root.order.add_edge(packaging_design, shelf_labeling)

# After labeling, engage both retail negotiation and tasting events in parallel
root.order.add_edge(shelf_labeling, retail_negotiation)
root.order.add_edge(shelf_labeling, tasting_event)

# Finally, collect customer feedback from both channels
root.order.add_edge(retail_negotiation, customer_feedback)
root.order.add_edge(tasting_event,     customer_feedback)