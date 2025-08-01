# Generated from: 09184b10-be75-4f64-ab55-47873349a23d.json
# Description: This process involves the authentication and provenance verification of rare artifacts, combining scientific analysis, historical research, and legal validation. The workflow includes initial artifact inspection, material composition testing, provenance tracing through archival databases, expert consultations, and legal ownership verification. Additional steps cover condition reporting, restoration assessment, forgery detection, and final certification issuance. This atypical process requires coordination between archaeologists, chemists, historians, legal experts, and conservators to ensure an artifact's authenticity and legality before it can be acquired or exhibited. The complex interplay of scientific, historical, and legal evaluations makes this process unique in the business context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_intake     = Transition(label='Artifact Intake')
t_visual     = Transition(label='Visual Scan')
t_material   = Transition(label='Material Test')
t_data       = Transition(label='Data Logging')
t_archive    = Transition(label='Archive Search')
t_expert     = Transition(label='Expert Consult')
t_condition  = Transition(label='Condition Check')
t_forgery    = Transition(label='Forgery Scan')
t_ownership  = Transition(label='Ownership Check')
t_legal      = Transition(label='Legal Review')
t_restoration= Transition(label='Restoration Plan')
t_report     = Transition(label='Report Draft')
t_cert       = Transition(label='Certification')
t_client     = Transition(label='Client Brief')
t_final      = Transition(label='Final Approval')
t_return     = Transition(label='Artifact Return')

# Silent transition for skipping branches
skip = SilentTransition()

# Loop: repeat archival search and expert consult until satisfied
loop_prov = OperatorPOWL(operator=Operator.LOOP, children=[t_archive, t_expert])

# XOR after forgery scan: either return immediately or continue workflow
xor_forgery = OperatorPOWL(operator=Operator.XOR, children=[t_return, skip])

# Build the overall partial order
root = StrictPartialOrder(
    nodes=[
        t_intake, t_visual, 
        t_material, t_data, 
        loop_prov, 
        t_condition, t_forgery, t_ownership, xor_forgery, 
        t_legal, t_restoration, t_report, 
        t_cert, t_client, t_final, t_return
    ]
)

# Define the control-flow dependencies
root.order.add_edge(t_intake,     t_visual)
root.order.add_edge(t_visual,     t_material)
root.order.add_edge(t_visual,     loop_prov)
root.order.add_edge(t_material,   t_data)
root.order.add_edge(loop_prov,    t_data)

root.order.add_edge(t_data,       t_condition)
root.order.add_edge(t_data,       t_ownership)
root.order.add_edge(t_data,       t_forgery)

root.order.add_edge(t_forgery,    xor_forgery)
root.order.add_edge(xor_forgery,  t_legal)

root.order.add_edge(t_condition,  t_legal)
root.order.add_edge(t_ownership,  t_legal)

root.order.add_edge(t_legal,      t_restoration)
root.order.add_edge(t_legal,      t_report)

root.order.add_edge(t_restoration,t_cert)
root.order.add_edge(t_report,     t_cert)

root.order.add_edge(t_cert,       t_client)
root.order.add_edge(t_client,     t_final)
root.order.add_edge(t_final,      t_return)