# Generated from: 189d8a94-b564-424a-a2d1-9f869c3d5584.json
# Description: This process involves establishing a fully operational vertical farm within an urban environment, integrating advanced hydroponic systems, AI-driven climate control, and renewable energy sources. It begins with site selection and proceeds through modular infrastructure assembly, nutrient solution formulation, seedling cultivation, continuous environmental monitoring, and automated harvesting. The process also includes waste recycling, data analytics for yield optimization, and final product packaging for local distribution. Unique challenges involve balancing technological integration with urban regulations, minimizing water usage, and ensuring crop diversity while maintaining sustainability goals throughout the farm lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Selection = Transition(label='Site Selection')
Design_Layout = Transition(label='Design Layout')
Permit_Approval = Transition(label='Permit Approval')
Infrastructure_Build = Transition(label='Infrastructure Build')
System_Install = Transition(label='System Install')
Nutrient_Mix = Transition(label='Nutrient Mix')
Seedling_Plant = Transition(label='Seedling Plant')
Climate_Setup = Transition(label='Climate Setup')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Water_Cycle = Transition(label='Water Cycle')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Harvest_Crop = Transition(label='Harvest Crop')
Waste_Process = Transition(label='Waste Process')
Data_Analyze = Transition(label='Data Analyze')
Package_Goods = Transition(label='Package Goods')
Local_Deliver = Transition(label='Local Deliver')

# Partial order for site selection and design before permit approval
pre_permit = StrictPartialOrder(nodes=[Site_Selection, Design_Layout, Permit_Approval])
pre_permit.order.add_edge(Site_Selection, Permit_Approval)
pre_permit.order.add_edge(Design_Layout, Permit_Approval)

# After permit, infrastructure build and system install partially ordered (can be concurrent)
infra_system = StrictPartialOrder(nodes=[Infrastructure_Build, System_Install])
# no order edge between them, so concurrent

# Nutrient mix must precede seedling plant
nutrient_seedling = StrictPartialOrder(nodes=[Nutrient_Mix, Seedling_Plant])
nutrient_seedling.order.add_edge(Nutrient_Mix, Seedling_Plant)

# Climate setup and sensor calibrate can be done concurrently but both precede water cycle
env_setup = StrictPartialOrder(nodes=[Climate_Setup, Sensor_Calibrate, Water_Cycle])
env_setup.order.add_edge(Climate_Setup, Water_Cycle)
env_setup.order.add_edge(Sensor_Calibrate, Water_Cycle)

# Growth monitor and pest control concurrent after water cycle
monitor_pest = StrictPartialOrder(nodes=[Growth_Monitor, Pest_Control])
# no edges - concurrent

# Loop for ongoing monitoring and pest control:
# Loop node: execute Growth Monitor, then choose to exit or execute Pest Control then Growth Monitor again
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[Growth_Monitor, Pest_Control])

# Harvest after loop completes (i.e. after monitoring & pest control cycles)
# Waste process and data analyze can be done concurrently after harvest
post_harvest_tasks = StrictPartialOrder(nodes=[Waste_Process, Data_Analyze])
# no edges - concurrent

# Package goods after both waste process and data analyze
package = StrictPartialOrder(nodes=[Waste_Process, Data_Analyze, Package_Goods])
package.order.add_edge(Waste_Process, Package_Goods)
package.order.add_edge(Data_Analyze, Package_Goods)

# Local deliver after packaging
deliver = StrictPartialOrder(nodes=[Package_Goods, Local_Deliver])
deliver.order.add_edge(Package_Goods, Local_Deliver)

# Combine all main phases in a partial order:
# 1) pre_permit -> infra_system -> nutrient_seedling -> env_setup -> loop_monitor -> Harvest_Crop -> post_harvest_tasks -> package -> deliver
main_flow = StrictPartialOrder(
    nodes=[pre_permit, infra_system, nutrient_seedling, env_setup, loop_monitor, Harvest_Crop, post_harvest_tasks, package, deliver]
)
main_flow.order.add_edge(pre_permit, infra_system)
main_flow.order.add_edge(infra_system, nutrient_seedling)
main_flow.order.add_edge(nutrient_seedling, env_setup)
main_flow.order.add_edge(env_setup, loop_monitor)
main_flow.order.add_edge(loop_monitor, Harvest_Crop)
main_flow.order.add_edge(Harvest_Crop, post_harvest_tasks)
main_flow.order.add_edge(post_harvest_tasks, package)
main_flow.order.add_edge(package, deliver)

root = main_flow