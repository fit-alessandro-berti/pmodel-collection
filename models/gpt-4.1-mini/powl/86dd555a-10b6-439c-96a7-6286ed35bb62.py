# Generated from: 86dd555a-10b6-439c-96a7-6286ed35bb62.json
# Description: This process outlines the detailed steps involved in establishing an urban rooftop farming system on commercial buildings. It includes initial site analysis, structural assessment, nutrient and soil testing, selection of suitable crops, installation of hydroponic or soil-based systems, integration of IoT sensors for monitoring, water recycling setup, pest control strategy design, community engagement for workforce and education, and final yield forecasting. Each activity ensures sustainability, regulatory compliance, and maximization of limited rooftop space for efficient food production within city environments, promoting local sourcing and reducing carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
Site_Survey = Transition(label='Site Survey')
Structure_Check = Transition(label='Structure Check')
Soil_Testing = Transition(label='Soil Testing')
Crop_Select = Transition(label='Crop Select')
System_Design = Transition(label='System Design')
Sensor_Setup = Transition(label='Sensor Setup')
Water_Setup = Transition(label='Water Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Plan = Transition(label='Pest Plan')
Energy_Audit = Transition(label='Energy Audit')
Community_Meet = Transition(label='Community Meet')
Permit_Obtain = Transition(label='Permit Obtain')
Install_Beds = Transition(label='Install Beds')
Plant_Seeds = Transition(label='Plant Seeds')
Monitor_Growth = Transition(label='Monitor Growth')
Data_Analyze = Transition(label='Data Analyze')
Harvest_Plan = Transition(label='Harvest Plan')
Waste_Manage = Transition(label='Waste Manage')

# Construct partial order representing the process flow
nodes = [Site_Survey, Structure_Check, Soil_Testing, Crop_Select,
         System_Design, Sensor_Setup, Water_Setup, Nutrient_Mix,
         Pest_Plan, Energy_Audit, Community_Meet, Permit_Obtain,
         Install_Beds, Plant_Seeds, Monitor_Growth, Data_Analyze,
         Harvest_Plan, Waste_Manage]

root = StrictPartialOrder(nodes=nodes)

# Add ordering edges according to described workflow

# Initial assessments: Site Survey → Structure Check → Soil Testing
root.order.add_edge(Site_Survey, Structure_Check)
root.order.add_edge(Structure_Check, Soil_Testing)

# Crop selection after soil testing
root.order.add_edge(Soil_Testing, Crop_Select)

# System Design after crop selection
root.order.add_edge(Crop_Select, System_Design)

# Parallel setup activities after system design:
# Sensor Setup, Water Setup, Nutrient Mix, Pest Plan, Energy Audit
# They can be performed concurrently after system design
root.order.add_edge(System_Design, Sensor_Setup)
root.order.add_edge(System_Design, Water_Setup)
root.order.add_edge(System_Design, Nutrient_Mix)
root.order.add_edge(System_Design, Pest_Plan)
root.order.add_edge(System_Design, Energy_Audit)

# Community Meet and Permit Obtain may be concurrent, but both depend on assessments
# We connect them after energy audit and pest plan (final preparation steps)
root.order.add_edge(Pest_Plan, Community_Meet)
root.order.add_edge(Energy_Audit, Community_Meet)
root.order.add_edge(Pest_Plan, Permit_Obtain)
root.order.add_edge(Energy_Audit, Permit_Obtain)

# Install Beds after permit obtained
root.order.add_edge(Permit_Obtain, Install_Beds)

# Plant Seeds after Install Beds
root.order.add_edge(Install_Beds, Plant_Seeds)

# Monitor Growth after Plant Seeds
root.order.add_edge(Plant_Seeds, Monitor_Growth)

# Data Analyze after Monitor Growth
root.order.add_edge(Monitor_Growth, Data_Analyze)

# Harvest Plan after Data Analyze
root.order.add_edge(Data_Analyze, Harvest_Plan)

# Waste Manage after Harvest Plan
root.order.add_edge(Harvest_Plan, Waste_Manage)