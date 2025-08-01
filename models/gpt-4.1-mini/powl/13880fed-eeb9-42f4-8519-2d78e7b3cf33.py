# Generated from: 13880fed-eeb9-42f4-8519-2d78e7b3cf33.json
# Description: This process involves establishing a multi-tiered vertical farm within an urban environment, integrating advanced hydroponic systems, renewable energy sources, and AI-driven environmental controls. It requires site assessment, modular structure installation, nutrient solution formulation, crop selection tailored to microclimates, and continuous monitoring for optimal growth. Post-harvest activities include automated sorting, packaging, and distribution logistics coordinated with local markets. The process ensures sustainability by recycling water and organic waste while adapting dynamically to urban constraints and demand fluctuations, ultimately producing fresh produce with minimal carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Permit_Acquire = Transition(label='Permit Acquire')
Structure_Build = Transition(label='Structure Build')
System_Install = Transition(label='System Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Select = Transition(label='Crop Select')
Seed_Plant = Transition(label='Seed Plant')
Environment_Tune = Transition(label='Environment Tune')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Crop = Transition(label='Harvest Crop')
Sort_Package = Transition(label='Sort Package')
Market_Coordinate = Transition(label='Market Coordinate')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Manage = Transition(label='Energy Manage')
Data_Analyze = Transition(label='Data Analyze')

# Pre-construction phase: Site Survey -> Design Layout -> Permit Acquire (strict order)
pre_construction = StrictPartialOrder(
    nodes=[Site_Survey, Design_Layout, Permit_Acquire]
)
pre_construction.order.add_edge(Site_Survey, Design_Layout)
pre_construction.order.add_edge(Design_Layout, Permit_Acquire)

# Construction phase: Structure Build -> System Install (strict order)
construction = StrictPartialOrder(
    nodes=[Structure_Build, System_Install]
)
construction.order.add_edge(Structure_Build, System_Install)

# Crop preparation phase: Nutrient Mix, Crop Select, Seed Plant (Nutrient Mix and Crop Select concurrent, both before Seed Plant)
crop_prep = StrictPartialOrder(
    nodes=[Nutrient_Mix, Crop_Select, Seed_Plant]
)
crop_prep.order.add_edge(Nutrient_Mix, Seed_Plant)
crop_prep.order.add_edge(Crop_Select, Seed_Plant)

# Environment controls phase: Environment Tune, Energy Manage, Data Analyze
# Energy Manage and Data Analyze concurrent; Environment Tune happens before Growth Monitor
env_controls = StrictPartialOrder(
    nodes=[Environment_Tune, Energy_Manage, Data_Analyze]
)
# No order edges between Energy Manage and Data Analyze (concurrent)

# The main growing monitor with pest control loop:
# LOOP between (Growth Monitor) and (Pest Control)
pest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Growth_Monitor, Pest_Control]
)

# Post-harvest phase: Harvest Crop -> Sort Package -> Market Coordinate (strict order)
post_harvest = StrictPartialOrder(
    nodes=[Harvest_Crop, Sort_Package, Market_Coordinate]
)
post_harvest.order.add_edge(Harvest_Crop, Sort_Package)
post_harvest.order.add_edge(Sort_Package, Market_Coordinate)

# Sustainability actions can run concurrently with post-harvest or other last phases:
# Waste Recycle can happen concurrently with Market Coordinate and Energy Manage
sustainability = StrictPartialOrder(
    nodes=[Waste_Recycle]
)
# No order edges needed

# Compose the full model:
# Order:
# pre_construction -> construction -> crop_prep -> env_controls -> pest_loop -> post_harvest
# sustainability runs concurrently with post_harvest and later

root = StrictPartialOrder(
    nodes=[
        pre_construction,
        construction,
        crop_prep,
        env_controls,
        pest_loop,
        post_harvest,
        sustainability
    ]
)

# Add edges to represent the sequence of phases
root.order.add_edge(pre_construction, construction)
root.order.add_edge(construction, crop_prep)
root.order.add_edge(crop_prep, env_controls)
root.order.add_edge(env_controls, pest_loop)
root.order.add_edge(pest_loop, post_harvest)
# sustainability concurrent with post_harvest, no edges
