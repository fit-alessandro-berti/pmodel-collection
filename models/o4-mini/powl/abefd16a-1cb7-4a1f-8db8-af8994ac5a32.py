# Generated from: abefd16a-1cb7-4a1f-8db8-af8994ac5a32.json
# Description: This process outlines the end-to-end establishment of an urban vertical farm within a repurposed warehouse. It involves site analysis, environmental control system installation, hydroponic setup, crop selection tailored for vertical growth, nutrient solution formulation, automated lighting programming, integrated pest management deployment, staff training on unique farming techniques, continuous monitoring via IoT sensors, data analysis for yield optimization, packaging design for urban consumers, logistics planning for fresh delivery, compliance checks with agricultural regulations, marketing strategy targeting local markets, and ongoing sustainability assessments to minimize energy and water consumption while maximizing crop output in an urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
SA = Transition(label='Site Analysis')
FM = Transition(label='Floor Mapping')
SI = Transition(label='System Install')
HS = Transition(label='Hydro Setup')
CS = Transition(label='Crop Select')
NM = Transition(label='Nutrient Mix')
LP = Transition(label='Light Program')
PC = Transition(label='Pest Control')
ST = Transition(label='Staff Training')
SS = Transition(label='Sensor Setup')
DR = Transition(label='Data Review')
PD = Transition(label='Package Design')
DP = Transition(label='Delivery Plan')
CC = Transition(label='Compliance Check')
ML = Transition(label='Market Launch')
SUS = Transition(label='Sustainability')

# Create the partial order
root = StrictPartialOrder(nodes=[SA, FM, SI, HS, CS, NM, LP, PC, ST, SS, DR, PD, DP, CC, ML, SUS])

# Define the control-flow dependencies
root.order.add_edge(SA, FM)
root.order.add_edge(FM, SI)
root.order.add_edge(SI, HS)
root.order.add_edge(HS, CS)
root.order.add_edge(CS, NM)
root.order.add_edge(NM, LP)
root.order.add_edge(LP, PC)
root.order.add_edge(PC, ST)
root.order.add_edge(ST, SS)
root.order.add_edge(SS, DR)

# After data review, branch into planning and launch activities
root.order.add_edge(DR, PD)
root.order.add_edge(DR, DP)
root.order.add_edge(DR, CC)
root.order.add_edge(DR, ML)

# Sustainability runs in parallel once the sensor setup is in place
root.order.add_edge(SS, SUS)