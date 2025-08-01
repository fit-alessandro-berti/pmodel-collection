# Generated from: 0fb071a7-30b2-4ae6-b923-f88aee39cb7e.json
# Description: This process involves the identification, negotiation, and acquisition of valuable corporate artifacts from defunct or merged companies. It begins with research to locate items of interest such as patents, prototypes, or historical documents. Following discovery, legal clearance and ownership verification are conducted to ensure rights to acquire and use the artifacts. Negotiations with sellers or estates proceed alongside appraisal and valuation to determine fair market price. Once acquired, artifacts undergo authentication and restoration if needed. The process concludes with cataloging, digital archiving, and integration into the company’s heritage collection to preserve corporate history and leverage intangible assets for branding and innovation inspiration.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Artifact_Research = Transition(label='Artifact Research')
Ownership_Verify = Transition(label='Ownership Verify')
Legal_Clearance = Transition(label='Legal Clearance')
Seller_Negotiate = Transition(label='Seller Negotiate')
Price_Appraise = Transition(label='Price Appraise')
Contract_Draft = Transition(label='Contract Draft')
Authentication_Test = Transition(label='Authentication Test')
Condition_Assess = Transition(label='Condition Assess')
Restoration_Plan = Transition(label='Restoration Plan')
Restoration_Work = Transition(label='Restoration Work')
Digital_Archive = Transition(label='Digital Archive')
Catalog_Entry = Transition(label='Catalog Entry')
Heritage_Integrate = Transition(label='Heritage Integrate')
Asset_Leverage = Transition(label='Asset Leverage')
Innovation_Inspire = Transition(label='Innovation Inspire')
Final_Review = Transition(label='Final Review')

# Research phase (start)
research_po = StrictPartialOrder(nodes=[Artifact_Research])

# Legal clearance and ownership verification in parallel (both must complete)
legal_ownership_po = StrictPartialOrder(
    nodes=[Ownership_Verify, Legal_Clearance]
)
# No edges means concurrent activities

# Negotiations and appraisal in parallel
negotiation_appraise_po = StrictPartialOrder(
    nodes=[Seller_Negotiate, Price_Appraise]
)

# Negotiation + appraisal --> contract drafting (after both negotiation and appraisal)
negotiation_contract_po = StrictPartialOrder(
    nodes=[negotiation_appraise_po, Contract_Draft]
)
negotiation_contract_po.order.add_edge(negotiation_appraise_po, Contract_Draft)

# After research:
# research -> (Ownership Verify, Legal Clearance) parallel
research_legal_ownership_po = StrictPartialOrder(
    nodes=[research_po, legal_ownership_po]
)
research_legal_ownership_po.order.add_edge(research_po, legal_ownership_po)

# After ownership/legal, negotiations+appraisal start
legal_negotiation_po = StrictPartialOrder(
    nodes=[legal_ownership_po, negotiation_appraise_po]
)
legal_negotiation_po.order.add_edge(legal_ownership_po, negotiation_appraise_po)

# Contract draft after negotiation+appraisal
# Combine all three: after legal_ownership do negotiation+appraisal then contract draft
legal_negotiation_contract_po = StrictPartialOrder(
    nodes=[legal_negotiation_po, Contract_Draft]
)
legal_negotiation_contract_po.order.add_edge(legal_negotiation_po, Contract_Draft)

# Authentication and condition assessment in parallel
auth_condition_po = StrictPartialOrder(
    nodes=[Authentication_Test, Condition_Assess]
)

# Restoration plan and work - work after plan
restoration_po = StrictPartialOrder(
    nodes=[Restoration_Plan, Restoration_Work]
)
restoration_po.order.add_edge(Restoration_Plan, Restoration_Work)

# Authentication/condition leads to restoration plan (preparation)
auth_condition_restoration_po = StrictPartialOrder(
    nodes=[auth_condition_po, restoration_po]
)
auth_condition_restoration_po.order.add_edge(auth_condition_po, restoration_po)

# After contract draft: authenticate/assess/restoration follow
contract_restoration_po = StrictPartialOrder(
    nodes=[Contract_Draft, auth_condition_restoration_po]
)
contract_restoration_po.order.add_edge(Contract_Draft, auth_condition_restoration_po)

# Final cataloging phase with these in partial order:
# Catalog Entry -> Digital Archive (catalog before archive)
catalog_digital_po = StrictPartialOrder(
    nodes=[Catalog_Entry, Digital_Archive]
)
catalog_digital_po.order.add_edge(Catalog_Entry, Digital_Archive)

# Heritage Integrate after digital archive, and Asset Leverage & Innovation Inspire concurrent after integrate
asset_innov_po = StrictPartialOrder(
    nodes=[Asset_Leverage, Innovation_Inspire]
)
# Heritage integrate before asset leverage and innovation inspire
heritage_asset_innov_po = StrictPartialOrder(
    nodes=[Heritage_Integrate, asset_innov_po]
)
heritage_asset_innov_po.order.add_edge(Heritage_Integrate, asset_innov_po)

# Sequence: catalog_digital -> heritage_asset_innov
catalog_heritage_po = StrictPartialOrder(
    nodes=[catalog_digital_po, heritage_asset_innov_po]
)
catalog_heritage_po.order.add_edge(catalog_digital_po, heritage_asset_innov_po)

# Final review after all cataloging and integration steps
final_catalog_po = StrictPartialOrder(
    nodes=[catalog_heritage_po, Final_Review]
)
final_catalog_po.order.add_edge(catalog_heritage_po, Final_Review)

# Now compose the total process:
# research_legal_ownership_po -> negotiation_appraisal + contract draft -> auth/cond/restoration -> cataloging -> final review
# We already have contract_restoration_po including contract draft and restoration steps
# Combine all parts in order

# Combine research -> legal_ownership -> negotiation+appraisal -> contract draft and restoration
start_to_restoration_po = StrictPartialOrder(
    nodes=[research_po, legal_ownership_po, negotiation_appraise_po, contract_restoration_po]
)
# research -> legal_ownership
start_to_restoration_po.order.add_edge(research_po, legal_ownership_po)
# legal_ownership -> negotiation_appraise
start_to_restoration_po.order.add_edge(legal_ownership_po, negotiation_appraise_po)
# negotiation_appraise inside contract_restoration_po
# contract_restoration_po includes Contract Draft after negotiation_appraise and restoration steps after contract draft
# So to proceed we link negotiation_appraise_po to contract_restoration_po to ensure contract and restoration after negotiation/appraise
start_to_restoration_po.order.add_edge(negotiation_appraise_po, contract_restoration_po)

# Now after restoration we do catalog + final
root = StrictPartialOrder(
    nodes=[start_to_restoration_po, catalog_heritage_po, Final_Review]
)
# last phase starts after restoration
root.order.add_edge(start_to_restoration_po, catalog_heritage_po)
# final review after catalog_heritage_po
root.order.add_edge(catalog_heritage_po, Final_Review)