# Generated from: a4e1efc0-519d-4794-a5d8-e4f1a96c01c2.json
# Description: This process outlines the complex and atypical steps involved in setting up an urban vertical farm in a densely populated city environment. It includes site assessment, modular structure design, hydroponic system integration, environmental control calibration, crop selection based on microclimate data, seed germination scheduling, nutrient solution formulation, pest monitoring with AI sensors, automated harvesting preparation, waste recycling workflows, market demand analysis, supply chain synchronization, energy consumption optimization, community engagement initiatives, and regulatory compliance verification to ensure sustainable and profitable urban agriculture operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Assessment = Transition(label='Site Assessment')
Structure_Design = Transition(label='Structure Design')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Env_Control = Transition(label='Env Control')
Crop_Selection = Transition(label='Crop Selection')
Seed_Scheduling = Transition(label='Seed Scheduling')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Monitoring = Transition(label='Pest Monitoring')
Harvest_Prep = Transition(label='Harvest Prep')
Waste_Recycling = Transition(label='Waste Recycling')
Market_Analysis = Transition(label='Market Analysis')
Supply_Sync = Transition(label='Supply Sync')
Energy_Optimize = Transition(label='Energy Optimize')
Community_Engage = Transition(label='Community Engage')
Compliance_Check = Transition(label='Compliance Check')

# Construct the partial order reflecting the logical or typical flow in the described process

nodes = [
    Site_Assessment,
    Structure_Design,
    Hydroponic_Setup,
    Env_Control,
    Crop_Selection,
    Seed_Scheduling,
    Nutrient_Mix,
    Pest_Monitoring,
    Harvest_Prep,
    Waste_Recycling,
    Market_Analysis,
    Supply_Sync,
    Energy_Optimize,
    Community_Engage,
    Compliance_Check
]

root = StrictPartialOrder(nodes=nodes)

# Site Assessment → Structure Design → Hydroponic Setup → Env Control → Crop Selection
root.order.add_edge(Site_Assessment, Structure_Design)
root.order.add_edge(Structure_Design, Hydroponic_Setup)
root.order.add_edge(Hydroponic_Setup, Env_Control)
root.order.add_edge(Env_Control, Crop_Selection)

# Crop Selection → Seed Scheduling → Nutrient Mix
root.order.add_edge(Crop_Selection, Seed_Scheduling)
root.order.add_edge(Seed_Scheduling, Nutrient_Mix)

# Nutrient Mix → Pest Monitoring → Harvest Prep
root.order.add_edge(Nutrient_Mix, Pest_Monitoring)
root.order.add_edge(Pest_Monitoring, Harvest_Prep)

# Harvest Prep → Waste Recycling (can be concurrent with Market Analysis)
root.order.add_edge(Harvest_Prep, Waste_Recycling)

# Market Analysis → Supply Sync → Energy Optimize
root.order.add_edge(Market_Analysis, Supply_Sync)
root.order.add_edge(Supply_Sync, Energy_Optimize)

# Waste Recycling and Market Analysis start after Harvest Prep (Waste Recycling depends on Harvest Prep)
# Since Market Analysis is independent, but conceptually after Harvest Prep we order Waste Recycling and Market Analysis running concurrently:
root.order.add_edge(Harvest_Prep, Market_Analysis)

# Energy Optimize → Community Engage → Compliance Check
root.order.add_edge(Energy_Optimize, Community_Engage)
root.order.add_edge(Community_Engage, Compliance_Check)