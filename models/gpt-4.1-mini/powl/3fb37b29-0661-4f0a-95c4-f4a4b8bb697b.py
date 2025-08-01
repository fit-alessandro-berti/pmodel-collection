# Generated from: 3fb37b29-0661-4f0a-95c4-f4a4b8bb697b.json
# Description: This process outlines the establishment of a vertical farming facility within an urban environment, integrating advanced hydroponics, climate control, and automated harvesting technologies. It involves site selection based on urban density and sunlight patterns, structural modifications to optimize vertical space, installation of nutrient delivery systems, calibration of LED grow lights tailored to plant species, implementation of IoT sensors for continuous monitoring, recruitment and training of specialized agronomists, and development of a supply chain for rapid distribution. The process also includes compliance with urban agricultural regulations and community engagement to promote sustainable practices. Continuous data analysis and system optimization ensure high yield and energy efficiency, making this atypical business operation a model for future urban agriculture initiatives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Light_Mapping = Transition(label='Light Mapping')
Structure_Design = Transition(label='Structure Design')
Permits_Acquire = Transition(label='Permits Acquire')
System_Install = Transition(label='System Install')
Nutrient_Setup = Transition(label='Nutrient Setup')
Light_Calibrate = Transition(label='Light Calibrate')
Sensor_Deploy = Transition(label='Sensor Deploy')
Staff_Hire = Transition(label='Staff Hire')
Training_Plan = Transition(label='Training Plan')
Crop_Select = Transition(label='Crop Select')
Planting_Stage = Transition(label='Planting Stage')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Automate = Transition(label='Harvest Automate')
Quality_Check = Transition(label='Quality Check')
Market_Launch = Transition(label='Market Launch')
Data_Review = Transition(label='Data Review')
Energy_Audit = Transition(label='Energy Audit')

# 1) Site selection occurs first, consisting of Site Survey --> Light Mapping
site_selection = StrictPartialOrder(nodes=[Site_Survey, Light_Mapping])
site_selection.order.add_edge(Site_Survey, Light_Mapping)

# 2) Structural modifications follow site selection: Structure Design after Light Mapping
structural_mod = StrictPartialOrder(nodes=[Structure_Design])
# We connect site_selection --> structural_mod after root is built

# 3) Permits are acquired in parallel with structural modifications (they must both be done before installation)
Permits = StrictPartialOrder(nodes=[Permits_Acquire])

# 4) System install requires System Install, Nutrient Setup, Light Calibrate, Sensor Deploy
system_preparation = StrictPartialOrder(nodes=[System_Install, Nutrient_Setup, Light_Calibrate, Sensor_Deploy])
# no order among these (concurrent)

# 5) Staff Hire and Training Plan in sequence
staff_training = StrictPartialOrder(nodes=[Staff_Hire, Training_Plan])
staff_training.order.add_edge(Staff_Hire, Training_Plan)

# 6) Crop Select --> Planting Stage sequential
planting = StrictPartialOrder(nodes=[Crop_Select, Planting_Stage])
planting.order.add_edge(Crop_Select, Planting_Stage)

# 7) Growth Monitor --> Harvest Automate --> Quality Check sequential
growth_harvest = StrictPartialOrder(nodes=[Growth_Monitor, Harvest_Automate, Quality_Check])
growth_harvest.order.add_edge(Growth_Monitor, Harvest_Automate)
growth_harvest.order.add_edge(Harvest_Automate, Quality_Check)

# 8) Market Launch and Compliance + Community Engagement (not explicitly listed, assume Permits = compliance & engagement)
# Market Launch after Quality Check
market_launch = StrictPartialOrder(nodes=[Market_Launch])

# 9) Continuous data analysis and system optimization: Data Review and Energy Audit, running cyclically as a loop after Market Launch
data_review = Transition(label='Data Review')
energy_audit = Transition(label='Energy Audit')
data_optimization = StrictPartialOrder(nodes=[data_review, energy_audit])
data_optimization.order.add_edge(data_review, energy_audit)

# Define the loop: * (data_optimization, Market_Launch)
# This models continuous data review and audit cycle followed by Market Launch, then repeat or exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_optimization, Market_Launch])

# Build installation phase partial order: system_preparation nodes, staff_training, planting, growth_harvest, Market Launch (loop after)
# Installation phase includes: system_preparation + staff_training + planting + growth_harvest + loop
installation_nodes = [system_preparation, staff_training, planting, growth_harvest, loop]

installation = StrictPartialOrder(nodes=installation_nodes)

# Orders within installation:
# system_preparation before staff_training
installation.order.add_edge(system_preparation, staff_training)
# staff_training before planting
installation.order.add_edge(staff_training, planting)
# planting before growth_harvest
installation.order.add_edge(planting, growth_harvest)
# growth_harvest before loop (market launch in loop)
installation.order.add_edge(growth_harvest, loop)

# Finally, top-level root composition:
# site_selection --> both structural_mod and permits (both parallel)
# structural_mod and permits --> installation (join before start)

root = StrictPartialOrder(
    nodes=[site_selection, structural_mod, Permits, installation]
)

# Add order edges top-level:
root.order.add_edge(site_selection, structural_mod)
root.order.add_edge(site_selection, Permits)
root.order.add_edge(structural_mod, installation)
root.order.add_edge(Permits, installation)