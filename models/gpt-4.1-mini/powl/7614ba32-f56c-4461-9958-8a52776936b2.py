# Generated from: 7614ba32-f56c-4461-9958-8a52776936b2.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed warehouse. It involves initial site assessment, environmental impact analysis, modular system design, installation of hydroponic and aeroponic units, integration of IoT sensors for climate control, training of staff on automated maintenance, development of crop rotation schedules, securing local compliance and certifications, implementation of renewable energy sources, continuous monitoring of plant health via AI, optimization of nutrient delivery, packaging logistics planning, marketing to local retailers, and establishing customer feedback loops to enhance product quality and operational efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Assess = Transition(label='Site Assess')
Impact_Study = Transition(label='Impact Study')
System_Design = Transition(label='System Design')
Unit_Install = Transition(label='Unit Install')
Sensor_Setup = Transition(label='Sensor Setup')
Staff_Train = Transition(label='Staff Train')
Crop_Schedule = Transition(label='Crop Schedule')
Compliance_Check = Transition(label='Compliance Check')
Energy_Deploy = Transition(label='Energy Deploy')
Health_Monitor = Transition(label='Health Monitor')
Nutrient_Tune = Transition(label='Nutrient Tune')
Package_Plan = Transition(label='Package Plan')
Market_Outreach = Transition(label='Market Outreach')
Feedback_Loop = Transition(label='Feedback Loop')
Data_Analyze = Transition(label='Data Analyze')

# Structure:
# 1) Site Assess -> Impact Study -> System Design
# 2) System Design -> parallel installation/setup/training:
#    Unit Install || Sensor Setup || Staff Train
# 3) After these parallel tasks, Crop Schedule and Compliance Check must be done in sequence
# 4) Then Energy Deploy
# 5) Then a loop of monitoring, tuning, packaging, marketing, and feedback with data analyze included:
#    This loop executes:
#    Health Monitor (A)
#    Body (B): Nutrient Tune -> Package Plan -> Market Outreach -> Feedback Loop -> Data Analyze
#    loop = *(Health Monitor, Nutrient Tune -> Package Plan -> Market Outreach -> Feedback Loop -> Data Analyze)

# Create parallel for Unit Install, Sensor Setup, Staff Train:
parallel_setup = StrictPartialOrder(nodes=[Unit_Install, Sensor_Setup, Staff_Train])
# no edges - fully concurrent

# Crop Schedule -> Compliance Check sequence:
crop_compliance = StrictPartialOrder(nodes=[Crop_Schedule, Compliance_Check])
crop_compliance.order.add_edge(Crop_Schedule, Compliance_Check)

# Body of the loop:
body_loop = StrictPartialOrder(
    nodes=[Nutrient_Tune, Package_Plan, Market_Outreach, Feedback_Loop, Data_Analyze]
)
body_loop.order.add_edge(Nutrient_Tune, Package_Plan)
body_loop.order.add_edge(Package_Plan, Market_Outreach)
body_loop.order.add_edge(Market_Outreach, Feedback_Loop)
body_loop.order.add_edge(Feedback_Loop, Data_Analyze)

# Loop:
loop = OperatorPOWL(operator=Operator.LOOP, children=[Health_Monitor, body_loop])

# Connect all steps in sequence except parallel: 
# Site Assess -> Impact Study -> System Design -> parallel_setup -> crop_compliance -> Energy Deploy -> loop

root = StrictPartialOrder(
    nodes=[
        Site_Assess,
        Impact_Study,
        System_Design,
        parallel_setup,
        crop_compliance,
        Energy_Deploy,
        loop,
    ]
)

root.order.add_edge(Site_Assess, Impact_Study)
root.order.add_edge(Impact_Study, System_Design)
root.order.add_edge(System_Design, parallel_setup)
root.order.add_edge(parallel_setup, crop_compliance)
root.order.add_edge(crop_compliance, Energy_Deploy)
root.order.add_edge(Energy_Deploy, loop)