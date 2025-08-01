# Generated from: d0cf4273-eab2-49ce-b5c6-f197073e53a3.json
# Description: This process details the intricate and atypical supply chain management of hand-crafted artisan goods, where raw materials are sourced from remote, sustainable locations, verified by cultural custodians, then transported using eco-friendly methods. Each batch undergoes quality storytelling sessions to preserve origin narratives before craftsmen transform them into unique products. Post-production, items are cataloged with provenance data, then marketed via niche community platforms targeting collectors. Finally, bespoke packaging is assembled by local cooperatives, ensuring minimal environmental impact and fostering social responsibility, followed by global distribution handled in collaboration with ethical logistics partners.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Material_Sourcing = Transition(label='Material Sourcing')
Cultural_Verify = Transition(label='Cultural Verify')
Eco_Transport = Transition(label='Eco Transport')
Batch_Storytelling = Transition(label='Batch Storytelling')
Craftsman_Assignment = Transition(label='Craftsman Assignment')
Product_Creation = Transition(label='Product Creation')
Provenance_Catalog = Transition(label='Provenance Catalog')
Community_Marketing = Transition(label='Community Marketing')
Collector_Targeting = Transition(label='Collector Targeting')
Package_Assembly = Transition(label='Package Assembly')
Local_Cooperatives = Transition(label='Local Cooperatives')
Environmental_Audit = Transition(label='Environmental Audit')
Ethical_Logistics = Transition(label='Ethical Logistics')
Global_Shipping = Transition(label='Global Shipping')
Feedback_Collection = Transition(label='Feedback Collection')

# Step 1-3: Material Sourcing → Cultural Verify → Eco Transport (strict order)
source_to_transport = StrictPartialOrder(nodes=[Material_Sourcing, Cultural_Verify, Eco_Transport])
source_to_transport.order.add_edge(Material_Sourcing, Cultural_Verify)
source_to_transport.order.add_edge(Cultural_Verify, Eco_Transport)

# Step 4: Batch Storytelling after Eco Transport
batch_story = StrictPartialOrder(nodes=[Eco_Transport, Batch_Storytelling])
batch_story.order.add_edge(Eco_Transport, Batch_Storytelling)

# Step 5-6: Craftsman Assignment → Product Creation (strict order from storytelling)
craft_and_create = StrictPartialOrder(nodes=[Batch_Storytelling, Craftsman_Assignment, Product_Creation])
craft_and_create.order.add_edge(Batch_Storytelling, Craftsman_Assignment)
craft_and_create.order.add_edge(Craftsman_Assignment, Product_Creation)

# Step 7-9: Provenance Catalog → Community Marketing → Collector Targeting
catalog_to_marketing = StrictPartialOrder(nodes=[Product_Creation, Provenance_Catalog, Community_Marketing, Collector_Targeting])
catalog_to_marketing.order.add_edge(Product_Creation, Provenance_Catalog)
catalog_to_marketing.order.add_edge(Provenance_Catalog, Community_Marketing)
catalog_to_marketing.order.add_edge(Community_Marketing, Collector_Targeting)

# Step 10-11: Package Assembly done by Local Cooperatives
# These two happen in sequence: Package Assembly → Local Cooperatives
packaging = StrictPartialOrder(nodes=[Collector_Targeting, Package_Assembly, Local_Cooperatives])
packaging.order.add_edge(Collector_Targeting, Package_Assembly)
packaging.order.add_edge(Package_Assembly, Local_Cooperatives)

# Step 12: Environmental Audit presumably concurrent with packaging or after local cooperatives?
# Since it is an audit ensuring minimal environmental impact, associate it after Local Cooperatives
audit = StrictPartialOrder(nodes=[Local_Cooperatives, Environmental_Audit])
audit.order.add_edge(Local_Cooperatives, Environmental_Audit)

# Step 13-14: Ethical Logistics → Global Shipping
logistics = StrictPartialOrder(nodes=[Environmental_Audit, Ethical_Logistics, Global_Shipping])
logistics.order.add_edge(Environmental_Audit, Ethical_Logistics)
logistics.order.add_edge(Ethical_Logistics, Global_Shipping)

# Step 15: Feedback Collection after Global Shipping
final_feedback = StrictPartialOrder(nodes=[Global_Shipping, Feedback_Collection])
final_feedback.order.add_edge(Global_Shipping, Feedback_Collection)

# Now we combine all partial orders in the correct sequence,
# linking the roots appropriately by edges between subprocesses.

# Combine all nodes
all_nodes = [
    source_to_transport,
    batch_story,
    craft_and_create,
    catalog_to_marketing,
    packaging,
    audit,
    logistics,
    final_feedback
]

# We build a main partial order with all subprocesses as nodes
root = StrictPartialOrder(nodes=all_nodes)

# Add edges between subprocesses to respect sequence:
# source_to_transport → batch_story
root.order.add_edge(source_to_transport, batch_story)
# batch_story → craft_and_create
root.order.add_edge(batch_story, craft_and_create)
# craft_and_create → catalog_to_marketing
root.order.add_edge(craft_and_create, catalog_to_marketing)
# catalog_to_marketing → packaging
root.order.add_edge(catalog_to_marketing, packaging)
# packaging → audit
root.order.add_edge(packaging, audit)
# audit → logistics
root.order.add_edge(audit, logistics)
# logistics → final_feedback
root.order.add_edge(logistics, final_feedback)