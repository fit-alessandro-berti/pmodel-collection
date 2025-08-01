# Generated from: b9ab5e38-c0d1-47ed-b839-3cb474361e31.json
# Description: This process outlines the comprehensive supply chain for artisan cheese production and distribution, starting from selecting rare milk sources to final delivery. It includes unique steps such as microbial culture optimization, aging environment control, sensory evaluation panels, and custom packaging design. The process integrates quality assurance with traditional craftsmanship, ensuring the preservation of unique flavor profiles while scaling production. It also incorporates traceability from farm to retailer, sustainable waste management, and customer feedback loops to continually refine the product and maintain artisanal authenticity in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing       = Transition(label='Milk Sourcing')
microbe_culturing   = Transition(label='Microbe Culturing')
coagulation         = Transition(label='Coagulation')
curd_cutting        = Transition(label='Curd Cutting')
whey_draining       = Transition(label='Whey Draining')
molding_press       = Transition(label='Molding Press')
salting_stage       = Transition(label='Salting Stage')
aging_control       = Transition(label='Aging Control')
humidity_check      = Transition(label='Humidity Check')
flavor_testing      = Transition(label='Flavor Testing')
packaging_design    = Transition(label='Packaging Design')
batch_tracking      = Transition(label='Batch Tracking')
transport_scheduling= Transition(label='Transport Scheduling')
retail_setup        = Transition(label='Retail Setup')
feedback_review     = Transition(label='Feedback Review')
waste_recycling     = Transition(label='Waste Recycling')

# Main production & distribution partial order
main = StrictPartialOrder(nodes=[
    milk_sourcing,
    microbe_culturing,
    coagulation,
    curd_cutting,
    whey_draining,
    molding_press,
    salting_stage,
    aging_control,
    humidity_check,
    flavor_testing,
    packaging_design,
    batch_tracking,
    transport_scheduling,
    retail_setup,
    waste_recycling
])

# Manufacturing sequence
main.order.add_edge(milk_sourcing, microbe_culturing)
main.order.add_edge(microbe_culturing, coagulation)
main.order.add_edge(coagulation, curd_cutting)
main.order.add_edge(curd_cutting, whey_draining)
main.order.add_edge(whey_draining, molding_press)
main.order.add_edge(molding_press, salting_stage)

# Quality‐control branching: aging & humidity in parallel, then flavor testing
main.order.add_edge(salting_stage, aging_control)
main.order.add_edge(salting_stage, humidity_check)
main.order.add_edge(aging_control, flavor_testing)
main.order.add_edge(humidity_check, flavor_testing)

# Distribution sequence
main.order.add_edge(flavor_testing, packaging_design)
main.order.add_edge(packaging_design, batch_tracking)
main.order.add_edge(batch_tracking, transport_scheduling)
main.order.add_edge(transport_scheduling, retail_setup)

# Sustainable waste management
main.order.add_edge(whey_draining, waste_recycling)
main.order.add_edge(packaging_design, waste_recycling)

# Improvement choice after feedback: either adjust microbes or packaging
improvement_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[microbe_culturing, packaging_design]
)

# Feedback sequence: review then choose improvement
feedback_seq = StrictPartialOrder(nodes=[feedback_review, improvement_choice])
feedback_seq.order.add_edge(feedback_review, improvement_choice)

# Loop: run main process, then either exit or do feedback_seq and repeat
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main, feedback_seq]
)