# Generated from: d06f813d-3ddc-4677-bbb0-504bf9218be7.json
# Description: This process outlines the comprehensive steps involved in authenticating historical artifacts for museum acquisition. It begins with initial provenance research, followed by multi-disciplinary scientific testing including spectroscopy and radiocarbon dating. Expert consultations and forensic analysis are conducted to verify authenticity, while legal checks ensure clear ownership. Parallelly, risk assessment and insurance valuation take place. The process concludes with detailed documentation and final approval by the acquisition committee, ensuring the artifact's legitimacy and compliance with regulatory standards before procurement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activity transitions
prov_check = Transition(label='Provenance Check')
specimen_sampling = Transition(label='Specimen Sampling')
spectroscopy_test = Transition(label='Spectroscopy Test')
radiocarbon_date = Transition(label='Radiocarbon Date')
material_analysis = Transition(label='Material Analysis')
expert_consult = Transition(label='Expert Consult')
forensic_review = Transition(label='Forensic Review')
legal_verify = Transition(label='Legal Verify')
ownership_audit = Transition(label='Ownership Audit')
risk_assess = Transition(label='Risk Assess')
insurance_quote = Transition(label='Insurance Quote')
condition_report = Transition(label='Condition Report')
documentation = Transition(label='Documentation')
committee_review = Transition(label='Committee Review')
final_approval = Transition(label='Final Approval')

# Scientific testing: spectroscopy and radiocarbon in parallel, then material analysis
sci_tests = StrictPartialOrder(nodes=[spectroscopy_test, radiocarbon_date, material_analysis])
sci_tests.order.add_edge(spectroscopy_test, material_analysis)
sci_tests.order.add_edge(radiocarbon_date, material_analysis)

# Authenticity branch: expert consult and forensic review in parallel
auth_branch = StrictPartialOrder(nodes=[expert_consult, forensic_review])
# Legal branch: sequential legal verify -> ownership audit
legal_branch = StrictPartialOrder(nodes=[legal_verify, ownership_audit])
legal_branch.order.add_edge(legal_verify, ownership_audit)
# Risk/insurance branch: sequential risk assess -> insurance quote
risk_branch = StrictPartialOrder(nodes=[risk_assess, insurance_quote])
risk_branch.order.add_edge(risk_assess, insurance_quote)

# Combine branches in parallel
branch_po = StrictPartialOrder(nodes=[auth_branch, legal_branch, risk_branch])

# Build the overall process
root = StrictPartialOrder(nodes=[
    prov_check,
    specimen_sampling,
    sci_tests,
    branch_po,
    condition_report,
    documentation,
    committee_review,
    final_approval
])
# Sequence edges
root.order.add_edge(prov_check, specimen_sampling)
root.order.add_edge(specimen_sampling, sci_tests)
root.order.add_edge(sci_tests, branch_po)
root.order.add_edge(branch_po, condition_report)
root.order.add_edge(condition_report, documentation)
root.order.add_edge(documentation, committee_review)
root.order.add_edge(committee_review, final_approval)