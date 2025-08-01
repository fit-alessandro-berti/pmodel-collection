# Generated from: 0d4beda5-f758-483e-b43d-016b77a5742c.json
# Description: This process involves the comprehensive authentication of rare historical artifacts prior to their acquisition by museums or private collectors. It begins with preliminary provenance research, followed by multispectral imaging and chemical composition analysis. Next, expert consultations and cross-referencing with databases are conducted to ensure authenticity and legality. Ethical considerations and cultural heritage laws are reviewed before final valuation and acquisition decisions. Throughout the process, documentation and chain-of-custody records are meticulously maintained to prevent fraud and ensure transparency in the artifact's history and ownership.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
ProvenanceCheck = Transition(label='Provenance Check')

ImageCapture = Transition(label='Image Capture')
SpectralScan = Transition(label='Spectral Scan')
ChemicalTest = Transition(label='Chemical Test')

DatabaseQuery = Transition(label='Database Query')
ExpertReview = Transition(label='Expert Review')

LegalAudit = Transition(label='Legal Audit')
EthicsReview = Transition(label='Ethics Review')

ValuationSetup = Transition(label='Valuation Setup')
AcquisitionVote = Transition(label='Acquisition Vote')
FinalApproval = Transition(label='Final Approval')

ConditionReport = Transition(label='Condition Report')
OwnershipVerify = Transition(label='Ownership Verify')

ChainRecord = Transition(label='Chain Record')
FraudAnalysis = Transition(label='Fraud Analysis')

# Step 1: preliminary provenance research: Provenance Check
# Step 2: multispectral imaging & chemical composition analysis: Image Capture, Spectral Scan, Chemical Test (concurrent)
multispectral_partial = StrictPartialOrder(nodes=[ImageCapture, SpectralScan, ChemicalTest])

# No order among Image Capture, Spectral Scan, Chemical Test (concurrent)
# So don't add any edges in multispectral_partial.order

# Step 3: Expert consultations and cross-referencing with databases
# Database Query and Expert Review concurrent

expert_partial = StrictPartialOrder(nodes=[DatabaseQuery, ExpertReview])

# Step 4: Ethical considerations and cultural heritage laws 
# Legal Audit and Ethics Review concurrent

ethics_partial = StrictPartialOrder(nodes=[LegalAudit, EthicsReview])

# Step 5: Final valuation and acquisition decisions
# Valuation Setup -> Acquisition Vote -> Final Approval

valuation_po = StrictPartialOrder(nodes=[ValuationSetup, AcquisitionVote, FinalApproval])
valuation_po.order.add_edge(ValuationSetup, AcquisitionVote)
valuation_po.order.add_edge(AcquisitionVote, FinalApproval)

# Step 6: Documentation and chain-of-custody records maintained throughout
# Chain Record and Fraud Analysis concurrent with entire process but presumably after provenance check.

# Condition Report and Ownership Verify appear as additional activities involved in documentation or verification,
# Let's consider them concurrent with Chain Record and Fraud Analysis for documentation.

documentation_partial = StrictPartialOrder(
    nodes=[ConditionReport, OwnershipVerify, ChainRecord, FraudAnalysis]
)
# No ordering edges among these - concurrent

# Now assemble the big model in order with appropriate dependencies:

# Provenance Check --> multispectral_partial --> expert_partial --> ethics_partial --> valuation_po

# Documentation_parallel is concurrent with the whole process or at least running throughout. 
# For simplicity, include documentation_partial as a concurrent branch parallel to others after Provenance Check.

# Construct top-level partial order nodes:
# nodes: ProvenanceCheck, multispectral_partial, expert_partial, ethics_partial, valuation_po, documentation_partial

top_nodes = [ProvenanceCheck,
             multispectral_partial,
             expert_partial,
             ethics_partial,
             valuation_po,
             documentation_partial]

root = StrictPartialOrder(nodes=top_nodes)

# Define ordering edges for process flow
root.order.add_edge(ProvenanceCheck, multispectral_partial)
root.order.add_edge(multispectral_partial, expert_partial)
root.order.add_edge(expert_partial, ethics_partial)
root.order.add_edge(ethics_partial, valuation_po)

# Documentation partial order is concurrent, so no edges to/from it, no ordering relation.

# Return root as final model