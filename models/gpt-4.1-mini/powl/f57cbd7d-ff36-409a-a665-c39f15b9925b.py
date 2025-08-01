# Generated from: f57cbd7d-ff36-409a-a665-c39f15b9925b.json
# Description: This process outlines the end-to-end flow for managing corporate innovation projects that deviate from traditional R&D workflows. It begins with external trend scanning and internal ideation sprints, followed by cross-departmental feasibility reviews and risk assessments. Selected ideas progress through rapid prototyping using minimal viable technologies, then undergo market simulation and stakeholder alignment workshops. Post-validation, projects enter a resource allocation phase involving budget rebalancing and talent sourcing, before moving into iterative pilot launches with continuous data-driven refinements. The process concludes with scalability analysis and integration planning to embed successful innovations into existing business units while managing change and knowledge transfer effectively across teams.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
ts = Transition(label='Trend Scan')
isprint = Transition(label='Idea Sprint')
fc = Transition(label='Feasibility Check')
rr = Transition(label='Risk Review')
tp = Transition(label='Tech Prototype')
ms = Transition(label='Market Simulate')
sa = Transition(label='Stakeholder Align')
ba = Transition(label='Budget Adjust')
tals = Transition(label='Talent Source')
pl = Transition(label='Pilot Launch')
dr = Transition(label='Data Refine')
sa2 = Transition(label='Scale Analysis')
ip = Transition(label='Integration Plan')
cm = Transition(label='Change Manage')
kt = Transition(label='Knowledge Transfer')

# First phase: Parallel start of Trend Scan and Idea Sprint
start_po = StrictPartialOrder(nodes=[ts, isprint])
# They are concurrent (no order edges)

# Second phase: Feasibility Check and Risk Review (performed after both trend scan and idea sprint)
f_rr_po = StrictPartialOrder(nodes=[fc, rr])
f_rr_po.order.add_edge(fc, rr)  # sequential order between feasibility check and risk review (assumed)
# The description mentions cross-departmental feasibility reviews and risk assessments, could be parallel or sequence.
# To create a partial order, assume feasibility check before risk review, but these can be swapped as well.
# Alternatively, make them concurrent:
f_rr_po = StrictPartialOrder(nodes=[fc, rr])
# We'll keep concurrency, because the text says "followed by cross-departmental feasibility reviews and risk assessments."
# So maybe they are concurrent after the first phase

# Third phase: Rapid prototyping with minimal viable technologies
# After feasibility and risk review, selected ideas progress to rapid prototyping
prototype_po = StrictPartialOrder(nodes=[tp])

# Fourth phase: market simulation and stakeholder alignment workshops - can be parallel
market_stakeholder_po = StrictPartialOrder(nodes=[ms, sa])
# no order edges: concurrent

# Fifth phase: Resource allocation phase involving budget rebalancing and talent sourcing - can be parallel
resource_po = StrictPartialOrder(nodes=[ba, tals])
# no order edges: concurrent

# Sixth phase: iterative pilot launches with continuous data-driven refinements
# This suggests a loop: Pilot Launch, then Data Refine, then back to Pilot Launch or exit
loop_pilot = OperatorPOWL(operator=Operator.LOOP, children=[pl, dr])

# Seventh phase: scalability analysis and integration planning - sequential
scale_integration_po = StrictPartialOrder(nodes=[sa2, ip])
scale_integration_po.order.add_edge(sa2, ip)

# Eighth phase: change management and knowledge transfer - parallel/concurrent
change_kt_po = StrictPartialOrder(nodes=[cm, kt])

# Now compose phases in order:

# 1 & 2: The first phase nodes must precede feasibility and risk review
po1_2_nodes = [start_po, f_rr_po]
po1_2 = StrictPartialOrder(nodes=po1_2_nodes)
po1_2.order.add_edge(start_po, f_rr_po)

# 3: Prototyping after feasibility and risk review
po1_3_nodes = [po1_2, prototype_po]
po1_3 = StrictPartialOrder(nodes=po1_3_nodes)
po1_3.order.add_edge(po1_2, prototype_po)

# 4: market simulation and stakeholder alignment after prototyping
po1_4_nodes = [po1_3, market_stakeholder_po]
po1_4 = StrictPartialOrder(nodes=po1_4_nodes)
po1_4.order.add_edge(po1_3, market_stakeholder_po)

# 5: resource allocation after market and stakeholder
po1_5_nodes = [po1_4, resource_po]
po1_5 = StrictPartialOrder(nodes=po1_5_nodes)
po1_5.order.add_edge(po1_4, resource_po)

# 6: iterative pilot launch loop after resource allocation
po1_6_nodes = [po1_5, loop_pilot]
po1_6 = StrictPartialOrder(nodes=po1_6_nodes)
po1_6.order.add_edge(po1_5, loop_pilot)

# 7: scale analysis and integration after pilot loop
po1_7_nodes = [po1_6, scale_integration_po]
po1_7 = StrictPartialOrder(nodes=po1_7_nodes)
po1_7.order.add_edge(po1_6, scale_integration_po)

# 8: change management and knowledge transfer after scale and integration
root = StrictPartialOrder(nodes=[po1_7, change_kt_po])
root.order.add_edge(po1_7, change_kt_po)