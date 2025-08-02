# Generated from: ba91bee8-533c-4a35-95b7-2ac1060cfbce.json
# Description: This complex process involves the verification and authentication of ancient artifacts for museums and private collectors. It begins with initial artifact intake and condition assessment, followed by material analysis using spectroscopy and radiocarbon dating. Next, provenance research is conducted through archival exploration and expert consultations. If discrepancies arise, forensic imaging and chemical residue testing are employed to validate authenticity. Concurrently, legal clearance and cultural heritage compliance checks are performed. Once verified, detailed documentation and digital archiving occur, alongside stakeholder reporting and insurance valuation. The final steps include secure packaging and coordinated shipment logistics to the client, ensuring preservation and chain of custody integrity throughout the process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
Artifact_Intake = Transition(label='Artifact Intake')
Condition_Check = Transition(label='Condition Check')

Material_Analysis = Transition(label='Material Analysis')
Spectroscopy_Test = Transition(label='Spectroscopy Test')
Radiocarbon_Date = Transition(label='Radiocarbon Date')

Provenance_Research = Transition(label='Provenance Research')
Archive_Search = Transition(label='Archive Search')
Expert_Consult = Transition(label='Expert Consult')

Forensic_Imaging = Transition(label='Forensic Imaging')
Residue_Testing = Transition(label='Residue Testing')

Legal_Clearance = Transition(label='Legal Clearance')
Compliance_Check = Transition(label='Compliance Check')

Documentation = Transition(label='Documentation')
Digital_Archive = Transition(label='Digital Archive')

Stakeholder_Report = Transition(label='Stakeholder Report')
Insurance_Valuation = Transition(label='Insurance Valuation')

Secure_Packaging = Transition(label='Secure Packaging')
Shipment_Logistics = Transition(label='Shipment Logistics')

# Material Analysis partial order (Spectroscopy Test and Radiocarbon Date concurrent after Material Analysis)
Material_Analysis_PO = StrictPartialOrder(nodes=[Material_Analysis, Spectroscopy_Test, Radiocarbon_Date])
Material_Analysis_PO.order.add_edge(Material_Analysis, Spectroscopy_Test)
Material_Analysis_PO.order.add_edge(Material_Analysis, Radiocarbon_Date)

# Provenance Research partial order (Archive Search and Expert Consult concurrent after Provenance Research)
Provenance_Research_PO = StrictPartialOrder(nodes=[Provenance_Research, Archive_Search, Expert_Consult])
Provenance_Research_PO.order.add_edge(Provenance_Research, Archive_Search)
Provenance_Research_PO.order.add_edge(Provenance_Research, Expert_Consult)

# Discrepancies detected: choice node (X) between skip (no discrepancies) and forensic checks (both concurrent)
forensic_checks_PO = StrictPartialOrder(
    nodes=[Forensic_Imaging, Residue_Testing]
)  # concurrent forensic imaging and residue testing

# XOR choice: either silent skip or forensic_checks_PO
skip = SilentTransition()
discrepancy_choice = OperatorPOWL(operator=Operator.XOR, children=[skip, forensic_checks_PO])

# Legal and Compliance concurrent
legal_compliance_PO = StrictPartialOrder(nodes=[Legal_Clearance, Compliance_Check])
# No explicit order between legal clearance and compliance check -> concurrent

# Verification step partial order: material_analysis_PO --> provenance_research_PO --> discrepancy_choice --> legal_compliance_PO
verification_PO = StrictPartialOrder(
    nodes=[Material_Analysis_PO, Provenance_Research_PO, discrepancy_choice, legal_compliance_PO]
)
verification_PO.order.add_edge(Material_Analysis_PO, Provenance_Research_PO)
verification_PO.order.add_edge(Provenance_Research_PO, discrepancy_choice)
verification_PO.order.add_edge(discrepancy_choice, legal_compliance_PO)

# Documentation partial order (Documentation --> Digital Archive)
documentation_PO = StrictPartialOrder(nodes=[Documentation, Digital_Archive])
documentation_PO.order.add_edge(Documentation, Digital_Archive)

# Reporting partial order (Stakeholder Report --> Insurance Valuation)
reporting_PO = StrictPartialOrder(nodes=[Stakeholder_Report, Insurance_Valuation])
reporting_PO.order.add_edge(Stakeholder_Report, Insurance_Valuation)

# Documentation and reporting concurrent
doc_report_PO = StrictPartialOrder(nodes=[documentation_PO, reporting_PO])
# no edges between documentation_PO and reporting_PO: concurrent partial orders

# After verification_PO comes doc_report_PO
post_verification_PO = StrictPartialOrder(nodes=[verification_PO, doc_report_PO])
post_verification_PO.order.add_edge(verification_PO, doc_report_PO)

# Final packaging partial order (Secure Packaging --> Shipment Logistics)
final_packaging_PO = StrictPartialOrder(nodes=[Secure_Packaging, Shipment_Logistics])
final_packaging_PO.order.add_edge(Secure_Packaging, Shipment_Logistics)

# Full process partial order:
# (Artifact Intake --> Condition Check) --> verification_PO --> doc_report_PO --> final_packaging_PO

initial_PO = StrictPartialOrder(nodes=[Artifact_Intake, Condition_Check])
initial_PO.order.add_edge(Artifact_Intake, Condition_Check)

middle_PO = StrictPartialOrder(nodes=[initial_PO, post_verification_PO])
middle_PO.order.add_edge(initial_PO, post_verification_PO)

root = StrictPartialOrder(nodes=[middle_PO, final_packaging_PO])
root.order.add_edge(middle_PO, final_packaging_PO)