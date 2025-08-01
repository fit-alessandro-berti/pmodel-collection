# Generated from: 43f10dd2-2c9e-49e6-9654-27f0937ba20f.json
# Description: This process outlines the complex integration of urban vertical farming systems within existing city infrastructure to optimize food production and sustainability. It involves selecting suitable building sites, retrofitting structures, installing hydroponic and aeroponic systems, integrating IoT sensors for climate control, managing energy consumption, coordinating with local supply chains, and ensuring regulatory compliance. The process also includes workforce training on new agricultural technologies, ongoing maintenance, real-time data analysis for crop optimization, and community engagement to promote urban agriculture awareness. This atypical business process bridges agriculture, technology, and urban planning to create a scalable model for sustainable city farming.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_select       = Transition(label='Site Select')
structure_assess  = Transition(label='Structure Assess')
retrofit_plan     = Transition(label='Retrofit Plan')
system_install    = Transition(label='System Install')
hydroponic_setup  = Transition(label='Hydroponic Setup')
aeroponic_setup   = Transition(label='Aeroponic Setup')
sensor_deploy     = Transition(label='Sensor Deploy')
climate_adjust    = Transition(label='Climate Adjust')
energy_manage     = Transition(label='Energy Manage')
supply_coord      = Transition(label='Supply Coordinate')
compliance_check  = Transition(label='Compliance Check')
staff_train       = Transition(label='Staff Train')
maintenance_run   = Transition(label='Maintenance Run')
data_analyze      = Transition(label='Data Analyze')
crop_optimize     = Transition(label='Crop Optimize')
community_engage  = Transition(label='Community Engage')

# Loop body: analyze then optimize, repeating maintenance
loop_body = StrictPartialOrder(nodes=[data_analyze, crop_optimize])
loop_body.order.add_edge(data_analyze, crop_optimize)
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintenance_run, loop_body]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_select,
    structure_assess,
    retrofit_plan,
    system_install,
    hydroponic_setup,
    aeroponic_setup,
    sensor_deploy,
    climate_adjust,
    energy_manage,
    supply_coord,
    compliance_check,
    staff_train,
    maintenance_loop,
    community_engage
])

# Define ordering (dependencies)
root.order.add_edge(site_select,      structure_assess)
root.order.add_edge(structure_assess, retrofit_plan)
root.order.add_edge(retrofit_plan,    system_install)
root.order.add_edge(system_install,   hydroponic_setup)
root.order.add_edge(system_install,   aeroponic_setup)
root.order.add_edge(hydroponic_setup, sensor_deploy)
root.order.add_edge(aeroponic_setup,  sensor_deploy)
root.order.add_edge(sensor_deploy,    climate_adjust)
root.order.add_edge(sensor_deploy,    energy_manage)
root.order.add_edge(climate_adjust,   supply_coord)
root.order.add_edge(energy_manage,    supply_coord)
root.order.add_edge(supply_coord,     compliance_check)
root.order.add_edge(compliance_check, staff_train)
root.order.add_edge(staff_train,      maintenance_loop)
# Community engagement can proceed after installation
root.order.add_edge(system_install,   community_engage)