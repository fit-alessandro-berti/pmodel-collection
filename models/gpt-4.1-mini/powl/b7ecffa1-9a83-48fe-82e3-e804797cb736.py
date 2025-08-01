# Generated from: b7ecffa1-9a83-48fe-82e3-e804797cb736.json
# Description: This process outlines the comprehensive steps involved in authenticating rare historical artifacts for museum acquisition. It includes initial artifact reception, condition assessment, provenance verification through archival research, scientific material analysis using spectroscopy, expert consultation for stylistic evaluation, and risk assessment of forgery. The workflow further involves documentation preparation, cross-referencing with international databases, legal clearance for export-import, insurance valuation, and final approval by the acquisition committee. Post-approval, artifacts are cataloged, conserved, and displayed with detailed authentication reports to ensure transparency and maintain cultural heritage integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Receive_Artifact = Transition(label='Receive Artifact')
Condition_Check = Transition(label='Condition Check')
Provenance_Research = Transition(label='Provenance Research')
Material_Analysis = Transition(label='Material Analysis')
Stylistic_Review = Transition(label='Stylistic Review')
Forgery_Risk = Transition(label='Forgery Risk')
Expert_Consult = Transition(label='Expert Consult')
Document_Prep = Transition(label='Document Prep')
Database_Cross = Transition(label='Database Cross')
Legal_Clearance = Transition(label='Legal Clearance')
Insurance_Quote = Transition(label='Insurance Quote')
Committee_Review = Transition(label='Committee Review')
Approval_Grant = Transition(label='Approval Grant')
Catalog_Entry = Transition(label='Catalog Entry')
Conservation = Transition(label='Conservation')
Display_Setup = Transition(label='Display Setup')

# Step 1 -> 2 (Receive Artifact -> Condition Check)
# After Condition Check, three analyses in parallel: Provenance Research, Material Analysis, Stylistic Review
# Stylistic Review requires Expert Consult first, and Forgery Risk also depends on Expert Consult
# So Expert Consult precedes Stylistic Review and Forgery Risk
# Provenance Research and Material Analysis are independent and parallel to Expert Consult branch

# Create Expert Consult sub-branch: Expert Consult -> (Stylistic Review and Forgery Risk parallel)
Expert_Consult_PO = StrictPartialOrder(nodes=[Expert_Consult, Stylistic_Review, Forgery_Risk])
Expert_Consult_PO.order.add_edge(Expert_Consult, Stylistic_Review)
Expert_Consult_PO.order.add_edge(Expert_Consult, Forgery_Risk)

# Create the three parallel analyses nodes: Provenance Research, Material Analysis, and Expert_Consult_PO (which includes Stylistic Review and Forgery Risk)
# So these three are concurrent after Condition Check
analyses = StrictPartialOrder(nodes=[Provenance_Research, Material_Analysis, Expert_Consult_PO])
# no order edges between these three - fully concurrent

# After the analyses, Document Prep
# Followed by Database Cross and Legal Clearance in parallel
docs_and_crosslegal = StrictPartialOrder(
    nodes=[Document_Prep, Database_Cross, Legal_Clearance]
)
docs_and_crosslegal.order.add_edge(Document_Prep, Database_Cross)
docs_and_crosslegal.order.add_edge(Document_Prep, Legal_Clearance)

# Insurance Quote follows Legal Clearance (seems logical: legal clearance -> insurance quote)
# So Legal Clearance --> Insurance Quote
insurance_po = StrictPartialOrder(nodes=[Legal_Clearance, Insurance_Quote])
insurance_po.order.add_edge(Legal_Clearance, Insurance_Quote)

# Committee Review follows Database Cross and Insurance Quote
# So both Database Cross and Insurance Quote --> Committee Review
committee_po = StrictPartialOrder(nodes=[Database_Cross, Insurance_Quote, Committee_Review])
committee_po.order.add_edge(Database_Cross, Committee_Review)
committee_po.order.add_edge(Insurance_Quote, Committee_Review)

# Approval Grant after Committee Review
approval_po = StrictPartialOrder(nodes=[Committee_Review, Approval_Grant])
approval_po.order.add_edge(Committee_Review, Approval_Grant)

# Post approval: Catalog Entry -> Conservation -> Display Setup sequentially
post_approval_po = StrictPartialOrder(nodes=[Catalog_Entry, Conservation, Display_Setup])
post_approval_po.order.add_edge(Catalog_Entry, Conservation)
post_approval_po.order.add_edge(Conservation, Display_Setup)

# Also the authentication reports mentioned are most likely part of Display Setup or implicit - use Display Setup as last

# Now combine all parts:

# 1->2->analyses
part1 = StrictPartialOrder(nodes=[Receive_Artifact, Condition_Check, analyses])
part1.order.add_edge(Receive_Artifact, Condition_Check)
part1.order.add_edge(Condition_Check, analyses)

# analyses has 3 nodes: Provenance Research, Material Analysis, Expert_Consult_PO
# analyses is a StrictPartialOrder with those three nodes and no edges (concurrent)

# analyses -> Document Prep start
# But Document Prep is in docs_and_crosslegal with Database Cross and Legal Clearance; Document Prep precedes Database Cross and Legal Clearance

