# Generated from: 77fc7bc0-3b16-4ca9-ab27-6e54a76bf7b1.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within constrained city environments. It includes site evaluation, modular system design, environmental control calibration, nutrient flow optimization, and continuous monitoring. The process integrates sustainable energy sourcing, waste recycling, and crop rotation scheduling to maximize yield while minimizing resource consumption. Stakeholder coordination, regulatory compliance, and technology integration are critical to ensure operational efficiency and scalability in dense urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
System_Fabricate = Transition(label='System Fabricate')
Energy_Setup = Transition(label='Energy Setup')
Install_Sensors = Transition(label='Install Sensors')
Calibrate_Controls = Transition(label='Calibrate Controls')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seed_Planting = Transition(label='Seed Planting')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Inspect = Transition(label='Pest Inspect')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Recycle = Transition(label='Waste Recycle')
Data_Analyze = Transition(label='Data Analyze')
Compliance_Check = Transition(label='Compliance Check')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Crop_Rotate = Transition(label='Crop Rotate')
Tech_Update = Transition(label='Tech Update')

# Define partial orders representing major sub-processes

# 1) Site Evaluation: Site Survey --> Design Layout --> System Fabricate
site_evaluation = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, System_Fabricate])
site_evaluation.order.add_edge(Site_Survey, Design_Layout)
site_evaluation.order.add_edge(Design_Layout, System_Fabricate)

# 2) Environmental Control Calibration:
# Energy Setup --> Install Sensors --> Calibrate Controls
env_control = StrictPartialOrder(nodes=[Energy_Setup, Install_Sensors, Calibrate_Controls])
env_control.order.add_edge(Energy_Setup, Install_Sensors)
env_control.order.add_edge(Install_Sensors, Calibrate_Controls)

# 3) Nutrient and Plant Setup:
# Nutrient Mix --> Seed Planting
nutrient_setup = StrictPartialOrder(nodes=[Nutrient_Mix, Seed_Planting])
nutrient_setup.order.add_edge(Nutrient_Mix, Seed_Planting)

# 4) Growth Cycle:
# Growth Monitor and Pest Inspect are concurrent, then Harvest Plan
growth_monitoring = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Inspect, Harvest_Plan])
growth_monitoring.order.add_edge(Growth_Monitor, Harvest_Plan)
growth_monitoring.order.add_edge(Pest_Inspect, Harvest_Plan)

# 5) Waste and Data Management:
# Waste Recycle --> Data Analyze
waste_data = StrictPartialOrder(nodes=[Waste_Recycle, Data_Analyze])
waste_data.order.add_edge(Waste_Recycle, Data_Analyze)

# 6) Compliance and Stakeholder Coordination:
# Compliance Check and Stakeholder Meet are concurrent
compliance_stakeholder = StrictPartialOrder(nodes=[Compliance_Check, Stakeholder_Meet])

# 7) Crop Rotation and Technology Update loop:
# Loop: Crop Rotate then Tech Update then back to Crop Rotate or exit
crop_tech_loop = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Rotate, Tech_Update])

# Now, compose all sub-processes into main PO with partial ordering to reflect dependencies:
root = StrictPartialOrder(
    nodes=[
        site_evaluation,
        env_control,
        nutrient_setup,
        growth_monitoring,
        waste_data,
        compliance_stakeholder,
        crop_tech_loop
    ]
)

# Define inter-subprocess ordering
# Site Evaluation precedes Environmental Control and Nutrient Setup
root.order.add_edge(site_evaluation, env_control)
root.order.add_edge(site_evaluation, nutrient_setup)

# Environmental Control and Nutrient Setup precede Growth Monitoring
root.order.add_edge(env_control, growth_monitoring)
root.order.add_edge(nutrient_setup, growth_monitoring)

# Growth Monitoring precedes Waste and Data Management
root.order.add_edge(growth_monitoring, waste_data)

# Waste and Data Management precedes Compliance and Stakeholder Coordination
root.order.add_edge(waste_data, compliance_stakeholder)

# Compliance and Stakeholder Coordination precedes Crop Rotation and Tech Update loop
root.order.add_edge(compliance_stakeholder, crop_tech_loop)