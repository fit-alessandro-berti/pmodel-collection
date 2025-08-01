# Generated from: 4c52a71f-479e-4155-994f-5689039fcc74.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a densely populated city environment. It involves securing rooftop space, designing modular hydroponic systems, obtaining necessary permits, sourcing specialized LED lighting, installing climate control units, and integrating IoT sensors for real-time monitoring. Activities include coordinating with local authorities for zoning approvals, selecting crop varieties suited for indoor growth, training staff on maintenance protocols, and implementing automated nutrient delivery mechanisms. The process also covers marketing strategies targeting local restaurants and markets, establishing supply chain logistics for fresh produce delivery, and continuous optimization based on data analytics to maximize yield while minimizing energy consumption and waste. The complexity arises from balancing urban regulations, technological integration, and sustainable farming practices, all within a limited spatial footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
Site_Survey = Transition(label='Site Survey')
Permit_Request = Transition(label='Permit Request')
Design_Layout = Transition(label='Design Layout')
System_Sourcing = Transition(label='System Sourcing')
Lighting_Setup = Transition(label='Lighting Setup')
Climate_Install = Transition(label='Climate Install')
Sensor_Deploy = Transition(label='Sensor Deploy')
Crop_Select = Transition(label='Crop Select')
Staff_Training = Transition(label='Staff Training')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automation_Setup = Transition(label='Automation Setup')
Marketing_Plan = Transition(label='Marketing Plan')
Logistics_Plan = Transition(label='Logistics Plan')
Data_Review = Transition(label='Data Review')
Yield_Optimize = Transition(label='Yield Optimize')
Waste_Manage = Transition(label='Waste Manage')

# Partial order for initial permits and design
perm_design = StrictPartialOrder(nodes=[Site_Survey, Permit_Request, Design_Layout, System_Sourcing])
perm_design.order.add_edge(Site_Survey, Permit_Request)
perm_design.order.add_edge(Permit_Request, Design_Layout)
perm_design.order.add_edge(Design_Layout, System_Sourcing)

# Parallel setup: lighting, climate, sensor deployment after sourcing
setup_lighting = Lighting_Setup
setup_climate = Climate_Install
setup_sensor = Sensor_Deploy
setup_parallel = StrictPartialOrder(nodes=[setup_lighting, setup_climate, setup_sensor])

# Crop select and staff training are concurrent after setup
crop_staff = StrictPartialOrder(nodes=[Crop_Select, Staff_Training])

# Nutrient mix and automation setup after crop and staff training
nutrient_automation = StrictPartialOrder(nodes=[Nutrient_Mix, Automation_Setup])
nutrient_automation.order.add_edge(Nutrient_Mix, Automation_Setup)

# Marketing and logistics in parallel after automation setup
marketing = Marketing_Plan
logistics = Logistics_Plan
market_logistics = StrictPartialOrder(nodes=[marketing, logistics])

# Data review and optimizations after market and logistics
data_optimize = StrictPartialOrder(nodes=[Data_Review, Yield_Optimize, Waste_Manage])
data_optimize.order.add_edge(Data_Review, Yield_Optimize)
data_optimize.order.add_edge(Data_Review, Waste_Manage)

# Assemble major phases in order
root = StrictPartialOrder(
    nodes=[perm_design, setup_parallel, crop_staff, nutrient_automation, market_logistics, data_optimize]
)
root.order.add_edge(perm_design, setup_parallel)
root.order.add_edge(setup_parallel, crop_staff)
root.order.add_edge(crop_staff, nutrient_automation)
root.order.add_edge(nutrient_automation, market_logistics)
root.order.add_edge(market_logistics, data_optimize)