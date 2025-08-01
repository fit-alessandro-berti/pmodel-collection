# Generated from: 23687625-c096-41d9-8076-2e820ff28f9e.json
# Description: This process involves the multi-layered verification of historical artifacts sourced from various private collectors, museums, and archaeological sites. Initially, artifacts undergo physical inspection and provenance validation, followed by advanced material composition analysis using spectroscopy. Concurrently, experts perform stylistic comparisons against known databases. The process includes legal clearance for export/import regulations and digital cataloging with blockchain certification for authenticity. Finally, artifacts are prepared for exhibition or sale, ensuring compliance with cultural heritage laws and ethical standards. This atypical workflow demands coordination among historians, scientists, legal advisors, and curators to guarantee artifact legitimacy and secure transfer.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
Initial_Inspect    = Transition(label='Initial Inspect')
Provenance_Check   = Transition(label='Provenance Check')
Material_Scan      = Transition(label='Material Scan')
Spectroscopy_Test  = Transition(label='Spectroscopy Test')
Stylistic_Match    = Transition(label='Stylistic Match')
Database_Query     = Transition(label='Database Query')
Legal_Review       = Transition(label='Legal Review')
Export_Clearance   = Transition(label='Export Clearance')
Blockchain_Certify = Transition(label='Blockchain Certify')
Digital_Catalog    = Transition(label='Digital Catalog')
Expert_Panel       = Transition(label='Expert Panel')
Condition_Report   = Transition(label='Condition Report')
Ethics_Audit       = Transition(label='Ethics Audit')
Exhibit_Prep       = Transition(label='Exhibit Prep')
Final_Approval     = Transition(label='Final Approval')
Transfer_Log       = Transition(label='Transfer Log')

# Build the partial order
root = StrictPartialOrder(nodes=[
    Initial_Inspect, Provenance_Check,
    Material_Scan, Spectroscopy_Test,
    Stylistic_Match, Database_Query,
    Legal_Review, Export_Clearance,
    Blockchain_Certify, Digital_Catalog,
    Expert_Panel, Condition_Report,
    Ethics_Audit, Exhibit_Prep,
    Final_Approval, Transfer_Log
])

# Sequence: initial inspection → provenance check
root.order.add_edge(Initial_Inspect, Provenance_Check)

# After provenance check, two branches run concurrently
# 1) Material analysis branch
root.order.add_edge(Provenance_Check, Material_Scan)
root.order.add_edge(Material_Scan, Spectroscopy_Test)

# 2) Stylistic comparison branch
root.order.add_edge(Provenance_Check, Stylistic_Match)
root.order.add_edge(Stylistic_Match, Database_Query)

# Merge branches into legal review
root.order.add_edge(Spectroscopy_Test, Legal_Review)
root.order.add_edge(Database_Query, Legal_Review)

# Legal clearance and cataloging chain
root.order.add_edge(Legal_Review, Export_Clearance)
root.order.add_edge(Export_Clearance, Blockchain_Certify)
root.order.add_edge(Blockchain_Certify, Digital_Catalog)

# After cataloging, three expert checks run in parallel
root.order.add_edge(Digital_Catalog, Expert_Panel)
root.order.add_edge(Digital_Catalog, Condition_Report)
root.order.add_edge(Digital_Catalog, Ethics_Audit)

# All checks complete before exhibit preparation
root.order.add_edge(Expert_Panel, Exhibit_Prep)
root.order.add_edge(Condition_Report, Exhibit_Prep)
root.order.add_edge(Ethics_Audit, Exhibit_Prep)

# Final approval and transfer logging
root.order.add_edge(Exhibit_Prep, Final_Approval)
root.order.add_edge(Final_Approval, Transfer_Log)