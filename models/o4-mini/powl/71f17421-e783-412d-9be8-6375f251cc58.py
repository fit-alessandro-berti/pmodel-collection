# Generated from: 71f17421-e783-412d-9be8-6375f251cc58.json
# Description: This process details the artisanal cheese supply chain involving small-scale farm production, quality fermentation, aging, and niche market distribution. It starts with milk sourcing from rare breed cows, followed by precise curd formation and hand-pressing techniques. The cheeses undergo microclimate-controlled aging, with periodic manual inspections and flavor profiling. Packaging uses biodegradable materials with custom labeling. The distribution leverages local gourmet shops and direct farmer-to-chef deliveries, requiring coordination with logistics providers for temperature-controlled transport. Feedback loops involve tasting panels and customer surveys to refine future batches, ensuring a consistent premium product that preserves traditional methods while meeting modern sustainability standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk = Transition(label='Milk Sourcing')
breed = Transition(label='Breed Selection')
curd = Transition(label='Curd Formation')
press = Transition(label='Hand Pressing')
salt = Transition(label='Salt Rubbing')
batch_label = Transition(label='Batch Labeling')
ferment_test = Transition(label='Fermentation Test')
aging = Transition(label='Microclimate Aging')
inspect = Transition(label='Manual Inspection')
profile = Transition(label='Flavor Profiling')
prep = Transition(label='Packaging Prep')
eco_pack = Transition(label='Eco Packaging')
plan = Transition(label='Logistics Planning')
transport = Transition(label='Cold Transport')
retail = Transition(label='Retail Delivery')
chef = Transition(label='Chef Coordination')
tasting = Transition(label='Tasting Panels')
survey = Transition(label='Customer Survey')

# Distribution choice: either retail delivery or direct chef coordination
distribution = OperatorPOWL(
    operator=Operator.XOR,
    children=[retail, chef]
)

# Main production & distribution partial order
main_flow = StrictPartialOrder(nodes=[
    milk, breed, curd, press, salt,
    batch_label, ferment_test, aging, inspect,
    profile, prep, eco_pack, plan, transport,
    distribution
])
# Define the control-flow ordering for main_flow
main_flow.order.add_edge(milk, breed)
main_flow.order.add_edge(breed, curd)
main_flow.order.add_edge(curd, press)
main_flow.order.add_edge(press, salt)
main_flow.order.add_edge(salt, batch_label)
main_flow.order.add_edge(batch_label, ferment_test)
main_flow.order.add_edge(ferment_test, aging)
main_flow.order.add_edge(aging, inspect)
main_flow.order.add_edge(inspect, profile)
main_flow.order.add_edge(profile, prep)
main_flow.order.add_edge(prep, eco_pack)
main_flow.order.add_edge(eco_pack, plan)
main_flow.order.add_edge(plan, transport)
main_flow.order.add_edge(transport, distribution)

# Feedback loop partial order: tasting panels then customer survey
feedback = StrictPartialOrder(nodes=[tasting, survey])
feedback.order.add_edge(tasting, survey)

# Loop: run the main_flow, then optionally collect feedback and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_flow, feedback]
)