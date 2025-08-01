# Generated from: 7f37c0a9-fb27-4443-a674-82d1319b8c65.json
# Description: This process details the comprehensive steps required to establish a sustainable urban rooftop farm on a commercial building. It involves initial site assessment, structural analysis, microclimate evaluation, soil-less media selection, modular bed construction, automated irrigation installation, crop selection based on local demand, integration of renewable energy sources, pest management planning, community engagement for education, regular monitoring of plant health, data-driven yield optimization, nutrient cycling strategies, waste composting, and final certification for organic produce sales. Each step ensures that the farm is both ecologically responsible and economically viable, blending advanced agritech with urban infrastructure constraints to create a robust urban agriculture solution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Assess = Transition(label='Site Assess')
Structure_Test = Transition(label='Structure Test')
Climate_Scan = Transition(label='Climate Scan')
Media_Select = Transition(label='Media Select')
Bed_Construct = Transition(label='Bed Construct')
Irrigation_Setup = Transition(label='Irrigation Setup')
Crop_Choose = Transition(label='Crop Choose')
Energy_Integrate = Transition(label='Energy Integrate')
Pest_Plan = Transition(label='Pest Plan')
Community_Engage = Transition(label='Community Engage')
Health_Monitor = Transition(label='Health Monitor')
Yield_Optimize = Transition(label='Yield Optimize')
Nutrient_Cycle = Transition(label='Nutrient Cycle')
Waste_Compost = Transition(label='Waste Compost')
Organic_Certify = Transition(label='Organic Certify')

# Build the partially ordered workflow
# Logical ordering based on the description:
# Initial assessment steps (Site Assess, Structure Test, Climate Scan) concurrent or sequential?
# They seem to be initial assessments; as site and structural and climate can be done overlapping or some ordering
# Let's order: Site Assess --> Structure Test and Site Assess --> Climate Scan (both after site assess)
# Then Media Select and Bed Construct (after Structure Test and Climate Scan)
# Irrigation Setup depends on Bed Construct
# Crop Choose depends on Irrigation Setup
# Energy Integrate and Pest Plan can be done concurrently after Crop Choose
# Community Engage depends on Pest Plan
# Health Monitor after Community Engage
# Yield Optimize after Health Monitor
# Nutrient Cycle and Waste Compost can be done concurrently after Yield Optimize
# Finally Organic Certify after Nutrient Cycle and Waste Compost

# Nodes list
nodes = [
    Site_Assess,
    Structure_Test,
    Climate_Scan,
    Media_Select,
    Bed_Construct,
    Irrigation_Setup,
    Crop_Choose,
    Energy_Integrate,
    Pest_Plan,
    Community_Engage,
    Health_Monitor,
    Yield_Optimize,
    Nutrient_Cycle,
    Waste_Compost,
    Organic_Certify
]

root = StrictPartialOrder(nodes=nodes)

# Add edges according to above reasoning

# Initial assessment ordering
root.order.add_edge(Site_Assess, Structure_Test)
root.order.add_edge(Site_Assess, Climate_Scan)

# Media Select after Structure Test and Climate Scan
root.order.add_edge(Structure_Test, Media_Select)
root.order.add_edge(Climate_Scan, Media_Select)

# Bed Construct after Media Select
root.order.add_edge(Media_Select, Bed_Construct)

# Irrigation Setup after Bed Construct
root.order.add_edge(Bed_Construct, Irrigation_Setup)

# Crop Choose after Irrigation Setup
root.order.add_edge(Irrigation_Setup, Crop_Choose)

# Energy Integrate and Pest Plan both after Crop Choose (concurrent)
root.order.add_edge(Crop_Choose, Energy_Integrate)
root.order.add_edge(Crop_Choose, Pest_Plan)

# Community Engage after Pest Plan
root.order.add_edge(Pest_Plan, Community_Engage)

# Health Monitor after Community Engage
root.order.add_edge(Community_Engage, Health_Monitor)

# Yield Optimize after Health Monitor
root.order.add_edge(Health_Monitor, Yield_Optimize)

# Nutrient Cycle and Waste Compost after Yield Optimize (concurrent)
root.order.add_edge(Yield_Optimize, Nutrient_Cycle)
root.order.add_edge(Yield_Optimize, Waste_Compost)

# Organic Certify after Nutrient Cycle and Waste Compost
root.order.add_edge(Nutrient_Cycle, Organic_Certify)
root.order.add_edge(Waste_Compost, Organic_Certify)