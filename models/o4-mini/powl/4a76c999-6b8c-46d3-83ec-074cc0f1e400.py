# Generated from: 4a76c999-6b8c-46d3-83ec-074cc0f1e400.json
# Description: This process outlines the comprehensive operational cycle of an urban vertical farm integrating advanced hydroponics, AI-driven climate control, and automated harvesting. Beginning with seed selection optimized for urban conditions, it proceeds through nutrient calibration, environmental monitoring, pest bio-control deployment, and energy-efficient lighting adjustments. The flow includes real-time data analytics to predict growth phases and yield, adaptive resource allocation to minimize waste, and robotic harvesting that ensures produce quality. Post-harvest, the cycle incorporates packaging customization based on market demand, waste recycling into biofertilizers, and distribution scheduling aligned with consumer freshness windows. The process is designed to maximize productivity in constrained urban spaces while maintaining sustainability and reducing carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
S  = Transition(label='Seed Selection')
N  = Transition(label='Nutrient Mix')
C  = Transition(label='Climate Setup')
SC = Transition(label='Sensor Calibration')
PC = Transition(label='Pest Control')
LA = Transition(label='Lighting Adjust')
GT = Transition(label='Growth Tracking')
DA = Transition(label='Data Analysis')
RS = Transition(label='Resource Shift')
RH = Transition(label='Robotic Harvest')
QC = Transition(label='Quality Check')
PS = Transition(label='Packaging Sort')
WC = Transition(label='Waste Cycle')
DP = Transition(label='Delivery Plan')
MS = Transition(label='Market Sync')

# Pre-harvest and harvest phase (A)
A = StrictPartialOrder(nodes=[S, N, C, SC, PC, LA, GT, DA, RS, RH, QC])
A.order.add_edge(S,  N)
A.order.add_edge(N,  C)
A.order.add_edge(C,  SC)
A.order.add_edge(SC, PC)
A.order.add_edge(PC, LA)
A.order.add_edge(LA, GT)
A.order.add_edge(GT, DA)
A.order.add_edge(DA, RS)
A.order.add_edge(RS, RH)
A.order.add_edge(RH, QC)

# Post-harvest phase (B)
B = StrictPartialOrder(nodes=[PS, WC, DP, MS])
# packaging sort leads to waste cycle and delivery plan in parallel
B.order.add_edge(PS, WC)
B.order.add_edge(PS, DP)
# both must complete before market sync
B.order.add_edge(WC, MS)
B.order.add_edge(DP, MS)

# Loop the whole cycle
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])