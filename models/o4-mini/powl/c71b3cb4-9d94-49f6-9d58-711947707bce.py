# Generated from: c71b3cb4-9d94-49f6-9d58-711947707bce.json
# Description: This process describes the comprehensive operational cycle of an urban vertical farm integrating hydroponic cultivation, automated nutrient delivery, and AI-driven climate control. It begins with seed selection and germination, followed by transplanting seedlings into multilayered vertical racks. Automated systems monitor and adjust water, nutrients, and light exposure based on real-time sensor data. Periodic health assessments detect pest or disease outbreaks, triggering targeted organic interventions. Harvesting is scheduled dynamically to optimize freshness and supply chain demands. Post-harvest, the system manages waste recycling and biomass conversion, feeding energy back into the farm's power grid. Data collected throughout the cycle informs predictive analytics for yield optimization and resource efficiency, ensuring sustainable urban agriculture with minimal environmental footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# define all transitions
seed_selection = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
seedling_transplant = Transition(label='Seedling Transplant')
nutrient_mix = Transition(label='Nutrient Mix')
water_delivery = Transition(label='Water Delivery')
light_adjustment = Transition(label='Light Adjustment')
climate_control = Transition(label='Climate Control')
sensor_monitoring = Transition(label='Sensor Monitoring')
health_check = Transition(label='Health Check')
pest_control = Transition(label='Pest Control')
harvest_planning = Transition(label='Harvest Planning')
crop_harvest = Transition(label='Crop Harvest')
waste_sorting = Transition(label='Waste Sorting')
biomass_process = Transition(label='Biomass Process')
energy_recycling = Transition(label='Energy Recycling')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')

# silent transition for choices
skip = SilentTransition()

# choice for pest control
pest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])

# partial order for sensor-driven adjustments: sensor first, then all four in parallel
adjustments = StrictPartialOrder(nodes=[sensor_monitoring, nutrient_mix, water_delivery, light_adjustment, climate_control])
adjustments.order.add_edge(sensor_monitoring, nutrient_mix)
adjustments.order.add_edge(sensor_monitoring, water_delivery)
adjustments.order.add_edge(sensor_monitoring, light_adjustment)
adjustments.order.add_edge(sensor_monitoring, climate_control)

# top‐level workflow
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    seedling_transplant,
    adjustments,
    health_check,
    pest_choice,
    harvest_planning,
    crop_harvest,
    waste_sorting,
    biomass_process,
    energy_recycling,
    data_analysis,
    yield_forecast
])

# sequencing edges
root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, seedling_transplant)
root.order.add_edge(seedling_transplant, adjustments)
root.order.add_edge(adjustments, health_check)
root.order.add_edge(health_check, pest_choice)
root.order.add_edge(pest_choice, harvest_planning)
root.order.add_edge(harvest_planning, crop_harvest)
root.order.add_edge(crop_harvest, waste_sorting)
root.order.add_edge(waste_sorting, biomass_process)
root.order.add_edge(biomass_process, energy_recycling)
root.order.add_edge(energy_recycling, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)