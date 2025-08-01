# Generated from: 3bc50827-0c76-4f4a-8720-7bdcdaa67a6c.json
# Description: This process involves the comprehensive management of urban beekeeping operations in a metropolitan environment, balancing ecological sustainability with city regulations. Activities include hive setup in constrained spaces, regular health assessments of bee colonies, monitoring urban flora for pollen diversity, and coordinating with local authorities on compliance. It also covers harvesting honey with minimal disruption to the ecosystem, processing and packaging products in small urban facilities, and community engagement through educational workshops. The process integrates data collection on bee behavior using IoT sensors, pest control with organic methods, and adaptive strategies to mitigate pollution impacts, ensuring a resilient urban apiary system that supports biodiversity while producing high-quality honey and bee products.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
hive_setup        = Transition(label='Hive Setup')
sensor_install    = Transition(label='Sensor Install')
regulation_review = Transition(label='Regulation Review')
colony_check      = Transition(label='Colony Check')
health_monitor    = Transition(label='Health Monitor')
pest_control      = Transition(label='Pest Control')
pollution_test    = Transition(label='Pollution Test')
data_logging      = Transition(label='Data Logging')
pollen_survey     = Transition(label='Pollen Survey')
flora_mapping     = Transition(label='Flora Mapping')
weather_watch     = Transition(label='Weather Watch')
harvest_honey     = Transition(label='Harvest Honey')
product_process   = Transition(label='Product Process')
package_goods     = Transition(label='Package Goods')
supply_order      = Transition(label='Supply Order')
waste_manage      = Transition(label='Waste Manage')
community_talk    = Transition(label='Community Talk')

# Loop for periodic colony assessment and data logging
monitor_body = StrictPartialOrder(nodes=[health_monitor,
                                         pest_control,
                                         pollution_test,
                                         data_logging])
loop_monitor = OperatorPOWL(operator=Operator.LOOP,
                            children=[colony_check, monitor_body])

# Concurrent surveying of urban flora and weather after monitoring
post_monitor_surveys = StrictPartialOrder(nodes=[pollen_survey,
                                                 flora_mapping,
                                                 weather_watch])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    hive_setup,
    sensor_install,
    regulation_review,
    loop_monitor,
    post_monitor_surveys,
    harvest_honey,
    product_process,
    package_goods,
    supply_order,
    waste_manage,
    community_talk
])

# Define the control‐flow (partial order) relations
root.order.add_edge(hive_setup,        sensor_install)
root.order.add_edge(sensor_install,    regulation_review)
root.order.add_edge(regulation_review, loop_monitor)
root.order.add_edge(loop_monitor,      post_monitor_surveys)
root.order.add_edge(post_monitor_surveys, harvest_honey)
root.order.add_edge(harvest_honey,       product_process)
root.order.add_edge(product_process,     package_goods)
root.order.add_edge(package_goods,       supply_order)
root.order.add_edge(package_goods,       waste_manage)
root.order.add_edge(supply_order,        community_talk)
root.order.add_edge(waste_manage,        community_talk)