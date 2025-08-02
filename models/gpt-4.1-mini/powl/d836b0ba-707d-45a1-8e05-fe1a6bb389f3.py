# Generated from: d836b0ba-707d-45a1-8e05-fe1a6bb389f3.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming operation within a dense metropolitan area. It includes site selection based on sunlight and accessibility, modular system design tailored to limited space, integration of IoT sensors for environmental monitoring, selection of crop varieties suited for vertical growth, soil and nutrient solution preparation, automated irrigation setup, pest management using biocontrol agents, energy-efficient LED lighting installation, staff training on system maintenance, regulatory compliance checks, market analysis for local distribution, packaging design for freshness retention, logistics planning for rapid delivery, data analytics for yield optimization, and continuous improvement through feedback loops. This atypical process requires coordination across agronomy, technology, logistics, and marketing disciplines to create a sustainable, productive urban farm that minimizes resource use while maximizing output and profitability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Select = Transition(label='Site Select')
Design_Layout = Transition(label='Design Layout')
Sensor_Integrate = Transition(label='Sensor Integrate')
Crop_Choose = Transition(label='Crop Choose')
Soil_Prepare = Transition(label='Soil Prepare')
Irrigation_Setup = Transition(label='Irrigation Setup')
Pest_Control = Transition(label='Pest Control')
Lighting_Install = Transition(label='Lighting Install')
Staff_Train = Transition(label='Staff Train')
Compliance_Check = Transition(label='Compliance Check')
Market_Analyze = Transition(label='Market Analyze')
Package_Design = Transition(label='Package Design')
Logistics_Plan = Transition(label='Logistics Plan')
Data_Analyze = Transition(label='Data Analyze')
Feedback_Loop = Transition(label='Feedback Loop')

# The process logic:
# 1) Site Select
# 2) Design Layout depends on Site Select
# 3) Sensor Integrate depends on Design Layout
# 4) Crop Choose depends on Sensor Integrate
# 5) Soil Prepare depends on Crop Choose
# 6) Irrigation Setup depends on Soil Prepare
# 7) Pest Control depends on Irrigation Setup
# 8) Lighting Install depends on Pest Control
# 9) Staff Train depends on Lighting Install
# 10) Compliance Check depends on Staff Train
# 11) Market Analyze depends on Compliance Check
# 12) Package Design depends on Market Analyze
# 13) Logistics Plan depends on Package Design
# 14) Data Analyze depends on Logistics Plan
# 15) Feedback Loop depends on Data Analyze and leads back as loop to Design Layout

# We'll model the feedback loop as a LOOP operator:
# LOOP(body=StrictPartialOrder(nodes=[Design_Layout ... Feedback_Loop], order=...), redo=Site_Select)

# Actually, looping from Feedback Loop back to Design Layout makes more sense (re-design improvement loop)
# But Site Select is before Design Layout, logically site selection is one-time

# So loop body: Design Layout to Feedback Loop sequentially
# Loop redo branch: Silent skip transition to end loop

# Create the sequence from Design Layout to Feedback Loop in a StrictPartialOrder
sequence_nodes = [
    Design_Layout,
    Sensor_Integrate,
    Crop_Choose,
    Soil_Prepare,
    Irrigation_Setup,
    Pest_Control,
    Lighting_Install,
    Staff_Train,
    Compliance_Check,
    Market_Analyze,
    Package_Design,
    Logistics_Plan,
    Data_Analyze,
    Feedback_Loop
]

sequence = StrictPartialOrder(nodes=sequence_nodes)
# Add edges to sequence in order
for i in range(len(sequence_nodes)-1):
    sequence.order.add_edge(sequence_nodes[i], sequence_nodes[i+1])

# loop with body=sequence (the improvement cycle), redo=SilentTransition (exit)
redo = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[sequence, redo])

# The full process partial order:
# Site_Select --> loop

root = StrictPartialOrder(nodes=[Site_Select, loop])
root.order.add_edge(Site_Select, loop)