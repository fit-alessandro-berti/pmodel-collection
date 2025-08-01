# Generated from: 96f43016-51c9-4278-9060-d7317a4843fb.json
# Description: This process involves the careful examination and verification of antique artifacts to determine their authenticity and provenance. It includes initial condition assessment, detailed material analysis, historical research, expert consultations, and cross-referencing with known databases. The procedure must account for potential forgeries, restoration history, and legal ownership verification. Final reporting includes certification and recommendations for preservation or sale, ensuring all findings are meticulously documented for collectors, museums, or auction houses.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Artifact_Intake = Transition(label='Artifact Intake')
Condition_Check = Transition(label='Condition Check')
Material_Scan = Transition(label='Material Scan')
Style_Compare = Transition(label='Style Compare')
Provenance_Trace = Transition(label='Provenance Trace')
Database_Search = Transition(label='Database Search')
Expert_Review = Transition(label='Expert Review')
Forgery_Detect = Transition(label='Forgery Detect')
Restoration_Check = Transition(label='Restoration Check')
Legal_Verify = Transition(label='Legal Verify')
Market_Analysis = Transition(label='Market Analysis')
Risk_Assess = Transition(label='Risk Assess')
Report_Draft = Transition(label='Report Draft')
Certification_Issue = Transition(label='Certification Issue')
Preservation_Advise = Transition(label='Preservation Advise')
Client_Brief = Transition(label='Client Brief')

# Initial sequence: Artifact Intake -> Condition Check
init_seq = StrictPartialOrder(nodes=[Artifact_Intake, Condition_Check])
init_seq.order.add_edge(Artifact_Intake, Condition_Check)

# Material Scan and Style Compare can be done in parallel after Condition Check
mat_style_PO = StrictPartialOrder(nodes=[Material_Scan, Style_Compare, Condition_Check])
mat_style_PO.order.add_edge(Condition_Check, Material_Scan)
mat_style_PO.order.add_edge(Condition_Check, Style_Compare)

# Provenance Trace and Database Search after Style Compare
prov_db_PO = StrictPartialOrder(nodes=[Provenance_Trace, Database_Search, Style_Compare])
prov_db_PO.order.add_edge(Style_Compare, Provenance_Trace)
prov_db_PO.order.add_edge(Style_Compare, Database_Search)

# Expert Review depends on Provenance Trace, Database Search, and Material Scan (all must complete before Expert Review)
# We'll build a PO with all these nodes and edges
expert_inputs = StrictPartialOrder(nodes=[Expert_Review, Provenance_Trace, Database_Search, Material_Scan])
expert_inputs.order.add_edge(Provenance_Trace, Expert_Review)
expert_inputs.order.add_edge(Database_Search, Expert_Review)
expert_inputs.order.add_edge(Material_Scan, Expert_Review)

# After Expert Review, run Forgery Detect and Restoration Check in parallel
forg_rest_PO = StrictPartialOrder(nodes=[Forgery_Detect, Restoration_Check, Expert_Review])
forg_rest_PO.order.add_edge(Expert_Review, Forgery_Detect)
forg_rest_PO.order.add_edge(Expert_Review, Restoration_Check)

# Legal Verify depends on Forgery Detect and Restoration Check both done
legal_verify_PO = StrictPartialOrder(nodes=[Legal_Verify, Forgery_Detect, Restoration_Check])
legal_verify_PO.order.add_edge(Forgery_Detect, Legal_Verify)
legal_verify_PO.order.add_edge(Restoration_Check, Legal_Verify)

# Market Analysis and Risk Assess parallel after Legal Verify
market_risk_PO = StrictPartialOrder(nodes=[Market_Analysis, Risk_Assess, Legal_Verify])
market_risk_PO.order.add_edge(Legal_Verify, Market_Analysis)
market_risk_PO.order.add_edge(Legal_Verify, Risk_Assess)

# After Market Analysis and Risk Assess, Report Draft
report_PO = StrictPartialOrder(nodes=[Report_Draft, Market_Analysis, Risk_Assess])
report_PO.order.add_edge(Market_Analysis, Report_Draft)
report_PO.order.add_edge(Risk_Assess, Report_Draft)

# Certification Issue after Report Draft
certification_PO = StrictPartialOrder(nodes=[Certification_Issue, Report_Draft])
certification_PO.order.add_edge(Report_Draft, Certification_Issue)

# Preservation Advise and Client Brief in parallel after Certification Issue
final_PO = StrictPartialOrder(nodes=[Preservation_Advise, Client_Brief, Certification_Issue])
final_PO.order.add_edge(Certification_Issue, Preservation_Advise)
final_PO.order.add_edge(Certification_Issue, Client_Brief)

# Now we combine all partial orders into one big PO connected by edges preserving ordering

# Combine stepwise by building a list of all nodes and edges, using a base PO
from pm4py.objects.powl.obj import StrictPartialOrder

nodes = [
    Artifact_Intake,
    Condition_Check,
    Material_Scan,
    Style_Compare,
    Provenance_Trace,
    Database_Search,
    Expert_Review,
    Forgery_Detect,
    Restoration_Check,
    Legal_Verify,
    Market_Analysis,
    Risk_Assess,
    Report_Draft,
    Certification_Issue,
    Preservation_Advise,
    Client_Brief
]

root = StrictPartialOrder(nodes=nodes)

# Add edges according to relationships above

# Initial
root.order.add_edge(Artifact_Intake, Condition_Check)

# Condition_Check to Material_Scan and Style_Compare
root.order.add_edge(Condition_Check, Material_Scan)
root.order.add_edge(Condition_Check, Style_Compare)

# Style_Compare to Provenance_Trace and Database_Search
root.order.add_edge(Style_Compare, Provenance_Trace)
root.order.add_edge(Style_Compare, Database_Search)

# Provenance_Trace, Database_Search, Material_Scan to Expert_Review
root.order.add_edge(Provenance_Trace, Expert_Review)
root.order.add_edge(Database_Search, Expert_Review)
root.order.add_edge(Material_Scan, Expert_Review)

# Expert_Review to Forgery_Detect and Restoration_Check
root.order.add_edge(Expert_Review, Forgery_Detect)
root.order.add_edge(Expert_Review, Restoration_Check)

# Forgery_Detect and Restoration_Check to Legal_Verify
root.order.add_edge(Forgery_Detect, Legal_Verify)
root.order.add_edge(Restoration_Check, Legal_Verify)

# Legal_Verify to Market_Analysis and Risk_Assess
root.order.add_edge(Legal_Verify, Market_Analysis)
root.order.add_edge(Legal_Verify, Risk_Assess)

# Market_Analysis and Risk_Assess to Report_Draft
root.order.add_edge(Market_Analysis, Report_Draft)
root.order.add_edge(Risk_Assess, Report_Draft)

# Report_Draft to Certification_Issue
root.order.add_edge(Report_Draft, Certification_Issue)

# Certification_Issue to Preservation_Advise and Client_Brief
root.order.add_edge(Certification_Issue, Preservation_Advise)
root.order.add_edge(Certification_Issue, Client_Brief)