# Generated from: 801a66b0-af7d-490e-b529-b5fc9423db19.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm, integrating technology, sustainability, and logistics. It includes stages from environmental monitoring and seed selection to nutrient balancing and automated harvesting. The process accounts for real-time data analysis, pest control without chemicals, energy optimization using renewable sources, and distribution logistics tailored for fresh produce delivery within city limits. Additionally, it incorporates waste recycling and community engagement efforts, ensuring a closed-loop system that maximizes yield while minimizing ecological footprint and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
t_seed            = Transition(label="Seed Selection")
t_soil            = Transition(label="Soil Prep")
t_climate         = Transition(label="Climate Setup")
t_nutrient        = Transition(label="Nutrient Mix")
t_planting        = Transition(label="Planting Seeds")
t_growth          = Transition(label="Growth Monitor")
t_pest            = Transition(label="Pest Scouting")
t_led             = Transition(label="LED Adjustment")
t_water           = Transition(label="Water Recycling")
t_energy          = Transition(label="Energy Audit")
t_harvest_timing  = Transition(label="Harvest Timing")
t_pick            = Transition(label="Automated Pick")
t_quality         = Transition(label="Quality Check")
t_packaging       = Transition(label="Packaging Prep")
t_delivery        = Transition(label="Local Delivery")
t_waste           = Transition(label="Waste Sorting")
t_community       = Transition(label="Community Outreach")

# Build the main production partial order A
A = StrictPartialOrder(nodes=[
    t_seed, t_soil, t_climate, t_nutrient, t_planting, t_growth,
    t_pest, t_led, t_water, t_energy,
    t_harvest_timing, t_pick, t_quality, t_packaging, t_delivery
])
# linear flow up to LED Adjustment
A.order.add_edge(t_seed,           t_soil)
A.order.add_edge(t_soil,           t_climate)
A.order.add_edge(t_climate,        t_nutrient)
A.order.add_edge(t_nutrient,       t_planting)
A.order.add_edge(t_planting,       t_growth)
A.order.add_edge(t_growth,         t_pest)
A.order.add_edge(t_pest,           t_led)
# branch into concurrent Water Recycling and Energy Audit
A.order.add_edge(t_led,            t_water)
A.order.add_edge(t_led,            t_energy)
# converge back to Harvest Timing
A.order.add_edge(t_water,          t_harvest_timing)
A.order.add_edge(t_energy,         t_harvest_timing)
# continue linear flow to delivery
A.order.add_edge(t_harvest_timing, t_pick)
A.order.add_edge(t_pick,           t_quality)
A.order.add_edge(t_quality,        t_packaging)
A.order.add_edge(t_packaging,      t_delivery)

# Build the post‐harvest partial order B (waste & community)
B = StrictPartialOrder(nodes=[t_waste, t_community])
B.order.add_edge(t_waste, t_community)

# Wrap into a loop: do A, then either exit or do B then A again
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])