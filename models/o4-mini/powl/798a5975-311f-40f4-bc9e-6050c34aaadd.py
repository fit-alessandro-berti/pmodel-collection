# Generated from: 798a5975-311f-40f4-bc9e-6050c34aaadd.json
# Description: This process outlines the complex sequence of activities required to establish an urban vertical farming facility within a repurposed industrial building. It involves site analysis, environmental control design, hydroponic system installation, crop selection tailored for limited space and light, integration of IoT sensors for monitoring, and the development of a sustainable waste recycling loop. The process also includes securing permits, engaging local stakeholders, and implementing automated harvesting and packaging systems to optimize yield and reduce labor costs. Continuous data analysis and system calibration ensure adaptability to urban microclimates and consumer demand fluctuations, making this an atypical but highly sustainable agricultural business model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
permit_filing     = Transition(label='Permit Filing')
stakeholder_meet  = Transition(label='Stakeholder Meet')
layout_design     = Transition(label='Layout Design')
enviro_setup      = Transition(label='Enviro Setup')
hydroponic_install= Transition(label='Hydroponic Install')
sensor_deploy     = Transition(label='Sensor Deploy')
crop_select       = Transition(label='Crop Select')
automation_setup  = Transition(label='Automation Setup')
harvest_plan      = Transition(label='Harvest Plan')
packaging_line    = Transition(label='Packaging Line')
waste_activity    = Transition(label='Waste Loop')
irrigation_tune   = Transition(label='Irrigation Tune')
climate_control   = Transition(label='Climate Control')
data_review       = Transition(label='Data Review')
market_align      = Transition(label='Market Align')
skip              = SilentTransition()

# Define the waste recycling loop: repeat 'Waste Loop' until exit
waste_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[waste_activity, skip]
)

# Define the calibration submodel (concurrent tuning tasks)
calibration = StrictPartialOrder(
    nodes=[irrigation_tune, climate_control]
)

# Define the continuous data analysis & calibration loop
data_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_review, calibration]
)

# Assemble the overall workflow as a partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_filing,
    stakeholder_meet,
    layout_design,
    enviro_setup,
    hydroponic_install,
    sensor_deploy,
    crop_select,
    automation_setup,
    harvest_plan,
    packaging_line,
    waste_loop,
    data_loop,
    market_align
])

# Add control-flow dependencies
root.order.add_edge(site_survey,       permit_filing)
root.order.add_edge(site_survey,       stakeholder_meet)
root.order.add_edge(permit_filing,     layout_design)
root.order.add_edge(stakeholder_meet,  layout_design)
root.order.add_edge(layout_design,     enviro_setup)
root.order.add_edge(layout_design,     hydroponic_install)
root.order.add_edge(enviro_setup,      sensor_deploy)
root.order.add_edge(hydroponic_install,sensor_deploy)
root.order.add_edge(sensor_deploy,     crop_select)
root.order.add_edge(crop_select,       automation_setup)
root.order.add_edge(automation_setup,  harvest_plan)
root.order.add_edge(harvest_plan,      packaging_line)
root.order.add_edge(packaging_line,    waste_loop)
root.order.add_edge(waste_loop,        data_loop)
root.order.add_edge(data_loop,         market_align)