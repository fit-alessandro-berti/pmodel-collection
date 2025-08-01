# Generated from: f0469137-9d56-4175-81bc-231607cd73fd.json
# Description: This process outlines the comprehensive management of an urban vertical farm focusing on optimizing crop yield and sustainability in limited space environments. It begins with site analysis and climate adaptation, followed by nutrient mixing and seed germination in controlled chambers. Automated planting ensures precise spacing, while multi-level irrigation systems deliver water and nutrients. Continuous monitoring through IoT sensors tracks growth parameters and pest presence, triggering targeted drone interventions for pollination or pesticide application. Harvesting involves robotic arms that selectively pick ripe produce, followed by quality inspection and packaging within sterile conditions. The cycle concludes with waste recycling and energy optimization to maintain eco-friendly operations, ensuring a closed-loop agricultural system tailored for urban settings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_analysis     = Transition(label='Site Analysis')
climate_setup     = Transition(label='Climate Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
seed_germinate    = Transition(label='Seed Germinate')
auto_planting     = Transition(label='Auto Planting')
irrigation_setup  = Transition(label='Irrigation Setup')
iot_monitoring    = Transition(label='IoT Monitoring')
pest_detection    = Transition(label='Pest Detection')
drone_pollinate   = Transition(label='Drone Pollinate')
pesticide_spray   = Transition(label='Pesticide Spray')
robotic_harvest   = Transition(label='Robotic Harvest')
quality_check     = Transition(label='Quality Check')
package_product   = Transition(label='Package Product')
waste_recycle     = Transition(label='Waste Recycle')
energy_optimize   = Transition(label='Energy Optimize')
data_logging      = Transition(label='Data Logging')

# Choice between pollination and pesticide application
intervention_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[drone_pollinate, pesticide_spray]
)

# The main cycle of operations (excluding the logging step)
main_cycle = StrictPartialOrder(nodes=[
    site_analysis,
    climate_setup,
    nutrient_mix,
    seed_germinate,
    auto_planting,
    irrigation_setup,
    iot_monitoring,
    pest_detection,
    intervention_choice,
    robotic_harvest,
    quality_check,
    package_product,
    waste_recycle,
    energy_optimize
])
# Define the partial order (sequential flow)
main_cycle.order.add_edge(site_analysis,  climate_setup)
main_cycle.order.add_edge(climate_setup,  nutrient_mix)
main_cycle.order.add_edge(nutrient_mix,   seed_germinate)
main_cycle.order.add_edge(seed_germinate, auto_planting)
main_cycle.order.add_edge(auto_planting,  irrigation_setup)
main_cycle.order.add_edge(irrigation_setup, iot_monitoring)
main_cycle.order.add_edge(iot_monitoring, pest_detection)
main_cycle.order.add_edge(pest_detection, intervention_choice)
main_cycle.order.add_edge(intervention_choice, robotic_harvest)
main_cycle.order.add_edge(robotic_harvest,    quality_check)
main_cycle.order.add_edge(quality_check,      package_product)
main_cycle.order.add_edge(package_product,    waste_recycle)
main_cycle.order.add_edge(waste_recycle,      energy_optimize)

# Wrap the entire process in a loop to model the closed-loop nature
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_cycle, data_logging]
)