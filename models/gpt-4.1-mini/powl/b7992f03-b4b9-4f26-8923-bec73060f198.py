# Generated from: b7992f03-b4b9-4f26-8923-bec73060f198.json
# Description: This process outlines the end-to-end setup of an urban vertical farming system within a repurposed commercial building. It begins with site assessment and structural analysis, followed by environmental control installation and nutrient cycling design. The process includes selecting appropriate crop varieties optimized for vertical growth, integrating IoT sensors for real-time monitoring, and implementing automated irrigation and lighting schedules. Staff training on system maintenance and crop management is conducted alongside regulatory compliance checks. The final stages involve pilot cultivation, yield analysis, and continuous optimization to ensure sustainable production and minimal resource consumption in a dense urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
Structure_Check = Transition(label='Structure Check')
Design_Layout = Transition(label='Design Layout')
Install_HVAC = Transition(label='Install HVAC')
Set_Lighting = Transition(label='Set Lighting')
Deploy_Sensors = Transition(label='Deploy Sensors')
Select_Crops = Transition(label='Select Crops')
Configure_Irrigation = Transition(label='Configure Irrigation')
Nutrient_Setup = Transition(label='Nutrient Setup')
Staff_Training = Transition(label='Staff Training')
Compliance_Audit = Transition(label='Compliance Audit')
Pilot_Cultivation = Transition(label='Pilot Cultivation')
Data_Monitoring = Transition(label='Data Monitoring')
Yield_Analysis = Transition(label='Yield Analysis')
Process_Review = Transition(label='Process Review')

# Group activities that are concurrent:
# Environmental control installation and nutrient cycling design:
# (Install HVAC, Set Lighting, Deploy Sensors) and Nutrient Setup can be concurrent with each other,
# but given description, nutrient setup may happen after design layout.
# We'll group Install HVAC, Set Lighting, Deploy Sensors in partial order but concurrent w.r.t each other

env_controls = StrictPartialOrder(nodes=[Install_HVAC, Set_Lighting, Deploy_Sensors])
# no order among these three = fully concurrent

# Staff Training and Compliance Audit conducted alongside each other
training_and_audit = StrictPartialOrder(nodes=[Staff_Training, Compliance_Audit])
# Concurrent, no edges

# Pilot Cultivation, Yield Analysis, Process Review form a sequential chain
final_stages = StrictPartialOrder(nodes=[Pilot_Cultivation, Yield_Analysis, Process_Review])
final_stages.order.add_edge(Pilot_Cultivation, Yield_Analysis)
final_stages.order.add_edge(Yield_Analysis, Process_Review)

# Nutrient Setup after Design Layout
nutrient_after_design = StrictPartialOrder(nodes=[Design_Layout, Nutrient_Setup])
nutrient_after_design.order.add_edge(Design_Layout, Nutrient_Setup)

# Environmental controls after Nutrient Setup
env_after_nutrient = StrictPartialOrder(nodes=[nutrient_after_design, env_controls])
env_after_nutrient.order.add_edge(nutrient_after_design, env_controls)

# Configure Irrigation and Select Crops can be concurrent but both after env controls
select_and_configure = StrictPartialOrder(nodes=[Select_Crops, Configure_Irrigation])
# concurrent, no edges between

post_env = StrictPartialOrder(nodes=[env_after_nutrient, select_and_configure])
post_env.order.add_edge(env_after_nutrient, select_and_configure)

# Data Monitoring after Pilot Cultivation (usually happens alongside, but logically after setup)
# But as description says "real-time monitoring" integrated with sensors - can assume monitoring after deploy sensors
# For modeling purposes, we put Data Monitoring after Deploy Sensors

monitoring_after_deploy = StrictPartialOrder(nodes=[Deploy_Sensors, Data_Monitoring])
monitoring_after_deploy.order.add_edge(Deploy_Sensors, Data_Monitoring)

# Replace env_controls with monitoring_after_deploy's env_controls variant
env_controls = monitoring_after_deploy
env_after_nutrient = StrictPartialOrder(nodes=[nutrient_after_design, env_controls])
env_after_nutrient.order.add_edge(nutrient_after_design, env_controls)

post_env = StrictPartialOrder(nodes=[env_after_nutrient, select_and_configure])
post_env.order.add_edge(env_after_nutrient, select_and_configure)

