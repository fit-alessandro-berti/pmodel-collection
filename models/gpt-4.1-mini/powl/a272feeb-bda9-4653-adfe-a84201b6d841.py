# Generated from: a272feeb-bda9-4653-adfe-a84201b6d841.json
# Description: This process involves identifying emerging technology startups globally, evaluating them through a decentralized expert panel, and allocating micro-investments via blockchain contracts. It includes iterative feedback loops where startups receive resources, pivot strategies, and submit progress reports. The process integrates AI-driven market trend analysis and community voting to prioritize funding proposals. Legal compliance checks across jurisdictions and intellectual property assessments ensure risk mitigation. The final stage consolidates impact metrics and reinvests returns into new innovation cycles, fostering a sustainable ecosystem for disruptive technology growth and collaborative venture capital.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Startup_Sourcing = Transition(label='Startup Sourcing')
Expert_Review = Transition(label='Expert Review')
Micro_Investment = Transition(label='Micro Investment')
Progress_Report = Transition(label='Progress Report')
Market_Analysis = Transition(label='Market Analysis')
Community_Vote = Transition(label='Community Vote')
Strategy_Pivot = Transition(label='Strategy Pivot')
Legal_Check = Transition(label='Legal Check')
IP_Assessment = Transition(label='IP Assessment')
Risk_Review = Transition(label='Risk Review')
Impact_Measure = Transition(label='Impact Measure')
Return_Reinvest = Transition(label='Return Reinvest')
Funding_Allocation = Transition(label='Funding Allocation')
Contract_Signing = Transition(label='Contract Signing')
Trend_Forecast = Transition(label='Trend Forecast')

# Step 1: Startup sourcing leads to expert review and market analysis + trend forecast (concurrent)
sourcing_PO = StrictPartialOrder(nodes=[Startup_Sourcing, Expert_Review, Market_Analysis, Trend_Forecast])
sourcing_PO.order.add_edge(Startup_Sourcing, Expert_Review)
sourcing_PO.order.add_edge(Startup_Sourcing, Market_Analysis)
sourcing_PO.order.add_edge(Startup_Sourcing, Trend_Forecast)

# Step 2: Expert Review leads to Legal Check, IP Assessment, and Risk Review (all concurrent)
legal_PO = StrictPartialOrder(nodes=[Legal_Check, IP_Assessment, Risk_Review])
# No order dependencies among them, fully concurrent

# Step 3: After assessments, funding allocation and contract signing in sequence
funding_PO = StrictPartialOrder(nodes=[Funding_Allocation, Contract_Signing])
funding_PO.order.add_edge(Funding_Allocation, Contract_Signing)

# Step 4: Micro Investment happens after Contract Signing
micro_PO = StrictPartialOrder(nodes=[Contract_Signing, Micro_Investment])
micro_PO.order.add_edge(Contract_Signing, Micro_Investment)

# Step 5: Loop body: Micro Investment -> Progress Report -> Strategy Pivot choice -> back to Micro Investment or exit loop
# Define Strategy Pivot choice: either do Strategy Pivot or skip (silent)
skip = SilentTransition()
strategy_choice = OperatorPOWL(operator=Operator.XOR, children=[Strategy_Pivot, skip])

# Loop: A = Micro_Investment -> Progress_Report , B = strategy_choice
# But the loop is defined as LOOP(A, B) with semantics:
# execute A,
# then choose to exit or execute B then A again
# So we need A to be Micro_Investment and Progress_Report in sequence,
# and B to be strategy_choice

A_loop_PO = StrictPartialOrder(nodes=[Micro_Investment, Progress_Report])
A_loop_PO.order.add_edge(Micro_Investment, Progress_Report)

loop = OperatorPOWL(operator=Operator.LOOP, children=[A_loop_PO, strategy_choice])

# Step 6: Community Vote after Expert Review and Market Analysis + Trend Forecast
cv_PO = StrictPartialOrder(nodes=[Expert_Review, Market_Analysis, Trend_Forecast, Community_Vote])
cv_PO.order.add_edge(Expert_Review, Community_Vote)
cv_PO.order.add_edge(Market_Analysis, Community_Vote)
cv_PO.order.add_edge(Trend_Forecast, Community_Vote)

