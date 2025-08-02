# Generated from: ecd9b0fc-4323-418e-88e9-4aebdaa2fbb2.json
# Description: This process involves establishing a multi-layer vertical farm within an urban environment to optimize space and maximize crop yield. It begins with site evaluation and structural analysis, followed by the installation of hydroponic systems and LED grow lights. Environmental controls like humidity, temperature, and CO2 levels are calibrated precisely. Seeds are selected based on local demand and growth cycles. Automated nutrient delivery and water recycling systems are integrated to minimize waste. Continuous monitoring through IoT sensors ensures optimal plant health, while periodic pest management using biological agents preserves organic standards. Harvest scheduling and packaging are coordinated to meet rapid urban distribution channels, ensuring fresh produce delivery within hours of picking. Finally, data analytics refine future crop selections and operational efficiency, supporting sustainability and profitability goals in a constrained urban footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Create Transition nodes for all activities
site_survey = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
hydroponic_install = Transition(label='Hydroponic Install')
lighting_setup = Transition(label='Lighting Setup')
climate_control = Transition(label='Climate Control')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
water_recycling = Transition(label='Water Recycling')
sensor_deploy = Transition(label='Sensor Deploy')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
packaging_prep = Transition(label='Packaging Prep')
delivery_route = Transition(label='Delivery Route')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')

# Phase 1: Site evaluation and structural analysis (sequential)
phase1 = StrictPartialOrder(nodes=[site_survey, structure_check])
phase1.order.add_edge(site_survey, structure_check)

# Phase 2: Installation - hydroponic and lighting in parallel
installations = StrictPartialOrder(nodes=[hydroponic_install, lighting_setup])
# parallel - no edges

# Phase 3: Environmental controls (climate control)
phase3 = climate_control

# Phase 4: Seed selection
phase4 = seed_selection

# Phase 5: Nutrient and water systems integration (can be done concurrently)
nutrient_water = StrictPartialOrder(nodes=[nutrient_mix, water_recycling])
# parallel - no edges

# Phase 6: Sensor deployment and pest control are concurrent activities
monitoring_pest = StrictPartialOrder(nodes=[sensor_deploy, pest_control])
# parallel - no edges

# Phase 7: Growth monitoring
phase7 = growth_monitor

# Phase 8: Harvest planning and packaging preparation can be parallel then delivery
harvest_packaging = StrictPartialOrder(nodes=[harvest_plan, packaging_prep])
# parallel - no edges

delivery = delivery_route

# Phase 9: Data analysis and yield forecasting are sequential
data_phase = StrictPartialOrder(nodes=[data_analysis, yield_forecast])
data_phase.order.add_edge(data_analysis, yield_forecast)

# Build partial orders representing the main sequence, while embedding parallelism

# Sequential order:
# phase1 --> installations --> phase3 --> phase4 --> nutrient_water --> monitoring_pest -->
# phase7 --> harvest_packaging --> delivery --> data_phase

# To unify all these we'll create nodes list and edges

nodes = [phase1, installations, phase3, phase4, nutrient_water, monitoring_pest,
         phase7, harvest_packaging, delivery, data_phase]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(phase1, installations)
root.order.add_edge(installations, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, nutrient_water)
root.order.add_edge(nutrient_water, monitoring_pest)
root.order.add_edge(monitoring_pest, phase7)
root.order.add_edge(phase7, harvest_packaging)
root.order.add_edge(harvest_packaging, delivery)
root.order.add_edge(delivery, data_phase)