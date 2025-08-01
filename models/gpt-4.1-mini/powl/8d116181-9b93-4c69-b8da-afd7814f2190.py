# Generated from: 8d116181-9b93-4c69-b8da-afd7814f2190.json
# Description: This process outlines the setup and operational workflow for an adaptive urban farming system that integrates IoT sensors, AI-driven crop optimization, and community engagement. It begins with site analysis and environmental scanning, followed by modular farm design tailored to spatial constraints. Subsequent steps include sensor deployment for real-time monitoring, nutrient cycling management, and dynamic planting schedules based on AI predictions. The process also incorporates waste-to-compost conversion, stakeholder coordination meetings, and ongoing data analytics for yield improvement. Community workshops and feedback loops ensure adaptability and sustainability, while periodic system audits maintain regulatory compliance and resource efficiency throughout the farm lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SA = Transition(label='Site Analysis')
ES = Transition(label='Env Scanning')
MD = Transition(label='Modular Design')
SD = Transition(label='Sensor Deploy')
NC = Transition(label='Nutrient Cycle')
AI = Transition(label='AI Scheduling')
WC = Transition(label='Waste Compost')
SM = Transition(label='Stakeholder Meet')
DA = Transition(label='Data Analytics')
YR = Transition(label='Yield Review')
CW = Transition(label='Community Workshop')
FL = Transition(label='Feedback Loop')
SAUD = Transition(label='System Audit')
RC = Transition(label='Regulatory Check')
RA = Transition(label='Resource Adjust')

# First phase: site preparation and design (SA --> ES --> MD)
prep = StrictPartialOrder(nodes=[SA, ES, MD])
prep.order.add_edge(SA, ES)
prep.order.add_edge(ES, MD)

# Monitoring and optimization loop:
# Loop consists of: Core monitoring cycle (SD --> NC --> AI)
core_cycle = StrictPartialOrder(nodes=[SD, NC, AI])
core_cycle.order.add_edge(SD, NC)
core_cycle.order.add_edge(NC, AI)

# Waste management (WC) can be done concurrently with Stakeholder meetings (SM)
waste_stake = StrictPartialOrder(nodes=[WC, SM])
# no edges, concurrent

# Data analytics and yield review run in sequence (DA --> YR)
data_yield = StrictPartialOrder(nodes=[DA, YR])
data_yield.order.add_edge(DA, YR)

# Community workshops and feedback loop run in sequence (CW --> FL)
work_feedback = StrictPartialOrder(nodes=[CW, FL])
work_feedback.order.add_edge(CW, FL)

# Compliance checks: system audit, regulatory check, resource adjust in sequence
compliance = StrictPartialOrder(nodes=[SAUD, RC, RA])
compliance.order.add_edge(SAUD, RC)
compliance.order.add_edge(RC, RA)

# Loop body:
# After core monitoring cycle, stakeholder meetings, waste compost, data analytics, workshops and feedback,
# then compliance checks happen at end of the loop
loop_body = StrictPartialOrder(nodes=[core_cycle, waste_stake, data_yield, work_feedback, compliance])
# Add edges from core_cycle to other concurrent parts to ensure core_cycle precedes them
loop_body.order.add_edge(core_cycle, waste_stake)
loop_body.order.add_edge(core_cycle, data_yield)
loop_body.order.add_edge(core_cycle, work_feedback)
loop_body.order.add_edge(waste_stake, data_yield)  # waste and stakeholder before data analytics
loop_body.order.add_edge(data_yield, work_feedback) # data analytics before workshop/feedback
loop_body.order.add_edge(work_feedback, compliance) # workshops/feedback before compliance

# Loop: execute loop_body repeatedly starting after Modular Design
loop = OperatorPOWL(operator=Operator.LOOP, children=[prep, loop_body])

root = loop