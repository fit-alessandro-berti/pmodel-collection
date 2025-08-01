# Generated from: 45c3a0ba-4bb9-43ed-ba5e-b009054a6829.json
# Description: This process outlines the intricate journey of artisan coffee beans from origin to cup, incorporating sustainable sourcing, quality verification, and direct farmer engagement. It involves coordinating micro-lot harvests, implementing blockchain traceability, specialized roasting profiles, and personalized distribution channels to ensure freshness and ethical standards. The process also integrates customer feedback loops for continuous blend refinement and adapts dynamically to seasonal crop variations and market demand fluctuations while maintaining transparency and premium quality assurance throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Activities
FS = Transition(label='Farm Selection')
LH = Transition(label='Lot Harvest')
ST = Transition(label='Sample Testing')
TL = Transition(label='Trace Logging')
QA = Transition(label='Quality Audit')
FP = Transition(label='Farmer Payment')
RP = Transition(label='Roast Profiling')
BRO = Transition(label='Batch Roasting')
FT = Transition(label='Flavor Tasting')
PS = Transition(label='Packaging Seal')
IC = Transition(label='Inventory Check')
OA = Transition(label='Order Allocation')
DR = Transition(label='Delivery Routing')
CF = Transition(label='Customer Feedback')
BRF = Transition(label='Blend Refinement')
MA = Transition(label='Market Analysis')
DF = Transition(label='Demand Forecast')

# Roasting + feedback loop
roast_seq = StrictPartialOrder(nodes=[RP, BRO, FT, PS, IC])
roast_seq.order.add_edge(RP, BRO)
roast_seq.order.add_edge(BRO, FT)
roast_seq.order.add_edge(FT, PS)
roast_seq.order.add_edge(PS, IC)

refinement_seq = StrictPartialOrder(nodes=[CF, BRF])
refinement_seq.order.add_edge(CF, BRF)

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[roast_seq, refinement_seq])

# Main process flow
full_proc = StrictPartialOrder(
    nodes=[FS, LH, ST, TL, QA, FP, feedback_loop, OA, DR]
)
full_proc.order.add_edge(FS, LH)
full_proc.order.add_edge(LH, ST)
full_proc.order.add_edge(ST, TL)
full_proc.order.add_edge(TL, QA)
full_proc.order.add_edge(QA, FP)
full_proc.order.add_edge(FP, feedback_loop)
full_proc.order.add_edge(feedback_loop, OA)
full_proc.order.add_edge(OA, DR)

# Adaptation loop (seasonal & market)
adapt_seq = StrictPartialOrder(nodes=[MA, DF])
adapt_seq.order.add_edge(MA, DF)

# Outer loop combining full process with periodic adaptation
root = OperatorPOWL(operator=Operator.LOOP, children=[full_proc, adapt_seq])