# Generated from: e209ef5f-0b28-49f8-93ad-c3bad34b6d72.json
# Description: This process outlines a complex and atypical adaptive urban farming cycle designed for maximizing crop yield in limited city spaces while integrating real-time environmental data and community input. It begins with soil analysis and urban site mapping, followed by modular bed setup and crop selection optimized for microclimates. Continuous sensor monitoring informs automated irrigation and nutrient delivery, while manual pest scouting combines with AI-driven pest prediction. Community workshops guide seasonal crop rotation planning and resource sharing. Waste composting and water recycling close the loop, enhancing sustainability. Data analytics assess productivity and help refine future cycles, ensuring resilience and scalability in urban agriculture amidst fluctuating environmental conditions and social dynamics.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the initial fixed activities
soil         = Transition(label="Soil Analyze")
site         = Transition(label="Site Mapping")
bed          = Transition(label="Bed Setup")
crop         = Transition(label="Crop Select")
sensor       = Transition(label="Sensor Deploy")
yield_report = Transition(label="Yield Report")

# Labels of the dynamic (iterative) activities
dynamic_labels = [
    "Irrigation Adjust", "Nutrient Feed",
    "Pest Scouting",     "Pest Predict",
    "Workshop Host",     "Crop Rotate",     "Resource Share",
    "Waste Compost",     "Water Recycle",
    "Data Analyze",      "Cycle Refine"
]

# Build the first body of the loop
body0_nodes = {lbl: Transition(label=lbl) for lbl in dynamic_labels}
body0 = StrictPartialOrder(nodes=list(body0_nodes.values()))
# Define a small partial order among them
body0.order.add_edge(body0_nodes["Irrigation Adjust"], body0_nodes["Nutrient Feed"])
body0.order.add_edge(body0_nodes["Pest Scouting"],      body0_nodes["Pest Predict"])
body0.order.add_edge(body0_nodes["Workshop Host"],      body0_nodes["Crop Rotate"])
body0.order.add_edge(body0_nodes["Workshop Host"],      body0_nodes["Resource Share"])
body0.order.add_edge(body0_nodes["Waste Compost"],      body0_nodes["Water Recycle"])
body0.order.add_edge(body0_nodes["Data Analyze"],       body0_nodes["Cycle Refine"])

# Build the redo‐body of the loop (same structure, separate nodes)
body1_nodes = {lbl: Transition(label=lbl) for lbl in dynamic_labels}
body1 = StrictPartialOrder(nodes=list(body1_nodes.values()))
body1.order.add_edge(body1_nodes["Irrigation Adjust"], body1_nodes["Nutrient Feed"])
body1.order.add_edge(body1_nodes["Pest Scouting"],      body1_nodes["Pest Predict"])
body1.order.add_edge(body1_nodes["Workshop Host"],      body1_nodes["Crop Rotate"])
body1.order.add_edge(body1_nodes["Workshop Host"],      body1_nodes["Resource Share"])
body1.order.add_edge(body1_nodes["Waste Compost"],      body1_nodes["Water Recycle"])
body1.order.add_edge(body1_nodes["Data Analyze"],       body1_nodes["Cycle Refine"])

# Define the loop operator: after sensor deploy, we enter the loop of adaptive tasks
loop = OperatorPOWL(operator=Operator.LOOP, children=[body0, body1])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[soil, site, bed, crop, sensor, loop, yield_report])
root.order.add_edge(soil,  bed)
root.order.add_edge(site,  bed)
root.order.add_edge(soil,  crop)
root.order.add_edge(site,  crop)
root.order.add_edge(bed,   sensor)
root.order.add_edge(crop,  sensor)
root.order.add_edge(sensor, loop)
root.order.add_edge(loop,   yield_report)

# 'root' now holds the complete POWL model