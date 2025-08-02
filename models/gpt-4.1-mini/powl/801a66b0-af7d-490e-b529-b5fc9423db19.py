# Generated from: 801a66b0-af7d-490e-b529-b5fc9423db19.json
# Description: This process outlines the comprehensive cycle of managing an urban vertical farm, integrating technology, sustainability, and logistics. It includes stages from environmental monitoring and seed selection to nutrient balancing and automated harvesting. The process accounts for real-time data analysis, pest control without chemicals, energy optimization using renewable sources, and distribution logistics tailored for fresh produce delivery within city limits. Additionally, it incorporates waste recycling and community engagement efforts, ensuring a closed-loop system that maximizes yield while minimizing ecological footprint and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Seed_Selection = Transition(label='Seed Selection')
Soil_Prep = Transition(label='Soil Prep')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Planting_Seeds = Transition(label='Planting Seeds')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Scouting = Transition(label='Pest Scouting')
LED_Adjustment = Transition(label='LED Adjustment')
Water_Recycling = Transition(label='Water Recycling')
Energy_Audit = Transition(label='Energy Audit')
Harvest_Timing = Transition(label='Harvest Timing')
Automated_Pick = Transition(label='Automated Pick')
Quality_Check = Transition(label='Quality Check')
Packaging_Prep = Transition(label='Packaging Prep')
Local_Delivery = Transition(label='Local Delivery')
Waste_Sorting = Transition(label='Waste Sorting')
Community_Outreach = Transition(label='Community Outreach')

# Model parts:

# 1) Initial preparation & planting sequence
prep_and_plant = StrictPartialOrder(nodes=[
    Seed_Selection,
    Soil_Prep,
    Climate_Setup,
    Nutrient_Mix,
    Planting_Seeds
])
prep_and_plant.order.add_edge(Seed_Selection, Soil_Prep)
prep_and_plant.order.add_edge(Soil_Prep, Climate_Setup)
prep_and_plant.order.add_edge(Climate_Setup, Nutrient_Mix)
prep_and_plant.order.add_edge(Nutrient_Mix, Planting_Seeds)

# 2) Growth monitoring with pest scouting and LED adjustment concurrently
# Growth Monitor is central with Pest Scouting and LED Adjustment done concurrently during growing phase
growth_monitoring = StrictPartialOrder(nodes=[
    Growth_Monitor,
    Pest_Scouting,
    LED_Adjustment
])
# Growth Monitor precedes quality check later, but all three can be concurrent here
# We keep no order edges between Pest_Scouting and LED_Adjustment for concurrency

# 3) Water recycling and Energy audit are ongoing sustainability efforts and concurrent with growth monitoring
sustainability = StrictPartialOrder(nodes=[
    Water_Recycling,
    Energy_Audit
])
# No order between sustainability and growth monitoring, run concurrently

# Combine growth_monitoring and sustainability concurrently
growth_and_sustain = StrictPartialOrder(nodes=[
    growth_monitoring,
    sustainability
])
# No edges connecting growth_monitoring to sustainability to keep concurrent

# 4) Harvesting loop: Harvest Timing leading to Automated Pick, then Quality Check
harvest_loop_body = StrictPartialOrder(nodes=[
    Harvest_Timing,
    Automated_Pick
])
harvest_loop_body.order.add_edge(Harvest_Timing, Automated_Pick)

harvest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[harvest_loop_body, Quality_Check]
)
# LOOP(X, Y) = do X, then choose exit or do Y and X again
# Here: execute Harvest Timing + Automated Pick,
# then choose to exit or do Quality Check and repeat harvesting again

# 5) Packaging + delivery after harvest loop ends
packaging_and_delivery = StrictPartialOrder(nodes=[
    Packaging_Prep,
    Local_Delivery
])
packaging_and_delivery.order.add_edge(Packaging_Prep, Local_Delivery)

# 6) Closing loop with Waste Sorting and Community Outreach as a partial order concurrent with packaging/delivery
closing_tasks = StrictPartialOrder(nodes=[
    Waste_Sorting,
    Community_Outreach
])
# They are concurrent, no order edges

# Combine packaging/delivery and closing tasks concurrently
finalization = StrictPartialOrder(nodes=[
    packaging_and_delivery,
    closing_tasks
])
# No order edge between packaging_and_delivery and closing_tasks

# Build top-level partial order:
# prep_and_plant -> growth_and_sustain -> harvest_loop -> finalization
root = StrictPartialOrder(nodes=[
    prep_and_plant,
    growth_and_sustain,
    harvest_loop,
    finalization
])
root.order.add_edge(prep_and_plant, growth_and_sustain)
root.order.add_edge(growth_and_sustain, harvest_loop)
root.order.add_edge(harvest_loop, finalization)