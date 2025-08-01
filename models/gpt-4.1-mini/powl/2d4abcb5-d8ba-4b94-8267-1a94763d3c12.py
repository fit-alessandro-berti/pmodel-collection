# Generated from: 2d4abcb5-d8ba-4b94-8267-1a94763d3c12.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a repurposed warehouse. It begins with site analysis and structural reinforcement, followed by climate system installation to optimize growth conditions. The process continues with hydroponic system setup, integration of IoT sensors for real-time monitoring, and selection of crop varieties tailored to urban demand. Subsequent activities include staff training on automated maintenance, pest control protocols, nutrient solution management, and energy efficiency auditing. Finally, the process covers harvest scheduling, packaging optimization for urban distribution, and customer feedback loops to continuously refine production and delivery methods, ensuring sustainability and profitability in a challenging urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Site_Analysis = Transition(label='Site Analysis')
Structure_Check = Transition(label='Structure Check')
Climate_Setup = Transition(label='Climate Setup')
Hydroponics_Install = Transition(label='Hydroponics Install')
Sensor_Integration = Transition(label='Sensor Integration')
Crop_Selection = Transition(label='Crop Selection')
Staff_Training = Transition(label='Staff Training')
Pest_Control = Transition(label='Pest Control')
Nutrient_Mix = Transition(label='Nutrient Mix')
Energy_Audit = Transition(label='Energy Audit')
Harvest_Plan = Transition(label='Harvest Plan')
Packaging_Opt = Transition(label='Packaging Opt')
Delivery_Setup = Transition(label='Delivery Setup')
Feedback_Loop = Transition(label='Feedback Loop')
Maintenance = Transition(label='Maintenance')
Data_Review = Transition(label='Data Review')

# Model the feedback loop:
# After Delivery_Setup, there is a loop involving Feedback_Loop, Maintenance, and Data_Review,
# looping back to Feedback_Loop until exit.
# So loop body = sequence of Maintenance --> Data_Review
# loop execution = Feedback_Loop then either exit or (Maintenance->Data_Review->Feedback_Loop)

# Loop operator children: 
#   A = Feedback_Loop (first body activity)
#   B = StrictPartialOrder of Maintenance --> Data_Review
loop_body = StrictPartialOrder(nodes=[Maintenance, Data_Review])
loop_body.order.add_edge(Maintenance, Data_Review)

feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Feedback_Loop, loop_body]
)

# Now build partial order (workflow)

# Sequence of initial activities: 
# Site Analysis --> Structure Check --> Climate Setup --> Hydroponics Install --> Sensor Integration --> Crop Selection --> Staff Training --> Pest Control --> Nutrient Mix --> Energy Audit
initial_sequence_nodes = [
    Site_Analysis, Structure_Check, Climate_Setup, Hydroponics_Install,
    Sensor_Integration, Crop_Selection, Staff_Training, Pest_Control,
    Nutrient_Mix, Energy_Audit
]

initial_sequence = StrictPartialOrder(nodes=initial_sequence_nodes)
for i in range(len(initial_sequence_nodes)-1):
    initial_sequence.order.add_edge(initial_sequence_nodes[i], initial_sequence_nodes[i+1])

# Final sequence: Harvest Plan --> Packaging Opt --> Delivery Setup --> feedback_loop
final_sequence_nodes = [Harvest_Plan, Packaging_Opt, Delivery_Setup, feedback_loop]
final_sequence = StrictPartialOrder(nodes=final_sequence_nodes)
final_sequence.order.add_edge(Harvest_Plan, Packaging_Opt)
final_sequence.order.add_edge(Packaging_Opt, Delivery_Setup)
final_sequence.order.add_edge(Delivery_Setup, feedback_loop)

# Combine initial_sequence and final_sequence into root
# The final starts only after initial_sequence ends
root = StrictPartialOrder(nodes=initial_sequence_nodes + final_sequence_nodes + [feedback_loop])
# Add initial sequence edges
for i in range(len(initial_sequence_nodes)-1):
    root.order.add_edge(initial_sequence_nodes[i], initial_sequence_nodes[i+1])
# Add edge from last of initial sequence to first of final_sequence
root.order.add_edge(initial_sequence_nodes[-1], Harvest_Plan)
# Add final sequence edges
root.order.add_edge(Harvest_Plan, Packaging_Opt)
root.order.add_edge(Packaging_Opt, Delivery_Setup)
root.order.add_edge(Delivery_Setup, feedback_loop)