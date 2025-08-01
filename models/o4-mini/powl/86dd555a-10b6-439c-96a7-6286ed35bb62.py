# Generated from: 86dd555a-10b6-439c-96a7-6286ed35bb62.json
# Description: This process outlines the detailed steps involved in establishing an urban rooftop farming system on commercial buildings. It includes initial site analysis, structural assessment, nutrient and soil testing, selection of suitable crops, installation of hydroponic or soil-based systems, integration of IoT sensors for monitoring, water recycling setup, pest control strategy design, community engagement for workforce and education, and final yield forecasting. Each activity ensures sustainability, regulatory compliance, and maximization of limited rooftop space for efficient food production within city environments, promoting local sourcing and reducing carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_survey     = Transition(label='Site Survey')
structure_check = Transition(label='Structure Check')
soil_testing    = Transition(label='Soil Testing')
crop_select     = Transition(label='Crop Select')
system_design   = Transition(label='System Design')
sensor_setup    = Transition(label='Sensor Setup')
water_setup     = Transition(label='Water Setup')
nutrient_mix    = Transition(label='Nutrient Mix')
pest_plan       = Transition(label='Pest Plan')
energy_audit    = Transition(label='Energy Audit')
community_meet  = Transition(label='Community Meet')
permit_obtain   = Transition(label='Permit Obtain')
install_beds    = Transition(label='Install Beds')
plant_seeds     = Transition(label='Plant Seeds')
monitor_growth  = Transition(label='Monitor Growth')
data_analyze    = Transition(label='Data Analyze')
harvest_plan    = Transition(label='Harvest Plan')
waste_manage    = Transition(label='Waste Manage')

# Loop for ongoing monitoring and data analysis
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_growth, data_analyze]
)

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey, structure_check, soil_testing, crop_select,
    system_design, sensor_setup, water_setup, nutrient_mix,
    pest_plan, energy_audit, community_meet, permit_obtain,
    install_beds, plant_seeds, monitor_loop, harvest_plan, waste_manage
])

# Define the control‐flow via partial‐order edges
root.order.add_edge(site_survey,     structure_check)
root.order.add_edge(site_survey,     soil_testing)
root.order.add_edge(site_survey,     energy_audit)

root.order.add_edge(structure_check, permit_obtain)
root.order.add_edge(energy_audit,    permit_obtain)

root.order.add_edge(permit_obtain,   community_meet)
root.order.add_edge(permit_obtain,   system_design)

root.order.add_edge(soil_testing,    nutrient_mix)
root.order.add_edge(nutrient_mix,    crop_select)

root.order.add_edge(crop_select,     system_design)
root.order.add_edge(community_meet,  system_design)

root.order.add_edge(system_design,   sensor_setup)
root.order.add_edge(system_design,   water_setup)
root.order.add_edge(system_design,   pest_plan)

root.order.add_edge(sensor_setup,    install_beds)
root.order.add_edge(water_setup,     install_beds)
root.order.add_edge(pest_plan,       install_beds)
root.order.add_edge(community_meet,  install_beds)

root.order.add_edge(install_beds,    plant_seeds)
root.order.add_edge(plant_seeds,     monitor_loop)
root.order.add_edge(monitor_loop,    harvest_plan)
root.order.add_edge(harvest_plan,    waste_manage)