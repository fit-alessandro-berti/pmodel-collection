# Generated from: 0c9a71a9-262d-4b3d-9858-d7dcd2f3b895.json
# Description: This process outlines the comprehensive steps involved in authenticating antique items for resale or auction. It begins with initial item intake and visual inspection, followed by provenance research and materials analysis using advanced spectroscopy. Expert consultations and historical context verification ensure accurate dating and origin identification. Condition reporting and restoration feasibility assessments are conducted next, before generating a detailed certification report. Finally, the item is digitally documented, insured, and prepared for market listing or archival storage, ensuring traceability and compliance with legal regulations throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
ItemIntake = Transition(label='Item Intake')
VisualInspect = Transition(label='Visual Inspect')

ProvenanceCheck = Transition(label='Provenance Check')

MaterialsScan = Transition(label='Materials Scan')
SpectroscopyTest = Transition(label='Spectroscopy Test')

ExpertConsult = Transition(label='Expert Consult')

ContextVerify = Transition(label='Context Verify')
DateConfirm = Transition(label='Date Confirm')
OriginIdentify = Transition(label='Origin Identify')

ConditionReport = Transition(label='Condition Report')
RestorationPlan = Transition(label='Restoration Plan')

CertificationGen = Transition(label='Certification Gen')

DigitalArchive = Transition(label='Digital Archive')
InsuranceSetup = Transition(label='Insurance Setup')

MarketPrep = Transition(label='Market Prep')

# Provenance research partial order: Provenance Check → (Materials Scan → Spectroscopy Test)
provenance_research = StrictPartialOrder(nodes=[ProvenanceCheck, MaterialsScan, SpectroscopyTest])
provenance_research.order.add_edge(ProvenanceCheck, MaterialsScan)
provenance_research.order.add_edge(MaterialsScan, SpectroscopyTest)

# Expert consultations and historical verification partial order:
# Expert Consult → (Context Verify → Date Confirm, Origin Identify)
expert_and_verification = StrictPartialOrder(
    nodes=[ExpertConsult, ContextVerify, DateConfirm, OriginIdentify]
)
expert_and_verification.order.add_edge(ExpertConsult, ContextVerify)
expert_and_verification.order.add_edge(ContextVerify, DateConfirm)
expert_and_verification.order.add_edge(ContextVerify, OriginIdentify)
# Date Confirm and Origin Identify are concurrent after Context Verify

# Condition reporting and restoration plan partial order:
cond_and_restore = StrictPartialOrder(nodes=[ConditionReport, RestorationPlan])
cond_and_restore.order.add_edge(ConditionReport, RestorationPlan)

# Final documentation and market prep partial order:
final_docs = StrictPartialOrder(nodes=[DigitalArchive, InsuranceSetup, MarketPrep])
final_docs.order.add_edge(DigitalArchive, InsuranceSetup)
final_docs.order.add_edge(InsuranceSetup, MarketPrep)

# Assemble the full partial order

# Initial sequence: Item Intake → Visual Inspect
initial = StrictPartialOrder(nodes=[ItemIntake, VisualInspect])
initial.order.add_edge(ItemIntake, VisualInspect)

# Then the provenance research after Visual Inspect
po1 = StrictPartialOrder(nodes=[initial, provenance_research])
po1.order.add_edge(initial, provenance_research)

# Then expert consultations and verification after provenance research
po2 = StrictPartialOrder(nodes=[po1, expert_and_verification])
po2.order.add_edge(po1, expert_and_verification)

# Then condition reporting and restoration plan after expert verification
po3 = StrictPartialOrder(nodes=[po2, cond_and_restore])
po3.order.add_edge(po2, cond_and_restore)

# Then certification generation after restoration plan
cert_gen = StrictPartialOrder(nodes=[CertificationGen])
# Connect restoration plan to CertificationGen
po4 = StrictPartialOrder(nodes=[po3, cert_gen])
po4.order.add_edge(po3, cert_gen)

# Then final documentation sequence after certification generation
root = StrictPartialOrder(nodes=[po4, final_docs])
root.order.add_edge(po4, final_docs)