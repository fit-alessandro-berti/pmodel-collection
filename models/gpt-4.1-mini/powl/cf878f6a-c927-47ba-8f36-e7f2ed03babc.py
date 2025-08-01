# Generated from: cf878f6a-c927-47ba-8f36-e7f2ed03babc.json
# Description: This process outlines the establishment of a vertical farming system within an urban environment, integrating multiple disciplines such as architecture, agriculture, technology, and logistics. It begins with site assessment and urban zoning compliance, followed by modular farm design focusing on maximizing space efficiency and energy use. Procurement of specialized hydroponic equipment and LED lighting systems ensures optimal plant growth. Installation includes automated climate control systems and sensor networks for real-time monitoring. Crop selection is based on local market demand and growth cycles. Seed germination and nutrient solution preparation are carefully managed to enhance yield. Continuous data analysis drives adjustments in environmental parameters. Harvesting employs robotic assistance to minimize labor costs and contamination risks. Post-harvest processing includes quality grading, packaging using sustainable materials, and cold chain logistics coordination. Marketing leverages digital platforms targeting local consumers and restaurants. The process concludes with waste recycling protocols and periodic system audits to ensure sustainability and scalability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Assess = Transition(label='Site Assess')
Zoning_Check = Transition(label='Zoning Check')
Design_Farm = Transition(label='Design Farm')
Procure_Gear = Transition(label='Procure Gear')
Install_Systems = Transition(label='Install Systems')
Setup_Sensors = Transition(label='Setup Sensors')
Select_Crops = Transition(label='Select Crops')
Prepare_Seeds = Transition(label='Prepare Seeds')
Mix_Nutrients = Transition(label='Mix Nutrients')
Monitor_Growth = Transition(label='Monitor Growth')
Adjust_Climate = Transition(label='Adjust Climate')
Robotic_Harvest = Transition(label='Robotic Harvest')
Grade_Quality = Transition(label='Grade Quality')
Pack_Produce = Transition(label='Pack Produce')
Manage_Logistics = Transition(label='Manage Logistics')
Market_Products = Transition(label='Market Products')
Recycle_Waste = Transition(label='Recycle Waste')
Audit_Systems = Transition(label='Audit Systems')

# Model continuous monitoring and adjustment as a loop:
# LOOP(body=Monitor Growth, redo=Adjust Climate)
# The semantics: execute Monitor Growth, then choose to either exit loop or execute Adjust Climate then Monitor Growth again
monitor_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[Monitor_Growth, Adjust_Climate])

# Procurement and installation are sequential, with Setup Sensors concurrent with Install Systems (usually sensor setup embedded, but let's order)
# For safety, treat Setup Sensors as after Install Systems
# Site Assess and Zoning Check are sequential
# Design Farm after Zoning Check
# Procurement after Design Farm
# Install Systems after Procure Gear
# Setup Sensors after Install Systems
# Select Crops after Setup Sensors
# Prepare Seeds and Mix Nutrients can be concurrent after Select Crops
# After preparation activities, loop on monitoring climate and adjustment
# After monitoring, proceed to harvesting, grading, packing, logistics, marketing
# Recycling and audit happen finally, both concurrent

# Concurrent node for Prepare Seeds and Mix Nutrients
prep_parallel = StrictPartialOrder(nodes=[Prepare_Seeds, Mix_Nutrients])  # no order between seeds and nutrients

# Concurrent node for Recycle Waste and Audit Systems at the end
cleanup_parallel = StrictPartialOrder(nodes=[Recycle_Waste, Audit_Systems])  # no order between waste recycling and audit

# Build the partial order nodes list
nodes = [
    Site_Assess,
    Zoning_Check,
    Design_Farm,
    Procure_Gear,
    Install_Systems,
    Setup_Sensors,
    Select_Crops,
    prep_parallel,
    monitor_adjust_loop,
    Robotic_Harvest,
    Grade_Quality,
    Pack_Produce,
    Manage_Logistics,
    Market_Products,
    cleanup_parallel
]

root = StrictPartialOrder(nodes=nodes)

# Define order edges according to the described process

# Site Assess --> Zoning Check
root.order.add_edge(Site_Assess, Zoning_Check)
# Zoning Check --> Design Farm
root.order.add_edge(Zoning_Check, Design_Farm)
# Design Farm --> Procure Gear
root.order.add_edge(Design_Farm, Procure_Gear)
# Procure Gear --> Install Systems
root.order.add_edge(Procure_Gear, Install_Systems)
# Install Systems --> Setup Sensors
root.order.add_edge(Install_Systems, Setup_Sensors)
# Setup Sensors --> Select Crops
root.order.add_edge(Setup_Sensors, Select_Crops)
# Select Crops --> Prepare Seeds (in prep_parallel)
root.order.add_edge(Select_Crops, prep_parallel)
# After prep_parallel --> monitor_adjust_loop
root.order.add_edge(prep_parallel, monitor_adjust_loop)
# After monitor_adjust_loop --> Robotic Harvest
root.order.add_edge(monitor_adjust_loop, Robotic_Harvest)
# Robotic Harvest --> Grade Quality
root.order.add_edge(Robotic_Harvest, Grade_Quality)
# Grade Quality --> Pack Produce
root.order.add_edge(Grade_Quality, Pack_Produce)
# Pack Produce --> Manage Logistics
root.order.add_edge(Pack_Produce, Manage_Logistics)
# Manage Logistics --> Market Products
root.order.add_edge(Manage_Logistics, Market_Products)
# Market Products --> cleanup_parallel (Recycle Waste and Audit Systems)
root.order.add_edge(Market_Products, cleanup_parallel)