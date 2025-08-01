# Generated from: 11b7fa99-927b-4be9-86d8-d19e9eff3743.json
# Description: This process outlines the complex and atypical steps involved in establishing a fully operational urban vertical farm within a metropolitan environment. It includes site selection based on sunlight and logistics, modular structure assembly, installation of hydroponic and aeroponic systems, integration of IoT sensors for environmental monitoring, automated nutrient delivery calibration, pest management using biocontrol agents, staff training in controlled environment agriculture, regulatory compliance checks, and market launch preparations. The process ensures sustainability, scalability, and maximized crop yield in limited urban spaces, leveraging innovative agricultural technology and smart data analytics to optimize plant growth cycles and reduce resource consumption in a highly controlled indoor ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Sunlight_Map = Transition(label='Sunlight Map')
Structure_Build = Transition(label='Structure Build')
System_Install = Transition(label='System Install')
Sensor_Setup = Transition(label='Sensor Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Pest_Control = Transition(label='Pest Control')
Data_Sync = Transition(label='Data Sync')
Staff_Train = Transition(label='Staff Train')
Regulation_Audit = Transition(label='Regulation Audit')
Crop_Plan = Transition(label='Crop Plan')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Prep = Transition(label='Harvest Prep')
Market_Launch = Transition(label='Market Launch')
Waste_Cycle = Transition(label='Waste Cycle')

# Create partial orders to reflect typical dependencies and concurrency described:

# Site survey and sunlight map are parallel activities for site selection
site_select = StrictPartialOrder(nodes=[Site_Survey, Sunlight_Map])
# No order edge between them to model concurrency

# After site selection, build structure
structure_phase = StrictPartialOrder(nodes=[site_select, Structure_Build])
structure_phase.order.add_edge(site_select, Structure_Build)

# After structure build install systems and sensor setup in parallel
install_and_sensor = StrictPartialOrder(nodes=[System_Install, Sensor_Setup])
# No edge between to model parallelism

# After system install and sensor setup, calibrate nutrient mix and pest control in parallel
nutrient_and_pest = StrictPartialOrder(nodes=[Nutrient_Mix, Pest_Control])
# No edge between

# Data sync and staff train in parallel for controls and operations
sync_and_train = StrictPartialOrder(nodes=[Data_Sync, Staff_Train])
# no edge between

# Compliance audit before crop plan
compliance = StrictPartialOrder(nodes=[Regulation_Audit, Crop_Plan])
compliance.order.add_edge(Regulation_Audit, Crop_Plan)

# Growth monitor and waste cycle run concurrently, monitor feeds into harvest prep
harvest_phase = StrictPartialOrder(nodes=[Growth_Monitor, Waste_Cycle, Harvest_Prep])
harvest_phase.order.add_edge(Growth_Monitor, Harvest_Prep)

# Market launch last step after harvest prep
market_phase = StrictPartialOrder(nodes=[harvest_phase, Market_Launch])
market_phase.order.add_edge(harvest_phase, Market_Launch)

# Assemble the main overall order:
# site_select --> structure_phase --> (install_and_sensor)
# (install_and_sensor) --> (nutrient_and_pest)
# (nutrient_and_pest) --> (sync_and_train)
# (sync_and_train) --> compliance --> crop_plan --> market_phase

# Link site_select and structure_build already inside structure_phase
# So start from structure_phase node
# We'll use all the phases in a top-level PO with these edges

root = StrictPartialOrder(nodes=[
    structure_phase,
    install_and_sensor,
    nutrient_and_pest,
    sync_and_train,
    compliance,
    crop_plan := Crop_Plan,  # already included in compliance PO but want distinct ref
    market_phase
])
# Need to access Crop_Plan inside compliance to link precisely
# Instead recreate compliance nodes list to separate Crop_Plan:

# Redefine compliance as PO with Regulation_Audit only, crop_plan separately
compliance = StrictPartialOrder(nodes=[Regulation_Audit])
crop_plan = Crop_Plan

root = StrictPartialOrder(nodes=[
    structure_phase,
    install_and_sensor,
    nutrient_and_pest,
    sync_and_train,
    compliance,
    crop_plan,
    market_phase
])

root.order.add_edge(structure_phase, install_and_sensor)
root.order.add_edge(install_and_sensor, nutrient_and_pest)
root.order.add_edge(nutrient_and_pest, sync_and_train)
root.order.add_edge(sync_and_train, compliance)
root.order.add_edge(compliance, crop_plan)
root.order.add_edge(crop_plan, market_phase)