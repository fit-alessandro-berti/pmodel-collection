# Generated from: ae04f80e-0f7a-45fc-9a41-e3a2be008733.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farming system within a repurposed warehouse. It includes site analysis, environmental control installation, seed selection, and nutrient calibration to optimize crop yields. The process further involves integrating automated harvesting robots, data-driven growth monitoring, and waste recycling protocols to ensure sustainability. Stakeholder coordination, regulatory compliance checks, and market launch strategies are also incorporated to guarantee a successful and scalable urban agriculture enterprise.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey       = Transition(label='Site Survey')
layout_design     = Transition(label='Layout Design')
environmental_setup = Transition(label='Environmental Setup')
seed_selection    = Transition(label='Seed Selection')
nutrient_mix      = Transition(label='Nutrient Mix')
lighting_install  = Transition(label='Lighting Install')
irrigation_setup  = Transition(label='Irrigation Setup')
sensor_calibration = Transition(label='Sensor Calibration')

growth_monitoring = Transition(label='Growth Monitoring')
data_analysis     = Transition(label='Data Analysis')
automated_harvest = Transition(label='Automated Harvest')
waste_recycling   = Transition(label='Waste Recycling')

stakeholder_meet  = Transition(label='Stakeholder Meet')
compliance_check  = Transition(label='Compliance Check')
market_launch     = Transition(label='Market Launch')

# Build the post‐processing partial order for the loop body:
# Data Analysis -> Automated Harvest -> Waste Recycling
post_processing = StrictPartialOrder(
    nodes=[data_analysis, automated_harvest, waste_recycling]
)
post_processing.order.add_edge(data_analysis, automated_harvest)
post_processing.order.add_edge(automated_harvest, waste_recycling)

# Define the monitoring/harvest/recycle loop:
# * (Growth Monitoring, post_processing)
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitoring, post_processing]
)

# Build the root partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        layout_design,
        environmental_setup,
        seed_selection,
        nutrient_mix,
        lighting_install,
        irrigation_setup,
        sensor_calibration,
        stakeholder_meet,
        compliance_check,
        loop,
        market_launch
    ]
)

# Linear setup sequence
root.order.add_edge(site_survey, layout_design)
root.order.add_edge(layout_design, environmental_setup)
root.order.add_edge(environmental_setup, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, lighting_install)
root.order.add_edge(lighting_install, irrigation_setup)
root.order.add_edge(irrigation_setup, sensor_calibration)

# After calibration, we can concurrently do stakeholder meetings, compliance checks, and start the loop
root.order.add_edge(sensor_calibration, stakeholder_meet)
root.order.add_edge(sensor_calibration, compliance_check)
root.order.add_edge(sensor_calibration, loop)

# All three branches must finish before the market launch
root.order.add_edge(stakeholder_meet, market_launch)
root.order.add_edge(compliance_check, market_launch)
root.order.add_edge(loop, market_launch)