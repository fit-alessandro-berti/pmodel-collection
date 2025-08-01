# Generated from: e2e48eb8-5a65-4447-8f8f-eed1c35c7e21.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm in a densely populated city. It includes site analysis, structural assessment, microclimate evaluation, soil preparation with hydroponic integration, seed selection tailored to urban conditions, installation of automated irrigation and nutrient delivery systems, pest monitoring using AI-driven sensors, community engagement for resource sharing, regulatory compliance checks, and the establishment of a local distribution network for produce. The process ensures optimization of limited space, maximizes yield through technology, and fosters urban food security by integrating environmental, technical, and social considerations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site          = Transition(label='Site Survey')
struct        = Transition(label='Structural Check')
climate       = Transition(label='Climate Study')
soil          = Transition(label='Soil Prep')
seed          = Transition(label='Seed Selection')
irrigation    = Transition(label='Irrigation Setup')
nutrient      = Transition(label='Nutrient Mix')
sensor        = Transition(label='Sensor Install')
pest          = Transition(label='Pest Monitor')
data          = Transition(label='Data Analysis')
regulation    = Transition(label='Regulation Review')
community     = Transition(label='Community Meet')
harvest       = Transition(label='Harvest Plan')
packaging     = Transition(label='Packaging Design')
distribution  = Transition(label='Distribution Map')
feedback      = Transition(label='Feedback Loop')
maintenance   = Transition(label='Maintenance Schedule')

# Define the improvement loop: after distribution, you may run feedback & maintenance, then re-distribute
B = StrictPartialOrder(nodes=[feedback, maintenance])
B.order.add_edge(feedback, maintenance)

loop = OperatorPOWL(operator=Operator.LOOP, children=[distribution, B])

# Assemble the main partial order
root = StrictPartialOrder(
    nodes=[
        site, struct, climate, soil,
        seed, irrigation, nutrient, sensor,
        pest, data, regulation, community,
        harvest, packaging, loop
    ]
)

# Add control-flow edges
root.order.add_edge(site, struct)
root.order.add_edge(struct, climate)
root.order.add_edge(climate, soil)

root.order.add_edge(soil, seed)
root.order.add_edge(soil, irrigation)
root.order.add_edge(soil, nutrient)

root.order.add_edge(irrigation, sensor)
root.order.add_edge(nutrient, sensor)
root.order.add_edge(sensor, pest)

root.order.add_edge(pest, data)
root.order.add_edge(pest, community)
root.order.add_edge(pest, regulation)

root.order.add_edge(data, harvest)
root.order.add_edge(community, harvest)
root.order.add_edge(regulation, harvest)

root.order.add_edge(harvest, packaging)
root.order.add_edge(packaging, loop)