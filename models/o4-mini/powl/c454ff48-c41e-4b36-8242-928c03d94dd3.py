# Generated from: c454ff48-c41e-4b36-8242-928c03d94dd3.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm. It begins with site assessment to evaluate structural integrity and sunlight exposure, followed by securing permits from local authorities. Afterward, soil analysis and selection of suitable crops occurs. The process continues with installation of irrigation and drainage systems designed for limited rooftop space, and integration of renewable energy sources like solar panels. Subsequent activities involve training staff on vertical farming techniques and pest management, while coordinating logistics for supply chain and distribution. The final stages include community engagement to promote urban agriculture awareness and continuous monitoring for environmental impact and crop yield optimization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the basic activities
site_assess     = Transition(label='Site Assess')
permit_obtain   = Transition(label='Permit Obtain')
soil_testing    = Transition(label='Soil Testing')
crop_select     = Transition(label='Crop Select')
irrigation_setup= Transition(label='Irrigation Setup')
drainage_install= Transition(label='Drainage Install')
energy_integrate= Transition(label='Energy Integrate')
staff_train     = Transition(label='Staff Train')
pest_control    = Transition(label='Pest Control')
logistics_plan  = Transition(label='Logistics Plan')
supply_coordinate= Transition(label='Supply Coordinate')
distribution_map= Transition(label='Distribution Map')
community_engage= Transition(label='Community Engage')
monitoring_setup= Transition(label='Monitoring Setup')
yield_optimize  = Transition(label='Yield Optimize')

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    permit_obtain,
    soil_testing,
    crop_select,
    irrigation_setup,
    drainage_install,
    energy_integrate,
    staff_train,
    pest_control,
    logistics_plan,
    supply_coordinate,
    distribution_map,
    community_engage,
    monitoring_setup,
    yield_optimize
])

# 1. Site Assess -> Permit Obtain
root.order.add_edge(site_assess, permit_obtain)

# 2. Permit Obtain -> {Soil Testing, Crop Select} (can run in parallel)
root.order.add_edge(permit_obtain, soil_testing)
root.order.add_edge(permit_obtain, crop_select)

# 3. {Soil Testing, Crop Select} -> {Irrigation Setup, Drainage Install}
root.order.add_edge(soil_testing, irrigation_setup)
root.order.add_edge(soil_testing, drainage_install)
root.order.add_edge(crop_select, irrigation_setup)
root.order.add_edge(crop_select, drainage_install)

# 4. {Irrigation Setup, Drainage Install} -> Energy Integrate
root.order.add_edge(irrigation_setup, energy_integrate)
root.order.add_edge(drainage_install, energy_integrate)

# 5. Energy Integrate -> {Staff Train, Pest Control}
root.order.add_edge(energy_integrate, staff_train)
root.order.add_edge(energy_integrate, pest_control)

# 6. {Staff Train, Pest Control} -> Logistics Plan
root.order.add_edge(staff_train, logistics_plan)
root.order.add_edge(pest_control, logistics_plan)

# 7. Logistics Plan -> Supply Coordinate -> Distribution Map
root.order.add_edge(logistics_plan, supply_coordinate)
root.order.add_edge(supply_coordinate, distribution_map)

# 8. Distribution Map -> Community Engage
root.order.add_edge(distribution_map, community_engage)

# 9. Community Engage -> Monitoring Setup -> Yield Optimize
root.order.add_edge(community_engage, monitoring_setup)
root.order.add_edge(monitoring_setup, yield_optimize)