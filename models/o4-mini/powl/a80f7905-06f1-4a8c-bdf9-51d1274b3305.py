# Generated from: a80f7905-06f1-4a8c-bdf9-51d1274b3305.json
# Description: This process outlines the establishment of an urban vertical farm integrating advanced hydroponic systems and AI-driven environmental controls. It begins with site analysis and urban zoning compliance, followed by modular structure design tailored for vertical stacking. Next, nutrient solution formulation and seed selection are optimized for rapid growth. Installation of sensor networks enables real-time monitoring of humidity, light, and CO2 levels. Concurrently, pest management protocols using biological controls are implemented to reduce chemical dependency. The process includes workforce training on automated harvesting equipment and data analytics platforms. Finally, crop yield forecasting and distribution logistics are coordinated to meet urban demand efficiently while maintaining sustainability standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_analysis     = Transition(label='Site Analysis')
zoning_review     = Transition(label='Zoning Review')
design_modules    = Transition(label='Design Modules')
structure_build   = Transition(label='Structure Build')
seed_selection    = Transition(label='Seed Selection')
nutrient_blend    = Transition(label='Nutrient Blend')
sensor_install    = Transition(label='Sensor Install')
pest_control      = Transition(label='Pest Control')
enviro_setup      = Transition(label='Enviro Setup')
staff_training    = Transition(label='Staff Training')
harvest_automate  = Transition(label='Harvest Automate')
data_monitor      = Transition(label='Data Monitor')
yield_forecast    = Transition(label='Yield Forecast')
logistics_plan    = Transition(label='Logistics Plan')
sustain_audit     = Transition(label='Sustain Audit')

# Build the partial order
root = StrictPartialOrder(
    nodes=[
        site_analysis, zoning_review, design_modules, structure_build,
        seed_selection, nutrient_blend,
        sensor_install, pest_control, enviro_setup,
        staff_training, harvest_automate, data_monitor,
        yield_forecast, logistics_plan, sustain_audit
    ]
)

# Sequence of planning and design
root.order.add_edge(site_analysis,     zoning_review)
root.order.add_edge(zoning_review,     design_modules)
root.order.add_edge(design_modules,    structure_build)

# Parallel optimization of seeds and nutrients
root.order.add_edge(structure_build, seed_selection)
root.order.add_edge(structure_build, nutrient_blend)

# Sensor installation depends on both seed & nutrient prep
root.order.add_edge(seed_selection,    sensor_install)
root.order.add_edge(nutrient_blend,    sensor_install)

# Pest control runs after structure build (concurrent with seed/nutrient tasks)
root.order.add_edge(structure_build,   pest_control)

# Set up AI/environmental controls after sensors are in place
root.order.add_edge(sensor_install,    enviro_setup)

# Train staff after environment setup
root.order.add_edge(enviro_setup,      staff_training)

# Staff training leads to two concurrent tasks
root.order.add_edge(staff_training,    harvest_automate)
root.order.add_edge(staff_training,    data_monitor)

# Forecasting waits on both harvesting automation and data monitoring
root.order.add_edge(harvest_automate,  yield_forecast)
root.order.add_edge(data_monitor,      yield_forecast)

# Final coordination steps
root.order.add_edge(yield_forecast,    logistics_plan)
root.order.add_edge(logistics_plan,    sustain_audit)