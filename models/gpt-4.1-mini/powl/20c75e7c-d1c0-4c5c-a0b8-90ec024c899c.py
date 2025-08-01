# Generated from: 20c75e7c-d1c0-4c5c-a0b8-90ec024c899c.json
# Description: This process outlines the end-to-end setup of an urban vertical farm in a repurposed industrial building. It involves site assessment, structural modifications, environmental system installation, crop selection based on microclimate analysis, automated irrigation programming, nutrient solution formulation, pest control integration using biocontrol agents, staff training on hydroponic techniques, ongoing yield monitoring through IoT sensors, energy consumption optimization, waste recycling protocols, market distribution planning, regulatory compliance verification, and continuous improvement feedback loops to ensure sustainability and profitability in an atypical urban agricultural context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Assess = Transition(label='Site Assess')
Structure_Mod = Transition(label='Structure Mod')
Enviro_Install = Transition(label='Enviro Install')
Crop_Select = Transition(label='Crop Select')
Irrigation_Set = Transition(label='Irrigation Set')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Control = Transition(label='Pest Control')
Staff_Train = Transition(label='Staff Train')
Yield_Monitor = Transition(label='Yield Monitor')
Energy_Audit = Transition(label='Energy Audit')
Waste_Recycle = Transition(label='Waste Recycle')
Market_Plan = Transition(label='Market Plan')
Compliance_Check = Transition(label='Compliance Check')
Feedback_Loop = Transition(label='Feedback Loop')
Tech_Upgrade = Transition(label='Tech Upgrade')

# Model the feedback loop as a LOOP operator:
# Loop body: Feedback_Loop
# Loop redo: Tech_Upgrade
# The loop structure represents continuous improvement feedback loops 
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[Feedback_Loop, Tech_Upgrade])

# Construct partial order representing the process flow

# Early setup steps in sequence:
# Site Assess --> Structure Mod --> Enviro Install
# Then Crop Select
# Then irrigation and nutrient mix can happen concurrently (both depend on Crop Select)
# Pest Control and Staff Train can proceed after irrigation and nutrient mix are done (both depend on both irrigation and nutrient mix)
# Yield Monitor, Energy Audit, Waste Recycle can proceed concurrently after Staff Train and Pest Control
# Market Plan and Compliance Check can proceed after the three above complete (Yield Monitor, Energy Audit, Waste Recycle)
# The feedback loop and tech upgrade are executed last as a loop, after Market Plan and Compliance Check

root = StrictPartialOrder(nodes=[
    Site_Assess,
    Structure_Mod,
    Enviro_Install,
    Crop_Select,
    Irrigation_Set,
    Nutrient_Mix,
    Pest_Control,
    Staff_Train,
    Yield_Monitor,
    Energy_Audit,
    Waste_Recycle,
    Market_Plan,
    Compliance_Check,
    loop_feedback
])

# Define order edges
order = root.order
order.add_edge(Site_Assess, Structure_Mod)
order.add_edge(Structure_Mod, Enviro_Install)
order.add_edge(Enviro_Install, Crop_Select)
order.add_edge(Crop_Select, Irrigation_Set)
order.add_edge(Crop_Select, Nutrient_Mix)

order.add_edge(Irrigation_Set, Pest_Control)
order.add_edge(Irrigation_Set, Staff_Train)
order.add_edge(Nutrient_Mix, Pest_Control)
order.add_edge(Nutrient_Mix, Staff_Train)

order.add_edge(Pest_Control, Yield_Monitor)
order.add_edge(Pest_Control, Energy_Audit)
order.add_edge(Pest_Control, Waste_Recycle)
order.add_edge(Staff_Train, Yield_Monitor)
order.add_edge(Staff_Train, Energy_Audit)
order.add_edge(Staff_Train, Waste_Recycle)

order.add_edge(Yield_Monitor, Market_Plan)
order.add_edge(Energy_Audit, Market_Plan)
order.add_edge(Waste_Recycle, Market_Plan)

order.add_edge(Yield_Monitor, Compliance_Check)
order.add_edge(Energy_Audit, Compliance_Check)
order.add_edge(Waste_Recycle, Compliance_Check)

order.add_edge(Market_Plan, loop_feedback)
order.add_edge(Compliance_Check, loop_feedback)