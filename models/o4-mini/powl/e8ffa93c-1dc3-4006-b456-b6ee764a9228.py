# Generated from: e8ffa93c-1dc3-4006-b456-b6ee764a9228.json
# Description: This process outlines the complex steps required to establish an urban vertical farming system within a densely populated city environment. It involves site assessment, environmental analysis, modular structure assembly, hydroponic system integration, nutrient solution calibration, automated climate control installation, energy optimization, crop selection based on urban demand, pest management without chemicals, data-driven growth monitoring, harvest scheduling, waste recycling, community engagement, and finally, market distribution coordination. Each phase requires close collaboration between agronomists, engineers, urban planners, and supply chain experts to ensure sustainability, efficiency, and profitability in limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey    = Transition(label='Site Survey')
env_analysis   = Transition(label='Env Analysis')
structure_build= Transition(label='Structure Build')
hydroponics_fit= Transition(label='Hydroponics Fit')
nutrient_mix   = Transition(label='Nutrient Mix')
climate_setup  = Transition(label='Climate Setup')
energy_audit   = Transition(label='Energy Audit')
crop_select    = Transition(label='Crop Select')
pest_control   = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan   = Transition(label='Harvest Plan')
waste_recycle  = Transition(label='Waste Recycle')
community_meet = Transition(label='Community Meet')
supply_sync    = Transition(label='Supply Sync')
data_review    = Transition(label='Data Review')

# Build a strict partial order reflecting the sequential workflow
root = StrictPartialOrder(nodes=[
    site_survey, env_analysis, structure_build, hydroponics_fit,
    nutrient_mix, climate_setup, energy_audit, crop_select,
    pest_control, growth_monitor, harvest_plan, waste_recycle,
    community_meet, supply_sync, data_review
])

# Add ordering edges
sequence = [
    site_survey, env_analysis, structure_build, hydroponics_fit,
    nutrient_mix, climate_setup, energy_audit, crop_select,
    pest_control, growth_monitor, harvest_plan, waste_recycle,
    community_meet, supply_sync, data_review
]
for src, tgt in zip(sequence, sequence[1:]):
    root.order.add_edge(src, tgt)