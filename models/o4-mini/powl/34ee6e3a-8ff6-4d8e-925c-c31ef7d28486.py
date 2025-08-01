# Generated from: 34ee6e3a-8ff6-4d8e-925c-c31ef7d28486.json
# Description: This process outlines the detailed workflow for authenticating historical artifacts within a museum's conservation department. It involves multidisciplinary collaboration among historians, material scientists, and digital analysts to verify provenance, composition, and authenticity. The workflow begins with initial artifact intake and condition assessment, followed by archival research and comparative analysis using advanced imaging techniques. Subsequent steps include chemical testing, digital fingerprinting, and expert panel review. The process concludes with documentation, digital cataloging, and preparation for public exhibition or secure storage, ensuring each artifact's legitimacy and preservation status are thoroughly validated before display or archival.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifactIntake   = Transition(label='Artifact Intake')
conditionCheck   = Transition(label='Condition Check')
archivalSearch   = Transition(label='Archival Search')
imagingScan      = Transition(label='Imaging Scan')
provenanceMap    = Transition(label='Provenance Map')
materialTest     = Transition(label='Material Test')
digitalTrace     = Transition(label='Digital Trace')
expertReview     = Transition(label='Expert Review')
panelMeeting     = Transition(label='Panel Meeting')
finalApproval    = Transition(label='Final Approval')
dataCorrelate    = Transition(label='Data Correlate')
reportDraft      = Transition(label='Report Draft')
catalogEntry     = Transition(label='Catalog Entry')
exhibitPrep      = Transition(label='Exhibit Prep')
storageSetup     = Transition(label='Storage Setup')

# Choice for end: either prepare for exhibition or secure storage
endChoice = OperatorPOWL(operator=Operator.XOR, children=[exhibitPrep, storageSetup])

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifactIntake, conditionCheck,
    archivalSearch, imagingScan, provenanceMap,
    materialTest, digitalTrace,
    expertReview, panelMeeting, finalApproval,
    dataCorrelate, reportDraft, catalogEntry,
    endChoice
])

# Control-flow edges
root.order.add_edge(artifactIntake, conditionCheck)

# Parallel research & imaging
root.order.add_edge(conditionCheck, archivalSearch)
root.order.add_edge(conditionCheck, imagingScan)

# Collate provenance
root.order.add_edge(archivalSearch, provenanceMap)
root.order.add_edge(imagingScan, provenanceMap)

# Testing & fingerprinting
root.order.add_edge(provenanceMap, materialTest)
root.order.add_edge(provenanceMap, digitalTrace)

# Expert review
root.order.add_edge(materialTest, expertReview)
root.order.add_edge(digitalTrace, expertReview)
root.order.add_edge(expertReview, panelMeeting)

# Approval
root.order.add_edge(panelMeeting, finalApproval)

# Documentation
root.order.add_edge(finalApproval, dataCorrelate)
root.order.add_edge(dataCorrelate, reportDraft)

# Catalog entry then final choice
root.order.add_edge(reportDraft, catalogEntry)
root.order.add_edge(catalogEntry, endChoice)