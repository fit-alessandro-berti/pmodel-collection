# Generated from: fa2e8902-5b89-4172-8b54-03a9d6b4330e.json
# Description: This process outlines the complex operations involved in managing an urban vertical farming facility. It integrates advanced hydroponic cultivation, automated climate control, and real-time nutrient monitoring to optimize plant growth in limited city spaces. The workflow handles seed selection, germination, growth phase transitions, pest management using biological controls, and harvest scheduling. Post-harvest, it includes quality inspection, packaging, and cold chain logistics tailored for rapid urban delivery. Additionally, the process incorporates data analytics to forecast yield, energy consumption optimization, and sustainability compliance reporting, ensuring both economic viability and environmental responsibility in high-density agricultural production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transition objects
Seed_Selection = Transition(label='Seed Selection')
Germination_Start = Transition(label='Germination Start')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Adjust = Transition(label='Climate Adjust')
Light_Scheduling = Transition(label='Light Scheduling')
Pest_Inspection = Transition(label='Pest Inspection')
Bio_Control = Transition(label='Bio Control')
Growth_Monitor = Transition(label='Growth Monitor')
Water_Recirc = Transition(label='Water Recirc')
Harvest_Plan = Transition(label='Harvest Plan')
Yield_Forecast = Transition(label='Yield Forecast')
Quality_Check = Transition(label='Quality Check')
Packaging_Prep = Transition(label='Packaging Prep')
Cold_Storage = Transition(label='Cold Storage')
Delivery_Route = Transition(label='Delivery Route')
Energy_Audit = Transition(label='Energy Audit')
Sustain_Report = Transition(label='Sustain Report')

# Pest management loop: Pest Inspection then Bio Control repeatedly until exit
pest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Pest_Inspection, Bio_Control]
)

# Growth phase is a partial order with nutrient, climate, light scheduling concurrently after germination
growth_phase = StrictPartialOrder(nodes=[Nutrient_Mix, Climate_Adjust, Light_Scheduling])
# All three run concurrently, no order needed inside growth phase

# Monitoring and water recirculation concurrent activities after growth phase
monitoring_phase = StrictPartialOrder(nodes=[Growth_Monitor, Water_Recirc])
# Concurrent activities

# Harvest and post-harvest sequence with concurrent packaging and cold storage, then delivery
packaging_and_storage = StrictPartialOrder(nodes=[Packaging_Prep, Cold_Storage])
# Packaging Prep and Cold Storage concurrent

post_harvest = StrictPartialOrder(
    nodes=[Quality_Check, packaging_and_storage, Delivery_Route],
)
# Quality check before packaging_and_storage and delivery; delivery after them both

post_harvest.order.add_edge(Quality_Check, packaging_and_storage)
post_harvest.order.add_edge(Quality_Check, Delivery_Route)
post_harvest.order.add_edge(packaging_and_storage, Delivery_Route)

# Analysis and reporting concurrent with harvest planning and post-harvest execution
analysis_reporting = StrictPartialOrder(
    nodes=[Yield_Forecast, Energy_Audit, Sustain_Report]
)
# All three concurrent

# Harvest plan before post harvest and concurrent analysis phase
harvest_and_post = StrictPartialOrder(
    nodes=[Harvest_Plan, post_harvest, analysis_reporting]
)
harvest_and_post.order.add_edge(Harvest_Plan, post_harvest)
harvest_and_post.order.add_edge(Harvest_Plan, analysis_reporting)

# Overall process construction as a partial order:
# Sequence:
# Seed Selection -> Germination Start -> Pest Loop (loop) -> growth phase -> monitoring phase -> harvest_and_post

root = StrictPartialOrder(
    nodes=[Seed_Selection,
           Germination_Start,
           pest_loop,
           growth_phase,
           monitoring_phase,
           harvest_and_post]
)

root.order.add_edge(Seed_Selection, Germination_Start)
root.order.add_edge(Germination_Start, pest_loop)
root.order.add_edge(pest_loop, growth_phase)
root.order.add_edge(growth_phase, monitoring_phase)
root.order.add_edge(monitoring_phase, harvest_and_post)