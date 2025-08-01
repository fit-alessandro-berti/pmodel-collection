# Generated from: 78227013-41dd-4239-9e95-b11a0ccca3fb.json
# Description: This process details the complex setup of an urban vertical farm within a repurposed warehouse space. It involves site analysis, environmental control installation, hydroponic system integration, nutrient solution calibration, lighting optimization, and automation programming. Coordination with local authorities for zoning and safety compliance is required, alongside workforce training for specialized agricultural and technical tasks. Ongoing monitoring and iterative adjustment ensure optimal crop yield and resource efficiency, while data analytics support predictive maintenance and supply chain synchronization. The process culminates in establishing a sustainable, scalable urban farming operation that minimizes ecological impact while maximizing productivity in a confined urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site = Transition(label='Site Survey')
zoning = Transition(label='Zoning Check')
layout = Transition(label='Layout Plan')
env = Transition(label='Env Control')
hydro = Transition(label='Hydro Setup')
nutrient = Transition(label='Nutrient Mix')
light = Transition(label='Light Config')
auto = Transition(label='Automation Dev')
safety = Transition(label='Safety Audit')
training = Transition(label='Staff Training')
system_test = Transition(label='System Test')
seeding = Transition(label='Crop Seeding')
data_monitor = Transition(label='Data Monitor')
yield_opt = Transition(label='Yield Optimize')
supply_align = Transition(label='Supply Align')
maint_plan = Transition(label='Maintenance Plan')

# Loop sub‐workflow for ongoing monitoring and iterative adjustment
po_b = StrictPartialOrder(nodes=[yield_opt, supply_align, maint_plan])
po_b.order.add_edge(yield_opt, supply_align)
po_b.order.add_edge(supply_align, maint_plan)

# LOOP children: 
#  A = data_monitor (measure/monitor)
#  B = po_b    (optimize yield, align supply, plan maintenance)
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor, po_b])

# Assemble the full process as a partial order
root = StrictPartialOrder(nodes=[
    site, zoning, layout,
    env, hydro, nutrient, light, auto,
    safety, training,
    system_test, seeding,
    loop
])
# Define the control‐flow ordering
root.order.add_edge(site, zoning)
root.order.add_edge(zoning, layout)
root.order.add_edge(layout, env)
root.order.add_edge(env, hydro)
root.order.add_edge(hydro, nutrient)
root.order.add_edge(nutrient, light)
root.order.add_edge(light, auto)
root.order.add_edge(auto, safety)
root.order.add_edge(safety, training)
root.order.add_edge(training, system_test)
root.order.add_edge(system_test, seeding)
root.order.add_edge(seeding, loop)