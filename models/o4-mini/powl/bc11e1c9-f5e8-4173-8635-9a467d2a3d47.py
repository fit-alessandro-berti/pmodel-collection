# Generated from: bc11e1c9-f5e8-4173-8635-9a467d2a3d47.json
# Description: This process outlines the intricate supply chain for artisan cheese production, starting from sourcing rare milk varieties from remote farms, through specialized fermentation monitoring, hand craftsmanship in curd cutting, aging under precise humidity controls, and finally bespoke packaging tailored for niche markets. The workflow involves quality assurance at multiple stages, logistics coordination with temperature-controlled transport, compliance with local food safety regulations, and dynamic inventory adjustments based on seasonal demand fluctuations. Collaboration with local farmers, artisan cheesemakers, and boutique retailers is essential to maintain product uniqueness and customer satisfaction in a highly competitive gourmet segment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
milk_sourcing    = Transition(label='Milk Sourcing')
quality_test_1   = Transition(label='Quality Testing')
curd_cutting     = Transition(label='Curd Cutting')
whey_draining    = Transition(label='Whey Draining')
salt_application = Transition(label='Salt Application')
fermentation_chk = Transition(label='Fermentation Check')
humidity_ctrl    = Transition(label='Humidity Control')
aging_monitor    = Transition(label='Aging Monitoring')
texture_testing  = Transition(label='Texture Testing')
flavor_profiling = Transition(label='Flavor Profiling')
quality_test_2   = Transition(label='Quality Testing')
packaging_design = Transition(label='Packaging Design')
label_printing   = Transition(label='Label Printing')
compliance_audit = Transition(label='Compliance Audit')
cold_storage     = Transition(label='Cold Storage')
transport_sched  = Transition(label='Transport Scheduling')
inventory_review = Transition(label='Inventory Review')
retail_coord     = Transition(label='Retail Coordination')

# Loop for fermentation & environmental control:
#   A = fermentation_chk
#   B = (humidity_ctrl -> aging_monitor)
body1 = StrictPartialOrder(nodes=[humidity_ctrl, aging_monitor])
body1.order.add_edge(humidity_ctrl, aging_monitor)
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_chk, body1])

# Loop for dynamic inventory adjustments:
#   A = inventory_review
#   B = retail_coord
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[inventory_review, retail_coord])

# Root partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_test_1,
    curd_cutting,
    whey_draining,
    salt_application,
    loop1,
    texture_testing,
    flavor_profiling,
    quality_test_2,
    packaging_design,
    label_printing,
    compliance_audit,
    cold_storage,
    transport_sched,
    loop2
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing,  quality_test_1)
root.order.add_edge(quality_test_1,  curd_cutting)
root.order.add_edge(curd_cutting,   whey_draining)
root.order.add_edge(whey_draining,  salt_application)
root.order.add_edge(salt_application, loop1)
root.order.add_edge(loop1,          texture_testing)
root.order.add_edge(texture_testing, flavor_profiling)
root.order.add_edge(flavor_profiling, quality_test_2)
root.order.add_edge(quality_test_2,  packaging_design)
root.order.add_edge(packaging_design, label_printing)
root.order.add_edge(label_printing,  compliance_audit)
# After compliance, logistics (concurrent)
root.order.add_edge(compliance_audit, cold_storage)
root.order.add_edge(compliance_audit, transport_sched)
# After logistics, inventory/retail loop
root.order.add_edge(cold_storage,    loop2)
root.order.add_edge(transport_sched, loop2)