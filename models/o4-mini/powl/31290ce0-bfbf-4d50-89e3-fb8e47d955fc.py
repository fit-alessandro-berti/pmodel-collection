# Generated from: 31290ce0-bfbf-4d50-89e3-fb8e47d955fc.json
# Description: This process outlines the complex steps involved in establishing a fully operational urban vertical farm within a constrained city environment. Starting with site assessment and zoning approval, it includes innovative modular design, integrating IoT-based climate control, and hydroponic system installation. The workflow addresses energy optimization through renewable sources, advanced nutrient delivery calibration, and pest management without chemicals. The process also incorporates community engagement for educational tours, continuous data monitoring, and adaptive crop scheduling based on market trends. Final stages involve certification for organic produce and launching a subscription-based delivery service, ensuring sustainability and profitability in urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_assess = Transition(label='Site Assess')
zoning_approve = Transition(label='Zoning Approve')
modular_design = Transition(label='Modular Design')
iot_setup = Transition(label='IoT Setup')
climate_config = Transition(label='Climate Config')
hydroponic_install = Transition(label='Hydroponic Install')
energy_audit = Transition(label='Energy Audit')
renewables_integrate = Transition(label='Renewables Integrate')
nutrient_calibrate = Transition(label='Nutrient Calibrate')
pest_control = Transition(label='Pest Control')
community_engage = Transition(label='Community Engage')
data_monitor = Transition(label='Data Monitor')
crop_schedule = Transition(label='Crop Schedule')
organic_certify = Transition(label='Organic Certify')
launch_delivery = Transition(label='Launch Delivery')

# Loop for continuous monitoring and adaptive scheduling
monitor_schedule_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_monitor, crop_schedule]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    zoning_approve,
    modular_design,
    iot_setup,
    climate_config,
    hydroponic_install,
    energy_audit,
    renewables_integrate,
    nutrient_calibrate,
    pest_control,
    community_engage,
    monitor_schedule_loop,
    organic_certify,
    launch_delivery
])

# Add sequencing edges
root.order.add_edge(site_assess, zoning_approve)
root.order.add_edge(zoning_approve, modular_design)
root.order.add_edge(modular_design, iot_setup)
root.order.add_edge(iot_setup, climate_config)
root.order.add_edge(climate_config, hydroponic_install)
root.order.add_edge(hydroponic_install, energy_audit)
root.order.add_edge(energy_audit, renewables_integrate)

# After renewables integration, nutrient calibration and pest control can proceed in parallel
root.order.add_edge(renewables_integrate, nutrient_calibrate)
root.order.add_edge(renewables_integrate, pest_control)

# Both calibration and pest control must finish before community engagement
root.order.add_edge(nutrient_calibrate, community_engage)
root.order.add_edge(pest_control, community_engage)

# Community engagement feeds into the monitoring-and-scheduling loop
root.order.add_edge(community_engage, monitor_schedule_loop)

# After exiting the loop, certify organic produce and launch delivery service
root.order.add_edge(monitor_schedule_loop, organic_certify)
root.order.add_edge(organic_certify, launch_delivery)