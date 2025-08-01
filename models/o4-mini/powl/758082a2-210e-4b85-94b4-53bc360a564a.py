# Generated from: 758082a2-210e-4b85-94b4-53bc360a564a.json
# Description: This process involves transforming underutilized urban rooftop spaces into productive agricultural environments. It includes assessing structural integrity, designing modular planting systems, sourcing sustainable materials, integrating automated irrigation and nutrient delivery, and coordinating with local regulations. The process also covers community workshops, environmental impact assessments, pest management, and harvesting logistics to ensure a thriving, eco-friendly rooftop farm that supports local food production and urban biodiversity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
load_testing     = Transition(label='Load Testing')
design_layout    = Transition(label='Design Layout')
material_sourcing= Transition(label='Material Sourcing')
system_assembly  = Transition(label='System Assembly')
irrigation_setup = Transition(label='Irrigation Setup')
soil_preparation = Transition(label='Soil Preparation')
nutrient_mixing  = Transition(label='Nutrient Mixing')
plant_selection  = Transition(label='Plant Selection')
regulation_check = Transition(label='Regulation Check')
community_training = Transition(label='Community Training')
pest_monitoring  = Transition(label='Pest Monitoring')
waste_recycling  = Transition(label='Waste Recycling')
harvest_planning = Transition(label='Harvest Planning')
performance_review= Transition(label='Performance Review')

# Build a loop for ongoing pest monitoring and waste recycling
# LOOP(children=[A, B]) means: do A, then either exit or do B and loop back to A
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_monitoring, waste_recycling])

# Assemble the overall partial‐order workflow
nodes = [
    site_survey, load_testing, design_layout, material_sourcing, system_assembly,
    irrigation_setup, soil_preparation, nutrient_mixing, plant_selection,
    regulation_check, community_training, pest_loop,
    harvest_planning, performance_review
]
root = StrictPartialOrder(nodes=nodes)

# Add the ordering constraints
root.order.add_edge(site_survey,      load_testing)
root.order.add_edge(load_testing,     design_layout)
root.order.add_edge(design_layout,    material_sourcing)
root.order.add_edge(material_sourcing, system_assembly)
root.order.add_edge(system_assembly,  irrigation_setup)
root.order.add_edge(irrigation_setup, soil_preparation)
root.order.add_edge(soil_preparation, nutrient_mixing)
root.order.add_edge(nutrient_mixing,  plant_selection)

# After plants are in, do regulation check and community training in parallel
root.order.add_edge(plant_selection,  regulation_check)
root.order.add_edge(plant_selection,  community_training)

# Once both are done, enter the pest/waste loop
root.order.add_edge(regulation_check,  pest_loop)
root.order.add_edge(community_training, pest_loop)

# After the loop finishes, plan harvest and then review performance
root.order.add_edge(pest_loop,        harvest_planning)
root.order.add_edge(harvest_planning, performance_review)