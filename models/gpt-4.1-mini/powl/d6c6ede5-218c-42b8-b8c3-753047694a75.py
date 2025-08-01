# Generated from: d6c6ede5-218c-42b8-b8c3-753047694a75.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farm on a commercial building. It involves initial feasibility studies including structural assessments, microclimate analysis, and local regulations review. Following approvals, the process continues with soil-less system design, procurement of specialized equipment such as hydroponic trays and automated irrigation systems, installation of solar-powered sensors for real-time monitoring, and staff training on sustainable farming practices. Finally, the setup includes pilot planting, data collection on crop yield and environmental impact, ongoing maintenance scheduling, and community engagement initiatives to promote urban agriculture awareness and participation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Load_Test = Transition(label='Load Test')
Climate_Study = Transition(label='Climate Study')
Permit_Check = Transition(label='Permit Check')
System_Design = Transition(label='System Design')
Equipment_Buy = Transition(label='Equipment Buy')
Sensor_Setup = Transition(label='Sensor Setup')
Irrigation_Fit = Transition(label='Irrigation Fit')
Solar_Install = Transition(label='Solar Install')
Staff_Train = Transition(label='Staff Train')
Pilot_Plant = Transition(label='Pilot Plant')
Data_Monitor = Transition(label='Data Monitor')
Crop_Harvest = Transition(label='Crop Harvest')
Maintenance_Plan = Transition(label='Maintenance Plan')
Community_Meet = Transition(label='Community Meet')

# Initial feasibility studies partial order: Site Survey -> (Load Test, Climate Study, Permit Check)
# Load Test, Climate Study, Permit Check can be concurrent after Site Survey
feasibility_PO = StrictPartialOrder(nodes=[Site_Survey, Load_Test, Climate_Study, Permit_Check])
feasibility_PO.order.add_edge(Site_Survey, Load_Test)
feasibility_PO.order.add_edge(Site_Survey, Climate_Study)
feasibility_PO.order.add_edge(Site_Survey, Permit_Check)

# Procurement and design steps to be done sequentially:
# System Design -> Equipment Buy -> (Sensor Setup, Irrigation Fit, Solar Install)
# Sensor_Setup, Irrigation_Fit, Solar_Install are concurrent after Equipment Buy
design_PO = StrictPartialOrder(nodes=[System_Design, Equipment_Buy, Sensor_Setup, Irrigation_Fit, Solar_Install])
design_PO.order.add_edge(System_Design, Equipment_Buy)
design_PO.order.add_edge(Equipment_Buy, Sensor_Setup)
design_PO.order.add_edge(Equipment_Buy, Irrigation_Fit)
design_PO.order.add_edge(Equipment_Buy, Solar_Install)

# Staff Train after sensor setup, irrigation fit, solar install (all must be done)
staff_PO = StrictPartialOrder(nodes=[Sensor_Setup, Irrigation_Fit, Solar_Install, Staff_Train])
staff_PO.order.add_edge(Sensor_Setup, Staff_Train)
staff_PO.order.add_edge(Irrigation_Fit, Staff_Train)
staff_PO.order.add_edge(Solar_Install, Staff_Train)

# Pilot planting and monitoring and harvesting and maintenance and community meet:
# Sequential flow:
# Pilot Plant -> Data Monitor -> Crop Harvest -> Maintenance Plan -> Community Meet
final_PO = StrictPartialOrder(nodes=[Pilot_Plant, Data_Monitor, Crop_Harvest, Maintenance_Plan, Community_Meet])
final_PO.order.add_edge(Pilot_Plant, Data_Monitor)
final_PO.order.add_edge(Data_Monitor, Crop_Harvest)
final_PO.order.add_edge(Crop_Harvest, Maintenance_Plan)
final_PO.order.add_edge(Maintenance_Plan, Community_Meet)

# Compose the entire model according to the logical process order:
# feasibility_PO -> System_Design + Equipment_Buy + sensor/irrigation/solar -> Staff_Train -> final (Pilot to Community)
# Note that the design_PO includes System_Design, Equipment_Buy, sensor etc., so
# Staff_Train depends on design_PO.
# feasibility_PO before design_PO
# design_PO before staff_PO (which overlaps design_PO nodes, but staff_PO explicitly includes Staff_Train)
# staff_PO before final_PO

# To combine these and maintain proper order, we build composite partial orders:
# First combine design_PO and staff_PO (staff_PO includes sensor etc. nodes also)
# But since staff_PO uses nodes already in design_PO, to avoid duplicate nodes, we do as follows:
# design_PO (all except Staff_Train)
# then add Staff_Train with dependencies on sensor etc.

design_except_staff = StrictPartialOrder(nodes=[System_Design, Equipment_Buy, Sensor_Setup, Irrigation_Fit, Solar_Install])
design_except_staff.order.add_edge(System_Design, Equipment_Buy)
design_except_staff.order.add_edge(Equipment_Buy, Sensor_Setup)
design_except_staff.order.add_edge(Equipment_Buy, Irrigation_Fit)
design_except_staff.order.add_edge(Equipment_Buy, Solar_Install)

# Staff Train node with order edges from last 3 sensor nodes
design_plus_staff = StrictPartialOrder(nodes=[System_Design, Equipment_Buy, Sensor_Setup, Irrigation_Fit, Solar_Install, Staff_Train])
design_plus_staff.order.add_edge(System_Design, Equipment_Buy)
design_plus_staff.order.add_edge(Equipment_Buy, Sensor_Setup)
design_plus_staff.order.add_edge(Equipment_Buy, Irrigation_Fit)
design_plus_staff.order.add_edge(Equipment_Buy, Solar_Install)
design_plus_staff.order.add_edge(Sensor_Setup, Staff_Train)
design_plus_staff.order.add_edge(Irrigation_Fit, Staff_Train)
design_plus_staff.order.add_edge(Solar_Install, Staff_Train)

# Now build the entire root partial order combining feasibility_PO, design_plus_staff, final_PO with dependencies

root = StrictPartialOrder(
    nodes=[
        Site_Survey, Load_Test, Climate_Study, Permit_Check,
        System_Design, Equipment_Buy, Sensor_Setup, Irrigation_Fit, Solar_Install, Staff_Train,
        Pilot_Plant, Data_Monitor, Crop_Harvest, Maintenance_Plan, Community_Meet
    ]
)

# Add feasibility_PO edges
root.order.add_edge(Site_Survey, Load_Test)
root.order.add_edge(Site_Survey, Climate_Study)
root.order.add_edge(Site_Survey, Permit_Check)

# Feasibility before design start
root.order.add_edge(Permit_Check, System_Design)
root.order.add_edge(Load_Test, System_Design)
root.order.add_edge(Climate_Study, System_Design)

# design_plus_staff edges
root.order.add_edge(System_Design, Equipment_Buy)
root.order.add_edge(Equipment_Buy, Sensor_Setup)
root.order.add_edge(Equipment_Buy, Irrigation_Fit)
root.order.add_edge(Equipment_Buy, Solar_Install)
root.order.add_edge(Sensor_Setup, Staff_Train)
root.order.add_edge(Irrigation_Fit, Staff_Train)
root.order.add_edge(Solar_Install, Staff_Train)

# staff before final_PO
root.order.add_edge(Staff_Train, Pilot_Plant)

# final_PO edges
root.order.add_edge(Pilot_Plant, Data_Monitor)
root.order.add_edge(Data_Monitor, Crop_Harvest)
root.order.add_edge(Crop_Harvest, Maintenance_Plan)
root.order.add_edge(Maintenance_Plan, Community_Meet)