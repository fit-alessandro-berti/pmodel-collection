# Generated from: 4858203c-885c-4710-b746-3579184eb9cc.json
# Description: This process involves the intricate validation and certification of rare historical artifacts before they are auctioned to collectors worldwide. It begins with provenance research, followed by material composition analysis using advanced spectroscopy. Next, expert forensic imaging is performed to detect any restoration or forgery attempts. The artifact then undergoes environmental impact testing to ensure preservation standards. Legal clearance checks confirm ownership legitimacy, while digital 3D modeling creates an archival record. The process also includes coordination with customs for export permits, insurance valuation, and final certification issuance. The entire workflow ensures authenticity, legality, and preservation compliance for high-value cultural items.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
ForensicImaging = Transition(label='Forensic Imaging')
RestorationDetect = Transition(label='Restoration Detect')
ImpactTesting = Transition(label='Impact Testing')
LegalReview = Transition(label='Legal Review')
OwnershipVerify = Transition(label='Ownership Verify')
Modeling3D = Transition(label='3D Modeling')
CustomsLiaison = Transition(label='Customs Liaison')
InsuranceQuote = Transition(label='Insurance Quote')
ValuationReview = Transition(label='Valuation Review')
Certification = Transition(label='Certification')
ArchivalUpload = Transition(label='Archival Upload')
ExportPermit = Transition(label='Export Permit')
FinalApproval = Transition(label='Final Approval')

# Construct partial order for provenance and material scan to restoration detect (sequential)
po1 = StrictPartialOrder(nodes=[ProvenanceCheck, MaterialScan, ForensicImaging, RestorationDetect])
po1.order.add_edge(ProvenanceCheck, MaterialScan)
po1.order.add_edge(MaterialScan, ForensicImaging)
po1.order.add_edge(ForensicImaging, RestorationDetect)

# Impact Testing independent but after RestorationDetect
# We'll add ImpactTesting to po2 with RestorationDetect order
po2 = StrictPartialOrder(nodes=[RestorationDetect, ImpactTesting])
po2.order.add_edge(RestorationDetect, ImpactTesting)

# Legal Review must be after Ownership Verify
legalPO = StrictPartialOrder(nodes=[LegalReview, OwnershipVerify])
legalPO.order.add_edge(OwnershipVerify, LegalReview)

# 3D Modeling (Modeling3D) and Archival Upload can run after Certification in parallel with Export Permit and Custom Liaison
# But Certification must be after ImpactTesting, LegalReview, InsuranceQuote and ValuationReview are sequenced accordingly:
# InsuranceQuote --> ValuationReview --> Certification
insurancePO = StrictPartialOrder(nodes=[InsuranceQuote, ValuationReview, Certification])
insurancePO.order.add_edge(InsuranceQuote, ValuationReview)
insurancePO.order.add_edge(ValuationReview, Certification)

# Certification depends on ImpactTesting and LegalReview
# We will build a PO combining ImpactTesting, LegalReview, InsuranceQuote, ValuationReview, Certification

# Combine ImpactTesting, LegalReview, InsuranceQuote, ValuationReview, Certification into a single PO
certification_nodes = [ImpactTesting, LegalReview, InsuranceQuote, ValuationReview, Certification]
certificationPO = StrictPartialOrder(nodes=certification_nodes)

certificationPO.order.add_edge(ImpactTesting, Certification)
certificationPO.order.add_edge(LegalReview, Certification)
certificationPO.order.add_edge(InsuranceQuote, ValuationReview)
certificationPO.order.add_edge(ValuationReview, Certification)

# ExportPermit and CustomsLiaison can run concurrently but after Certification
post_cert_nodes = [Certification, ArchivalUpload, ExportPermit, CustomsLiaison, FinalApproval]

post_cert_PO = StrictPartialOrder(nodes=post_cert_nodes)
post_cert_PO.order.add_edge(Certification, ArchivalUpload)
post_cert_PO.order.add_edge(Certification, ExportPermit)
post_cert_PO.order.add_edge(Certification, CustomsLiaison)

# FinalApproval depends on ArchivalUpload, ExportPermit, CustomsLiaison
post_cert_PO.order.add_edge(ArchivalUpload, FinalApproval)
post_cert_PO.order.add_edge(ExportPermit, FinalApproval)
post_cert_PO.order.add_edge(CustomsLiaison, FinalApproval)

# OwnershipVerify must happen before LegalReview (already set in legalPO)
# We also need to consider that LegalReview is in certPO, so let's merge OwnershipVerify accordingly

# Build a PO that merges OwnershipVerify, LegalReview, ImpactTesting, InsuranceQuote, ValuationReview, Certification
pre_cert_nodes = [OwnershipVerify, LegalReview, ImpactTesting, InsuranceQuote, ValuationReview, Certification]
pre_cert_PO = StrictPartialOrder(nodes=pre_cert_nodes)
pre_cert_PO.order.add_edge(OwnershipVerify, LegalReview)
pre_cert_PO.order.add_edge(LegalReview, Certification)
pre_cert_PO.order.add_edge(ImpactTesting, Certification)
pre_cert_PO.order.add_edge(InsuranceQuote, ValuationReview)
pre_cert_PO.order.add_edge(ValuationReview, Certification)

# Provenance to RestorationDetect sequence then ImpactTesting
# Build complete workflow top PO by joining first po1 + pre_cert_PO (where RestorationDetect precedes ImpactTesting)
# Also add link RestorationDetect --> ImpactTesting

topPO_nodes = [ProvenanceCheck, MaterialScan, ForensicImaging, RestorationDetect,
               OwnershipVerify, LegalReview, ImpactTesting,
               InsuranceQuote, ValuationReview, Certification,
               ArchivalUpload, ExportPermit, CustomsLiaison, FinalApproval,
               Modeling3D]

topPO = StrictPartialOrder(nodes=topPO_nodes)

# From po1 chain: ProvenanceCheck-->MaterialScan-->ForensicImaging-->RestorationDetect
topPO.order.add_edge(ProvenanceCheck, MaterialScan)
topPO.order.add_edge(MaterialScan, ForensicImaging)
topPO.order.add_edge(ForensicImaging, RestorationDetect)

# Add RestorationDetect --> ImpactTesting
topPO.order.add_edge(RestorationDetect, ImpactTesting)

# OwnershipVerify --> LegalReview
topPO.order.add_edge(OwnershipVerify, LegalReview)

# LegalReview --> Certification
topPO.order.add_edge(LegalReview, Certification)

# ImpactTesting --> Certification
topPO.order.add_edge(ImpactTesting, Certification)

# InsuranceQuote --> ValuationReview --> Certification
topPO.order.add_edge(InsuranceQuote, ValuationReview)
topPO.order.add_edge(ValuationReview, Certification)

# Certification --> ArchivalUpload, ExportPermit, CustomsLiaison
topPO.order.add_edge(Certification, ArchivalUpload)
topPO.order.add_edge(Certification, ExportPermit)
topPO.order.add_edge(Certification, CustomsLiaison)

# ArchivalUpload, ExportPermit, CustomsLiaison --> FinalApproval
topPO.order.add_edge(ArchivalUpload, FinalApproval)
topPO.order.add_edge(ExportPermit, FinalApproval)
topPO.order.add_edge(CustomsLiaison, FinalApproval)

# 3D Modeling can be done independently anytime after MaterialScan (assumption)
topPO.order.add_edge(MaterialScan, Modeling3D)

root = topPO