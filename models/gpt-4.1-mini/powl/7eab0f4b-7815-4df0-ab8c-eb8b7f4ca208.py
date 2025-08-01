# Generated from: 7eab0f4b-7815-4df0-ab8c-eb8b7f4ca208.json
# Description: This process involves the creation and management of a corporate time capsule intended to preserve company culture, achievements, and predictions for future employees. The process starts with idea generation and asset collection, followed by authentication and cataloging of items. Afterward, it requires coordination with legal and archival teams to ensure compliance and preservation standards. Packaging and secure sealing of the capsule precede the selection of a physical or digital storage location. Finally, formal documentation and a future opening protocol are established to guarantee the capsule's integrity and relevance over decades, involving periodic reviews and updates to the contents as the company evolves.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Idea_Setup = Transition(label='Idea Setup')
Asset_Gather = Transition(label='Asset Gather')
Item_Authenticate = Transition(label='Item Authenticate')
Catalog_Entry = Transition(label='Catalog Entry')
Legal_Review = Transition(label='Legal Review')
Archive_Check = Transition(label='Archive Check')
Package_Items = Transition(label='Package Items')
Seal_Capsule = Transition(label='Seal Capsule')
Location_Scan = Transition(label='Location Scan')
Storage_Setup = Transition(label='Storage Setup')
Access_Control = Transition(label='Access Control')
Document_Protocol = Transition(label='Document Protocol')
Future_Plan = Transition(label='Future Plan')
Review_Cycle = Transition(label='Review Cycle')
Update_Content = Transition(label='Update Content')

# Define the loop body: Review Cycle followed by Update Content, then back to loop start (Review Cycle again) or exit
loop_body = StrictPartialOrder(nodes=[Review_Cycle, Update_Content])
loop_body.order.add_edge(Review_Cycle, Update_Content)
loop = OperatorPOWL(operator=Operator.LOOP, children=[Future_Plan, loop_body])

# Partial order for initial setup: Idea_Setup --> Asset_Gather --> Item_Authenticate --> Catalog_Entry
initial_setup = StrictPartialOrder(
    nodes=[Idea_Setup, Asset_Gather, Item_Authenticate, Catalog_Entry]
)
initial_setup.order.add_edge(Idea_Setup, Asset_Gather)
initial_setup.order.add_edge(Asset_Gather, Item_Authenticate)
initial_setup.order.add_edge(Item_Authenticate, Catalog_Entry)

# Partial order for compliance check: Legal_Review --> Archive_Check
compliance_check = StrictPartialOrder(nodes=[Legal_Review, Archive_Check])
compliance_check.order.add_edge(Legal_Review, Archive_Check)

# Partial order for packaging: Package_Items --> Seal_Capsule
packaging = StrictPartialOrder(nodes=[Package_Items, Seal_Capsule])
packaging.order.add_edge(Package_Items, Seal_Capsule)

# Partial order for storage setup: Location_Scan and Storage_Setup can be concurrent, both precede Access_Control
storage = StrictPartialOrder(nodes=[Location_Scan, Storage_Setup, Access_Control])
storage.order.add_edge(Location_Scan, Access_Control)
storage.order.add_edge(Storage_Setup, Access_Control)

# Combine all major parts into the final StrictPartialOrder
root = StrictPartialOrder(
    nodes=[initial_setup, compliance_check, packaging, storage, Document_Protocol, loop]
)

# Define order dependencies between parts according to the process description:
# initial_setup --> compliance_check --> packaging --> storage --> Document_Protocol --> loop (Future_Plan + Review/Update loop)
root.order.add_edge(initial_setup, compliance_check)
root.order.add_edge(compliance_check, packaging)
root.order.add_edge(packaging, storage)
root.order.add_edge(storage, Document_Protocol)
root.order.add_edge(Document_Protocol, loop)