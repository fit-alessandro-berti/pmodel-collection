# Generated from: 55f34aba-595d-4319-9d1c-d1e418ed4ed9.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming system within a repurposed industrial building. It includes site analysis for structural integrity, environmental impact review, modular hydroponic system design, nutrient solution formulation, advanced lighting configuration, climate control integration, crop selection based on local demand, IoT sensor deployment for real-time monitoring, staff training on automated systems, community engagement for urban agriculture education, regulatory compliance checks, waste recycling protocols, yield data analytics setup, and finally, continuous optimization for energy efficiency and crop productivity to ensure sustainable urban food production.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
structure_test   = Transition(label='Structure Test')
impact_review    = Transition(label='Impact Review')
system_design    = Transition(label='System Design')
nutrient_mix     = Transition(label='Nutrient Mix')
light_setup      = Transition(label='Light Setup')
climate_sync     = Transition(label='Climate Sync')
crop_select      = Transition(label='Crop Select')
sensor_deploy    = Transition(label='Sensor Deploy')
staff_train      = Transition(label='Staff Train')
community_meet   = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
waste_cycle      = Transition(label='Waste Cycle')
data_analyze     = Transition(label='Data Analyze')
optimize_run     = Transition(label='Optimize Run')

# Silent transition for loop exit
skip = SilentTransition()

# Continuous optimization loop: run Optimize Run, then choose to exit or repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[optimize_run, skip])

# Build the overall process as a partial order with a trailing loop
root = StrictPartialOrder(nodes=[
    site_survey, structure_test, impact_review, system_design, nutrient_mix,
    light_setup, climate_sync, crop_select, sensor_deploy, staff_train,
    community_meet, compliance_check, waste_cycle, data_analyze, loop
])

# Add sequential dependencies
seq = [
    (site_survey, structure_test),
    (structure_test, impact_review),
    (impact_review, system_design),
    (system_design, nutrient_mix),
    (nutrient_mix, light_setup),
    (light_setup, climate_sync),
    (climate_sync, crop_select),
    (crop_select, sensor_deploy),
    (sensor_deploy, staff_train),
    (staff_train, community_meet),
    (community_meet, compliance_check),
    (compliance_check, waste_cycle),
    (waste_cycle, data_analyze),
    (data_analyze, loop)
]
for src, tgt in seq:
    root.order.add_edge(src, tgt)