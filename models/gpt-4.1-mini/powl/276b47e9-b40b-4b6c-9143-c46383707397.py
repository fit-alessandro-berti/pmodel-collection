# Generated from: 276b47e9-b40b-4b6c-9143-c46383707397.json
# Description: This process outlines the complex setup of an urban vertical farm integrating hydroponics and renewable energy systems. It involves site analysis, modular design adaptation, climate control calibration, nutrient formula optimization, automated irrigation programming, sensor deployment, energy storage integration, waste recycling implementation, community engagement, and continuous system monitoring to ensure sustainable crop yields in constrained city environments. The process requires coordination between agronomists, engineers, sustainability experts, and local authorities to balance productivity with environmental impact while leveraging IoT technologies for data-driven decisions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
module_fabricate = Transition(label='Module Fabricate')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
irrigation_code = Transition(label='Irrigation Code')
sensor_install = Transition(label='Sensor Install')
energy_grid = Transition(label='Energy Grid')
waste_process = Transition(label='Waste Process')
data_sync = Transition(label='Data Sync')
yield_forecast = Transition(label='Yield Forecast')
staff_train = Transition(label='Staff Train')
community_meet = Transition(label='Community Meet')
system_test = Transition(label='System Test')
monitor_adjust = Transition(label='Monitor Adjust')

# Partial Order representing the process logic:

# Step 1: Site Survey leads to Design Layout
# Step 2: Design Layout leads to Module Fabricate and Climate Setup (which can be concurrent)
# Step 3: Climate Setup leads to Nutrient Mix
# Step 4: Nutrient Mix leads to Irrigation Code (concurrent with Sensor Install)
# Step 5: Module Fabricate leads to Sensor Install
# Steps 4 and 5's resulting activities (Irrigation Code and Sensor Install) happen concurrently and both must complete before Energy Grid
# Step 6: Energy Grid leads to Waste Process and Data Sync concurrently
# Step 7: Waste Process leads to Community Meet
# Step 8: Data Sync leads to Yield Forecast and Staff Train concurrently
# Step 9: Yield Forecast, Staff Train, and Community Meet must all complete before System Test
# Step 10: System Test leads to a loop where Monitor Adjust may repeat system_test monitoring until exit.

# For the loop: * (System Test, Monitor Adjust)
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[system_test, monitor_adjust])

# Build overall partial order with all nodes involved:
nodes = [site_survey, design_layout, module_fabricate, climate_setup, nutrient_mix, irrigation_code,
         sensor_install, energy_grid, waste_process, data_sync, yield_forecast, staff_train,
         community_meet, loop_monitor]

root = StrictPartialOrder(nodes=nodes)

# Define order edges:

# 1. Site Survey -> Design Layout
root.order.add_edge(site_survey, design_layout)

# 2. Design Layout -> Module Fabricate and Design Layout -> Climate Setup
root.order.add_edge(design_layout, module_fabricate)
root.order.add_edge(design_layout, climate_setup)

# 3. Climate Setup -> Nutrient Mix
root.order.add_edge(climate_setup, nutrient_mix)

# 4a. Nutrient Mix -> Irrigation Code
root.order.add_edge(nutrient_mix, irrigation_code)

# 4b. Module Fabricate -> Sensor Install
root.order.add_edge(module_fabricate, sensor_install)

# 5. Irrigation Code and Sensor Install must complete before Energy Grid
root.order.add_edge(irrigation_code, energy_grid)
root.order.add_edge(sensor_install, energy_grid)

# 6. Energy Grid -> Waste Process and Energy Grid -> Data Sync
root.order.add_edge(energy_grid, waste_process)
root.order.add_edge(energy_grid, data_sync)

# 7. Waste Process -> Community Meet
root.order.add_edge(waste_process, community_meet)

# 8. Data Sync -> Yield Forecast and Data Sync -> Staff Train
root.order.add_edge(data_sync, yield_forecast)
root.order.add_edge(data_sync, staff_train)

# 9. Yield Forecast, Staff Train, Community Meet -> System Test (loop root)
root.order.add_edge(yield_forecast, loop_monitor)
root.order.add_edge(staff_train, loop_monitor)
root.order.add_edge(community_meet, loop_monitor)

# No edges inside the loop needed here since loop_monitor defines structure internally

# root variable contains the complete POWL model