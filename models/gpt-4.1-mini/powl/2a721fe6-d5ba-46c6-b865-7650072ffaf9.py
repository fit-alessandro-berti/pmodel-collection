# Generated from: 2a721fe6-d5ba-46c6-b865-7650072ffaf9.json
# Description: This process outlines the establishment of an urban vertical farming system designed to optimize limited city space for sustainable agriculture. It involves selecting appropriate building infrastructure, integrating advanced hydroponic and aeroponic systems, implementing automated climate control and nutrient delivery, and establishing real-time monitoring via IoT sensors. The process further includes regulatory compliance checks, community engagement for local sourcing, workforce training on specialized equipment, and continuous yield optimization through data analytics. The complexity arises from merging construction, agriculture technology, environmental control, and urban planning within a compact footprint, ensuring efficient resource use and maximizing crop output year-round.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Structure_Design = Transition(label='Structure Design')
System_Integration = Transition(label='System Integration')
Sensor_Install = Transition(label='Sensor Install')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Water_Cycle = Transition(label='Water Cycle')
Lighting_Config = Transition(label='Lighting Config')
Automation_Test = Transition(label='Automation Test')
Regulation_Check = Transition(label='Regulation Check')
Staff_Training = Transition(label='Staff Training')
Crop_Seeding = Transition(label='Crop Seeding')
Growth_Monitoring = Transition(label='Growth Monitoring')
Data_Analysis = Transition(label='Data Analysis')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Manage = Transition(label='Waste Manage')
Community_Meet = Transition(label='Community Meet')

# Set up partial order reflecting the process description

# Construction activities sequence
construction = StrictPartialOrder(nodes=[Site_Survey, Structure_Design, System_Integration])
construction.order.add_edge(Site_Survey, Structure_Design)
construction.order.add_edge(Structure_Design, System_Integration)

# Environmental control partial order
env_control_nodes = [
    Sensor_Install,
    Climate_Setup,
    Nutrient_Mix,
    Water_Cycle,
    Lighting_Config,
    Automation_Test
]
env_control = StrictPartialOrder(nodes=env_control_nodes)
# Setup a chain order roughly indicating typical setup sequence
env_control.order.add_edge(Sensor_Install, Climate_Setup)
env_control.order.add_edge(Sensor_Install, Nutrient_Mix)
env_control.order.add_edge(Sensor_Install, Water_Cycle)
env_control.order.add_edge(Sensor_Install, Lighting_Config)
env_control.order.add_edge(Climate_Setup, Automation_Test)
env_control.order.add_edge(Nutrient_Mix, Automation_Test)
env_control.order.add_edge(Water_Cycle, Automation_Test)
env_control.order.add_edge(Lighting_Config, Automation_Test)

# Compliance and community branch
compliance = StrictPartialOrder(nodes=[Regulation_Check, Community_Meet])
# No direct order, concurrent activities potentially, leave order empty

# Workforce and training
training = StrictPartialOrder(nodes=[Staff_Training])
# Single node, no order needed

# Agriculture and ongoing activities (seeding to harvest)
agri_nodes = [Crop_Seeding, Growth_Monitoring, Data_Analysis, Harvest_Plan, Waste_Manage]
agri = StrictPartialOrder(nodes=agri_nodes)
agri.order.add_edge(Crop_Seeding, Growth_Monitoring)
agri.order.add_edge(Growth_Monitoring, Data_Analysis)
agri.order.add_edge(Data_Analysis, Harvest_Plan)
agri.order.add_edge(Harvest_Plan, Waste_Manage)

# Compose the entire process partial order
# We can order construction before env_control and compliance so those start after structure is integrated
# Training and agri can start after compliance and env_control are done

root = StrictPartialOrder(nodes=[construction, env_control, compliance, training, agri])

# Construction precedes env_control and compliance
root.order.add_edge(construction, env_control)
root.order.add_edge(construction, compliance)

# env_control and compliance precede training and agriculture
root.order.add_edge(env_control, training)
root.order.add_edge(compliance, training)
root.order.add_edge(env_control, agri)
root.order.add_edge(compliance, agri)

# Training precedes agriculture (assumed workforce must be trained before/agri)
root.order.add_edge(training, agri)