# So link analyses --> Document Prep (Document_Prep is node of docs_and_crosslegal)
# So create full ordering between analyses and docs_and_crosslegal.Document_Prep

# Since analyses is a StrictPartialOrder object, link to Document_Prep node (in docs_and_crosslegal)
# pm4py expects nodes as objects; linking analyses to Document_Prep node outside means ordering from analyses to Document_Prep node

# Similarly, link docs_and_crosslegal with insurance_po to reflect Legal Clearance --> Insurance Quote edge
# They share Legal_Clearance node, so no problem

# Link insurance_po to committee_po: Insurance_Quote and Database_Cross nodes are shared

# To create one big PO, take union of all nodes and add edges:

all_nodes = [
    Receive_Artifact,
    Condition_Check,
    Provenance_Research,
    Material_Analysis,
    Expert_Consult_PO,
    Expert_Consult, Stylistic_Review, Forgery_Risk,
    Document_Prep,
    Database_Cross,
    Legal_Clearance,
    Insurance_Quote,
    Committee_Review,
    Approval_Grant,
    Catalog_Entry,
    Conservation,
    Display_Setup,
]

# Actually, Expert_Consult_PO already contains Expert_Consult, Stylistic_Review, Forgery_Risk
# Nodes of Expert_Consult_PO are: [Expert_Consult, Stylistic_Review, Forgery_Risk]
# So to avoid duplicates, in the final PO nodes list we include Expert_Consult_PO as node for concurrency,
# but since it's POWL, we should keep Expert_Consult_PO as node inside concurrency group
# But since analyses is a PO with nodes = {Provenance Research, Material Analysis, Expert_Consult_PO}
# Already included in part1

# To preserve the hierarchy we can combine parts as follows:

# Build analyses as nodes=[Provenance_Research, Material_Analysis, Expert_Consult_PO]

# Now build part1 nodes = [Receive_Artifact, Condition_Check, analyses]

# Then build full PO as nodes=[part1, docs_and_crosslegal, insurance_po, committee_po, approval_po, post_approval_po]

# Add ordering edges between these components:
# part1 --> Document_Prep (belongs to docs_and_crosslegal)
# Document_Prep --> Legal_Clearance and Database_Cross (inside docs_and_crosslegal)
# Legal_Clearance --> Insurance Quote (inside insurance_po)
# Database_Cross, Insurance_Quote --> Committee Review (inside committee_po)
# Committee Review --> Approval Grant (inside approval_po)
# Approval Grant --> Catalog Entry (approval_po -> post_approval_po)
# Catalog Entry -> Conservation -> Display Setup (inside post_approval_po)

# Because some nodes appear in multiple POs (like Legal_Clearance in docs_and_crosslegal and insurance_po),
# we have to unify nodes and add cross edges accordingly

# To avoid confusion, let's build a single StrictPartialOrder with all nodes and edges.

root = StrictPartialOrder(nodes=[
    Receive_Artifact, Condition_Check,
    Provenance_Research, Material_Analysis,
    Expert_Consult, Stylistic_Review, Forgery_Risk,
    Document_Prep, Database_Cross, Legal_Clearance,
    Insurance_Quote, Committee_Review, Approval_Grant,
    Catalog_Entry, Conservation, Display_Setup
])

# Add edges according to the described sequencing:

# Receive Artifact --> Condition Check
root.order.add_edge(Receive_Artifact, Condition_Check)

# Condition Check --> Provenance Research, Material Analysis, Expert Consult
root.order.add_edge(Condition_Check, Provenance_Research)
root.order.add_edge(Condition_Check, Material_Analysis)
root.order.add_edge(Condition_Check, Expert_Consult)

# Expert Consult --> Stylistic Review and Forgery Risk
root.order.add_edge(Expert_Consult, Stylistic_Review)
root.order.add_edge(Expert_Consult, Forgery_Risk)

# Provenance Research, Material Analysis, and Expert Consult branches are concurrent (no order between them)

# After all three analyses, Document Prep (so Provenance Research, Material Analysis, Stylistic Review, Forgery Risk all --> Document Prep)
root.order.add_edge(Provenance_Research, Document_Prep)
root.order.add_edge(Material_Analysis, Document_Prep)
root.order.add_edge(Stylistic_Review, Document_Prep)
root.order.add_edge(Forgery_Risk, Document_Prep)

# Document Prep --> Database Cross and Legal Clearance
root.order.add_edge(Document_Prep, Database_Cross)
root.order.add_edge(Document_Prep, Legal_Clearance)

# Legal Clearance --> Insurance Quote
root.order.add_edge(Legal_Clearance, Insurance_Quote)

# Database Cross and Insurance Quote --> Committee Review
root.order.add_edge(Database_Cross, Committee_Review)
root.order.add_edge(Insurance_Quote, Committee_Review)

# Committee Review --> Approval Grant
root.order.add_edge(Committee_Review, Approval_Grant)

# Approval Grant --> Catalog Entry
root.order.add_edge(Approval_Grant, Catalog_Entry)

# Catalog Entry --> Conservation --> Display Setup
root.order.add_edge(Catalog_Entry, Conservation)
root.order.add_edge(Conservation, Display_Setup)