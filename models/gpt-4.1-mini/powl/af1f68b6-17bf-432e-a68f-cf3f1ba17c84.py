# Generated from: af1f68b6-17bf-432e-a68f-cf3f1ba17c84.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farming operation within a repurposed industrial building. It involves site analysis, structural retrofitting, environmental system integration, crop selection, automation setup, nutrient cycling design, community engagement, and regulatory compliance. The process must balance sustainable resource use, technological innovation, and local food production goals while addressing unique challenges such as lighting optimization, water recycling, pest management without chemicals, and efficient harvest logistics. The integration of IoT sensors to monitor microclimates and plant health is critical, alongside employee training and continuous process refinement based on data analytics to maximize yield and minimize environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Retrofit_Plan = Transition(label='Retrofit Plan')

Lighting_Setup = Transition(label='Lighting Setup')
Irrigation_Install = Transition(label='Irrigation Install')
Sensor_Deploy = Transition(label='Sensor Deploy')

Crop_Select = Transition(label='Crop Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Control = Transition(label='Pest Control')

Automation_Config = Transition(label='Automation Config')
Data_Monitor = Transition(label='Data Monitor')
Employee_Train = Transition(label='Employee Train')

Community_Meet = Transition(label='Community Meet')
Compliance_Audit = Transition(label='Compliance Audit')

Harvest_Plan = Transition(label='Harvest Plan')
Waste_Recycle = Transition(label='Waste Recycle')
Energy_Audit = Transition(label='Energy Audit')

# Partial order for initial site analysis and retrofitting plan (sequential)
site_prep = StrictPartialOrder(nodes=[Site_Survey, Structural_Check, Retrofit_Plan])
site_prep.order.add_edge(Site_Survey, Structural_Check)
site_prep.order.add_edge(Structural_Check, Retrofit_Plan)

# Environmental systems integration (Lighting, Irrigation, Sensors) concurrent
env_setup = StrictPartialOrder(nodes=[Lighting_Setup, Irrigation_Install, Sensor_Deploy])

# Crop and nutrient management choice to allow pest control loop if needed
# Loop: execute Pest_Control, then choose exit or reapply pest control (simplified as loop of Crop_Select (A) and Pest_Control (B))
crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Select, Pest_Control])  # execute Crop_Select then optional Pest_Control repeat

# Nutrient_Mix happens concurrently with crop loop
crop_nutrition = StrictPartialOrder(nodes=[crop_loop, Nutrient_Mix])

# Automation configuration and data monitoring with employee training concurrent
automation_training = StrictPartialOrder(nodes=[Automation_Config, Data_Monitor, Employee_Train])

# Community engagement and compliance audit concurrent
community_compliance = StrictPartialOrder(nodes=[Community_Meet, Compliance_Audit])

# Harvest planning and waste recycling concurrent with energy audit
harvest_waste_energy = StrictPartialOrder(nodes=[Harvest_Plan, Waste_Recycle, Energy_Audit])

# Build top-level model combining all parts with dependencies showing typical process flow:

# 1) site prep must finish before environment setup and crop/nutrition setup
# 2) environment setup must finish before automation/training and community/compliance
# 3) crop/nutrition must finish before automation/training and community/compliance
# 4) automation/training and community/compliance must both finish before harvest/waste/energy

root = StrictPartialOrder(nodes=[site_prep, env_setup, crop_nutrition, automation_training, community_compliance, harvest_waste_energy])

# site_prep -> env_setup, crop_nutrition
root.order.add_edge(site_prep, env_setup)
root.order.add_edge(site_prep, crop_nutrition)

# env_setup -> automation_training, community_compliance
root.order.add_edge(env_setup, automation_training)
root.order.add_edge(env_setup, community_compliance)

# crop_nutrition -> automation_training, community_compliance
root.order.add_edge(crop_nutrition, automation_training)
root.order.add_edge(crop_nutrition, community_compliance)

# automation_training, community_compliance -> harvest_waste_energy
root.order.add_edge(automation_training, harvest_waste_energy)
root.order.add_edge(community_compliance, harvest_waste_energy)