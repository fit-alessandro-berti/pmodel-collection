# Generated from: e5f30513-2f2d-4e30-a95f-d16edc56a39e.json
# Description: This process outlines the detailed steps involved in authenticating rare historical artifacts for a high-profile auction house. It begins with initial artifact intake and preliminary inspection, followed by provenance verification through archival research. Scientific analysis, including material composition and radiocarbon dating, is conducted to confirm authenticity. Parallelly, expert consultations are arranged to assess stylistic and cultural relevance. Findings are compiled into a comprehensive report, reviewed internally, and then presented to the client. Final approval triggers secure packaging and logistics coordination for transport to the auction venue. Throughout, strict chain-of-custody protocols ensure artifact integrity and legal compliance, minimizing risks of forgery or damage during handling and transit.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
intake_review      = Transition(label="Intake Review")
preliminary_inspect= Transition(label="Preliminary Inspect")
prov_check         = Transition(label="Provenance Check")
arch_research      = Transition(label="Archival Research")
mat_testing        = Transition(label="Material Testing")
rad_date           = Transition(label="Radiocarbon Date")
styl_assess        = Transition(label="Stylistic Assess")
expert_consult     = Transition(label="Expert Consult")
findings_compile   = Transition(label="Findings Compile")
internal_review    = Transition(label="Internal Review")
client_present     = Transition(label="Client Present")
approval_confirm   = Transition(label="Approval Confirm")
secure_package     = Transition(label="Secure Package")
transport_arrange  = Transition(label="Transport Arrange")
chain_custody      = Transition(label="Chain Custody")

# Sub-workflow: Provenance verification (sequential)
prov_workflow = StrictPartialOrder(nodes=[prov_check, arch_research])
prov_workflow.order.add_edge(prov_check, arch_research)

# Sub-workflow: Scientific analysis (sequential)
sci_workflow = StrictPartialOrder(nodes=[mat_testing, rad_date])
sci_workflow.order.add_edge(mat_testing, rad_date)

# Sub-workflow: Expert consultations (sequential)
expert_workflow = StrictPartialOrder(nodes=[styl_assess, expert_consult])
expert_workflow.order.add_edge(styl_assess, expert_consult)

# Root workflow with concurrency and sequencing
root = StrictPartialOrder(nodes=[
    intake_review,
    preliminary_inspect,
    prov_workflow,
    sci_workflow,
    expert_workflow,
    findings_compile,
    internal_review,
    client_present,
    approval_confirm,
    secure_package,
    transport_arrange,
    chain_custody
])

# Main sequence: Intake -> Preliminary Inspect
root.order.add_edge(intake_review, preliminary_inspect)

# After Preliminary Inspect, three subprocesses run in parallel
root.order.add_edge(preliminary_inspect, prov_workflow)
root.order.add_edge(preliminary_inspect, sci_workflow)
root.order.add_edge(preliminary_inspect, expert_workflow)

# After all three subprocesses complete -> Findings Compile
root.order.add_edge(prov_workflow, findings_compile)
root.order.add_edge(sci_workflow, findings_compile)
root.order.add_edge(expert_workflow, findings_compile)

# Then sequential review and approval
root.order.add_edge(findings_compile, internal_review)
root.order.add_edge(internal_review, client_present)
root.order.add_edge(client_present, approval_confirm)

# Final packaging & transport
root.order.add_edge(approval_confirm, secure_package)
root.order.add_edge(secure_package, transport_arrange)

# 'Chain Custody' runs concurrently throughout (no explicit edges)