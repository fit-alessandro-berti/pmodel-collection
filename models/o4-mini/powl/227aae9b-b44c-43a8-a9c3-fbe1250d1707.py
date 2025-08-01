# Generated from: 227aae9b-b44c-43a8-a9c3-fbe1250d1707.json
# Description: This process outlines the detailed steps involved in authenticating historical artifacts for museums or private collectors. It begins with initial artifact intake and documentation, followed by non-invasive imaging and chemical analysis to identify materials and age. Experts conduct provenance research and comparative stylistic evaluation to verify authenticity. If discrepancies arise, advanced techniques like carbon dating or microscopic fiber analysis are employed. After scientific validation, legal checks ensure compliance with cultural heritage laws. The process concludes with detailed reporting, certification issuance, and secure archive storage. Throughout, cross-disciplinary collaboration and iterative reviews maintain accuracy and integrity in authentication.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
intake = Transition(label='Artifact Intake')
scan = Transition(label='Initial Scan')
material = Transition(label='Material Test')
pc1 = Transition(label='Provenance Check')
sc1 = Transition(label='Style Compare')
panel = Transition(label='Expert Panel')
pc2 = Transition(label='Provenance Check')
sc2 = Transition(label='Style Compare')
carbon = Transition(label='Carbon Dating')
fiber = Transition(label='Fiber Analysis')
legal = Transition(label='Legal Review')
cond_report = Transition(label='Condition Report')
certification = Transition(label='Certification')
final_approval = Transition(label='Final Approval')
client_brief = Transition(label='Client Brief')
data_archive = Transition(label='Data Archive')
secure_storage = Transition(label='Secure Storage')
skip = SilentTransition()

# 1) After intake, imaging and chemical analysis can run in parallel
par_initial = StrictPartialOrder(nodes=[scan, material])

# 2) After that, provenance check & style compare in parallel
par_prov_style = StrictPartialOrder(nodes=[pc1, sc1])

# 3) Expert panel with iterative reviews (loop: panel ⇒ (re-check ⇒ panel)* )
par_review = StrictPartialOrder(nodes=[pc2, sc2])
loop_panel = OperatorPOWL(operator=Operator.LOOP, children=[panel, par_review])

# 4) If discrepancies, either do advanced analyses in parallel or skip
par_advanced = StrictPartialOrder(nodes=[carbon, fiber])
choice_advanced = OperatorPOWL(operator=Operator.XOR, children=[par_advanced, skip])

# 5) After scientific & legal checks, produce report, certify, approve
#    then archive data, brief client, and secure storage in parallel
end_block = StrictPartialOrder(nodes=[client_brief, data_archive, secure_storage])

# Assemble the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        intake,
        par_initial,
        par_prov_style,
        loop_panel,
        choice_advanced,
        legal,
        cond_report,
        certification,
        final_approval,
        end_block
    ]
)

# Define the control‐flow order
root.order.add_edge(intake, par_initial)
root.order.add_edge(par_initial, par_prov_style)
root.order.add_edge(par_prov_style, loop_panel)
root.order.add_edge(loop_panel, choice_advanced)
root.order.add_edge(choice_advanced, legal)
root.order.add_edge(legal, cond_report)
root.order.add_edge(cond_report, certification)
root.order.add_edge(certification, final_approval)
root.order.add_edge(final_approval, end_block)