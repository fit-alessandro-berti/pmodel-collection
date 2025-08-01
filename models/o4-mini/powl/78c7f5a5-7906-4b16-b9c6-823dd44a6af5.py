# Generated from: 78c7f5a5-7906-4b16-b9c6-823dd44a6af5.json
# Description: This process involves the intricate steps required to produce, age, and distribute artisanal cheeses with a focus on maintaining unique flavors and quality standards. Starting from sourcing rare milk varieties from small farms, the process includes controlled fermentation, manual curd cutting, and precision aging under varying humidity and temperature conditions. Quality checks are performed at multiple stages including microbial analysis and flavor profiling. The process also integrates customized packaging to preserve freshness and storytelling elements for branding. Finally, the cheese is distributed through niche gourmet channels and specialty retailers, ensuring traceability and consumer education about the product’s heritage and production methods.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
milk_sourcing      = Transition(label='Milk Sourcing')
milk_testing       = Transition(label='Milk Testing')
coagulation_start  = Transition(label='Coagulation Start')
curd_cutting       = Transition(label='Curd Cutting')
whey_drain         = Transition(label='Whey Drain')
molding_cheese     = Transition(label='Molding Cheese')
salt_application   = Transition(label='Salt Application')
fermentation_control = Transition(label='Fermentation Control')
aging_setup        = Transition(label='Aging Setup')
humidity_adjust    = Transition(label='Humidity Adjust')
temperature_adjust = Transition(label='Temperature Adjust')
microbial_test     = Transition(label='Microbial Test')
flavor_profile     = Transition(label='Flavor Profile')
packaging_design   = Transition(label='Packaging Design')
traceability_log   = Transition(label='Traceability Log')
distributor_notify = Transition(label='Distributor Notify')
retail_training    = Transition(label='Retail Training')

# Create the root partial order with all nodes
root = StrictPartialOrder(nodes=[
    milk_sourcing, milk_testing, coagulation_start, curd_cutting, whey_drain,
    molding_cheese, salt_application, fermentation_control, aging_setup,
    humidity_adjust, temperature_adjust, microbial_test, flavor_profile,
    packaging_design, traceability_log, distributor_notify, retail_training
])

# Add control-flow edges (-->)
root.order.add_edge(milk_sourcing,      milk_testing)
root.order.add_edge(milk_testing,       coagulation_start)
root.order.add_edge(coagulation_start,  curd_cutting)
root.order.add_edge(curd_cutting,       whey_drain)
root.order.add_edge(whey_drain,         molding_cheese)
root.order.add_edge(molding_cheese,     salt_application)
root.order.add_edge(salt_application,   fermentation_control)
root.order.add_edge(fermentation_control, aging_setup)

# Aging adjustments are concurrent
root.order.add_edge(aging_setup,        humidity_adjust)
root.order.add_edge(aging_setup,        temperature_adjust)

# Quality checks after both adjustments
root.order.add_edge(humidity_adjust,    microbial_test)
root.order.add_edge(temperature_adjust, microbial_test)
root.order.add_edge(humidity_adjust,    flavor_profile)
root.order.add_edge(temperature_adjust, flavor_profile)

# Packaging and traceability happen after both quality checks
root.order.add_edge(microbial_test,     packaging_design)
root.order.add_edge(flavor_profile,     packaging_design)
root.order.add_edge(microbial_test,     traceability_log)
root.order.add_edge(flavor_profile,     traceability_log)

# Distribution tasks start after packaging and traceability; they run in parallel
root.order.add_edge(packaging_design,   distributor_notify)
root.order.add_edge(traceability_log,   distributor_notify)
root.order.add_edge(packaging_design,   retail_training)
root.order.add_edge(traceability_log,   retail_training)