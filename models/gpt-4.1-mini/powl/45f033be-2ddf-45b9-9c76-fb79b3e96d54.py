# Generated from: 45f033be-2ddf-45b9-9c76-fb79b3e96d54.json
# Description: This process outlines the complex journey of artisanal cheese from farm to international markets, involving intricate steps such as raw milk sourcing, microbial culture management, controlled aging, quality certification, packaging customization, and compliance with diverse export regulations. The process also integrates seasonal production adjustments, artisan skill assessments, and dynamic logistics coordination to ensure product integrity and timely delivery across multiple countries with varying import standards and consumer preferences.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Prep = Transition(label='Culture Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Drain = Transition(label='Whey Drain')
Mold_Inoculate = Transition(label='Mold Inoculate')
Press_Forming = Transition(label='Press Forming')
Controlled_Aging = Transition(label='Controlled Aging')
Quality_Inspect = Transition(label='Quality Inspect')
Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')
Export_License = Transition(label='Export License')
Customs_Filing = Transition(label='Customs Filing')
Logistics_Plan = Transition(label='Logistics Plan')
Vendor_Audit = Transition(label='Vendor Audit')
Season_Adjust = Transition(label='Season Adjust')
Skill_Assess = Transition(label='Skill Assess')
Delivery_Track = Transition(label='Delivery Track')

# Define partial orders for the main cheese making sequence
milk_preparation = StrictPartialOrder(nodes=[Milk_Sourcing, Culture_Prep, Milk_Pasteurize])
milk_preparation.order.add_edge(Milk_Sourcing, Culture_Prep)
milk_preparation.order.add_edge(Culture_Prep, Milk_Pasteurize)

curd_process = StrictPartialOrder(
    nodes=[Curd_Cutting, Whey_Drain, Mold_Inoculate, Press_Forming]
)
curd_process.order.add_edge(Curd_Cutting, Whey_Drain)
curd_process.order.add_edge(Whey_Drain, Mold_Inoculate)
curd_process.order.add_edge(Mold_Inoculate, Press_Forming)

aging_and_inspect = StrictPartialOrder(nodes=[Controlled_Aging, Quality_Inspect])
aging_and_inspect.order.add_edge(Controlled_Aging, Quality_Inspect)

packaging_and_label = StrictPartialOrder(nodes=[Packaging_Design, Label_Approval])
packaging_and_label.order.add_edge(Packaging_Design, Label_Approval)

export_and_compliance = StrictPartialOrder(nodes=[Export_License, Customs_Filing])
export_and_compliance.order.add_edge(Export_License, Customs_Filing)

logistics = StrictPartialOrder(nodes=[Logistics_Plan, Vendor_Audit])
logistics.order.add_edge(Logistics_Plan, Vendor_Audit)

season_and_skill = StrictPartialOrder(nodes=[Season_Adjust, Skill_Assess])
season_and_skill.order.add_edge(Season_Adjust, Skill_Assess)

# Combine packaging, export, logistics, season & skill in parallel
post_quality = StrictPartialOrder(nodes=[packaging_and_label,
                                         export_and_compliance,
                                         logistics,
                                         season_and_skill])

# Connect partial orders in sequence:
# milk_preparation -> curd_process -> aging_and_inspect -> post_quality
root = StrictPartialOrder(
    nodes=[milk_preparation, curd_process, aging_and_inspect, post_quality, Delivery_Track]
)
root.order.add_edge(milk_preparation, curd_process)
root.order.add_edge(curd_process, aging_and_inspect)
root.order.add_edge(aging_and_inspect, post_quality)
root.order.add_edge(post_quality, Delivery_Track)