# Generated from: 8e8e1d61-a1c8-40ec-ad4e-4ea961281a86.json
# Description: This process outlines the steps required to establish an urban rooftop farming operation on a commercial building. It involves assessing structural integrity, selecting suitable crops for rooftop conditions, designing irrigation and nutrient delivery systems, obtaining necessary permits, installing solar-powered sensors for environmental monitoring, and launching a community engagement program to promote local produce. The process also incorporates waste recycling protocols, pest management without chemicals, and continuous yield optimization through data analysis, ensuring sustainability and profitability in an unconventional agriculture setting within a dense urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
load_testing     = Transition(label='Load Testing')
crop_selection   = Transition(label='Crop Selection')
design_layout    = Transition(label='Design Layout')
permit_filing    = Transition(label='Permit Filing')
solar_paneling   = Transition(label='Solar Paneling')
sensor_setup     = Transition(label='Sensor Setup')
irrigation_install = Transition(label='Irrigation Install')
nutrient_mix     = Transition(label='Nutrient Mix')
waste_sorting    = Transition(label='Waste Sorting')
pest_control     = Transition(label='Pest Control')
data_collection  = Transition(label='Data Collection')
community_meet   = Transition(label='Community Meet')
yield_review     = Transition(label='Yield Review')
report_draft     = Transition(label='Report Draft')

# Loop for continuous yield optimization: collect data, review yield, repeat or exit
loop_optimization = OperatorPOWL(operator=Operator.LOOP, 
                                 children=[data_collection, yield_review])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    site_survey, load_testing, crop_selection, design_layout,
    permit_filing, solar_paneling, sensor_setup,
    irrigation_install, nutrient_mix,
    waste_sorting, pest_control,
    community_meet, loop_optimization,
    report_draft
])

# Structural integrity assessment
root.order.add_edge(site_survey, load_testing)

# Crop selection & layout design
root.order.add_edge(load_testing, crop_selection)
root.order.add_edge(crop_selection, design_layout)

# Permit filing after load test
root.order.add_edge(load_testing, permit_filing)

# After design: irrigation and nutrient systems in parallel
root.order.add_edge(design_layout, irrigation_install)
root.order.add_edge(design_layout, nutrient_mix)

# Setup of solar‐powered sensors after permit
root.order.add_edge(permit_filing, solar_paneling)
root.order.add_edge(solar_paneling, sensor_setup)

# Waste recycling, pest control, community engagement start after permit
root.order.add_edge(permit_filing, waste_sorting)
root.order.add_edge(permit_filing, pest_control)
root.order.add_edge(permit_filing, community_meet)

# Start continuous yield‐optimization loop after permits
root.order.add_edge(permit_filing, loop_optimization)

# All branches synchronize into the final report
for predecessor in [
    sensor_setup, irrigation_install, nutrient_mix,
    waste_sorting, pest_control, community_meet,
    loop_optimization
]:
    root.order.add_edge(predecessor, report_draft)