# Generated from: ccdbefad-10dd-4877-a709-0f47d3f9ca54.json
# Description: This process outlines the unconventional supply chain management for a handcrafted artisan goods company that integrates local sourcing, community collaboration, and sustainable packaging. The process begins with raw material scouting in niche markets, followed by artisan vetting and skill validation. Production scheduling is highly flexible to accommodate custom orders and seasonal availability. Quality control extends beyond product inspection to include social impact assessments. Logistics involve multi-modal transport with eco-friendly carriers and dynamic routing to reduce carbon footprint. Customer feedback loops are incorporated early and continuously to refine craftsmanship and material selection. The process concludes with adaptive inventory management that balances scarcity with demand, and a community-driven marketing strategy emphasizing storytelling and heritage preservation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Material_Scout = Transition(label='Material Scout')
Supplier_Vetting = Transition(label='Supplier Vetting')
Skill_Audit = Transition(label='Skill Audit')
Order_Forecast = Transition(label='Order Forecast')
Custom_Scheduling = Transition(label='Custom Scheduling')
Impact_Review = Transition(label='Impact Review')
Product_Inspect = Transition(label='Product Inspect')
Eco_Packaging = Transition(label='Eco Packaging')
Multi_Transport = Transition(label='Multi Transport')
Route_Optimize = Transition(label='Route Optimize')
Feedback_Loop = Transition(label='Feedback Loop')
Craft_Refine = Transition(label='Craft Refine')
Inventory_Balance = Transition(label='Inventory Balance')
Story_Marketing = Transition(label='Story Marketing')
Heritage_Share = Transition(label='Heritage Share')
Demand_Adjust = Transition(label='Demand Adjust')
Community_Sync = Transition(label='Community Sync')

# Part 1: Material Scout -> Supplier Vetting -> Skill Audit
part1 = StrictPartialOrder(nodes=[Material_Scout, Supplier_Vetting, Skill_Audit])
part1.order.add_edge(Material_Scout, Supplier_Vetting)
part1.order.add_edge(Supplier_Vetting, Skill_Audit)

# Part 2: Order Forecast, then choice of Custom Scheduling or (demand adjust + community sync)
demand_part = StrictPartialOrder(nodes=[Demand_Adjust, Community_Sync])
demand_part.order.add_edge(Demand_Adjust, Community_Sync)
custom_or_demand = OperatorPOWL(operator=Operator.XOR, children=[Custom_Scheduling, demand_part])
part2 = StrictPartialOrder(nodes=[Order_Forecast, custom_or_demand])
part2.order.add_edge(Order_Forecast, custom_or_demand)

# Part 3: Quality Control as parallel of Impact Review and Product Inspect
quality_control = StrictPartialOrder(nodes=[Impact_Review, Product_Inspect])
# no edges: they are concurrent

# Part 4: Logistics: Multi Transport -> Route Optimize
logistics = StrictPartialOrder(nodes=[Multi_Transport, Route_Optimize])
logistics.order.add_edge(Multi_Transport, Route_Optimize)

# Part 5: Feedback loop modeled as a LOOP: craft refine <- feedback loop
# LOOP(A, B) means execute A, then choose to exit or execute B then A again...
# Model: A=Craft Refine; B=Feedback Loop (repeat feedback refining continuously)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Craft_Refine, Feedback_Loop])

# Part 6: Packaging (Eco Packaging) and inventory balance
packaging_inventory = StrictPartialOrder(nodes=[Eco_Packaging, Inventory_Balance])
# no order => concurrent

# Part 7: Marketing: Story Marketing -> Heritage Share
marketing = StrictPartialOrder(nodes=[Story_Marketing, Heritage_Share])
marketing.order.add_edge(Story_Marketing, Heritage_Share)

# Part 8: Compose all parts in overall partial order
nodes = [part1, part2, quality_control, logistics, feedback_loop,
         packaging_inventory, marketing]

root = StrictPartialOrder(nodes=nodes)

# Define ordering between process phases:

# After skill audit -> order forecast
root.order.add_edge(part1, part2)

# After part2 -> quality control
root.order.add_edge(part2, quality_control)

# quality control -> logistics
root.order.add_edge(quality_control, logistics)

# logistics -> packaging & inventory
root.order.add_edge(logistics, packaging_inventory)

# packaging & inventory -> feedback loop (refine/craft)
root.order.add_edge(packaging_inventory, feedback_loop)

# feedback loop -> marketing
root.order.add_edge(feedback_loop, marketing)