# Generated from: 6734dc9e-536f-40bf-a717-032633d46d55.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming facility within a repurposed industrial building. It includes initial site assessment, modular system design, environmental control calibration, automated nutrient delivery setup, and integration with local distribution networks. The process also covers regulatory compliance, waste recycling implementation, real-time crop monitoring, and adaptive pest control strategies. Special attention is given to energy optimization, workforce training, data analytics for yield prediction, and continuous system maintenance to ensure sustainable and efficient production in a high-density urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

SS = Transition(label='Site Survey')
SD = Transition(label='System Design')
PA = Transition(label='Permits Acquire')
MB = Transition(label='Modular Build')
EC = Transition(label='Env Control')
NS = Transition(label='Nutrient Setup')
LI = Transition(label='Lighting Install')
IT = Transition(label='Irrigation Test')
SDp = Transition(label='Sensor Deploy')
WP = Transition(label='Waste Plan')
PC = Transition(label='Pest Control')
EA = Transition(label='Energy Audit')
ST = Transition(label='Staff Training')
DS = Transition(label='Data Setup')
YM = Transition(label='Yield Monitor')
LS = Transition(label='Logistics Sync')
MP = Transition(label='Maintenance Plan')

# Define partial orders reflecting the logical order and concurrency

# Initial assessment and planning
init_po = StrictPartialOrder(nodes=[SS, SD, PA])
init_po.order.add_edge(SS, SD)
init_po.order.add_edge(SS, PA)

# Modular build depends on system design and permits
build_po = StrictPartialOrder(nodes=[MB, SD, PA])
build_po.order.add_edge(SD, MB)
build_po.order.add_edge(PA, MB)

# Environmental setup: Env Control, Nutrient Setup, Lighting Install, Irrigation Test, Sensor Deploy
env_nodes = [EC, NS, LI, IT, SDp]
env_po = StrictPartialOrder(nodes=env_nodes)
# These are concurrent so no edges

# Waste plan and Pest Control (can be concurrent with some activity)
waste_pest_po = StrictPartialOrder(nodes=[WP, PC])

# Energy audit and staff training, training after audit
energy_staff_po = StrictPartialOrder(nodes=[EA, ST])
energy_staff_po.order.add_edge(EA, ST)

# Data setup and yield monitoring in sequence
data_yield_po = StrictPartialOrder(nodes=[DS, YM])
data_yield_po.order.add_edge(DS, YM)

# Logistics sync after yield monitor
logistics_po = StrictPartialOrder(nodes=[YM, LS])
logistics_po.order.add_edge(YM, LS)

# Maintenance plan after logistics
maint_po = StrictPartialOrder(nodes=[LS, MP])
maint_po.order.add_edge(LS, MP)

# Combine all top-level POs into one PO

# Nodes collection
nodes = [
    init_po,
    build_po,
    env_po,
    waste_pest_po,
    energy_staff_po,
    data_yield_po,
    logistics_po,
    maint_po,
]

root = StrictPartialOrder(nodes=nodes)

# Add dependencies between the parts

# After initial assessment and planning -> modular build (already inside build_po depends on SD and PA)
# To connect initial assessment Po with build_po:
root.order.add_edge(init_po, build_po)

# Modular build must finish before environmental setup starts
root.order.add_edge(build_po, env_po)

# Environmental setup before waste & pest control and energy audit & staff training
root.order.add_edge(env_po, waste_pest_po)
root.order.add_edge(env_po, energy_staff_po)

# Waste & pest control and energy_staff can run concurrently, no order needed

# Both waste_pest_po and energy_staff_po before data setup & yield monitor
root.order.add_edge(waste_pest_po, data_yield_po)
root.order.add_edge(energy_staff_po, data_yield_po)

# Data_yield_po before logistics_po
root.order.add_edge(data_yield_po, logistics_po)

# Logistics_po before maintenance
root.order.add_edge(logistics_po, maint_po)