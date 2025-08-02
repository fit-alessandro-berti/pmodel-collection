# Generated from: a3e5fd65-eadd-49f0-84c9-6c108eaf923a.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming operation within a repurposed industrial building. It integrates architectural redesign, hydroponic system installation, environmental monitoring calibration, crop selection based on microclimate data, and iterative growth optimization cycles. The procedure also includes stakeholder engagement for community integration, waste recycling strategies, and digital platform synchronization for real-time yield tracking, ensuring a sustainable, technology-driven urban agriculture model.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Structural_Audit = Transition(label='Structural Audit')
Lighting_Setup = Transition(label='Lighting Setup')
Hydroponic_Install = Transition(label='Hydroponic Install')
Climate_Config = Transition(label='Climate Config')
Water_Testing = Transition(label='Water Testing')
Crop_Selection = Transition(label='Crop Selection')
Nutrient_Prep = Transition(label='Nutrient Prep')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Waste_Plan = Transition(label='Waste Plan')
Staff_Training = Transition(label='Staff Training')
Trial_Growth = Transition(label='Trial Growth')
Data_Sync = Transition(label='Data Sync')
Community_Meet = Transition(label='Community Meet')
Yield_Review = Transition(label='Yield Review')
System_Upgrade = Transition(label='System Upgrade')

# Create a loop for iterative growth optimization cycles:
# Loop body: Trial Growth (A) then Yield Review (B)
# Loop pattern in POWL: *(A,B) means do A then choose exit or do B then A again

# Let's model Trial Growth and Yield Review in a loop, with System Upgrade before Trial Growth
upgrade_and_trial = StrictPartialOrder(nodes=[System_Upgrade, Trial_Growth])
upgrade_and_trial.order.add_edge(System_Upgrade, Trial_Growth)

growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[upgrade_and_trial, Yield_Review])

# Environmental monitoring calibration includes Sensor Calibrate and Climate Config
# They can be partial orders with Sensor_Calibrate before Climate_Config
env_monitoring = StrictPartialOrder(nodes=[Sensor_Calibrate, Climate_Config])
env_monitoring.order.add_edge(Sensor_Calibrate, Climate_Config)

# Crop selection depends on Water Testing and Nutrient Prep
crop_select_prep = StrictPartialOrder(nodes=[Water_Testing, Nutrient_Prep])
# They can be done concurrently, no order between these two

# Crop Selection depends on Water Testing and Nutrient Prep
crop_selection_order = StrictPartialOrder(
    nodes=[crop_select_prep, Crop_Selection]
)
crop_selection_order.order.add_edge(crop_select_prep, Crop_Selection)

# Build a partial order for the setup phase:
# Structural_Audit precedes Design Layout
# Design Layout precedes Lighting Setup and Hydroponic Install (concurrent)
setup_phase = StrictPartialOrder(
    nodes=[Site_Survey, Structural_Audit, Design_Layout, Lighting_Setup, Hydroponic_Install]
)
setup_phase.order.add_edge(Site_Survey, Structural_Audit)
setup_phase.order.add_edge(Structural_Audit, Design_Layout)
setup_phase.order.add_edge(Design_Layout, Lighting_Setup)
setup_phase.order.add_edge(Design_Layout, Hydroponic_Install)

# Stakeholder engagement and waste recycling run concurrently with staff training and data sync
community_and_waste = StrictPartialOrder(nodes=[Community_Meet, Waste_Plan])
staff_and_data = StrictPartialOrder(nodes=[Staff_Training, Data_Sync])

# Combine community_and_waste with staff_and_data in a partial order with no edges => concurrent
stakeholders_and_operations = StrictPartialOrder(
    nodes=[community_and_waste, staff_and_data]
)
# no added edges, concurrent

# Now combine environmental monitoring, crop selection, and stakeholders/operations all in parallel
mid_phase = StrictPartialOrder(
    nodes=[env_monitoring, crop_selection_order, stakeholders_and_operations]
)

# Finally build the entire workflow partial order:
# setup_phase --> mid_phase --> growth_loop

root = StrictPartialOrder(nodes=[setup_phase, mid_phase, growth_loop])
root.order.add_edge(setup_phase, mid_phase)
root.order.add_edge(mid_phase, growth_loop)