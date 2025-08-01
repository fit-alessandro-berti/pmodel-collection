# Generated from: 7eab0f4b-7815-4df0-ab8c-eb8b7f4ca208.json
# Description: This process involves the creation and management of a corporate time capsule intended to preserve company culture, achievements, and predictions for future employees. The process starts with idea generation and asset collection, followed by authentication and cataloging of items. Afterward, it requires coordination with legal and archival teams to ensure compliance and preservation standards. Packaging and secure sealing of the capsule precede the selection of a physical or digital storage location. Finally, formal documentation and a future opening protocol are established to guarantee the capsule's integrity and relevance over decades, involving periodic reviews and updates to the contents as the company evolves.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
idea_setup        = Transition(label='Idea Setup')
asset_gather      = Transition(label='Asset Gather')
item_authenticate = Transition(label='Item Authenticate')
catalog_entry     = Transition(label='Catalog Entry')
legal_review      = Transition(label='Legal Review')
archive_check     = Transition(label='Archive Check')
package_items     = Transition(label='Package Items')
seal_capsule      = Transition(label='Seal Capsule')
location_scan     = Transition(label='Location Scan')
storage_setup     = Transition(label='Storage Setup')
access_control    = Transition(label='Access Control')
document_protocol = Transition(label='Document Protocol')
future_plan       = Transition(label='Future Plan')
review_cycle      = Transition(label='Review Cycle')
update_content    = Transition(label='Update Content')

# Define the loop for periodic review & update
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[review_cycle, update_content]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    idea_setup,
    asset_gather,
    item_authenticate,
    catalog_entry,
    legal_review,
    archive_check,
    package_items,
    seal_capsule,
    location_scan,
    storage_setup,
    access_control,
    document_protocol,
    future_plan,
    loop
])

# Sequential control-flow edges
root.order.add_edge(idea_setup,        asset_gather)
root.order.add_edge(asset_gather,      item_authenticate)
root.order.add_edge(item_authenticate, catalog_entry)
root.order.add_edge(catalog_entry,     legal_review)
root.order.add_edge(legal_review,      archive_check)
root.order.add_edge(archive_check,     package_items)
root.order.add_edge(package_items,     seal_capsule)
root.order.add_edge(seal_capsule,      location_scan)
root.order.add_edge(location_scan,     storage_setup)
root.order.add_edge(storage_setup,     access_control)
root.order.add_edge(access_control,    document_protocol)
root.order.add_edge(document_protocol, future_plan)
root.order.add_edge(future_plan,       loop)