# Generated from: 590b9f33-219f-4d8c-8a2e-56c2a2c45d32.json
# Description: This process outlines the integration of vertical farming systems within urban infrastructure to optimize space usage, enhance food production, and reduce environmental impact. It involves site analysis, modular system design, automated nutrient delivery, energy optimization, and continuous monitoring. The process includes collaboration with local authorities for permits, community engagement for awareness, and adaptive maintenance strategies to ensure sustainability. Data from IoT sensors is analyzed to adjust environmental controls dynamically, while logistics management handles distribution to local markets. The approach supports circular economy principles by recycling water and organic waste, integrating renewable energy sources, and fostering urban biodiversity through green corridors. The goal is to create resilient, efficient, and scalable urban agriculture solutions tailored to diverse city landscapes.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
permit_review    = Transition(label='Permit Review')
design_layout    = Transition(label='Design Layout')
modular_build    = Transition(label='Modular Build')
sensor_install   = Transition(label='Sensor Install')
nutrient_mix     = Transition(label='Nutrient Mix')
water_cycle      = Transition(label='Water Cycle')
energy_audit     = Transition(label='Energy Audit')
iot_setup        = Transition(label='IoT Setup')
data_analyze     = Transition(label='Data Analyze')
env_control      = Transition(label='Env Control')
waste_recycle    = Transition(label='Waste Recycle')
system_maintain  = Transition(label='System Maintain')
community_meet   = Transition(label='Community Meet')
market_link      = Transition(label='Market Link')
biodiversity_plan= Transition(label='Biodiversity Plan')
renewable_sync   = Transition(label='Renewable Sync')

# Define the loop for continuous monitoring & adaptive maintenance
# Body A = data analysis
# Redo B = concurrent execution of env_control, waste_recycle, system_maintain
redo_branch = StrictPartialOrder(nodes=[env_control, waste_recycle, system_maintain])
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, redo_branch])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey, permit_review, biodiversity_plan, community_meet,
        design_layout, modular_build,
        sensor_install, nutrient_mix, water_cycle, energy_audit, iot_setup,
        renewable_sync,
        loop,
        market_link
    ]
)

# 1) Initial site analysis, collaborations & planning
root.order.add_edge(site_survey, permit_review)
root.order.add_edge(site_survey, biodiversity_plan)
root.order.add_edge(site_survey, community_meet)

# 2) Design after permits & biodiversity planning
root.order.add_edge(permit_review, design_layout)
root.order.add_edge(biodiversity_plan, design_layout)

# 3) Build phase
root.order.add_edge(design_layout, modular_build)

# 4) After build, parallel setup of systems
root.order.add_edge(modular_build, sensor_install)
root.order.add_edge(modular_build, nutrient_mix)
root.order.add_edge(modular_build, energy_audit)
root.order.add_edge(modular_build, iot_setup)

# 5) Water cycle depends on nutrient mix
root.order.add_edge(nutrient_mix, water_cycle)

# 6) Renewable integration follows energy audit
root.order.add_edge(energy_audit, renewable_sync)

# 7) Start continuous monitoring & maintenance loop only after all setups
root.order.add_edge(sensor_install, loop)
root.order.add_edge(iot_setup, loop)
root.order.add_edge(water_cycle, loop)
root.order.add_edge(renewable_sync, loop)

# 8) Once the loop exits, link to distribution logistics
root.order.add_edge(loop, market_link)