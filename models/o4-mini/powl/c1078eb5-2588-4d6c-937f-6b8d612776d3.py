# Generated from: c1078eb5-2588-4d6c-937f-6b8d612776d3.json
# Description: This process details a comprehensive artifact authentication workflow used by museums and private collectors to verify the provenance and authenticity of rare historical items. It involves multidisciplinary expert evaluations, advanced material analysis, provenance record cross-checking, and digital fingerprinting technology. The workflow integrates collaboration between historians, chemists, and data scientists to ensure artifacts are genuine, mitigating risks of forgeries. Final verification results are documented and archived securely to support insurance and exhibition planning. The process requires iterative validation rounds and consensus building among experts before final certification is granted.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
InitialReview      = Transition(label='Initial Review')
ProvenanceCheck    = Transition(label='Provenance Check')
MaterialScan       = Transition(label='Material Scan')
ChemicalTest       = Transition(label='Chemical Test')
RadiocarbonDate    = Transition(label='Radiocarbon Date')
DigitalImaging     = Transition(label='Digital Imaging')
FingerprintMatch   = Transition(label='Fingerprint Match')
HistoricalCompare  = Transition(label='Historical Compare')
ContextAnalysis    = Transition(label='Context Analysis')
ExpertConsult      = Transition(label='Expert Consult')
ForgeryDetection   = Transition(label='Forgery Detection')
ConsensusMeeting   = Transition(label='Consensus Meeting')
CertificationPrep  = Transition(label='Certification Prep')
Documentation      = Transition(label='Documentation')
ArchiveStorage     = Transition(label='Archive Storage')
InsuranceLiaison   = Transition(label='Insurance Liaison')
ExhibitSetup       = Transition(label='Exhibit Setup')

# Build the redo-part of the validation loop: ForgeryDetection -> ConsensusMeeting
redo_po = StrictPartialOrder(nodes=[ForgeryDetection, ConsensusMeeting])
redo_po.order.add_edge(ForgeryDetection, ConsensusMeeting)

# Loop: ExpertConsult is the body; redo_po is the repetition part
validation_loop = OperatorPOWL(operator=Operator.LOOP, children=[ExpertConsult, redo_po])

# Top‐level partial order
root = StrictPartialOrder(nodes=[
    InitialReview,
    ProvenanceCheck,
    MaterialScan,
    ChemicalTest,
    RadiocarbonDate,
    DigitalImaging,
    FingerprintMatch,
    HistoricalCompare,
    ContextAnalysis,
    validation_loop,
    CertificationPrep,
    Documentation,
    ArchiveStorage,
    InsuranceLiaison,
    ExhibitSetup
])

# Control‐flow dependencies
root.order.add_edge(InitialReview, ProvenanceCheck)
root.order.add_edge(InitialReview, MaterialScan)
root.order.add_edge(InitialReview, DigitalImaging)
root.order.add_edge(ProvenanceCheck, HistoricalCompare)
root.order.add_edge(HistoricalCompare, ContextAnalysis)
root.order.add_edge(MaterialScan, ChemicalTest)
root.order.add_edge(MaterialScan, RadiocarbonDate)
root.order.add_edge(DigitalImaging, FingerprintMatch)

# Join before the expert‐validation loop
root.order.add_edge(ChemicalTest, validation_loop)
root.order.add_edge(RadiocarbonDate, validation_loop)
root.order.add_edge(FingerprintMatch, validation_loop)
root.order.add_edge(ContextAnalysis, validation_loop)

# After loop: certification and archiving/exhibit preparation
root.order.add_edge(validation_loop, CertificationPrep)
root.order.add_edge(CertificationPrep, Documentation)
root.order.add_edge(Documentation, ArchiveStorage)
root.order.add_edge(Documentation, InsuranceLiaison)
root.order.add_edge(Documentation, ExhibitSetup)