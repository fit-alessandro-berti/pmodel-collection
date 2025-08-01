# Generated from: 2153676c-d141-4308-8b3d-94ffafe1726e.json
# Description: This process manages the end-to-end flow of handcrafted materials from local artisan sourcing through quality verification, customized order assembly, and eco-friendly packaging to final distribution. It integrates traditional craftsmanship validation with modern logistics coordination, ensuring sustainable sourcing, traceability, and timely delivery while maintaining artisan uniqueness and regulatory compliance. The process includes dynamic inventory adjustments based on seasonal artisan availability and customer demand forecasting, alongside continuous feedback loops for artisan skill development and customer satisfaction enhancement.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
source_artisans = Transition(label='Source Artisans')
verify_quality = Transition(label='Verify Quality')
design_custom = Transition(label='Design Custom')
order_assembly = Transition(label='Order Assembly')
material_sorting = Transition(label='Material Sorting')
skill_assessment = Transition(label='Skill Assessment')
inventory_update = Transition(label='Inventory Update')
demand_forecast = Transition(label='Demand Forecast')
package_eco = Transition(label='Package Eco')
compliance_check = Transition(label='Compliance Check')
logistics_plan = Transition(label='Logistics Plan')
dispatch_goods = Transition(label='Dispatch Goods')
customer_feedback = Transition(label='Customer Feedback')
skill_training = Transition(label='Skill Training')
traceability_log = Transition(label='Traceability Log')
seasonal_adjust = Transition(label='Seasonal Adjust')

# Skill development continuous feedback loop:
# loop: execute Skill Assessment then choose exit or execute Skill Training then Skill Assessment again
skill_loop = OperatorPOWL(operator=Operator.LOOP, children=[skill_assessment, skill_training])

# Inventory adjustment feedback loop:
# loop: execute Demand Forecast then choose exit or execute Seasonal Adjust then Demand Forecast again
inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, seasonal_adjust])

# Customer satisfaction feedback loop (feedback on process via Customer Feedback)
# Model as a choice of (Customer Feedback or silent transition to allow skipping feedback)
skip = SilentTransition()
customer_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])

# The main sequence partial order from sourcing to dispatching
main_po = StrictPartialOrder(nodes=[
    source_artisans,
    verify_quality,
    design_custom,
    order_assembly,
    material_sorting,
    skill_loop,
    inventory_update,
    inventory_loop,
    package_eco,
    compliance_check,
    traceability_log,
    logistics_plan,
    dispatch_goods,
    customer_feedback_choice
])

# Add edges for the main process flow
main_po.order.add_edge(source_artisans, verify_quality)
main_po.order.add_edge(verify_quality, design_custom)
main_po.order.add_edge(design_custom, order_assembly)
main_po.order.add_edge(order_assembly, material_sorting)

# After material sorting, skill_loop and inventory_update happen (partially ordered: skill_loop and inventory_update do not depend on each other)
main_po.order.add_edge(material_sorting, skill_loop)
main_po.order.add_edge(material_sorting, inventory_update)

# skill_loop must finish before package_eco
main_po.order.add_edge(skill_loop, package_eco)
# inventory_update precedes inventory_loop
main_po.order.add_edge(inventory_update, inventory_loop)
# inventory_loop precedes package_eco
main_po.order.add_edge(inventory_loop, package_eco)

# Then from package_eco to compliance_check, traceability_log, logistics_plan in parallel (all after package_eco)
main_po.order.add_edge(package_eco, compliance_check)
main_po.order.add_edge(package_eco, traceability_log)
main_po.order.add_edge(package_eco, logistics_plan)

# compliance_check and traceability_log must complete before dispatch_goods
main_po.order.add_edge(compliance_check, dispatch_goods)
main_po.order.add_edge(traceability_log, dispatch_goods)

# logistics_plan must complete before dispatch_goods
main_po.order.add_edge(logistics_plan, dispatch_goods)

# dispatch_goods precedes customer feedback (choice between feedback or skip)
main_po.order.add_edge(dispatch_goods, customer_feedback_choice)

root = main_po