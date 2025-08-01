# Generated from: c454ff48-c41e-4b36-8242-928c03d94dd3.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm. It begins with site assessment to evaluate structural integrity and sunlight exposure, followed by securing permits from local authorities. Afterward, soil analysis and selection of suitable crops occurs. The process continues with installation of irrigation and drainage systems designed for limited rooftop space, and integration of renewable energy sources like solar panels. Subsequent activities involve training staff on vertical farming techniques and pest management, while coordinating logistics for supply chain and distribution. The final stages include community engagement to promote urban agriculture awareness and continuous monitoring for environmental impact and crop yield optimization.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Assess = Transition(label='Site Assess')
Permit_Obtain = Transition(label='Permit Obtain')
Soil_Testing = Transition(label='Soil Testing')
Crop_Select = Transition(label='Crop Select')
Irrigation_Setup = Transition(label='Irrigation Setup')
Drainage_Install = Transition(label='Drainage Install')
Energy_Integrate = Transition(label='Energy Integrate')
Staff_Train = Transition(label='Staff Train')
Pest_Control = Transition(label='Pest Control')
Logistics_Plan = Transition(label='Logistics Plan')
Supply_Coordinate = Transition(label='Supply Coordinate')
Distribution_Map = Transition(label='Distribution Map')
Community_Engage = Transition(label='Community Engage')
Monitoring_Setup = Transition(label='Monitoring Setup')
Yield_Optimize = Transition(label='Yield Optimize')

# Create partial orders representing groups of activities, based on description

# 1. Initial site assessment and permits (sequential)
initial_phase = StrictPartialOrder(nodes=[Site_Assess, Permit_Obtain])
initial_phase.order.add_edge(Site_Assess, Permit_Obtain)

# 2. Soil analysis and crop selection (sequential)
soil_crop = StrictPartialOrder(nodes=[Soil_Testing, Crop_Select])
soil_crop.order.add_edge(Soil_Testing, Crop_Select)

# 3. Irrigation and drainage installation (can be concurrent or sequential - likely sequential in rooftop farm)
irrigation_drainage = StrictPartialOrder(nodes=[Irrigation_Setup, Drainage_Install])
irrigation_drainage.order.add_edge(Irrigation_Setup, Drainage_Install)

# 4. Energy integration (solar panels etc.) - alone step
energy = Energy_Integrate

# 5. Staff training and pest control (sequential)
training_pest = StrictPartialOrder(nodes=[Staff_Train, Pest_Control])
training_pest.order.add_edge(Staff_Train, Pest_Control)

# 6. Logistics planning, supply coordination, and distribution mapping (sequential)
logistics = StrictPartialOrder(
    nodes=[Logistics_Plan, Supply_Coordinate, Distribution_Map]
)
logistics.order.add_edge(Logistics_Plan, Supply_Coordinate)
logistics.order.add_edge(Supply_Coordinate, Distribution_Map)

# 7. Community engagement (alone)
community = Community_Engage

# 8. Monitoring setup and yield optimization (sequential)
monitoring = StrictPartialOrder(nodes=[Monitoring_Setup, Yield_Optimize])
monitoring.order.add_edge(Monitoring_Setup, Yield_Optimize)

# Define partial order to combine activities after permits:
# From description, after permits: soil/crop, irrigation/drainage, energy integration
# "The process continues with installation..., and integration of renewable energy..."
# These three can be concurrent after permits, so they run concurrently

after_permit = StrictPartialOrder(
    nodes=[soil_crop, irrigation_drainage, energy]
)
# No edges => concurrent between soil_crop, irrigation_drainage, energy

# After that, training and pest control, logistics planning, community engagement, monitoring steps follow
# The description suggests training etc. happen after installation steps, and finally community engagement and monitoring

# Combine:
# initial_phase --> after_permit --> training_pest --> logistics --> community --> monitoring

root = StrictPartialOrder(
    nodes=[
        initial_phase,
        after_permit,
        training_pest,
        logistics,
        community,
        monitoring
    ]
)

# define order edges between phases

root.order.add_edge(initial_phase, after_permit)
root.order.add_edge(after_permit, training_pest)
root.order.add_edge(training_pest, logistics)
root.order.add_edge(logistics, community)
root.order.add_edge(community, monitoring)