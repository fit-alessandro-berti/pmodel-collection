# Generated from: 281cc54d-69b1-4b3d-a186-a4fd59d38bff.json
# Description: This process describes the end-to-end operational cycle of an urban vertical farming system that integrates automated environmental controls, crop monitoring, nutrient delivery, and waste recycling. The system starts with seed selection and ends with packaging and distribution, incorporating real-time data analysis to optimize growth conditions. The process also includes preventive maintenance of hydroponic equipment, pest detection via AI imaging, and energy consumption balancing to ensure sustainability in dense urban environments. Each step involves coordination between IoT devices, human operators, and cloud-based analytics platforms to maximize crop yield and minimize resource use, representing a cutting-edge approach to urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
seed_selection    = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
nutrient_mix      = Transition(label='Nutrient Mix')
planting_setup    = Transition(label='Planting Setup')
light_adjustment  = Transition(label='Light Adjustment')
humidity_control  = Transition(label='Humidity Control')
air_circulation   = Transition(label='Air Circulation')
growth_monitoring = Transition(label='Growth Monitoring')
pest_detection    = Transition(label='Pest Detection')
data_analysis     = Transition(label='Data Analysis')
equipment_check   = Transition(label='Equipment Check')
energy_audit      = Transition(label='Energy Audit')
water_recycling   = Transition(label='Water Recycling')
waste_processing  = Transition(label='Waste Processing')
harvest_timing    = Transition(label='Harvest Timing')
crop_packaging    = Transition(label='Crop Packaging')
distribution_prep = Transition(label='Distribution Prep')

# Build the partially ordered workflow
root = StrictPartialOrder(nodes=[
    seed_selection, germination_start, nutrient_mix, planting_setup,
    light_adjustment, humidity_control, air_circulation, growth_monitoring,
    pest_detection, data_analysis, equipment_check, energy_audit,
    water_recycling, waste_processing,
    harvest_timing, crop_packaging, distribution_prep
])

# Sequential phase: seed to setup
root.order.add_edge(seed_selection,    germination_start)
root.order.add_edge(germination_start, nutrient_mix)
root.order.add_edge(nutrient_mix,      planting_setup)

# Environmental controls converge into growth monitoring
root.order.add_edge(planting_setup,    light_adjustment)
root.order.add_edge(planting_setup,    humidity_control)
root.order.add_edge(planting_setup,    air_circulation)
root.order.add_edge(light_adjustment,  growth_monitoring)
root.order.add_edge(humidity_control,  growth_monitoring)
root.order.add_edge(air_circulation,   growth_monitoring)

# After monitoring, parallel tasks for analytics, maintenance, sustainability
root.order.add_edge(growth_monitoring, pest_detection)
root.order.add_edge(growth_monitoring, data_analysis)
root.order.add_edge(growth_monitoring, equipment_check)
root.order.add_edge(growth_monitoring, energy_audit)
root.order.add_edge(growth_monitoring, water_recycling)
root.order.add_edge(growth_monitoring, waste_processing)

# Synchronize before harvest
for prev in [
    pest_detection, data_analysis, equipment_check,
    energy_audit, water_recycling, waste_processing
]:
    root.order.add_edge(prev, harvest_timing)

# Final packaging and distribution
root.order.add_edge(harvest_timing,  crop_packaging)
root.order.add_edge(crop_packaging,  distribution_prep)