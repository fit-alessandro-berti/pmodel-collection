# Generated from: 36848c87-2525-4cc9-b3cc-ff407f7d9286.json
# Description: This process outlines the intricate journey of sourcing, processing, and distributing small-batch artisanal coffee beans from remote farms to specialty cafes worldwide. It involves unique steps such as local farmer engagement, micro-lot selection, hand-processing, quality cupping, eco-friendly packaging, and bespoke logistics coordination. The process emphasizes sustainability, traceability, and maintaining bean integrity throughout transportation and roasting. Each activity ensures the preservation of flavor profiles and ethical practices, resulting in a premium coffee experience for discerning consumers.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
farm_outreach = Transition(label='Farm Outreach')
bean_selection = Transition(label='Bean Selection')
hand_picking = Transition(label='Hand Picking')
initial_sorting = Transition(label='Initial Sorting')
wet_processing = Transition(label='Wet Processing')
sun_drying = Transition(label='Sun Drying')
quality_cupping = Transition(label='Quality Cupping')
micro_lot_grading = Transition(label='Micro-lot Grading')
eco_packaging = Transition(label='Eco Packaging')
custom_labeling = Transition(label='Custom Labeling')
inventory_sync = Transition(label='Inventory Sync')
specialty_roasting = Transition(label='Specialty Roasting')
logistics_setup = Transition(label='Logistics Setup')
cafe_delivery = Transition(label='Cafe Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Craft a partial order reflecting the described process:

# Phase 1: Sourcing & processing beans
# Farm Outreach --> Bean Selection and Hand Picking (concurrent after outreach)
# Bean Selection and Hand Picking --> Initial Sorting
# Initial Sorting --> wet processing and sun drying in parallel
# Wet Processing and Sun Drying --> Quality Cupping
# Quality Cupping --> Micro-lot Grading

# Phase 2: Packaging & preparing for market
# Micro-lot Grading --> Eco Packaging --> Custom Labeling
# Custom Labeling --> Inventory Sync (preparation for roasting)

# Phase 3: Roasting & delivery
# Inventory Sync --> Specialty Roasting --> Logistics Setup
# Logistics Setup --> Cafe Delivery --> Customer Feedback

# Some concurrency:
# Bean Selection and Hand Picking can proceed concurrently after Farm Outreach
# Wet Processing and Sun Drying proceed concurrently after Initial Sorting

# Create the PO nodes
nodes = [
    farm_outreach,
    bean_selection,
    hand_picking,
    initial_sorting,
    wet_processing,
    sun_drying,
    quality_cupping,
    micro_lot_grading,
    eco_packaging,
    custom_labeling,
    inventory_sync,
    specialty_roasting,
    logistics_setup,
    cafe_delivery,
    customer_feedback
]

root = StrictPartialOrder(nodes=nodes)

# Add edges:

# Farm Outreach --> {Bean Selection, Hand Picking}
root.order.add_edge(farm_outreach, bean_selection)
root.order.add_edge(farm_outreach, hand_picking)

# Bean Selection --> Initial Sorting
root.order.add_edge(bean_selection, initial_sorting)

# Hand Picking --> Initial Sorting
root.order.add_edge(hand_picking, initial_sorting)

# Initial Sorting --> Wet Processing and Sun Drying (concurrent)
root.order.add_edge(initial_sorting, wet_processing)
root.order.add_edge(initial_sorting, sun_drying)

# Wet Processing --> Quality Cupping
root.order.add_edge(wet_processing, quality_cupping)

# Sun Drying --> Quality Cupping
root.order.add_edge(sun_drying, quality_cupping)

# Quality Cupping --> Micro-lot Grading
root.order.add_edge(quality_cupping, micro_lot_grading)

# Micro-lot Grading --> Eco Packaging
root.order.add_edge(micro_lot_grading, eco_packaging)

# Eco Packaging --> Custom Labeling
root.order.add_edge(eco_packaging, custom_labeling)

# Custom Labeling --> Inventory Sync
root.order.add_edge(custom_labeling, inventory_sync)

# Inventory Sync --> Specialty Roasting
root.order.add_edge(inventory_sync, specialty_roasting)

# Specialty Roasting --> Logistics Setup
root.order.add_edge(specialty_roasting, logistics_setup)

# Logistics Setup --> Cafe Delivery
root.order.add_edge(logistics_setup, cafe_delivery)

# Cafe Delivery --> Customer Feedback
root.order.add_edge(cafe_delivery, customer_feedback)