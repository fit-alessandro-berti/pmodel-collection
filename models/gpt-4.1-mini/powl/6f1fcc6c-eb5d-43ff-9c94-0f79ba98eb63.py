# Generated from: 6f1fcc6c-eb5d-43ff-9c94-0f79ba98eb63.json
# Description: This process involves establishing a multi-tiered urban vertical farm within a repurposed industrial building. It encompasses site analysis, environmental control system installation, hydroponic infrastructure setup, nutrient formulation, automated monitoring deployment, crop seeding, growth cycle management, pest control using integrated biological agents, harvesting, post-harvest processing, quality assurance, packaging, logistics coordination, and sustainable waste recycling. The complexity arises from integrating cutting-edge agricultural technology with urban architectural constraints, regulatory compliance, and real-time data analytics to maximize yield and minimize environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Install_HVAC = Transition(label='Install HVAC')
Setup_Hydroponics = Transition(label='Setup Hydroponics')
Formulate_Nutrients = Transition(label='Formulate Nutrients')
Deploy_Sensors = Transition(label='Deploy Sensors')
Seed_Crops = Transition(label='Seed Crops')
Monitor_Growth = Transition(label='Monitor Growth')
Apply_Biocontrol = Transition(label='Apply Biocontrol')
Harvest_Crops = Transition(label='Harvest Crops')
Process_Yield = Transition(label='Process Yield')
Quality_Check = Transition(label='Quality Check')
Package_Produce = Transition(label='Package Produce')
Arrange_Transport = Transition(label='Arrange Transport')
Recycle_Waste = Transition(label='Recycle Waste')

# Model construction according to the process description and logical order:

# Initial phase: Site Survey -> Design Layout
initial_phase = StrictPartialOrder(nodes=[Site_Survey, Design_Layout])
initial_phase.order.add_edge(Site_Survey, Design_Layout)

# Technical installations after design
install_phase = StrictPartialOrder(nodes=[Install_HVAC, Setup_Hydroponics])
install_phase.order.add_edge(Install_HVAC, Setup_Hydroponics)

# Nutrient and sensor setup after installation
nutrient_and_sensor = StrictPartialOrder(nodes=[Formulate_Nutrients, Deploy_Sensors])
nutrient_and_sensor.order.add_edge(Formulate_Nutrients, Deploy_Sensors)

# Planting and growing cycle
# Growth cycle management with monitoring and biocontrol application can be partially concurrent:
# Seed Crops -> loop: (Monitor Growth then optionally Apply Biocontrol then re-monitor or exit)
monitor = Monitor_Growth
biocontrol = Apply_Biocontrol
loop_monitor_biocontrol = OperatorPOWL(operator=Operator.LOOP, children=[monitor, biocontrol])

planting_phase = StrictPartialOrder(nodes=[Seed_Crops, loop_monitor_biocontrol])
planting_phase.order.add_edge(Seed_Crops, loop_monitor_biocontrol)

# Harvest and subsequent processing phases in sequence
harvest_phase = StrictPartialOrder(nodes=[
    Harvest_Crops,
    Process_Yield,
    Quality_Check,
    Package_Produce,
    Arrange_Transport,
    Recycle_Waste
])
harvest_phase.order.add_edge(Harvest_Crops, Process_Yield)
harvest_phase.order.add_edge(Process_Yield, Quality_Check)
harvest_phase.order.add_edge(Quality_Check, Package_Produce)
harvest_phase.order.add_edge(Package_Produce, Arrange_Transport)
harvest_phase.order.add_edge(Arrange_Transport, Recycle_Waste)

# Compose overall partial order
# Sequential dependencies:
# initial_phase -> install_phase -> nutrient_and_sensor -> planting_phase -> harvest_phase
nodes = [
    initial_phase,
    install_phase,
    nutrient_and_sensor,
    planting_phase,
    harvest_phase,
]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(initial_phase, install_phase)
root.order.add_edge(install_phase, nutrient_and_sensor)
root.order.add_edge(nutrient_and_sensor, planting_phase)
root.order.add_edge(planting_phase, harvest_phase)