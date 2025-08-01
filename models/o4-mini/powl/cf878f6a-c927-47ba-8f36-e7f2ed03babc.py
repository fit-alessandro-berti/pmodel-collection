# Generated from: cf878f6a-c927-47ba-8f36-e7f2ed03babc.json
# Description: This process outlines the establishment of a vertical farming system within an urban environment, integrating multiple disciplines such as architecture, agriculture, technology, and logistics. It begins with site assessment and urban zoning compliance, followed by modular farm design focusing on maximizing space efficiency and energy use. Procurement of specialized hydroponic equipment and LED lighting systems ensures optimal plant growth. Installation includes automated climate control systems and sensor networks for real-time monitoring. Crop selection is based on local market demand and growth cycles. Seed germination and nutrient solution preparation are carefully managed to enhance yield. Continuous data analysis drives adjustments in environmental parameters. Harvesting employs robotic assistance to minimize labor costs and contamination risks. Post-harvest processing includes quality grading, packaging using sustainable materials, and cold chain logistics coordination. Marketing leverages digital platforms targeting local consumers and restaurants. The process concludes with waste recycling protocols and periodic system audits to ensure sustainability and scalability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site    = Transition(label='Site Assess')
zoning  = Transition(label='Zoning Check')
design  = Transition(label='Design Farm')
procure = Transition(label='Procure Gear')
install = Transition(label='Install Systems')
setup   = Transition(label='Setup Sensors')
select  = Transition(label='Select Crops')
prepare = Transition(label='Prepare Seeds')
mix     = Transition(label='Mix Nutrients')
monitor = Transition(label='Monitor Growth')
adjust  = Transition(label='Adjust Climate')
harvest = Transition(label='Robotic Harvest')
grade   = Transition(label='Grade Quality')
pack    = Transition(label='Pack Produce')
logistics = Transition(label='Manage Logistics')
market  = Transition(label='Market Products')
recycle = Transition(label='Recycle Waste')
audit   = Transition(label='Audit Systems')

# Model the monitoring–adjustment loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, adjust])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site, zoning, design, procure, install, setup, select,
    prepare, mix, loop, harvest, grade, pack,
    logistics, market, recycle, audit
])

# Define the sequence flow
root.order.add_edge(site, zoning)
root.order.add_edge(zoning, design)
root.order.add_edge(design, procure)
root.order.add_edge(procure, install)
root.order.add_edge(install, setup)
root.order.add_edge(setup, select)
root.order.add_edge(select, prepare)
root.order.add_edge(prepare, mix)
root.order.add_edge(mix, loop)
root.order.add_edge(loop, harvest)
root.order.add_edge(harvest, grade)
root.order.add_edge(grade, pack)
root.order.add_edge(pack, logistics)
root.order.add_edge(logistics, market)
root.order.add_edge(market, recycle)
root.order.add_edge(recycle, audit)