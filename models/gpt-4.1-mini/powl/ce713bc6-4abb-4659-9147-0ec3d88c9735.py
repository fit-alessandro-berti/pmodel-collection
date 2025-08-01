# Generated from: ce713bc6-4abb-4659-9147-0ec3d88c9735.json
# Description: This process involves the detailed verification and authentication of cultural artifacts before acquisition by a museum or private collector. It includes multi-layered historical research, forensic material analysis, legal ownership tracing, and ethical compliance checks. The process ensures that each artifact's origin is accurately documented to prevent illicit trade and to uphold provenance integrity. Activities consist of interdisciplinary collaboration among historians, scientists, legal experts, and conservators, culminating in a comprehensive provenance report and approval for acquisition or repatriation decisions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Initial_Inquiry = Transition(label='Initial Inquiry')
Document_Review = Transition(label='Document Review')
Historical_Research = Transition(label='Historical Research')
Material_Sampling = Transition(label='Material Sampling')
Forensic_Testing = Transition(label='Forensic Testing')
Ownership_Audit = Transition(label='Ownership Audit')
Legal_Verification = Transition(label='Legal Verification')
Ethical_Screening = Transition(label='Ethical Screening')
Expert_Consultation = Transition(label='Expert Consultation')
Cultural_Assessment = Transition(label='Cultural Assessment')
Condition_Survey = Transition(label='Condition Survey')
Provenance_Mapping = Transition(label='Provenance Mapping')
Risk_Analysis = Transition(label='Risk Analysis')
Report_Compilation = Transition(label='Report Compilation')
Acquisition_Approval = Transition(label='Acquisition Approval')
Repatriation_Review = Transition(label='Repatriation Review')
Archival_Storage = Transition(label='Archival Storage')

# Part 1: Initial inquiry and document review
# Initial Inquiry -> Document Review
po_1 = StrictPartialOrder(nodes=[Initial_Inquiry, Document_Review])
po_1.order.add_edge(Initial_Inquiry, Document_Review)

# Part 2: Historical Research (historians) and Forensic Testing (scientists) in parallel
# Historical Research runs first, then fork forensic path and ownership+legal path
# Historical Research before Material Sampling
po_hist = StrictPartialOrder(nodes=[Historical_Research, Material_Sampling])
po_hist.order.add_edge(Historical_Research, Material_Sampling)
# Material Sampling before Forensic Testing
po_forensic = StrictPartialOrder(nodes=[Material_Sampling, Forensic_Testing])
po_forensic.order.add_edge(Material_Sampling, Forensic_Testing)

# Ownership Audit and Legal Verification happen in parallel after Document Review
po_ownership_legal = StrictPartialOrder(nodes=[Ownership_Audit, Legal_Verification])
# no edges, concurrent

# After forensic testing, ownership audit and legal verification, these join into Ethical Screening
# For this, we create a PO that synchronizes Forensic Testing, Ownership Audit, Legal Verification before Ethical Screening

# Combine forensic, ownership and legal in one PO, with edges to Ethical Screening
# Nodes: Forensic Testing, Ownership Audit, Legal Verification, Ethical Screening
po_ethics = StrictPartialOrder(nodes=[Forensic_Testing, Ownership_Audit, Legal_Verification, Ethical_Screening])
po_ethics.order.add_edge(Forensic_Testing, Ethical_Screening)
po_ethics.order.add_edge(Ownership_Audit, Ethical_Screening)
po_ethics.order.add_edge(Legal_Verification, Ethical_Screening)

# Part 3: Expert Consultation and Cultural Assessment in parallel after Ethical Screening
po_expert_cultural = StrictPartialOrder(nodes=[Expert_Consultation, Cultural_Assessment])
# no edges, concurrent

# Both  Expert Consultation and Cultural Assessment before Condition Survey
po_condition = StrictPartialOrder(nodes=[Expert_Consultation, Cultural_Assessment, Condition_Survey])
po_condition.order.add_edge(Expert_Consultation, Condition_Survey)
po_condition.order.add_edge(Cultural_Assessment, Condition_Survey)

# Condition Survey before Provenance Mapping
po_map = StrictPartialOrder(nodes=[Condition_Survey, Provenance_Mapping])
po_map.order.add_edge(Condition_Survey, Provenance_Mapping)

# Provenance Mapping before Risk Analysis
po_risk = StrictPartialOrder(nodes=[Provenance_Mapping, Risk_Analysis])
po_risk.order.add_edge(Provenance_Mapping, Risk_Analysis)

