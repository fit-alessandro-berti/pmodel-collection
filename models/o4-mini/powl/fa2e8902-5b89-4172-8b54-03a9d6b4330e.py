# Generated from: fa2e8902-5b89-4172-8b54-03a9d6b4330e.json
# Description: This process outlines the complex operations involved in managing an urban vertical farming facility. It integrates advanced hydroponic cultivation, automated climate control, and real-time nutrient monitoring to optimize plant growth in limited city spaces. The workflow handles seed selection, germination, growth phase transitions, pest management using biological controls, and harvest scheduling. Post-harvest, it includes quality inspection, packaging, and cold chain logistics tailored for rapid urban delivery. Additionally, the process incorporates data analytics to forecast yield, energy consumption optimization, and sustainability compliance reporting, ensuring both economic viability and environmental responsibility in high-density agricultural production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
seed_selection   = Transition(label='Seed Selection')
germination_start= Transition(label='Germination Start')
nutrient_mix     = Transition(label='Nutrient Mix')
climate_adjust   = Transition(label='Climate Adjust')
light_scheduling = Transition(label='Light Scheduling')
pest_inspection  = Transition(label='Pest Inspection')
bio_control      = Transition(label='Bio Control')
growth_monitor   = Transition(label='Growth Monitor')
water_recirc     = Transition(label='Water Recirc')
harvest_plan     = Transition(label='Harvest Plan')
yield_forecast   = Transition(label='Yield Forecast')
quality_check    = Transition(label='Quality Check')
packaging_prep   = Transition(label='Packaging Prep')
cold_storage     = Transition(label='Cold Storage')
delivery_route   = Transition(label='Delivery Route')
energy_audit     = Transition(label='Energy Audit')
sustain_report   = Transition(label='Sustain Report')
skip             = SilentTransition()

# Pest management choice: after inspection either do bio control or skip
pest_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[skip, bio_control]
)

# Define the body of the growth loop: nutrient, climate, light, water, pest inspection + choice
growth_body = StrictPartialOrder(nodes=[
    nutrient_mix,
    climate_adjust,
    light_scheduling,
    water_recirc,
    pest_inspection,
    pest_choice
])
growth_body.order.add_edge(nutrient_mix,   climate_adjust)
growth_body.order.add_edge(climate_adjust, light_scheduling)
growth_body.order.add_edge(light_scheduling, water_recirc)
growth_body.order.add_edge(water_recirc,    pest_inspection)
growth_body.order.add_edge(pest_inspection, pest_choice)

# Loop: monitor growth, then either exit or execute the growth body and monitor again
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitor, growth_body]
)

# Top‐level partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    growth_loop,
    harvest_plan,
    quality_check,
    packaging_prep,
    cold_storage,
    delivery_route,
    yield_forecast,
    energy_audit,
    sustain_report
])

# Define control‐flow
root.order.add_edge(seed_selection,    germination_start)
root.order.add_edge(germination_start, growth_loop)
root.order.add_edge(growth_loop,       harvest_plan)
root.order.add_edge(harvest_plan,      quality_check)
root.order.add_edge(quality_check,     packaging_prep)
root.order.add_edge(packaging_prep,    cold_storage)
root.order.add_edge(cold_storage,      delivery_route)

# Analytics tasks start after harvest plan, in parallel
root.order.add_edge(harvest_plan,      yield_forecast)
root.order.add_edge(harvest_plan,      energy_audit)
root.order.add_edge(harvest_plan,      sustain_report)