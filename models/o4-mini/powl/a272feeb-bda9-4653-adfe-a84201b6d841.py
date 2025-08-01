# Generated from: a272feeb-bda9-4653-adfe-a84201b6d841.json
# Description: This process involves identifying emerging technology startups globally, evaluating them through a decentralized expert panel, and allocating micro-investments via blockchain contracts. It includes iterative feedback loops where startups receive resources, pivot strategies, and submit progress reports. The process integrates AI-driven market trend analysis and community voting to prioritize funding proposals. Legal compliance checks across jurisdictions and intellectual property assessments ensure risk mitigation. The final stage consolidates impact metrics and reinvests returns into new innovation cycles, fostering a sustainable ecosystem for disruptive technology growth and collaborative venture capital.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
sourcing         = Transition(label='Startup Sourcing')
market           = Transition(label='Market Analysis')
trend            = Transition(label='Trend Forecast')
vote             = Transition(label='Community Vote')
expert           = Transition(label='Expert Review')
legal            = Transition(label='Legal Check')
ip               = Transition(label='IP Assessment')
risk             = Transition(label='Risk Review')
fund             = Transition(label='Funding Allocation')
contract         = Transition(label='Contract Signing')
micro            = Transition(label='Micro Investment')
impact           = Transition(label='Impact Measure')
reinvest         = Transition(label='Return Reinvest')

# Loop body: iterative pivot & progress report
pivot_a      = Transition(label='Strategy Pivot')
progress_a   = Transition(label='Progress Report')
pivot_b      = Transition(label='Strategy Pivot')
progress_b   = Transition(label='Progress Report')

# Define the two subgraphs for the loop
pivot_phase_a = StrictPartialOrder(nodes=[pivot_a, progress_a])
pivot_phase_a.order.add_edge(pivot_a, progress_a)

pivot_phase_b = StrictPartialOrder(nodes=[pivot_b, progress_b])
pivot_phase_b.order.add_edge(pivot_b, progress_b)

# Loop operator: repeat pivot->report until exit
loop_pivot = OperatorPOWL(operator=Operator.LOOP, children=[pivot_phase_a, pivot_phase_b])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    sourcing, market, trend, vote, expert,
    legal, ip, risk,
    fund, contract, micro,
    loop_pivot,
    impact, reinvest
])

# Sequential dependencies
root.order.add_edge(sourcing,   market)
root.order.add_edge(market,     trend)
root.order.add_edge(trend,      vote)
root.order.add_edge(vote,       expert)
root.order.add_edge(expert,     legal)
root.order.add_edge(legal,      ip)
root.order.add_edge(ip,         risk)
root.order.add_edge(risk,       fund)
root.order.add_edge(fund,       contract)
root.order.add_edge(contract,   micro)
root.order.add_edge(micro,      loop_pivot)
root.order.add_edge(loop_pivot, impact)
root.order.add_edge(impact,     reinvest)