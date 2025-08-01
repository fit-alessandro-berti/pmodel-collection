# Generated from: a76c6456-d81f-48af-9145-077e5ffa2536.json
# Description: This process outlines the setup of an urban rooftop farming system integrating sustainable agriculture with smart technology on city rooftops. It begins with site assessment and structural analysis, followed by modular bed installation and soil conditioning. The process then incorporates automated irrigation setup, sensor deployment for real-time monitoring, and nutrient management calibration. Subsequent activities include crop selection based on microclimate data, pest control via integrated biological agents, and periodic growth assessment using drones. The process concludes with harvest scheduling, produce packaging optimization, and data-driven yield forecasting to maximize productivity and sustainability in limited urban spaces.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_assess     = Transition(label='Site Assess')
structure_check = Transition(label='Structure Check')
bed_install     = Transition(label='Bed Install')
soil_prep       = Transition(label='Soil Prep')
irrigation_set  = Transition(label='Irrigation Set')
sensor_deploy   = Transition(label='Sensor Deploy')
nutrient_tune   = Transition(label='Nutrient Tune')
crop_select     = Transition(label='Crop Select')
pest_control    = Transition(label='Pest Control')
growth_scan     = Transition(label='Growth Scan')
drone_survey    = Transition(label='Drone Survey')
harvest_plan    = Transition(label='Harvest Plan')
package_opt     = Transition(label='Package Opt')
yield_forecast  = Transition(label='Yield Forecast')
waste_manage    = Transition(label='Waste Manage')

# Build a linear partial order
nodes = [
    site_assess,
    structure_check,
    bed_install,
    soil_prep,
    irrigation_set,
    sensor_deploy,
    nutrient_tune,
    crop_select,
    pest_control,
    growth_scan,
    drone_survey,
    harvest_plan,
    package_opt,
    yield_forecast,
    waste_manage
]

root = StrictPartialOrder(nodes=nodes)
# Add sequential dependencies
for src, tgt in zip(nodes, nodes[1:]):
    root.order.add_edge(src, tgt)