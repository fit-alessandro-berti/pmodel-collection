# Generated from: bf70ebf0-094f-4f21-bf8b-69e865a1ee27.json
# Description: This process involves transforming underutilized urban rooftops into sustainable farming spaces that produce fresh produce for local communities. It includes initial site assessment, structural analysis, sourcing eco-friendly materials, soil preparation with organic compost, installing modular hydroponic systems, setting up rainwater harvesting, integrating renewable energy sources, training local workers on urban agriculture techniques, implementing pest control using natural methods, scheduling crop cycles to maximize yield, conducting regular maintenance and monitoring plant health, facilitating community engagement workshops, managing produce distribution channels, and evaluating environmental impact to ensure ongoing sustainability and scalability of the rooftop farms.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Assess = Transition(label='Site Assess')
Structure_Check = Transition(label='Structure Check')
Material_Sourcing = Transition(label='Material Sourcing')
Soil_Prep = Transition(label='Soil Prep')
Hydroponic_Install = Transition(label='Hydroponic Install')
Water_Harvest = Transition(label='Water Harvest')
Energy_Setup = Transition(label='Energy Setup')
Worker_Training = Transition(label='Worker Training')
Pest_Control = Transition(label='Pest Control')
Crop_Scheduling = Transition(label='Crop Scheduling')
Maintenance = Transition(label='Maintenance')
Health_Monitor = Transition(label='Health Monitor')
Community_Workshop = Transition(label='Community Workshop')
Produce_Distrib = Transition(label='Produce Distrib')
Impact_Review = Transition(label='Impact Review')

# The process is mostly sequential based on the description:
# Site Assess → Structure Check → Material Sourcing → Soil Prep → Hydroponic Install → Water Harvest → Energy Setup
# → Worker Training → Pest Control → Crop Scheduling → Maintenance → Health Monitor → Community Workshop
# → Produce Distrib → Impact Review

nodes = [
    Site_Assess, Structure_Check, Material_Sourcing, Soil_Prep,
    Hydroponic_Install, Water_Harvest, Energy_Setup, Worker_Training,
    Pest_Control, Crop_Scheduling, Maintenance, Health_Monitor,
    Community_Workshop, Produce_Distrib, Impact_Review
]

root = StrictPartialOrder(nodes=nodes)

root.order.add_edge(Site_Assess, Structure_Check)
root.order.add_edge(Structure_Check, Material_Sourcing)
root.order.add_edge(Material_Sourcing, Soil_Prep)
root.order.add_edge(Soil_Prep, Hydroponic_Install)
root.order.add_edge(Hydroponic_Install, Water_Harvest)
root.order.add_edge(Water_Harvest, Energy_Setup)
root.order.add_edge(Energy_Setup, Worker_Training)
root.order.add_edge(Worker_Training, Pest_Control)
root.order.add_edge(Pest_Control, Crop_Scheduling)
root.order.add_edge(Crop_Scheduling, Maintenance)
root.order.add_edge(Maintenance, Health_Monitor)
root.order.add_edge(Health_Monitor, Community_Workshop)
root.order.add_edge(Community_Workshop, Produce_Distrib)
root.order.add_edge(Produce_Distrib, Impact_Review)