# Generated from: 0155ce86-a786-454c-9042-13c629ba6da3.json
# Description: This process outlines the comprehensive workflow used by cultural heritage institutions to authenticate and verify the provenance of rare artifacts. The steps include initial artifact intake, condition assessment, historical data mining, scientific material analysis, expert panel review, digital imaging, and provenance chain verification. It integrates multidisciplinary expertise, advanced technology, and legal checks to ensure each artifact's authenticity and rightful ownership before cataloging for exhibition or sale. The process also incorporates risk assessment for potential forgeries and legal compliance with international cultural property laws, culminating in a final certification and archival documentation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions based on the given activities
Artifact_Intake = Transition(label='Artifact Intake')
Condition_Check = Transition(label='Condition Check')
Data_Mining = Transition(label='Data Mining')
Material_Scan = Transition(label='Material Scan')
Scientific_Test = Transition(label='Scientific Test')
Expert_Review = Transition(label='Expert Review')
Digital_Imaging = Transition(label='Digital Imaging')
Provenance_Check = Transition(label='Provenance Check')
Forgery_Risk = Transition(label='Forgery Risk')
Legal_Audit = Transition(label='Legal Audit')
Ownership_Verify = Transition(label='Ownership Verify')
Certification = Transition(label='Certification')
Archival_Store = Transition(label='Archival Store')
Catalog_Entry = Transition(label='Catalog Entry')
Exhibit_Prep = Transition(label='Exhibit Prep')
Sale_Approval = Transition(label='Sale Approval')

# Build partial orders for parallel or sequential activities where applicable

# Scientific analysis branch: Material_Scan and Scientific_Test in sequence
scientific_branch = StrictPartialOrder(nodes=[Material_Scan, Scientific_Test])
scientific_branch.order.add_edge(Material_Scan, Scientific_Test)

# Provenance verification branch: Provenance_Check -> Forgery_Risk -> Legal_Audit -> Ownership_Verify
provenance_branch = StrictPartialOrder(nodes=[Provenance_Check, Forgery_Risk, Legal_Audit, Ownership_Verify])
provenance_branch.order.add_edge(Provenance_Check, Forgery_Risk)
provenance_branch.order.add_edge(Forgery_Risk, Legal_Audit)
provenance_branch.order.add_edge(Legal_Audit, Ownership_Verify)

# After both scientific_branch and provenance_branch, expert review happens
# Expert_Review depends on both scientific_branch and provenance_branch being done

# Prepare a PO for scientific_branch and provenance_branch running in parallel
parallel_branches = StrictPartialOrder(nodes=[scientific_branch, provenance_branch])
# no edges between them (concurrent)

# Expert_Review after both branches
post_expert = StrictPartialOrder(nodes=[parallel_branches, Expert_Review])
post_expert.order.add_edge(parallel_branches, Expert_Review)

# After expert review, digital imaging and data mining can proceed in parallel
imaging_data = StrictPartialOrder(nodes=[Digital_Imaging, Data_Mining])
# no edges, so concurrent

# After them, catalog entry
post_catalog = StrictPartialOrder(nodes=[imaging_data, Catalog_Entry])
post_catalog.order.add_edge(imaging_data, Catalog_Entry)

# The last steps before the final certification are exhibit prep and sale approval in parallel
final_prep = StrictPartialOrder(nodes=[Exhibit_Prep, Sale_Approval])
# no edges, concurrent

# Certification depends on catalog entry and final prep both
certification_phase = StrictPartialOrder(nodes=[post_catalog, final_prep, Certification])
certification_phase.order.add_edge(post_catalog, Certification)
certification_phase.order.add_edge(final_prep, Certification)

# Archival store after certification
final_phase = StrictPartialOrder(nodes=[certification_phase, Archival_Store])
final_phase.order.add_edge(certification_phase, Archival_Store)

# Overall model order:
# Artifact Intake -> Condition Check -> (parallel branches: scientific_branch, provenance_branch)
# -> Expert Review -> (parallel: Digital Imaging, Data Mining)
# -> Catalog Entry -> (parallel: Exhibit Prep, Sale Approval)
# -> Certification -> Archival Store

root = StrictPartialOrder(nodes=[
    Artifact_Intake,
    Condition_Check,
    scientific_branch,
    provenance_branch,
    Expert_Review,
    Digital_Imaging,
    Data_Mining,
    Catalog_Entry,
    Exhibit_Prep,
    Sale_Approval,
    Certification,
    Archival_Store
])

# Add main edges reflecting the described workflow
root.order.add_edge(Artifact_Intake, Condition_Check)

# Condition check to both scientific_branch and provenance_branch (parallel)
root.order.add_edge(Condition_Check, scientific_branch)
root.order.add_edge(Condition_Check, provenance_branch)

# Both branches to Expert Review
root.order.add_edge(scientific_branch, Expert_Review)
root.order.add_edge(provenance_branch, Expert_Review)

# Expert review to Digital Imaging and Data Mining (parallel)
root.order.add_edge(Expert_Review, Digital_Imaging)
root.order.add_edge(Expert_Review, Data_Mining)

# Both Digital Imaging and Data Mining to Catalog Entry
root.order.add_edge(Digital_Imaging, Catalog_Entry)
root.order.add_edge(Data_Mining, Catalog_Entry)

# Catalog Entry to Exhibit Prep and Sale Approval (parallel)
root.order.add_edge(Catalog_Entry, Exhibit_Prep)
root.order.add_edge(Catalog_Entry, Sale_Approval)

# Exhibit Prep and Sale Approval to Certification
root.order.add_edge(Exhibit_Prep, Certification)
root.order.add_edge(Sale_Approval, Certification)

# Certification to Archival Store
root.order.add_edge(Certification, Archival_Store)