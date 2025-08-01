# Generated from: f57cbd7d-ff36-409a-a665-c39f15b9925b.json
# Description: This process outlines the end-to-end flow for managing corporate innovation projects that deviate from traditional R&D workflows. It begins with external trend scanning and internal ideation sprints, followed by cross-departmental feasibility reviews and risk assessments. Selected ideas progress through rapid prototyping using minimal viable technologies, then undergo market simulation and stakeholder alignment workshops. Post-validation, projects enter a resource allocation phase involving budget rebalancing and talent sourcing, before moving into iterative pilot launches with continuous data-driven refinements. The process concludes with scalability analysis and integration planning to embed successful innovations into existing business units while managing change and knowledge transfer effectively across teams.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t_ts    = Transition(label='Trend Scan')
t_is    = Transition(label='Idea Sprint')
t_fc    = Transition(label='Feasibility Check')
t_rr    = Transition(label='Risk Review')
t_tp    = Transition(label='Tech Prototype')
t_ms    = Transition(label='Market Simulate')
t_sa    = Transition(label='Stakeholder Align')
t_ba    = Transition(label='Budget Adjust')
t_tsrc  = Transition(label='Talent Source')
t_pl    = Transition(label='Pilot Launch')
t_dr    = Transition(label='Data Refine')
t_sca   = Transition(label='Scale Analysis')
t_ip    = Transition(label='Integration Plan')
t_cm    = Transition(label='Change Manage')
t_kt    = Transition(label='Knowledge Transfer')

# Define the iterative pilot loop: launch then refine
loop_pilot = OperatorPOWL(operator=Operator.LOOP, children=[t_pl, t_dr])

# Assemble the partial order
root = StrictPartialOrder(nodes=[
    t_ts, t_is,
    t_fc, t_rr,
    t_tp,
    t_ms, t_sa,
    t_ba, t_tsrc,
    loop_pilot,
    t_sca, t_ip, t_cm, t_kt
])

# Initial parallel: Trend Scan & Idea Sprint -> Feasibility & Risk
root.order.add_edge(t_ts,  t_fc)
root.order.add_edge(t_is,  t_fc)
root.order.add_edge(t_ts,  t_rr)
root.order.add_edge(t_is,  t_rr)

# Feasibility & Risk -> Prototype
root.order.add_edge(t_fc,  t_tp)
root.order.add_edge(t_rr,  t_tp)

# Prototype -> Market Simulate & Stakeholder Align
root.order.add_edge(t_tp,  t_ms)
root.order.add_edge(t_tp,  t_sa)

# Market Simulate & Stakeholder Align -> Budget Adjust & Talent Source
root.order.add_edge(t_ms,   t_ba)
root.order.add_edge(t_sa,   t_ba)
root.order.add_edge(t_ms,   t_tsrc)
root.order.add_edge(t_sa,   t_tsrc)

# Resource allocation -> iterative pilot loop
root.order.add_edge(t_ba,    loop_pilot)
root.order.add_edge(t_tsrc,  loop_pilot)

# After pilots -> Scale Analysis -> Integration Plan -> Change Manage -> Knowledge Transfer
root.order.add_edge(loop_pilot, t_sca)
root.order.add_edge(t_sca,      t_ip)
root.order.add_edge(t_ip,       t_cm)
root.order.add_edge(t_cm,       t_kt)