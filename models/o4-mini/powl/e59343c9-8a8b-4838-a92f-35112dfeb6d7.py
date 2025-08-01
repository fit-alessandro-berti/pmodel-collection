# Generated from: e59343c9-8a8b-4838-a92f-35112dfeb6d7.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm in a densely populated city environment. It combines aspects of architecture, agriculture, technology integration, and sustainability. The process begins with site analysis and regulatory approval, followed by structural design tailored for vertical hydroponic systems. Procurement of specialized equipment and organic nutrients ensures optimal growth conditions. Installation of IoT sensors and AI-driven climate control systems enables precise environmental management. Seed selection and germination protocols emphasize crop diversity and yield maximization. Continuous monitoring and data analytics support adaptive maintenance and pest control strategies. Finally, the process concludes with packaging and distribution logistics optimized for freshness and minimal environmental impact, ensuring a sustainable urban food supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
permit_approval  = Transition(label='Permit Approval')
design_layout    = Transition(label='Design Layout')
system_procure   = Transition(label='System Procure')
nutrient_prep    = Transition(label='Nutrient Prep')
structure_build  = Transition(label='Structure Build')
sensor_install   = Transition(label='Sensor Install')
climate_setup    = Transition(label='Climate Setup')
seed_select      = Transition(label='Seed Select')
germinate_seeds  = Transition(label='Germinate Seeds')
monitor_growth   = Transition(label='Monitor Growth')
data_analyze     = Transition(label='Data Analyze')
pest_control     = Transition(label='Pest Control')
harvest_crop     = Transition(label='Harvest Crop')
package_goods    = Transition(label='Package Goods')
ship_products    = Transition(label='Ship Products')

# Build the loop for continuous monitoring, analytics, and pest control
pre_monitor = StrictPartialOrder(nodes=[monitor_growth, data_analyze])
pre_monitor.order.add_edge(monitor_growth, data_analyze)
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[pre_monitor, pest_control])

# Assemble the top‐level workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    permit_approval,
    design_layout,
    system_procure,
    nutrient_prep,
    structure_build,
    sensor_install,
    climate_setup,
    seed_select,
    germinate_seeds,
    loop_monitor,
    harvest_crop,
    package_goods,
    ship_products
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey,     permit_approval)
root.order.add_edge(permit_approval, design_layout)

# Parallel procurement of system and nutrients after design
root.order.add_edge(design_layout, system_procure)
root.order.add_edge(design_layout, nutrient_prep)

# Both procurement steps must finish before building the structure
root.order.add_edge(system_procure,  structure_build)
root.order.add_edge(nutrient_prep,   structure_build)

# After the structure is up, install sensors and set up climate (in parallel)
root.order.add_edge(structure_build, sensor_install)
root.order.add_edge(structure_build, climate_setup)

# Both sensor and climate setups must complete before selecting seeds
root.order.add_edge(sensor_install, seed_select)
root.order.add_edge(climate_setup,  seed_select)

# Planting steps
root.order.add_edge(seed_select,     germinate_seeds)

# Upon germination, enter the monitoring loop
root.order.add_edge(germinate_seeds, loop_monitor)

# After exiting the loop, proceed to harvest, package, and ship
root.order.add_edge(loop_monitor,    harvest_crop)
root.order.add_edge(harvest_crop,    package_goods)
root.order.add_edge(package_goods,   ship_products)