# Step 7: After Community Vote and Legal/Assessment checks, do funding (Funding Allocation PO created above)
# So we merge legal_PO and cv_PO and make their outputs prerequisites for funding_PO
pre_funding_PO = StrictPartialOrder(nodes=[Legal_Check, IP_Assessment, Risk_Review,
                                           Expert_Review, Market_Analysis, Trend_Forecast, Community_Vote])
# No ordering inside legal_PO (legal check, ip, risk concurrent)
# Community vote depends on expert review, market analysis, trend forecast (already ordered in cv_PO)
pre_funding_PO.order.add_edge(Expert_Review, Community_Vote)
pre_funding_PO.order.add_edge(Market_Analysis, Community_Vote)
pre_funding_PO.order.add_edge(Trend_Forecast, Community_Vote)

# The legal checks are concurrent with community vote but logical to have funding after both
# So add edges from each legal check to funding allocation
# We'll integrate funding_PO into root PO - the edges will be added later.

# Step 8: Final stage after loop: Impact Measure -> Return Reinvest
final_PO = StrictPartialOrder(nodes=[Impact_Measure, Return_Reinvest])
final_PO.order.add_edge(Impact_Measure, Return_Reinvest)

# Step 9: Assemble full model

# Nodes to include:
#  - sourcing_PO to expert review and market analysis/trend forecast (done)
#  - pre_funding_PO (legal + community vote)
#  - funding_PO (funding allocation -> contract signing)
#  - micro investment loop (loop node)
#  - final_PO (impact measure, return reinvest)

# Because expert review, market analysis, trend forecast appear multiple times, ensure single instances
# The nodes used are: Startup_Sourcing, Expert_Review, Market_Analysis, Trend_Forecast,
# Legal_Check, IP_Assessment, Risk_Review, Community_Vote,
# Funding_Allocation, Contract_Signing, loop (Micro_Investment + Progress_Report + Strategy Pivot loop),
# Impact_Measure, Return_Reinvest

# Create root PO with all nodes
root_nodes = [Startup_Sourcing,
              Expert_Review,
              Market_Analysis,
              Trend_Forecast,
              Legal_Check,
              IP_Assessment,
              Risk_Review,
              Community_Vote,
              Funding_Allocation,
              Contract_Signing,
              loop,
              Impact_Measure,
              Return_Reinvest]

root = StrictPartialOrder(nodes=root_nodes)

# Add ordering edges:

# Startup Sourcing -> Expert Review, Market Analysis, Trend Forecast
root.order.add_edge(Startup_Sourcing, Expert_Review)
root.order.add_edge(Startup_Sourcing, Market_Analysis)
root.order.add_edge(Startup_Sourcing, Trend_Forecast)

# Expert Review, Market Analysis, Trend Forecast -> Community Vote
root.order.add_edge(Expert_Review, Community_Vote)
root.order.add_edge(Market_Analysis, Community_Vote)
root.order.add_edge(Trend_Forecast, Community_Vote)

# Expert Review -> Legal Checks (assuming legal checks happen after expert review)
root.order.add_edge(Expert_Review, Legal_Check)
root.order.add_edge(Expert_Review, IP_Assessment)
root.order.add_edge(Expert_Review, Risk_Review)

# Legal checks and Community Vote must finish before Funding Allocation
root.order.add_edge(Legal_Check, Funding_Allocation)
root.order.add_edge(IP_Assessment, Funding_Allocation)
root.order.add_edge(Risk_Review, Funding_Allocation)
root.order.add_edge(Community_Vote, Funding_Allocation)

# Funding Allocation -> Contract Signing
root.order.add_edge(Funding_Allocation, Contract_Signing)

# Contract Signing -> Loop (micro investment + progress reports + strategy pivot)
root.order.add_edge(Contract_Signing, loop)

# After loop finishes, Impact Measure -> Return Reinvest
root.order.add_edge(Impact_Measure, Return_Reinvest)

# Loop is followed by impact measure (loop end must lead to Impact Measure)
root.order.add_edge(loop, Impact_Measure)