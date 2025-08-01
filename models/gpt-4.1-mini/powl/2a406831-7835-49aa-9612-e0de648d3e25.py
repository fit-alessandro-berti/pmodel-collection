# Generated from: 2a406831-7835-49aa-9612-e0de648d3e25.json
# Description: This process outlines the complex establishment of an urban vertical farm within a dense city environment. It involves site assessment, modular system design, environmental impact evaluation, securing permits, sourcing specialized hydroponic equipment, installing automated climate controls, integrating AI-driven nutrient delivery, recruiting skilled agronomists, conducting pilot crop trials, optimizing energy consumption, establishing local distribution channels, and implementing continuous monitoring for yield maximization and sustainability compliance. The goal is to create a scalable, high-efficiency farming solution that minimizes footprint while maximizing fresh produce output year-round in urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
System_Design = Transition(label='System Design')
Impact_Study = Transition(label='Impact Study')
Permit_Filing = Transition(label='Permit Filing')
Equipment_Sourcing = Transition(label='Equipment Sourcing')
Climate_Setup = Transition(label='Climate Setup')
AI_Integration = Transition(label='AI Integration')
Staff_Hiring = Transition(label='Staff Hiring')
Crop_Testing = Transition(label='Crop Testing')
Energy_Audit = Transition(label='Energy Audit')
Logistics_Plan = Transition(label='Logistics Plan')
Yield_Analysis = Transition(label='Yield Analysis')
Sustainability_Check = Transition(label='Sustainability Check')
Market_Launch = Transition(label='Market Launch')
Feedback_Loop = Transition(label='Feedback Loop')

# Loop modeling the feedback cycle: after market launch, continuous monitoring and refinement:
# Execute Yield Analysis, then Sustainability Check, then optionally loop back for Feedback Loop and again yield analysis...
# We'll put Feedback_Loop as the looping condition with Yield Analysis as the first part of the loop, Sustainability Check as the "do again" part
loop = OperatorPOWL(operator=Operator.LOOP, children=[Yield_Analysis, StrictPartialOrder(nodes=[Feedback_Loop, Sustainability_Check])])

# Partial order capturing the main flow
# Sequential order:
# Site Survey --> System Design --> Impact Study --> Permit Filing --> Equipment Sourcing --> Climate Setup --> AI Integration --> Staff Hiring --> Crop Testing --> Energy Audit --> Logistics Plan --> Market Launch --> loop

nodes = [
    Site_Survey,
    System_Design,
    Impact_Study,
    Permit_Filing,
    Equipment_Sourcing,
    Climate_Setup,
    AI_Integration,
    Staff_Hiring,
    Crop_Testing,
    Energy_Audit,
    Logistics_Plan,
    Market_Launch,
    loop
]

root = StrictPartialOrder(nodes=nodes)

root.order.add_edge(Site_Survey, System_Design)
root.order.add_edge(System_Design, Impact_Study)
root.order.add_edge(Impact_Study, Permit_Filing)
root.order.add_edge(Permit_Filing, Equipment_Sourcing)
root.order.add_edge(Equipment_Sourcing, Climate_Setup)
root.order.add_edge(Climate_Setup, AI_Integration)
root.order.add_edge(AI_Integration, Staff_Hiring)
root.order.add_edge(Staff_Hiring, Crop_Testing)
root.order.add_edge(Crop_Testing, Energy_Audit)
root.order.add_edge(Energy_Audit, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Market_Launch)
root.order.add_edge(Market_Launch, loop)