# Risk Analysis before Report Compilation
po_report = StrictPartialOrder(nodes=[Risk_Analysis, Report_Compilation])
po_report.order.add_edge(Risk_Analysis, Report_Compilation)

# After report compilation, decision choice:
# Either Acquisition Approval or Repatriation Review (exclusive choice)
decision_choice = OperatorPOWL(operator=Operator.XOR, children=[Acquisition_Approval, Repatriation_Review])

# Both choices lead to Archival Storage (final)
po_final = StrictPartialOrder(nodes=[decision_choice, Archival_Storage])
po_final.order.add_edge(decision_choice, Archival_Storage)

# Now link all partial orders into a big PO reflecting the overall process

# We'll create a PO with all main nodes as sub-POs or transitions:
# po_1 (Initial Inquiry -> Document Review)
# po_hist + po_forensic (Historical Research -> Material Sampling -> Forensic Testing)
# po_ownership_legal (Ownership Audit, Legal Verification)
# po_ethics (Forensic Testing, Ownership Audit, Legal Verification -> Ethical Screening)
# po_expert_cultural (Expert Consultation, Cultural Assessment)
# po_condition, po_map, po_risk, po_report (linear)
# decision_choice (XOR)
# po_final (decision -> Archival Storage)

# For clarity: 
# Document Review leads to Historical Research (start of research), and also triggers Ownership & Legal audits
# Historical Research is predecessor of Material Sampling (forensic path)
# So Document Review -> Historical Research
# Document Review -> Ownership Audit and Legal Verification
# For forensic, pass through Historical Research and Material Sampling to Forensic Testing
# Forensic Testing, Ownership Audit, and Legal Verification converge on Ethical Screening
# Ethical Screening -> Expert Consultation and Cultural Assessment (concurrent)
# Both -> Condition Survey -> Provenance Mapping -> Risk Analysis -> Report Compilation -> Decision -> Archival Storage

# Let's create the big StrictPartialOrder with all nodes:

nodes_all = [
    po_1,  # contains Initial Inquiry, Document Review
    po_hist,  # Historical Research -> Material Sampling
    Forensic_Testing,
    po_ownership_legal,  # Ownership Audit, Legal Verification
    po_ethics,  # Forensic Testing, Ownership Audit, Legal Verification -> Ethical Screening
    po_expert_cultural,  # Expert Consultation, Cultural Assessment
    po_condition,  # Expert Consultation, Cultural Assessment -> Condition Survey
    po_map,  # Condition Survey -> Provenance Mapping
    po_risk,  # Provenance Mapping -> Risk Analysis
    po_report,  # Risk Analysis -> Report Compilation
    decision_choice,  # XOR choice: Acquisition Approval or Repatriation Review
    Archival_Storage
]

root = StrictPartialOrder(nodes=nodes_all)

# Add edges for top-level ordering

# po_1 Document Review precedes Historical Research and Ownership/Legal audits
# We add edges from po_1 -> po_hist and po_1 -> po_ownership_legal

root.order.add_edge(po_1, po_hist)
root.order.add_edge(po_1, po_ownership_legal)

# po_hist -> Forensic Testing 
root.order.add_edge(po_hist, Forensic_Testing)

# po_ownership_legal are parallel to Forensic Testing, so no order edges among them
# po_ethics includes Forensic Testing, Ownership_Audit, Legal_Verification and Ethical Screening
# so we connect Forensic Testing, Ownership_Audit, Legal_Verification (inside po_ethics)
# But at root level, Forensic Testing and po_ownership_legal precede po_ethics
root.order.add_edge(Forensic_Testing, po_ethics)
root.order.add_edge(po_ownership_legal, po_ethics)

# po_ethics -> po_expert_cultural
root.order.add_edge(po_ethics, po_expert_cultural)

# po_expert_cultural -> po_condition
root.order.add_edge(po_expert_cultural, po_condition)

# po_condition -> po_map
root.order.add_edge(po_condition, po_map)

# po_map -> po_risk
root.order.add_edge(po_map, po_risk)

# po_risk -> po_report
root.order.add_edge(po_risk, po_report)

# po_report -> decision_choice
root.order.add_edge(po_report, decision_choice)

# decision_choice -> Archival_Storage (already in po_final, but here we add explicitly for root)
root.order.add_edge(decision_choice, Archival_Storage)