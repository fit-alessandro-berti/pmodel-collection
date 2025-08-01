# Generated from: 557c0b15-285d-4b0c-9893-2ce559499eaf.json
# Description: This process outlines the planning, implementation, and optimization of an urban vertical farming system designed to maximize crop yield in limited city spaces. It begins with site analysis and environmental assessment, followed by modular unit design and material sourcing. Installation involves setting up hydroponic systems, lighting, and climate control, with ongoing monitoring of plant health and resource consumption. The process further includes automated nutrient adjustments, pest control strategies without chemicals, data analytics for yield prediction, and integration with local distribution networks. Continuous improvement cycles ensure sustainability, cost efficiency, and adaptability to changing urban conditions and crop varieties.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
site_survey       = Transition(label='Site Survey')
env_assess        = Transition(label='Env Assess')
modular_design    = Transition(label='Modular Design')
material_procure  = Transition(label='Material Procure')
hydroponic_install= Transition(label='Hydroponic Install')
light_setup       = Transition(label='Light Setup')
climate_control   = Transition(label='Climate Control')
plant_seeding     = Transition(label='Plant Seeding')
nutrient_mix      = Transition(label='Nutrient Mix')
pest_monitor      = Transition(label='Pest Monitor')
data_capture      = Transition(label='Data Capture')
yield_analyze     = Transition(label='Yield Analyze')
waste_manage      = Transition(label='Waste Manage')
local_partner     = Transition(label='Local Partner')
system_upgrade    = Transition(label='System Upgrade')
cost_review       = Transition(label='Cost Review')

# Silent transition for loop continuation
skip = SilentTransition()

# Continuous improvement subprocess (waste management, upgrades, cost review)
improvement_seq = StrictPartialOrder(nodes=[
    waste_manage,
    system_upgrade,
    cost_review
])
# no internal ordering => these can proceed in parallel

# Loop: do improvement_seq, then either exit or repeat
improvement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[improvement_seq, skip]
)

# Root partial order
root = StrictPartialOrder(nodes=[
    site_survey, env_assess,
    modular_design, material_procure,
    hydroponic_install, light_setup, climate_control,
    plant_seeding,
    nutrient_mix, pest_monitor,
    data_capture, yield_analyze,
    local_partner,
    improvement_loop
])

# Add control-flow dependencies
# Planning
root.order.add_edge(site_survey, modular_design)
root.order.add_edge(env_assess, modular_design)
root.order.add_edge(site_survey, material_procure)
root.order.add_edge(env_assess, material_procure)

# Installation
for inst in [hydroponic_install, light_setup, climate_control]:
    root.order.add_edge(modular_design, inst)
    root.order.add_edge(material_procure, inst)
    root.order.add_edge(inst, plant_seeding)

# Monitoring & initial analytics
root.order.add_edge(plant_seeding, nutrient_mix)
root.order.add_edge(plant_seeding, pest_monitor)
root.order.add_edge(nutrient_mix, data_capture)
root.order.add_edge(pest_monitor, data_capture)
root.order.add_edge(data_capture, yield_analyze)

# Distribution integration
root.order.add_edge(yield_analyze, local_partner)

# Enter continuous improvement loop
root.order.add_edge(local_partner, improvement_loop)