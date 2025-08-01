# Generated from: ed957f4d-133f-452b-b47e-cb615d9c850a.json
# Description: This process manages the end-to-end supply chain for urban beekeeping equipment, integrating sustainable sourcing, community engagement, and adaptive logistics to meet fluctuating local demand. Activities include raw material vetting from urban farms, modular product design for limited spaces, micro-warehousing in city hubs, and dynamic customer feedback loops to refine offerings. The process emphasizes eco-friendly packaging and real-time inventory tracking through IoT sensors, balancing rapid response times with minimizing carbon footprint. Additionally, it incorporates urban pollinator habitat mapping for strategic marketing and partnerships with local environmental groups to enhance brand authenticity and social impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_source        = Transition(label='Source Materials')
t_vet           = Transition(label='Vet Suppliers')
t_permit        = Transition(label='Secure Permits')
t_design        = Transition(label='Design Modules')
t_prototype     = Transition(label='Prototype Build')
t_test          = Transition(label='Test Durability')
t_adjust        = Transition(label='Adjust Production')
t_map           = Transition(label='Map Habitats')
t_partner       = Transition(label='Partner NGOs')
t_launch        = Transition(label='Launch Campaign')
t_micro_wh      = Transition(label='Micro Warehouse')
t_monitor       = Transition(label='Monitor Sensors')
t_sync          = Transition(label='Inventory Sync')
t_route         = Transition(label='Route Optimize')
t_pack          = Transition(label='Pack Sustainably')
t_engage        = Transition(label='Engage Community')
t_feedback      = Transition(label='Collect Feedback')
t_report        = Transition(label='Report Impact')

# Loop for prototype iteration: build -> test, optional adjust, repeat
po_build_test = StrictPartialOrder(nodes=[t_prototype, t_test])
po_build_test.order.add_edge(t_prototype, t_test)
loop_prototype = OperatorPOWL(operator=Operator.LOOP, children=[po_build_test, t_adjust])

# Loop for community feedback: engage -> collect -> report, optional adjust, repeat
po_feedback = StrictPartialOrder(nodes=[t_engage, t_feedback, t_report])
po_feedback.order.add_edge(t_engage, t_feedback)
po_feedback.order.add_edge(t_feedback, t_report)
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[po_feedback, t_adjust])

# Top-level partial order
root = StrictPartialOrder(nodes=[
    t_source, t_vet, t_permit, t_design, loop_prototype,
    t_map, t_partner, t_launch,
    t_micro_wh, t_monitor, t_sync, t_route, t_pack,
    loop_feedback
])

# Supply & design flow
root.order.add_edge(t_source, t_vet)
root.order.add_edge(t_vet, t_permit)
root.order.add_edge(t_permit, t_design)
root.order.add_edge(t_design, loop_prototype)

# Habitat mapping & marketing
root.order.add_edge(t_permit, t_map)
root.order.add_edge(t_map, t_partner)
root.order.add_edge(t_partner, t_launch)

# Warehousing & logistics flow
root.order.add_edge(loop_prototype, t_micro_wh)
root.order.add_edge(loop_prototype, t_monitor)
root.order.add_edge(t_monitor, t_sync)
root.order.add_edge(t_micro_wh, t_route)
root.order.add_edge(t_sync, t_route)
root.order.add_edge(t_route, t_pack)

# Customer feedback loop after launch
root.order.add_edge(t_launch, loop_feedback)