# Generated from: 29baf9f8-36f4-4f09-be56-cddb789d4878.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm in a densely populated city. It includes site assessment for structural integrity and sunlight exposure, regulatory compliance checks, soil and water testing, modular bed construction, seed selection for microclimates, installation of automated irrigation and nutrient delivery systems, pest management using integrated biological controls, community engagement for local participation, ongoing data monitoring through IoT sensors, yield forecasting, and seasonal crop rotation planning. The process also integrates waste composting from urban sources and renewable energy usage to minimize environmental footprint, ensuring economic viability and social impact in an unconventional agricultural setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site      = Transition(label='Site Survey')
risk      = Transition(label='Risk Assess')
permit    = Transition(label='Permit Check')
soil      = Transition(label='Soil Sample')
water     = Transition(label='Water Test')
bed       = Transition(label='Bed Build')
compost   = Transition(label='Waste Compost')
energy    = Transition(label='Energy Integrate')
seed      = Transition(label='Seed Select')
irrig     = Transition(label='Irrigation Install')
nutrient  = Transition(label='Nutrient Setup')
pest      = Transition(label='Pest Control')
community = Transition(label='Community Engage')
sensor    = Transition(label='Sensor Deploy')

# Build the monitoring+forecast sub‐process for the loop body (A)
monitor  = Transition(label='Data Monitor')
forecast = Transition(label='Yield Forecast')
A = StrictPartialOrder(nodes=[monitor, forecast])
A.order.add_edge(monitor, forecast)

# Define the loop: repeat A or exit; on each iteration after A you may do Crop Rotate
crop_rotate = Transition(label='Crop Rotate')
monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[A, crop_rotate])

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[
    site, risk, permit, soil, water, bed,
    compost, energy, seed, irrig, nutrient,
    pest, community, sensor,
    monitoring_loop
])

# Sequence the main setup steps
root.order.add_edge(site,   risk)
root.order.add_edge(risk,   permit)
root.order.add_edge(permit, soil)
root.order.add_edge(soil,   water)
root.order.add_edge(water,  bed)

# After bed build, composting and energy integration happen in parallel
root.order.add_edge(bed,     compost)
root.order.add_edge(bed,     energy)
# Both finish before seed selection
root.order.add_edge(compost, seed)
root.order.add_edge(energy,  seed)

# Continue linear setup
root.order.add_edge(seed,      irrig)
root.order.add_edge(irrig,     nutrient)
root.order.add_edge(nutrient,  pest)
root.order.add_edge(pest,      community)
root.order.add_edge(community, sensor)

# After deploying sensors, enter the monitoring/rotation loop
root.order.add_edge(sensor, monitoring_loop)