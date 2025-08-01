# Generated from: b044b1b4-3eef-46bb-9b31-e3320961c8d7.json
# Description: This process involves the authentication and validation of rare artifacts for a specialized auction house. It begins with initial artifact intake, followed by detailed provenance research, material composition analysis using advanced spectroscopy, expert stylistic comparison, and historical context verification. Each artifact undergoes multi-disciplinary review sessions, condition assessment, and restoration feasibility studies. Legal ownership checks and export compliance reviews are conducted before final valuation and cataloging. The process concludes with secure storage preparation and digital archiving of all findings to ensure transparency and traceability for high-value sales.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
Artifact_Intake    = Transition(label='Artifact Intake')
Provenance_Check   = Transition(label='Provenance Check')
Material_Scan      = Transition(label='Material Scan')
Style_Review       = Transition(label='Style Review')
Context_Verify     = Transition(label='Context Verify')
Expert_Panel       = Transition(label='Expert Panel')
Condition_Report   = Transition(label='Condition Report')
Restoration_Plan   = Transition(label='Restoration Plan')
Ownership_Audit    = Transition(label='Ownership Audit')
Export_Review      = Transition(label='Export Review')
Final_Valuation    = Transition(label='Final Valuation')
Catalog_Entry      = Transition(label='Catalog Entry')
Storage_Prep       = Transition(label='Storage Prep')
Digital_Archive    = Transition(label='Digital Archive')
Sales_Approval     = Transition(label='Sales Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    Artifact_Intake,
    Provenance_Check, Material_Scan, Style_Review, Context_Verify,
    Expert_Panel,
    Condition_Report, Restoration_Plan,
    Ownership_Audit, Export_Review,
    Final_Valuation,
    Catalog_Entry,
    Storage_Prep, Digital_Archive,
    Sales_Approval
])

# Order dependencies
# Intake precedes all initial checks
for check in [Provenance_Check, Material_Scan, Style_Review, Context_Verify]:
    root.order.add_edge(Artifact_Intake, check)

# All checks precede the expert panel
for check in [Provenance_Check, Material_Scan, Style_Review, Context_Verify]:
    root.order.add_edge(check, Expert_Panel)

# Expert panel precedes condition assessment and restoration planning
root.order.add_edge(Expert_Panel, Condition_Report)
root.order.add_edge(Expert_Panel, Restoration_Plan)

# Condition and restoration precede legal and export reviews
for prev in [Condition_Report, Restoration_Plan]:
    root.order.add_edge(prev, Ownership_Audit)
    root.order.add_edge(prev, Export_Review)

# Legal and export reviews precede final valuation
root.order.add_edge(Ownership_Audit, Final_Valuation)
root.order.add_edge(Export_Review, Final_Valuation)

# Final valuation precedes catalog entry
root.order.add_edge(Final_Valuation, Catalog_Entry)

# Catalog entry precedes storage prep and digital archiving
root.order.add_edge(Catalog_Entry, Storage_Prep)
root.order.add_edge(Catalog_Entry, Digital_Archive)

# Storage prep and archiving precede sales approval
root.order.add_edge(Storage_Prep, Sales_Approval)
root.order.add_edge(Digital_Archive, Sales_Approval)