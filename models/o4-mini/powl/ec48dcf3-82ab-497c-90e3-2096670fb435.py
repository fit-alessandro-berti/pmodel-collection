# Generated from: ec48dcf3-82ab-497c-90e3-2096670fb435.json
# Description: This process details the complex setup of an urban vertical farm, integrating sustainable agriculture within limited city spaces. It involves site analysis, modular structure assembly, hydroponic system installation, climate control calibration, nutrient solution formulation, seed selection and germination, automated monitoring integration, pest management planning, workforce training, yield forecasting, and community engagement initiatives, all designed to optimize crop production while minimizing environmental impact and ensuring scalability in dense urban environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey     = Transition(label='Site Survey')
design_layout   = Transition(label='Design Layout')
structure_build = Transition(label='Structure Build')
system_install  = Transition(label='System Install')
climate_setup   = Transition(label='Climate Setup')
nutrient_prep   = Transition(label='Nutrient Prep')
seed_germinate  = Transition(label='Seed Germinate')
planting_phase  = Transition(label='Planting Phase')
sensor_deploy   = Transition(label='Sensor Deploy')
pest_control    = Transition(label='Pest Control')
water_monitor   = Transition(label='Water Monitor')
data_analyze    = Transition(label='Data Analyze')
staff_train     = Transition(label='Staff Train')
yield_forecast  = Transition(label='Yield Forecast')
community_meet  = Transition(label='Community Meet')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    structure_build,
    system_install,
    climate_setup,
    nutrient_prep,
    seed_germinate,
    planting_phase,
    sensor_deploy,
    pest_control,
    water_monitor,
    data_analyze,
    staff_train,
    yield_forecast,
    community_meet
])

# Define the control‐flow (precedence) relations
root.order.add_edge(site_survey,   design_layout)
root.order.add_edge(design_layout, structure_build)
root.order.add_edge(structure_build, system_install)
root.order.add_edge(system_install, climate_setup)

# After climate setup two streams run in parallel:
#  1) Prepare nutrients → germinate seeds → planting
#  2) Train staff
root.order.add_edge(climate_setup, nutrient_prep)
root.order.add_edge(nutrient_prep, seed_germinate)
root.order.add_edge(seed_germinate, planting_phase)

root.order.add_edge(climate_setup, staff_train)

# After planting, deploy sensors, plan pest control, and set up water monitoring (all concurrent)
root.order.add_edge(planting_phase, sensor_deploy)
root.order.add_edge(planting_phase, pest_control)
root.order.add_edge(planting_phase, water_monitor)

# Monitoring data analysis depends on sensor & water streams
root.order.add_edge(sensor_deploy, data_analyze)
root.order.add_edge(water_monitor, data_analyze)

# Final forecasting and community engagement
root.order.add_edge(data_analyze,   yield_forecast)
root.order.add_edge(yield_forecast, community_meet)