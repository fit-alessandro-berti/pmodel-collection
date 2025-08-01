# Generated from: 30434e6b-4042-4a29-a743-09a0cb86b4d7.json
# Description: This process involves establishing a fully functional urban vertical farming system within a repurposed industrial space. It includes site analysis, modular structure assembly, environmental system installation, crop selection based on local climate data, automated irrigation setup, nutrient solution calibration, integrated pest management, real-time monitoring system deployment, staff training, trial cultivation, data analytics for yield optimization, marketing strategy development, supply chain coordination, and continuous maintenance scheduling to ensure sustainable urban agriculture with minimal environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Structure_Build = Transition(label='Structure Build')
Enviro_Setup = Transition(label='Enviro Setup')
Crop_Select = Transition(label='Crop Select')
Irrigation_Config = Transition(label='Irrigation Config')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Control = Transition(label='Pest Control')
Sensor_Install = Transition(label='Sensor Install')
System_Testing = Transition(label='System Testing')
Staff_Training = Transition(label='Staff Training')
Trial_Grow = Transition(label='Trial Grow')
Data_Review = Transition(label='Data Review')
Market_Plan = Transition(label='Market Plan')
Supply_Sync = Transition(label='Supply Sync')
Maintenance_Plan = Transition(label='Maintenance Plan')

# Define the partial order according to the description:
# Sequential steps: 
# Site Survey -> Design Layout -> Structure Build -> Enviro Setup
# Enviro Setup branches into Crop Select and Irrigation Config and Pest Control (independent)
# Crop Select -> Irrigation Config -> Nutrient Mix
# Pest Control runs in parallel with Nutrient Mix
# After Nutrient Mix and Pest Control, Sensor Install -> System Testing
# Then Staff Training -> Trial Grow -> Data Review
# Finally Market Plan -> Supply Sync -> Maintenance Plan

# We note that Crop Select depends on local climate data and should come before Irrigation Config and Nutrient Mix,
# Pest Control is a separate activity done in parallel but before sensor install/testing
# Staff Training before Trial Grow
# Trial Grow before Data Review
# Then final marketing, supply, maintenance

nodes = [
    Site_Survey, Design_Layout, Structure_Build, Enviro_Setup,
    Crop_Select, Irrigation_Config, Nutrient_Mix, Pest_Control,
    Sensor_Install, System_Testing,
    Staff_Training, Trial_Grow, Data_Review,
    Market_Plan, Supply_Sync, Maintenance_Plan
]

root = StrictPartialOrder(nodes=nodes)
o = root.order
# Sequential ordering
o.add_edge(Site_Survey, Design_Layout)
o.add_edge(Design_Layout, Structure_Build)
o.add_edge(Structure_Build, Enviro_Setup)

# Enviro Setup to three parallel branches - Crop Select, Irrigation Config, Pest Control
o.add_edge(Enviro_Setup, Crop_Select)

# Crop_Select -> Irrigation_Config -> Nutrient_Mix chain
o.add_edge(Crop_Select, Irrigation_Config)
o.add_edge(Irrigation_Config, Nutrient_Mix)

# Pest Control parallel branch after Enviro Setup
o.add_edge(Enviro_Setup, Pest_Control)

# Nutrient Mix and Pest Control both precede Sensor Install and System Testing
o.add_edge(Nutrient_Mix, Sensor_Install)
o.add_edge(Pest_Control, Sensor_Install)

o.add_edge(Sensor_Install, System_Testing)

# Staff Training after System Testing
o.add_edge(System_Testing, Staff_Training)
o.add_edge(Staff_Training, Trial_Grow)
o.add_edge(Trial_Grow, Data_Review)

# Final chain: Market Plan -> Supply Sync -> Maintenance Plan
o.add_edge(Data_Review, Market_Plan)
o.add_edge(Market_Plan, Supply_Sync)
o.add_edge(Supply_Sync, Maintenance_Plan)