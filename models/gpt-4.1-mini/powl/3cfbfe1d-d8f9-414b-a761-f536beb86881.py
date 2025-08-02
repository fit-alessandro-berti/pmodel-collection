# Generated from: 3cfbfe1d-d8f9-414b-a761-f536beb86881.json
# Description: This process manages the end-to-end supply chain for handcrafted luxury goods, integrating rare material sourcing, artisan allocation, quality assurance through traditional methods, custom order management, and dynamic pricing strategies based on market trends. It involves coordination between remote workshops, seasonal artisan availability, and bespoke packaging tailored to client preferences, ensuring authenticity and sustainability are maintained throughout the production and distribution lifecycle. The process also includes feedback loops for continuous artisan skill development and selective retailer partnerships to preserve brand exclusivity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Material_Sourcing = Transition(label='Material Sourcing')
Vendor_Vetting = Transition(label='Vendor Vetting')
Artisan_Selection = Transition(label='Artisan Selection')
Order_Customization = Transition(label='Order Customization')
Design_Approval = Transition(label='Design Approval')
Workshop_Scheduling = Transition(label='Workshop Scheduling')
Material_Inspection = Transition(label='Material Inspection')
Handcrafting = Transition(label='Handcrafting')
Quality_Checking = Transition(label='Quality Checking')
Packaging_Design = Transition(label='Packaging Design')
Sustainability_Audit = Transition(label='Sustainability Audit')
Pricing_Update = Transition(label='Pricing Update')
Inventory_Sync = Transition(label='Inventory Sync')
Retailer_Onboarding = Transition(label='Retailer Onboarding')
Skill_Feedback = Transition(label='Skill Feedback')

# LOOP for continuous artisan skill development:
# Loop body A: Skill_Feedback
# Loop body B: Artisan_Selection (retrain artisans before feedback)
loop_skill_development = OperatorPOWL(operator=Operator.LOOP, children=[Skill_Feedback, Artisan_Selection])

# Partial order for material sourcing and vendor vetting
material_procurement = StrictPartialOrder(nodes=[Material_Sourcing, Vendor_Vetting])
material_procurement.order.add_edge(Material_Sourcing, Vendor_Vetting)

# Artisan allocation part:
artisan_alloc = StrictPartialOrder(nodes=[loop_skill_development, Workshop_Scheduling])

# Quality assurance partial order:
quality_assurance = StrictPartialOrder(nodes=[Material_Inspection, Handcrafting, Quality_Checking, Sustainability_Audit])
quality_assurance.order.add_edge(Material_Inspection, Handcrafting)
quality_assurance.order.add_edge(Handcrafting, Quality_Checking)
quality_assurance.order.add_edge(Quality_Checking, Sustainability_Audit)

# Custom order and design approval partial order:
custom_order_flow = StrictPartialOrder(nodes=[Order_Customization, Design_Approval])
custom_order_flow.order.add_edge(Order_Customization, Design_Approval)

# Packaging and pricing partial order (dynamic pricing based on market trends after packaging design)
packaging_pricing = StrictPartialOrder(nodes=[Packaging_Design, Pricing_Update])
packaging_pricing.order.add_edge(Packaging_Design, Pricing_Update)

# Inventory sync and retailer onboarding (selective retailer partnerships)
inventory_retailer = StrictPartialOrder(nodes=[Inventory_Sync, Retailer_Onboarding])
inventory_retailer.order.add_edge(Inventory_Sync, Retailer_Onboarding)

# Compose the full supply chain partial order.
# Dependency and concurrency assumptions based on description:

root = StrictPartialOrder(
    nodes=[
        material_procurement,
        artisan_alloc,
        quality_assurance,
        custom_order_flow,
        packaging_pricing,
        inventory_retailer,
    ]
)

# Define edges between major phases to reflect partial order:
root.order.add_edge(material_procurement, artisan_alloc)          # artisan allocation after materials procured
root.order.add_edge(artisan_alloc, quality_assurance)              # quality assurance after artisan scheduling
root.order.add_edge(quality_assurance, custom_order_flow)          # customization after quality checked
root.order.add_edge(custom_order_flow, packaging_pricing)          # packaging and pricing after order design
root.order.add_edge(packaging_pricing, inventory_retailer)         # inventory sync before retailer onboarding

# The partial order between nodes inside sub posets is already defined

# root is the final POWL model