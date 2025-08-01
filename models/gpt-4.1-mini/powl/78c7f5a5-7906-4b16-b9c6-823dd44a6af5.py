# Generated from: 78c7f5a5-7906-4b16-b9c6-823dd44a6af5.json
# Description: This process involves the intricate steps required to produce, age, and distribute artisanal cheeses with a focus on maintaining unique flavors and quality standards. Starting from sourcing rare milk varieties from small farms, the process includes controlled fermentation, manual curd cutting, and precision aging under varying humidity and temperature conditions. Quality checks are performed at multiple stages including microbial analysis and flavor profiling. The process also integrates customized packaging to preserve freshness and storytelling elements for branding. Finally, the cheese is distributed through niche gourmet channels and specialty retailers, ensuring traceability and consumer education about the product’s heritage and production methods.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
milk_testing = Transition(label='Milk Testing')
coag_start = Transition(label='Coagulation Start')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
molding_cheese = Transition(label='Molding Cheese')
salt_application = Transition(label='Salt Application')
fermentation_control = Transition(label='Fermentation Control')
aging_setup = Transition(label='Aging Setup')
humidity_adjust = Transition(label='Humidity Adjust')
temperature_adjust = Transition(label='Temperature Adjust')
microbial_test = Transition(label='Microbial Test')
flavor_profile = Transition(label='Flavor Profile')
packaging_design = Transition(label='Packaging Design')
traceability_log = Transition(label='Traceability Log')
distributor_notify = Transition(label='Distributor Notify')
retail_training = Transition(label='Retail Training')

# Define partial order nodes and order edges
# Constructing the workflow in meaningful sequence with concurrency where possible:

# First: Milk Sourcing --> Milk Testing --> Coagulation Start
po1 = StrictPartialOrder(nodes=[milk_sourcing, milk_testing, coag_start])
po1.order.add_edge(milk_sourcing, milk_testing)
po1.order.add_edge(milk_testing, coag_start)

# Then manual steps: Curd Cutting --> Whey Drain --> Molding Cheese --> Salt Application
po2 = StrictPartialOrder(nodes=[curd_cutting, whey_drain, molding_cheese, salt_application])
po2.order.add_edge(curd_cutting, whey_drain)
po2.order.add_edge(whey_drain, molding_cheese)
po2.order.add_edge(molding_cheese, salt_application)

# Fermentation Control after Salt Application
# Fermentation Control leads to Aging Setup
po3 = StrictPartialOrder(nodes=[salt_application, fermentation_control, aging_setup])
po3.order.add_edge(salt_application, fermentation_control)
po3.order.add_edge(fermentation_control, aging_setup)

# Humidity Adjust and Temperature Adjust happen in parallel after Aging Setup
# (Concurrency between Humidity Adjust and Temperature Adjust)
po4 = StrictPartialOrder(nodes=[aging_setup, humidity_adjust, temperature_adjust])
po4.order.add_edge(aging_setup, humidity_adjust)
po4.order.add_edge(aging_setup, temperature_adjust)

# Quality checks: Microbial Test and Flavor Profile run in parallel after humidity & temperature adjustments
po5 = StrictPartialOrder(nodes=[humidity_adjust, temperature_adjust, microbial_test, flavor_profile])
# humidity_adjust and temperature_adjust must finish before microbial_test and flavor_profile
po5.order.add_edge(humidity_adjust, microbial_test)
po5.order.add_edge(humidity_adjust, flavor_profile)
po5.order.add_edge(temperature_adjust, microbial_test)
po5.order.add_edge(temperature_adjust, flavor_profile)

# Packaging Design after quality checks
po6 = StrictPartialOrder(nodes=[microbial_test, flavor_profile, packaging_design])
po6.order.add_edge(microbial_test, packaging_design)
po6.order.add_edge(flavor_profile, packaging_design)

# Traceability Log after Packaging Design
trace_pack_po = StrictPartialOrder(nodes=[packaging_design, traceability_log])
trace_pack_po.order.add_edge(packaging_design, traceability_log)

# Distributor Notify after Traceability Log
distributor_po = StrictPartialOrder(nodes=[traceability_log, distributor_notify])
distributor_po.order.add_edge(traceability_log, distributor_notify)

# Retail Training after Distributor Notify
retail_po = StrictPartialOrder(nodes=[distributor_notify, retail_training])
retail_po.order.add_edge(distributor_notify, retail_training)

# Compose the entire process partial orders sequentially with correct dependencies:
# po1 -> po2 -> po3 -> po4 -> po5 -> po6 -> trace_pack_po -> distributor_po -> retail_po

# Top level partial order nodes include all these partial orders (some involve overlap nodes, but pm4py
# StrictPartialOrder expects nodes as Transition or OperatorPOWL objects, so we will connect partial orders 
# by edges between their start/end nodes.

# Since nodes in pm4py StrictPartialOrder are atomic transitions or OperatorPOWL nodes only,
# we'll combine by making composite StrictPartialOrder over all individual nodes and edges.

nodes = [
    milk_sourcing, milk_testing, coag_start,
    curd_cutting, whey_drain, molding_cheese, salt_application,
    fermentation_control, aging_setup,
    humidity_adjust, temperature_adjust,
    microbial_test, flavor_profile,
    packaging_design, traceability_log,
    distributor_notify, retail_training
]

root = StrictPartialOrder(nodes=nodes)

# Add edges representing the control flow described above:

# po1
root.order.add_edge(milk_sourcing, milk_testing)
root.order.add_edge(milk_testing, coag_start)

# po2
root.order.add_edge(coag_start, curd_cutting)  # Link po1 to po2 start
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, molding_cheese)
root.order.add_edge(molding_cheese, salt_application)

# po3
root.order.add_edge(salt_application, fermentation_control)
root.order.add_edge(fermentation_control, aging_setup)

# po4
root.order.add_edge(aging_setup, humidity_adjust)
root.order.add_edge(aging_setup, temperature_adjust)

# po5
root.order.add_edge(humidity_adjust, microbial_test)
root.order.add_edge(humidity_adjust, flavor_profile)
root.order.add_edge(temperature_adjust, microbial_test)
root.order.add_edge(temperature_adjust, flavor_profile)

# po6
root.order.add_edge(microbial_test, packaging_design)
root.order.add_edge(flavor_profile, packaging_design)

# trace_pack_po
root.order.add_edge(packaging_design, traceability_log)

# distributor_po
root.order.add_edge(traceability_log, distributor_notify)

# retail_po
root.order.add_edge(distributor_notify, retail_training)