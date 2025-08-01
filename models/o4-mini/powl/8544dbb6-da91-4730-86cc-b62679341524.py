# Generated from: 8544dbb6-da91-4730-86cc-b62679341524.json
# Description: This process governs the end-to-end management of urban beekeeping supplies, starting from sourcing sustainable materials to packaging and distributing specialized equipment tailored for city environments. It involves coordinating with local artisans for custom hive designs, ensuring regulatory compliance for urban apiaries, managing seasonal demand fluctuations, and integrating feedback from beekeepers to continuously improve product offerings while minimizing environmental impact through eco-friendly logistics and waste reduction strategies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
t_ms = Transition(label="Material Sourcing")
t_sv = Transition(label="Supplier Vetting")
t_dc = Transition(label="Design Customization")
t_pt = Transition(label="Prototype Testing")
t_rr = Transition(label="Regulation Review")
t_ca = Transition(label="Compliance Audit")
t_is = Transition(label="Inventory Setup")
t_sp = Transition(label="Seasonal Planning")
t_df = Transition(label="Demand Forecast")
t_op = Transition(label="Order Processing")
t_al = Transition(label="Assembly Line")
t_qc = Transition(label="Quality Check")
t_pd = Transition(label="Packaging Design")
t_el = Transition(label="Eco Logistics")
t_wm = Transition(label="Waste Management")
t_ct = Transition(label="Customer Training")
t_fa = Transition(label="Feedback Analysis")

# Silent skip for optional compliance audit
skip = SilentTransition()

# Loop for prototype‐test cycle: first Prototype Testing, then optionally redesign and test again
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[t_pt, t_dc])

# Exclusive choice: either do a Compliance Audit or skip it
choice_compliance = OperatorPOWL(operator=Operator.XOR, children=[t_ca, skip])

# Feedback‐driven redesign loop: analyze feedback then optionally go back to Design Customization
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[t_fa, t_dc])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    t_ms, t_sv, t_dc, test_loop,
    t_is, t_sp, t_df, t_op, t_al, t_qc, t_pd,
    t_rr, choice_compliance,
    t_el, t_wm, t_ct, feedback_loop
])

# Define the control‐flow edges
root.order.add_edge(t_ms, t_sv)

# After vetting we both set up inventory and start customization in parallel
root.order.add_edge(t_sv, t_is)
root.order.add_edge(t_sv, t_dc)

# After design, enter the prototype‐test loop
root.order.add_edge(t_dc, test_loop)

# Inventory setup leads to seasonal planning → demand forecast
root.order.add_edge(t_is, t_sp)
root.order.add_edge(t_sp, t_df)

# Join: after demand forecast and test_loop complete, process orders
root.order.add_edge(t_df, t_op)
root.order.add_edge(test_loop, t_op)

# Core production line
root.order.add_edge(t_op, t_al)
root.order.add_edge(t_al, t_qc)
root.order.add_edge(t_qc, t_pd)

# Regulatory compliance after packaging design
root.order.add_edge(t_pd, t_rr)
root.order.add_edge(t_rr, choice_compliance)

# After (optional) audit, do eco‐logistics and waste management concurrently
root.order.add_edge(choice_compliance, t_el)
root.order.add_edge(choice_compliance, t_wm)

# Both logistics and waste management must complete before customer training
root.order.add_edge(t_el, t_ct)
root.order.add_edge(t_wm, t_ct)

# After training, enter the feedback loop
root.order.add_edge(t_ct, feedback_loop)