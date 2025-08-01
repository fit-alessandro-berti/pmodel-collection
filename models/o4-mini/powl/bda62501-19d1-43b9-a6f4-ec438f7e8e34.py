# Generated from: bda62501-19d1-43b9-a6f4-ec438f7e8e34.json
# Description: This process manages the sourcing, verification, and distribution of rare artisanal goods across multiple continents. It involves intricate coordination between local artisan communities, regional quality inspectors, international logistics teams, and digital marketplace platforms. The process ensures authenticity through multi-layered certification, incorporates environmental impact assessments, and adapts dynamically to geopolitical and climate-related disruptions while maintaining sustainable practices and ethical trade standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
AS = Transition(label='Artisan Sourcing')
MT = Transition(label='Material Testing')
QA = Transition(label='Quality Audit')
CO = Transition(label='Certify Origin')
CS = Transition(label='Carbon Scan')
RM = Transition(label='Risk Mapping')
CD = Transition(label='Contract Draft')
LT = Transition(label='Local Training')
IS = Transition(label='Inventory Sync')
CF = Transition(label='Customs Filing')
FB = Transition(label='Freight Booking')
DI = Transition(label='Damage Inspect')
ML = Transition(label='Market Listing')
DF = Transition(label='Demand Forecast')
SR = Transition(label='Sales Report')
FL = Transition(label='Feedback Loop')
RP = Transition(label='Reorder Planning')

# Loop for environmental / geopolitical reassessment (may repeat Carbon Scan → Risk Mapping)
scan_cycle = StrictPartialOrder(nodes=[CS, RM])
scan_cycle.order.add_edge(CS, RM)
loop_disruption = OperatorPOWL(operator=Operator.LOOP, children=[scan_cycle, scan_cycle])

# Main sourcing → certification → delivery flow
main_seq = StrictPartialOrder(nodes=[
    AS, MT, QA, CO,
    loop_disruption,
    CD, LT, IS, CF, FB, DI
])
main_seq.order.add_edge(AS, MT)
main_seq.order.add_edge(MT, QA)
main_seq.order.add_edge(QA, CO)
main_seq.order.add_edge(CO, loop_disruption)
main_seq.order.add_edge(loop_disruption, CD)
main_seq.order.add_edge(CD, LT)
main_seq.order.add_edge(LT, IS)
main_seq.order.add_edge(IS, CF)
main_seq.order.add_edge(CF, FB)
main_seq.order.add_edge(FB, DI)

# Loop for market listing → forecast → reporting → feedback → reorder
post_seq = StrictPartialOrder(nodes=[ML, DF, SR])
post_seq.order.add_edge(ML, DF)
post_seq.order.add_edge(DF, SR)

feedback_cycle = StrictPartialOrder(nodes=[FL, RP])
feedback_cycle.order.add_edge(FL, RP)

loop_market = OperatorPOWL(operator=Operator.LOOP, children=[post_seq, feedback_cycle])

# Root POWL: after delivery you enter the market/feedback loop
root = StrictPartialOrder(nodes=[main_seq, loop_market])
root.order.add_edge(main_seq, loop_market)