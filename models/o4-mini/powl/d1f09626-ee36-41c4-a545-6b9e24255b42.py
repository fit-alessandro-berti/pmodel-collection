# Generated from: d1f09626-ee36-41c4-a545-6b9e24255b42.json
# Description: This process outlines the comprehensive steps involved in establishing a sustainable urban rooftop farm. It includes site assessment, structural analysis, soil testing, and microclimate evaluation to ensure optimal plant growth conditions. The process also covers selecting appropriate crop varieties, designing irrigation systems, installing renewable energy sources, and integrating pest management strategies. Community engagement and regulatory compliance are addressed to foster local support and legal operation. Finally, ongoing maintenance protocols and yield monitoring are implemented to maximize productivity and sustainability over time.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
site_survey       = Transition(label='Site Survey')
load_test         = Transition(label='Load Test')
soil_sample       = Transition(label='Soil Sample')
climate_check     = Transition(label='Climate Check')
crop_select       = Transition(label='Crop Select')
irrigation_plan   = Transition(label='Irrigation Plan')
energy_setup      = Transition(label='Energy Setup')
pest_control      = Transition(label='Pest Control')
stakeholder_meet  = Transition(label='Stakeholder Meet')
permit_obtain     = Transition(label='Permit Obtain')
bed_construction  = Transition(label='Bed Construction')
seed_planting     = Transition(label='Seed Planting')
water_schedule    = Transition(label='Water Schedule')
growth_monitor    = Transition(label='Growth Monitor')
yield_report      = Transition(label='Yield Report')
waste_recycle     = Transition(label='Waste Recycle')
harvest_plan      = Transition(label='Harvest Plan')

# Define the cycle body: Growth Monitor -> Yield Report -> Waste Recycle
cycle_body = StrictPartialOrder(nodes=[growth_monitor, yield_report, waste_recycle])
cycle_body.order.add_edge(growth_monitor, yield_report)
cycle_body.order.add_edge(yield_report, waste_recycle)

# Define the loop: repeat Water Schedule then (optionally) the cycle body
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[water_schedule, cycle_body]
)

# Assemble the top‐level process in partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_test, soil_sample, climate_check,
    crop_select, irrigation_plan, energy_setup, pest_control,
    stakeholder_meet, permit_obtain, bed_construction, seed_planting,
    loop, harvest_plan
])

# Add the sequential dependencies
root.order.add_edge(site_survey,      load_test)
root.order.add_edge(load_test,        soil_sample)
root.order.add_edge(soil_sample,      climate_check)
root.order.add_edge(climate_check,    crop_select)
root.order.add_edge(crop_select,      irrigation_plan)
root.order.add_edge(irrigation_plan,  energy_setup)
root.order.add_edge(energy_setup,     pest_control)
root.order.add_edge(pest_control,     stakeholder_meet)
root.order.add_edge(stakeholder_meet, permit_obtain)
root.order.add_edge(permit_obtain,    bed_construction)
root.order.add_edge(bed_construction, seed_planting)
root.order.add_edge(seed_planting,    loop)
root.order.add_edge(loop,             harvest_plan)