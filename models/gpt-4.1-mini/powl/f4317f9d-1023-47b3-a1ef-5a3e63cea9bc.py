# Generated from: f4317f9d-1023-47b3-a1ef-5a3e63cea9bc.json
# Description: This process governs the intricate steps involved in authenticating rare antiques for auction houses. Starting with initial provenance research, experts conduct material analysis and stylistic comparison using both manual examination and AI-enhanced imaging. Following this, chemical tests verify aging patterns, while historical records are cross-checked with global databases. The item then undergoes expert panel review and market valuation, where risk assessments for forgery are performed. Finally, a detailed authentication report is generated and certified, after which the item is prepared for secure transport to auction. Throughout, multi-level approval and documentation ensure transparency and legal compliance in this atypical yet critical authentication process.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define basic transitions
provenance_check = Transition(label='Provenance Check')

material_scan = Transition(label='Material Scan')
style_compare = Transition(label='Style Compare')
ai_imaging = Transition(label='AI Imaging')

chemical_test = Transition(label='Chemical Test')
aging_verify = Transition(label='Aging Verify')

record_match = Transition(label='Record Match')
database_query = Transition(label='Database Query')

panel_review = Transition(label='Panel Review')
forgery_risk = Transition(label='Forgery Risk')
market_value = Transition(label='Market Value')

report_draft = Transition(label='Report Draft')
certification = Transition(label='Certification')

approval_stage = Transition(label='Approval Stage')

secure_packing = Transition(label='Secure Packing')
transport_prep = Transition(label='Transport Prep')

# Construct partial orders for parallel AND branches by not connecting nodes

# 1) material analysis and stylistic comparison (manual + AI imaging)
# "Material Scan" AND ("Style Compare" XOR "AI Imaging")
# The text says stylistic comparison using both manual examination and AI imaging, 
# but the wording "using both manual examination and AI-enhanced imaging" suggests concurrency rather than choice.
# So Style Compare and AI Imaging run concurrently after Material Scan.

# We'll do Material Scan --> (Style Compare & AI Imaging in parallel)
material_analysis = StrictPartialOrder(nodes=[material_scan, style_compare, ai_imaging])
material_analysis.order.add_edge(material_scan, style_compare)
material_analysis.order.add_edge(material_scan, ai_imaging)

# 2) chemical tests and aging verify, likely sequential (Chemical Test --> Aging Verify)
chem_age = StrictPartialOrder(nodes=[chemical_test, aging_verify])
chem_age.order.add_edge(chemical_test, aging_verify)

# 3) historical records cross-checked with global DB (Record Match & Database Query in parallel, no order given)
record_db = StrictPartialOrder(nodes=[record_match, database_query])
# no edges = concurrency

# 4) expert panel review and market valuation with forgery risk
# The text says: "panel review and market valuation, where risk assessments are performed"
# Suggests forgery risk and market value happen during panel review step? 
# We'll model panel review --> forgery risk --> market value (sequential)
panel_market = StrictPartialOrder(nodes=[panel_review, forgery_risk, market_value])
panel_market.order.add_edge(panel_review, forgery_risk)
panel_market.order.add_edge(forgery_risk, market_value)

# 5) report draft then certification
report_cert = StrictPartialOrder(nodes=[report_draft, certification])
report_cert.order.add_edge(report_draft, certification)

# 6) approval stage (multi-level approval and documentation)
# No further detail -> single transition

# 7) secure packing then transport prep
pack_transport = StrictPartialOrder(nodes=[secure_packing, transport_prep])
pack_transport.order.add_edge(secure_packing, transport_prep)

# Now arrange the big partial order:
# Start: Provenance Check
# Then: Material Analysis branch (Material Scan -> Style Compare & AI Imaging parallel)
# Then: Chemical & Aging Verify branch
# Then: Records & DB branch (concurrent)
# Then: Expert Panel etc (sequential)
# Then: Report & Certification (sequential)
# Then: Approval Stage
# Then: Packing & Transport

# Put all nodes in one partial order, link edges accordingly

all_nodes = [
    provenance_check,
    material_analysis,
    chem_age,
    record_db,
    panel_market,
    report_cert,
    approval_stage,
    pack_transport,
]

root = StrictPartialOrder(nodes=all_nodes)

# Add edges for the main flow

# Provenance Check --> Material Analysis
root.order.add_edge(provenance_check, material_analysis)

# Material Analysis --> Chemical + Aging
root.order.add_edge(material_analysis, chem_age)

# Chemical + Aging --> Records + DB
root.order.add_edge(chem_age, record_db)

# Records + DB --> Panel Market
root.order.add_edge(record_db, panel_market)

# Panel Market --> Report + Certification
root.order.add_edge(panel_market, report_cert)

# Report + Certification --> Approval Stage
root.order.add_edge(report_cert, approval_stage)

# Approval Stage --> Packing + Transport
root.order.add_edge(approval_stage, pack_transport)