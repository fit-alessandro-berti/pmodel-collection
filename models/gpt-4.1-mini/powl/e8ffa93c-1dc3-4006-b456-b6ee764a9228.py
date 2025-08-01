# Generated from: e8ffa93c-1dc3-4006-b456-b6ee764a9228.json
# Description: This process outlines the complex steps required to establish an urban vertical farming system within a densely populated city environment. It involves site assessment, environmental analysis, modular structure assembly, hydroponic system integration, nutrient solution calibration, automated climate control installation, energy optimization, crop selection based on urban demand, pest management without chemicals, data-driven growth monitoring, harvest scheduling, waste recycling, community engagement, and finally, market distribution coordination. Each phase requires close collaboration between agronomists, engineers, urban planners, and supply chain experts to ensure sustainability, efficiency, and profitability in limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
site_survey = Transition(label='Site Survey')
env_analysis = Transition(label='Env Analysis')
structure_build = Transition(label='Structure Build')
hydroponics_fit = Transition(label='Hydroponics Fit')
nutrient_mix = Transition(label='Nutrient Mix')
climate_setup = Transition(label='Climate Setup')
energy_audit = Transition(label='Energy Audit')
crop_select = Transition(label='Crop Select')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
community_meet = Transition(label='Community Meet')
supply_sync = Transition(label='Supply Sync')
data_review = Transition(label='Data Review')

# Create partial order nodes list
nodes = [
    site_survey,
    env_analysis,
    structure_build,
    hydroponics_fit,
    nutrient_mix,
    climate_setup,
    energy_audit,
    crop_select,
    pest_control,
    growth_monitor,
    harvest_plan,
    waste_recycle,
    community_meet,
    supply_sync,
    data_review,
]

# Build partial order with realistic dependencies according to description.
root = StrictPartialOrder(nodes=nodes)

# Sites assessment and environment analysis first
root.order.add_edge(site_survey, env_analysis)

# Once environment is analyzed, structure can be built
root.order.add_edge(env_analysis, structure_build)

# After structure is built, hydroponics can be fitted
root.order.add_edge(structure_build, hydroponics_fit)

# Nutrient mix depends on hydroponics fitted
root.order.add_edge(hydroponics_fit, nutrient_mix)

# Climate setup and energy audit happen after nutrient mixing
root.order.add_edge(nutrient_mix, climate_setup)
root.order.add_edge(nutrient_mix, energy_audit)

# Crop selection depends on environmental analysis and can run in parallel with pest control
root.order.add_edge(env_analysis, crop_select)

# Pest control likely after hydroponics is fitted, no chemicals means integrated with crop select
root.order.add_edge(hydroponics_fit, pest_control)

# Growth monitor depends on climate, energy, crop, and pest control setup
root.order.add_edge(climate_setup, growth_monitor)
root.order.add_edge(energy_audit, growth_monitor)
root.order.add_edge(crop_select, growth_monitor)
root.order.add_edge(pest_control, growth_monitor)

# Harvest plan depends on growth monitoring
root.order.add_edge(growth_monitor, harvest_plan)

# Waste recycle and community meet can run in parallel after harvest planning
root.order.add_edge(harvest_plan, waste_recycle)
root.order.add_edge(harvest_plan, community_meet)

# Supply sync depends on community meet and waste recycle
root.order.add_edge(waste_recycle, supply_sync)
root.order.add_edge(community_meet, supply_sync)

# Data review depends on growth monitor and supply sync for decision making
root.order.add_edge(growth_monitor, data_review)
root.order.add_edge(supply_sync, data_review)