# Generated from: 01876e64-9333-4e00-9384-7cf232147d5d.json
# Description: This process outlines the comprehensive steps required to establish and operate an urban vertical farming facility within a repurposed industrial building. It involves initial site analysis, structural modification, installation of climate control and hydroponic systems, integration of IoT sensors for real-time monitoring, seed selection and planting, nutrient delivery optimization, pest management using biological controls, automated harvesting, data-driven yield analysis, packaging, and distribution logistics tailored for local markets. The process emphasizes sustainability through energy-efficient practices and waste recycling, ensuring minimal environmental impact while maximizing crop output and quality in limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Structural_Assess = Transition(label='Structural Assess')
Climate_Setup = Transition(label='Climate Setup')
Hydroponic_Install = Transition(label='Hydroponic Install')
Sensor_Network = Transition(label='Sensor Network')
Seed_Selection = Transition(label='Seed Selection')
Planting_Phase = Transition(label='Planting Phase')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Control = Transition(label='Pest Control')
Growth_Monitor = Transition(label='Growth Monitor')
Automated_Harvest = Transition(label='Automated Harvest')
Yield_Analysis = Transition(label='Yield Analysis')
Packaging_Prep = Transition(label='Packaging Prep')
Local_Dispatch = Transition(label='Local Dispatch')
Waste_Recycling = Transition(label='Waste Recycling')
Energy_Audit = Transition(label='Energy Audit')

# Setup Phases partial order
setup_phases = StrictPartialOrder(nodes=[
    Site_Survey,
    Structural_Assess,
    Climate_Setup,
    Hydroponic_Install,
    Sensor_Network,
    Energy_Audit,
    Waste_Recycling
])
setup_phases.order.add_edge(Site_Survey, Structural_Assess)
setup_phases.order.add_edge(Structural_Assess, Climate_Setup)
setup_phases.order.add_edge(Climate_Setup, Hydroponic_Install)
setup_phases.order.add_edge(Hydroponic_Install, Sensor_Network)
# Energy Audit and Waste Recycling run concurrently after Sensor Network 
setup_phases.order.add_edge(Sensor_Network, Energy_Audit)
setup_phases.order.add_edge(Sensor_Network, Waste_Recycling)

# Production phases partial order (planting to automated harvest)
production_phases = StrictPartialOrder(nodes=[
    Seed_Selection,
    Planting_Phase,
    Nutrient_Mix,
    Pest_Control,
    Growth_Monitor,
    Automated_Harvest
])
production_phases.order.add_edge(Seed_Selection, Planting_Phase)
production_phases.order.add_edge(Planting_Phase, Nutrient_Mix)
production_phases.order.add_edge(Nutrient_Mix, Pest_Control)
production_phases.order.add_edge(Pest_Control, Growth_Monitor)
production_phases.order.add_edge(Growth_Monitor, Automated_Harvest)

# Post-harvest phases partial order (yield analysis to local dispatch)
post_harvest = StrictPartialOrder(nodes=[
    Yield_Analysis,
    Packaging_Prep,
    Local_Dispatch
])
post_harvest.order.add_edge(Yield_Analysis, Packaging_Prep)
post_harvest.order.add_edge(Packaging_Prep, Local_Dispatch)

# Combine production and post-harvest in order
prod_post = StrictPartialOrder(nodes=[production_phases, post_harvest])
prod_post.order.add_edge(production_phases, post_harvest)

# Overall flow: setup_phases -> prod_post
root = StrictPartialOrder(nodes=[setup_phases, prod_post])
root.order.add_edge(setup_phases, prod_post)