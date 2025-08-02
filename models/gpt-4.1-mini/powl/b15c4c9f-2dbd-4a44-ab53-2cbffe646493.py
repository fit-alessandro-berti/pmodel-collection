# Generated from: b15c4c9f-2dbd-4a44-ab53-2cbffe646493.json
# Description: This process manages the end-to-end supply chain for handcrafted artisan goods, integrating unpredictable raw material sourcing from remote locations, specialized artisan scheduling, quality validation by expert panels, and bespoke packaging options. It includes dynamic demand forecasting based on cultural trends, adaptive logistics for fragile items, and collaborative marketing with local communities to preserve authenticity while scaling distribution globally. The process ensures traceability of materials, artisan skill certification, and sustainable practices compliance, creating a unique blend of traditional craftsmanship and modern supply chain management that supports niche markets and ethical consumerism.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities as atomic transitions
Source_Materials = Transition(label='Source Materials')
Verify_Origins = Transition(label='Verify Origins')
Schedule_Artisans = Transition(label='Schedule Artisans')
Assign_Orders = Transition(label='Assign Orders')
Craft_Items = Transition(label='Craft Items')
Quality_Review = Transition(label='Quality Review')
Panel_Approval = Transition(label='Panel Approval')
Material_Trace = Transition(label='Material Trace')
Certify_Skills = Transition(label='Certify Skills')
Package_Custom = Transition(label='Package Custom')
Plan_Logistics = Transition(label='Plan Logistics')
Arrange_Shipping = Transition(label='Arrange Shipping')
Track_Deliveries = Transition(label='Track Deliveries')
Collect_Feedback = Transition(label='Collect Feedback')
Update_Forecast = Transition(label='Update Forecast')
Engage_Communities = Transition(label='Engage Communities')
Sustainability_Audit = Transition(label='Sustainability Audit')
Market_Collaborate = Transition(label='Market Collaborate')

# Modeling the supply chain process logic with partial orders and control flow operators.
# 1) Source Materials and Verify Origins happen in sequence (raw material sourcing)
raw_material_sourcing = StrictPartialOrder(nodes=[Source_Materials, Verify_Origins])
raw_material_sourcing.order.add_edge(Source_Materials, Verify_Origins)

# 2) Schedule Artisans and Assign Orders happen after Verify Origins, can be partially concurrent after it
artisan_scheduling = StrictPartialOrder(nodes=[Schedule_Artisans, Assign_Orders])
artisan_scheduling.order.add_edge(Schedule_Artisans, Assign_Orders)

# 3) Craft Items depends on Assign Orders
# 4) Quality Review and Panel Approval form a sequence quality validation step after Craft Items
quality_validation = StrictPartialOrder(nodes=[Quality_Review, Panel_Approval])
quality_validation.order.add_edge(Quality_Review, Panel_Approval)

# 5) Material Trace and Certify Skills happen concurrently to ensure compliance before packaging
compliance_checks = StrictPartialOrder(nodes=[Material_Trace, Certify_Skills])

# 6) Package Custom depends on compliance checks completed
package_custom = Package_Custom

# 7) Plan Logistics, Arrange Shipping, Track Deliveries are sequential for logistics tracking
logistics = StrictPartialOrder(nodes=[Plan_Logistics, Arrange_Shipping, Track_Deliveries])
logistics.order.add_edge(Plan_Logistics, Arrange_Shipping)
logistics.order.add_edge(Arrange_Shipping, Track_Deliveries)

# 8) Collect Feedback and Update Forecast form a loop related to demand forecasting and feedback
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Update_Forecast, Collect_Feedback])

# 9) Engage Communities and Market Collaborate happen possibly in parallel after feedback loop
community_marketing = StrictPartialOrder(nodes=[Engage_Communities, Market_Collaborate])

# 10) Sustainability Audit happens as a compliance ongoing measure, concurrent with community marketing
# Let's merge sustainability audit with community marketing as partial order (concurrent)
community_sustainability = StrictPartialOrder(nodes=[Sustainability_Audit, Engage_Communities, Market_Collaborate])
community_sustainability.order.add_edge(Engage_Communities, Market_Collaborate)

# Compose the main flow using partial orders and edges to express process dependencies

# Step 1->2: Verify Origins to artisan_scheduling's first node Schedule Artisans
# Step 2->3: Assign Orders to Craft Items
# Step 3->4: Craft Items to quality_validation
# Step 4->5: Panel Approval to compliance_checks nodes
# Step 5->6: compliance_checks to Package Custom
# Step 6->7: Package Custom to logistics
# Step 7->8: logistics to feedback_loop
# Step 8->9: feedback_loop to community_sustainability

# Define composite process step nodes to connect edges
# For compound partial orders we use the objects directly.

# Define a partial order for artisan scheduling chain (Schedule Artisans->Assign Orders)
artisan_scheduling_complete = StrictPartialOrder(nodes=[Schedule_Artisans, Assign_Orders])
artisan_scheduling_complete.order.add_edge(Schedule_Artisans, Assign_Orders)

# Connect all together in a larger partial order
nodes = [
    raw_material_sourcing,
    artisan_scheduling_complete,
    Craft_Items,
    quality_validation,
    compliance_checks,
    Package_Custom,
    logistics,
    feedback_loop,
    community_sustainability
]

root = StrictPartialOrder(nodes=nodes)

# Add edges to enforce order:
# raw_material_sourcing --> artisan_scheduling_complete
root.order.add_edge(raw_material_sourcing, artisan_scheduling_complete)
# artisan_scheduling_complete --> Craft_Items
root.order.add_edge(artisan_scheduling_complete, Craft_Items)
# Craft_Items --> quality_validation
root.order.add_edge(Craft_Items, quality_validation)
# quality_validation --> compliance_checks
root.order.add_edge(quality_validation, compliance_checks)
# compliance_checks --> Package_Custom
root.order.add_edge(compliance_checks, Package_Custom)
# Package_Custom --> logistics
root.order.add_edge(Package_Custom, logistics)
# logistics --> feedback_loop
root.order.add_edge(logistics, feedback_loop)
# feedback_loop --> community_sustainability
root.order.add_edge(feedback_loop, community_sustainability)