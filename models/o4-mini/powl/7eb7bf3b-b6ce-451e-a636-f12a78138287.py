# Generated from: 7eb7bf3b-b6ce-451e-a636-f12a78138287.json
# Description: This process outlines the establishment of an urban rooftop farm in a dense metropolitan area, integrating sustainable practices with modern technology. It involves assessing structural integrity, securing permits, designing modular grow systems, sourcing organic seeds, installing automated irrigation, and setting up solar-powered climate control. The process continues with soil preparation, planting, monitoring plant health through IoT sensors, managing pest control organically, harvesting, packaging for local distribution, and conducting community workshops on urban agriculture. Each step requires coordination with city officials, engineers, suppliers, and local residents to ensure environmental compliance and community engagement, fostering a sustainable food source within the urban ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
site_survey    = Transition(label='Site Survey')
permit_check   = Transition(label='Permit Check')
load_test      = Transition(label='Load Test')
design_plan    = Transition(label='Design Plan')
seed_order     = Transition(label='Seed Order')
irrigation_set = Transition(label='Irrigation Setup')
solar_install  = Transition(label='Solar Install')
soil_prep      = Transition(label='Soil Prep')
plant_seeds    = Transition(label='Plant Seeds')
sensor_deploy  = Transition(label='Sensor Deploy')
health_monitor = Transition(label='Health Monitor')
pest_control   = Transition(label='Pest Control')
harvest_crop   = Transition(label='Harvest Crop')
package_goods  = Transition(label='Package Goods')
host_workshop  = Transition(label='Host Workshop')

# Build a partial order
root = StrictPartialOrder(
    nodes=[
        site_survey, permit_check, load_test, design_plan,
        seed_order, irrigation_set, solar_install,
        soil_prep, plant_seeds, sensor_deploy,
        health_monitor, pest_control,
        harvest_crop, package_goods, host_workshop
    ]
)

# Define the control-flow dependencies
# Core linear progression
root.order.add_edge(site_survey, permit_check)
root.order.add_edge(permit_check, load_test)
root.order.add_edge(load_test, design_plan)

# After design, order seeds, then set up systems (can be in parallel)
root.order.add_edge(design_plan, seed_order)
root.order.add_edge(seed_order, irrigation_set)
root.order.add_edge(seed_order, solar_install)

# Both installations must finish before preparing soil
root.order.add_edge(irrigation_set, soil_prep)
root.order.add_edge(solar_install, soil_prep)

# Then the rest is sequential
root.order.add_edge(soil_prep, plant_seeds)
root.order.add_edge(plant_seeds, sensor_deploy)
root.order.add_edge(sensor_deploy, health_monitor)
root.order.add_edge(health_monitor, pest_control)
root.order.add_edge(pest_control, harvest_crop)
root.order.add_edge(harvest_crop, package_goods)
root.order.add_edge(package_goods, host_workshop)