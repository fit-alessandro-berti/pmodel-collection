# Generated from: 57f5a3b5-b1f1-4c86-ae30-8a1cdb0c7200.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming system within a repurposed industrial building. It involves site analysis, environmental control installation, hydroponic system setup, seed selection, nutrient management, and continuous monitoring to optimize crop yield in limited urban spaces. The process also includes integration of IoT sensors for real-time data collection, pest control management using bio-agents, employee training for system operation, and coordination with local distributors for efficient produce delivery. Additionally, it covers waste recycling protocols to minimize environmental impact and the implementation of energy-efficient lighting and climate control systems to ensure sustainable operation throughout varied seasonal conditions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ss = Transition(label='Site Survey')
dl = Transition(label='Design Layout')
hvac = Transition(label='Install HVAC')
ea = Transition(label='Energy Audit')
setup = Transition(label='Setup Hydroponics')
iot = Transition(label='IoT Integration')
seed = Transition(label='Seed Selection')
nutrient = Transition(label='Nutrient Mix')
train = Transition(label='Employee Train')
monitor = Transition(label='Monitor Growth')
pest = Transition(label='Pest Control')
waste = Transition(label='Waste Recycle')
hp = Transition(label='Harvest Plan')
pack = Transition(label='Packaging Prep')
sync = Transition(label='Distributor Sync')

# Parallel installation of HVAC and energy audit
install_order = StrictPartialOrder(nodes=[hvac, ea])

# Parallel preparation of seed and nutrient mix
seed_order = StrictPartialOrder(nodes=[seed, nutrient])

# Maintenance loop: monitor growth, then repeat pest control & waste recycle
maint_iter = StrictPartialOrder(nodes=[pest, waste])
loop_maint = OperatorPOWL(operator=Operator.LOOP, children=[monitor, maint_iter])

# Assemble the overall workflow
root = StrictPartialOrder(nodes=[
    ss, dl, install_order, setup, iot, seed_order,
    train, loop_maint, hp, pack, sync
])

# Define the partial order edges
root.order.add_edge(ss, dl)
root.order.add_edge(dl, install_order)
root.order.add_edge(install_order, setup)
root.order.add_edge(setup, iot)
root.order.add_edge(iot, seed_order)
root.order.add_edge(seed_order, train)
root.order.add_edge(train, loop_maint)
root.order.add_edge(loop_maint, hp)
root.order.add_edge(hp, pack)
root.order.add_edge(pack, sync)