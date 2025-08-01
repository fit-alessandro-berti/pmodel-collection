# Generated from: 64f82b1d-8541-4d8f-a3cc-ac2d4f6bee2a.json
# Description: This process outlines the adaptive urban farming cycle designed for optimizing limited city space agriculture through iterative environmental sensing, dynamic resource allocation, and community feedback integration. Beginning with soil analysis and microclimate monitoring, the system adapts water and nutrient delivery in real-time. Crop selection is continuously adjusted via AI-driven growth predictions, while pest management employs biological controls activated by sensor alerts. Harvesting schedules are coordinated with local market demands, and waste recycling integrates organic residues back into the soil. Community workshops and digital platforms gather resident input, feeding into future cycles for sustainable and responsive urban food production. This atypical yet practical approach ensures resilience and efficiency in metropolitan agronomy.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activity transitions
t1 = Transition(label='Soil Testing')
t2 = Transition(label='Climate Scan')
t3 = Transition(label='Water Allocation')
t4 = Transition(label='Nutrient Dosing')
t5 = Transition(label='Growth Prediction')
t6 = Transition(label='Crop Adjustment')
t7 = Transition(label='Pest Detection')
t8 = Transition(label='Biocontrol Release')
t9 = Transition(label='Harvest Planning')
t10 = Transition(label='Market Sync')
t11 = Transition(label='Waste Collection')
t12 = Transition(label='Compost Processing')
t13 = Transition(label='Community Feedback')
t14 = Transition(label='Workshop Hosting')
t15 = Transition(label='Data Integration')
t16 = Transition(label='Cycle Review')

# Silent transition for loop exit
skip = SilentTransition()

# Build the cycle body as a partial order
body = StrictPartialOrder(nodes=[t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16])

# Sensor readings -> resource allocation
body.order.add_edge(t1, t3)
body.order.add_edge(t2, t3)
body.order.add_edge(t1, t4)
body.order.add_edge(t2, t4)

# Resource delivery -> growth prediction
body.order.add_edge(t3, t5)
body.order.add_edge(t4, t5)

# Growth prediction -> crop adjustment
body.order.add_edge(t5, t6)

# Crop adjustment -> pest detection -> biocontrol
body.order.add_edge(t6, t7)
body.order.add_edge(t7, t8)

# Biocontrol -> harvesting & market sync (concurrent)
body.order.add_edge(t8, t9)
body.order.add_edge(t8, t10)

# Harvest & market sync -> waste collection
body.order.add_edge(t9, t11)
body.order.add_edge(t10, t11)

# Waste collection -> compost processing
body.order.add_edge(t11, t12)

# Compost -> community feedback & workshops (concurrent)
body.order.add_edge(t12, t13)
body.order.add_edge(t12, t14)

# Feedback/workshop -> data integration
body.order.add_edge(t13, t15)
body.order.add_edge(t14, t15)

# Data integration -> cycle review
body.order.add_edge(t15, t16)

# Define the looping structure: repeat the cycle until exit
root = OperatorPOWL(operator=Operator.LOOP, children=[body, skip])