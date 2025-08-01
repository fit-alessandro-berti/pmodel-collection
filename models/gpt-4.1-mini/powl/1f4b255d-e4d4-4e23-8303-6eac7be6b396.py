# Generated from: 1f4b255d-e4d4-4e23-8303-6eac7be6b396.json
# Description: This process outlines the establishment of a vertical farming system within an urban environment, integrating advanced hydroponic techniques, automated climate control, and sustainable energy sources. It involves site analysis, modular structure assembly, nutrient solution preparation, sensor calibration, crop selection, growth monitoring, pest management using bio-controls, and yield optimization. The process ensures minimal water usage and maximizes space efficiency while adhering to local regulations and community engagement for urban agriculture promotion. Continuous data analysis and iterative improvements maintain crop health and operational sustainability.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Permit_Check = Transition(label='Permit Check')
Design_Layout = Transition(label='Design Layout')
Structure_Build = Transition(label='Structure Build')
Install_Lighting = Transition(label='Install Lighting')
Setup_Hydroponics = Transition(label='Setup Hydroponics')
Prepare_Nutrients = Transition(label='Prepare Nutrients')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Select_Crops = Transition(label='Select Crops')
Plant_Seeding = Transition(label='Plant Seeding')
Climate_Adjust = Transition(label='Climate Adjust')
Monitor_Growth = Transition(label='Monitor Growth')
Pest_Control = Transition(label='Pest Control')
Data_Logging = Transition(label='Data Logging')
Harvest_Cycle = Transition(label='Harvest Cycle')
Waste_Manage = Transition(label='Waste Manage')
Community_Outreach = Transition(label='Community Outreach')

# Create partial orders for some sequential chains

# Initial site preparation and design
prep_design = StrictPartialOrder(nodes=[
    Site_Survey, Permit_Check, Design_Layout, Structure_Build, Install_Lighting
])
prep_design.order.add_edge(Site_Survey, Permit_Check)
prep_design.order.add_edge(Permit_Check, Design_Layout)
prep_design.order.add_edge(Design_Layout, Structure_Build)
prep_design.order.add_edge(Structure_Build, Install_Lighting)

# Setup hydroponics and nutrient preparation can be concurrent
setup_nutrients = StrictPartialOrder(nodes=[Setup_Hydroponics, Prepare_Nutrients, Calibrate_Sensors])
# Setup_Hydroponics --> Prepare_Nutrients and Calibrate_Sensors (these two concurrent)
setup_nutrients.order.add_edge(Setup_Hydroponics, Prepare_Nutrients)
setup_nutrients.order.add_edge(Setup_Hydroponics, Calibrate_Sensors)

# Crop selection and planting
crop_plant = StrictPartialOrder(nodes=[Select_Crops, Plant_Seeding])
crop_plant.order.add_edge(Select_Crops, Plant_Seeding)

# Monitoring and controls loop:
# LOOP node: do Monitor Growth then either exit or do Pest Control + Climate Adjust then loop again
monitor = Monitor_Growth
pest_climate = StrictPartialOrder(nodes=[Pest_Control, Climate_Adjust])
pest_climate.order.add_edge(Pest_Control, Climate_Adjust)

monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor, pest_climate])

# Data logging and harvesting (can be concurrent with waste management)
harvest_and_waste = StrictPartialOrder(nodes=[Harvest_Cycle, Waste_Manage])
# No direct order among Harvest_Cycle and Waste_Manage (concurrent)

# Community outreach can run parallel to harvest and waste management
final_phase = StrictPartialOrder(nodes=[harvest_and_waste, Community_Outreach])

# Data logging runs parallel to harvest_and_waste and community outreach
final_with_logging = StrictPartialOrder(nodes=[Data_Logging, final_phase])

# Now sequentially compose the entire process:

# Step 1: prep_design
# Step 2: setup_nutrients (can only start after Install_Lighting)
# Step 3: crop_plant (after setup and nutrients)
# Step 4: monitor_loop
# Step 5: final_with_logging

root = StrictPartialOrder(nodes=[prep_design, setup_nutrients, crop_plant, monitor_loop, final_with_logging])

# Add edges to enforce sequential order among these main phases:
root.order.add_edge(prep_design, setup_nutrients)
root.order.add_edge(setup_nutrients, crop_plant)
root.order.add_edge(crop_plant, monitor_loop)
root.order.add_edge(monitor_loop, final_with_logging)