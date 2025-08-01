# Generated from: 34ee6e3a-8ff6-4d8e-925c-c31ef7d28486.json
# Description: This process outlines the detailed workflow for authenticating historical artifacts within a museum's conservation department. It involves multidisciplinary collaboration among historians, material scientists, and digital analysts to verify provenance, composition, and authenticity. The workflow begins with initial artifact intake and condition assessment, followed by archival research and comparative analysis using advanced imaging techniques. Subsequent steps include chemical testing, digital fingerprinting, and expert panel review. The process concludes with documentation, digital cataloging, and preparation for public exhibition or secure storage, ensuring each artifact's legitimacy and preservation status are thoroughly validated before display or archival.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ArtifactIntake = Transition(label='Artifact Intake')
ConditionCheck = Transition(label='Condition Check')
ArchivalSearch = Transition(label='Archival Search')
ImagingScan = Transition(label='Imaging Scan')
MaterialTest = Transition(label='Material Test')
DigitalTrace = Transition(label='Digital Trace')
ProvenanceMap = Transition(label='Provenance Map')
ExpertReview = Transition(label='Expert Review')
DataCorrelate = Transition(label='Data Correlate')
ReportDraft = Transition(label='Report Draft')
PanelMeeting = Transition(label='Panel Meeting')
FinalApproval = Transition(label='Final Approval')
CatalogEntry = Transition(label='Catalog Entry')
ExhibitPrep = Transition(label='Exhibit Prep')
StorageSetup = Transition(label='Storage Setup')

# Define sub partial orders and operators representing the process described

# Initial intake and condition assessment (serial)
init_PO = StrictPartialOrder(nodes=[ArtifactIntake, ConditionCheck])
init_PO.order.add_edge(ArtifactIntake, ConditionCheck)

# Archival research and imaging scan (concurrent)
research_imaging_PO = StrictPartialOrder(nodes=[ArchivalSearch, ImagingScan])

# Chemical testing and digital fingerprinting (concurrent)
testing_fingerprinting_PO = StrictPartialOrder(nodes=[MaterialTest, DigitalTrace])

# Provenance map and expert review (serial)
prov_exp_PO = StrictPartialOrder(nodes=[ProvenanceMap, ExpertReview])
prov_exp_PO.order.add_edge(ProvenanceMap, ExpertReview)

# Data correlate and report draft (serial)
data_report_PO = StrictPartialOrder(nodes=[DataCorrelate, ReportDraft])
data_report_PO.order.add_edge(DataCorrelate, ReportDraft)

# Panel meeting and final approval (serial)
panel_final_PO = StrictPartialOrder(nodes=[PanelMeeting, FinalApproval])
panel_final_PO.order.add_edge(PanelMeeting, FinalApproval)

# Documentation & digital cataloging (serial)
doc_catalog_PO = StrictPartialOrder(nodes=[CatalogEntry])

# Preparation for exhibit or storage is a choice (exclusive choice)
exhibit_or_storage = OperatorPOWL(operator=Operator.XOR, children=[ExhibitPrep, StorageSetup])

# Now, combine the major blocks into a PO:
# The top-level ordering:
#   init_PO --> research_imaging_PO --> testing_fingerprinting_PO --> prov_exp_PO --> data_report_PO --> panel_final_PO --> doc_catalog_PO --> exhibit_or_storage

root = StrictPartialOrder(nodes=[
    init_PO,
    research_imaging_PO,
    testing_fingerprinting_PO,
    prov_exp_PO,
    data_report_PO,
    panel_final_PO,
    doc_catalog_PO,
    exhibit_or_storage
])

# Add edges reflecting the stated sequence
root.order.add_edge(init_PO, research_imaging_PO)
root.order.add_edge(research_imaging_PO, testing_fingerprinting_PO)
root.order.add_edge(testing_fingerprinting_PO, prov_exp_PO)
root.order.add_edge(prov_exp_PO, data_report_PO)
root.order.add_edge(data_report_PO, panel_final_PO)
root.order.add_edge(panel_final_PO, doc_catalog_PO)
root.order.add_edge(doc_catalog_PO, exhibit_or_storage)