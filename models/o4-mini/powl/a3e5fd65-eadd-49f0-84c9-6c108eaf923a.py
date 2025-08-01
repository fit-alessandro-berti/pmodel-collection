# Generated from: a3e5fd65-eadd-49f0-84c9-6c108eaf923a.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming operation within a repurposed industrial building. It integrates architectural redesign, hydroponic system installation, environmental monitoring calibration, crop selection based on microclimate data, and iterative growth optimization cycles. The procedure also includes stakeholder engagement for community integration, waste recycling strategies, and digital platform synchronization for real-time yield tracking, ensuring a sustainable, technology-driven urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as POWL transitions
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
design_layout = Transition(label='Design Layout')
lighting_setup = Transition(label='Lighting Setup')
hydroponic_install = Transition(label='Hydroponic Install')
climate_config = Transition(label='Climate Config')
water_testing = Transition(label='Water Testing')
crop_selection = Transition(label='Crop Selection')
nutrient_prep = Transition(label='Nutrient Prep')
sensor_calibrate = Transition(label='Sensor Calibrate')
waste_plan = Transition(label='Waste Plan')
community_meet = Transition(label='Community Meet')
staff_training = Transition(label='Staff Training')
trial_growth = Transition(label='Trial Growth')
data_sync = Transition(label='Data Sync')
yield_review = Transition(label='Yield Review')
system_upgrade = Transition(label='System Upgrade')

# Inner loop: Data Sync -> Yield Review -> System Upgrade
inner_po = StrictPartialOrder(nodes=[data_sync, yield_review, system_upgrade])
inner_po.order.add_edge(data_sync, yield_review)
inner_po.order.add_edge(yield_review, system_upgrade)

# Loop operator: Trial Growth, then optionally (Data Sync -> Yield Review -> System Upgrade) and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[trial_growth, inner_po])

# Root partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_audit, design_layout,
    lighting_setup, hydroponic_install, climate_config,
    water_testing, sensor_calibrate, crop_selection,
    nutrient_prep, waste_plan, community_meet,
    staff_training, loop
])

# Define the control-flow / data dependencies
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, design_layout)
root.order.add_edge(design_layout, lighting_setup)
root.order.add_edge(design_layout, hydroponic_install)
root.order.add_edge(lighting_setup, climate_config)
root.order.add_edge(hydroponic_install, climate_config)
root.order.add_edge(climate_config, water_testing)
root.order.add_edge(climate_config, sensor_calibrate)
root.order.add_edge(water_testing, crop_selection)
root.order.add_edge(sensor_calibrate, crop_selection)
root.order.add_edge(crop_selection, nutrient_prep)
root.order.add_edge(nutrient_prep, waste_plan)
root.order.add_edge(nutrient_prep, community_meet)
root.order.add_edge(sensor_calibrate, staff_training)
# Gate the iterative growth loop on completion of key setup activities
root.order.add_edge(nutrient_prep, loop)
root.order.add_edge(sensor_calibrate, loop)
root.order.add_edge(staff_training, loop)
root.order.add_edge(waste_plan, loop)
root.order.add_edge(community_meet, loop)