# Staff training and compliance audit alongside everything after irrigation and crop selection, pilot cultivation comes last
# So training_and_audit can start after select_and_configure (or concurrent with Pilot Cultivation)
# We'll place training_and_audit concurrent with pilot cultivation using a partial order

post_select = StrictPartialOrder(nodes=[select_and_configure, training_and_audit])
# training_and_audit and select_and_configure concurrent - no edge

# Pilot Cultivation after select_and_configure (and staff training & audit can overlap)
pilot_after_select = StrictPartialOrder(nodes=[post_select, Pilot_Cultivation])
pilot_after_select.order.add_edge(post_select, Pilot_Cultivation)

# Final stages after pilot cultivation
final_chain = StrictPartialOrder(nodes=[pilot_after_select, Yield_Analysis, Process_Review])
final_chain.order.add_edge(pilot_after_select, Yield_Analysis)
final_chain.order.add_edge(Yield_Analysis, Process_Review)

# Initial phase: Site Survey --> Structure Check --> Design Layout
initial_phase = StrictPartialOrder(nodes=[Site_Survey, Structure_Check, Design_Layout])
initial_phase.order.add_edge(Site_Survey, Structure_Check)
initial_phase.order.add_edge(Structure_Check, Design_Layout)

# Now combine initial phase and the rest:
root = StrictPartialOrder(nodes=[initial_phase, nutrient_after_design, env_after_nutrient, post_env,
                                post_select, training_and_audit, pilot_after_select, final_stages])

# But this duplicates nodes, better to connect initial_phase to nutrient_after_design to ensure proper order

# Construct stepwise:

# initial_phase already contains Design_Layout at end
# Nutrient_After_Design is on top of initial_phase, but the nodes overlap (Design_Layout appears twice)
# To avoid duplication, better to define clear nodes and partial orders without repeated nodes

# Instead of complicated nested, we can do a flat partial order reflecting the sequence and concurrency exactly as described:

root = StrictPartialOrder(nodes=[
    Site_Survey,
    Structure_Check,
    Design_Layout,
    Nutrient_Setup,
    Install_HVAC,
    Set_Lighting,
    Deploy_Sensors,
    Select_Crops,
    Configure_Irrigation,
    Staff_Training,
    Compliance_Audit,
    Pilot_Cultivation,
    Data_Monitoring,
    Yield_Analysis,
    Process_Review
])

# Add order edges:

# Linear initial phase
root.order.add_edge(Site_Survey, Structure_Check)
root.order.add_edge(Structure_Check, Design_Layout)

# Nutrient Setup after Design Layout
root.order.add_edge(Design_Layout, Nutrient_Setup)

# Environmental controls after Nutrient Setup
root.order.add_edge(Nutrient_Setup, Install_HVAC)
root.order.add_edge(Nutrient_Setup, Set_Lighting)
root.order.add_edge(Nutrient_Setup, Deploy_Sensors)

# Data Monitoring after Deploy Sensors
root.order.add_edge(Deploy_Sensors, Data_Monitoring)

# Select Crops and Configure Irrigation after Env controls (after Install HVAC, Set Lighting, Deploy Sensors)
root.order.add_edge(Install_HVAC, Select_Crops)
root.order.add_edge(Set_Lighting, Select_Crops)
root.order.add_edge(Deploy_Sensors, Select_Crops)

root.order.add_edge(Install_HVAC, Configure_Irrigation)
root.order.add_edge(Set_Lighting, Configure_Irrigation)
root.order.add_edge(Deploy_Sensors, Configure_Irrigation)

# Staff Training and Compliance Audit after Select Crops and Configure Irrigation
root.order.add_edge(Select_Crops, Staff_Training)
root.order.add_edge(Configure_Irrigation, Staff_Training)
root.order.add_edge(Select_Crops, Compliance_Audit)
root.order.add_edge(Configure_Irrigation, Compliance_Audit)

# Pilot Cultivation after Staff Training and Compliance Audit
root.order.add_edge(Staff_Training, Pilot_Cultivation)
root.order.add_edge(Compliance_Audit, Pilot_Cultivation)

# Yield Analysis after Pilot Cultivation and Data Monitoring
root.order.add_edge(Pilot_Cultivation, Yield_Analysis)
root.order.add_edge(Data_Monitoring, Yield_Analysis)

# Process Review after Yield Analysis
root.order.add_edge(Yield_Analysis, Process_Review)