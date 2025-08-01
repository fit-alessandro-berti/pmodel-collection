# Generated from: 778cb7b4-3125-47f0-89a0-37031c55e91b.json
# Description: This process outlines the establishment of an urban vertical farming system within a repurposed industrial building. It covers site assessment, modular rack installation, environmental control calibration, hydroponic nutrient solution preparation, seedling propagation, automated monitoring setup, and integration with local food distribution networks. The process requires coordination between agricultural experts, engineers, and logistics teams to ensure sustainable crop yield, energy efficiency, and rapid market delivery. Continuous data analysis and system optimization follow initial deployment to adapt to seasonal variations and urban constraints, maximizing productivity within limited space while minimizing resource consumption and waste.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
t1  = Transition(label='Site Survey')
t2  = Transition(label='Structural Check')
t3  = Transition(label='Rack Setup')
t4  = Transition(label='Lighting Install')
t5  = Transition(label='Env Calibration')
t6  = Transition(label='Water Testing')
t7  = Transition(label='Nutrient Mix')
t8  = Transition(label='Seedling Plant')
t9  = Transition(label='Sensor Deploy')
t10 = Transition(label='System Sync')
t11 = Transition(label='Growth Monitor')
t12 = Transition(label='Pest Inspect')
t13 = Transition(label='Harvest Plan')
t14 = Transition(label='Packaging Prep')
t15 = Transition(label='Market Link')
t16 = Transition(label='Waste Manage')
t17 = Transition(label='Data Review')
t18 = Transition(label='Energy Audit')

# Loop for continuous optimization: Data Review then optionally Energy Audit repeated
loop_opt = OperatorPOWL(operator=Operator.LOOP, children=[t17, t18])

# Build the partial order
root = StrictPartialOrder(nodes=[
    t1, t2, t3, t4, t5, t6, t7, t8, t9, t10,
    t11, t12, t13, t14, t15, t16,
    loop_opt
])

# Sequence of setup and installation
root.order.add_edge(t1, t2)
root.order.add_edge(t2, t3)
root.order.add_edge(t3, t4)
root.order.add_edge(t4, t5)
root.order.add_edge(t5, t6)
root.order.add_edge(t6, t7)
root.order.add_edge(t7, t8)
root.order.add_edge(t8, t9)
root.order.add_edge(t9, t10)

# Parallel monitoring setup: Growth Monitor and Pest Inspect after system sync
root.order.add_edge(t10, t11)
root.order.add_edge(t10, t12)
# Join before harvesting plan
root.order.add_edge(t11, t13)
root.order.add_edge(t12, t13)

# Harvesting and distribution sequence
root.order.add_edge(t13, t14)
root.order.add_edge(t14, t15)
root.order.add_edge(t15, t16)

# Start continuous optimization loop after waste management
root.order.add_edge(t16, loop_opt)