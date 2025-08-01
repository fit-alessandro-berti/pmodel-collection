# Generated from: 5bc20f9d-dbd3-4f3c-9d30-e1da52e781b5.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming system in a densely populated city environment. It includes site analysis for optimal sunlight and space utilization, modular structure design to maximize crop yield vertically, integration of hydroponic and aeroponic systems for water and nutrient efficiency, automation setup for climate control and harvesting, and continuous monitoring through IoT sensors. The process also involves compliance checks with local regulations, community engagement for urban acceptance, pilot crop trials, and scaling strategies to expand production sustainably while minimizing environmental impact and operational costs.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Analysis = Transition(label='Site Analysis')
Light_Mapping = Transition(label='Light Mapping')
Structure_Design = Transition(label='Structure Design')
System_Integration = Transition(label='System Integration')
Water_Setup = Transition(label='Water Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automation_Config = Transition(label='Automation Config')
Sensor_Install = Transition(label='Sensor Install')
Climate_Control = Transition(label='Climate Control')
Compliance_Review = Transition(label='Compliance Review')
Community_Meet = Transition(label='Community Meet')
Pilot_Planting = Transition(label='Pilot Planting')
Data_Monitoring = Transition(label='Data Monitoring')
Harvest_Trial = Transition(label='Harvest Trial')
Scale_Planning = Transition(label='Scale Planning')
Waste_Reuse = Transition(label='Waste Reuse')

# Build partial orders to represent the flow

# Site Analysis -> Light Mapping (subtask of site analysis)
site_analysis_po = StrictPartialOrder(nodes=[Site_Analysis, Light_Mapping])
site_analysis_po.order.add_edge(Site_Analysis, Light_Mapping)

# Structure Design after Site Analysis and Light Mapping
structure_design_po = StrictPartialOrder(nodes=[site_analysis_po, Structure_Design])
structure_design_po.order.add_edge(site_analysis_po, Structure_Design)

# System Integration: Water Setup and Nutrient Mix in parallel, then System Integration
water_nutrient_po = StrictPartialOrder(nodes=[Water_Setup, Nutrient_Mix])
# no order between water and nutrient = concurrent

system_integration_po = StrictPartialOrder(nodes=[water_nutrient_po, System_Integration])
system_integration_po.order.add_edge(water_nutrient_po, System_Integration)

# Automation Config and Sensor Install in parallel
automation_sensor_po = StrictPartialOrder(nodes=[Automation_Config, Sensor_Install])
# no order between automation and sensor = concurrent

# Climate Control after Automation Config and Sensor Install
automation_sensor_climate_po = StrictPartialOrder(nodes=[automation_sensor_po, Climate_Control])
automation_sensor_climate_po.order.add_edge(automation_sensor_po, Climate_Control)

# Compliance Review and Community Meet in parallel
compliance_community_po = StrictPartialOrder(nodes=[Compliance_Review, Community_Meet])
# no order between compliance and community

# Pilot Planting after Compliance Review and Community Meet
pilot_planting_po = StrictPartialOrder(nodes=[compliance_community_po, Pilot_Planting])
pilot_planting_po.order.add_edge(compliance_community_po, Pilot_Planting)

# Data Monitoring and Harvest Trial in parallel after Pilot Planting
monitoring_harvest_po = StrictPartialOrder(nodes=[Data_Monitoring, Harvest_Trial])
# no order between monitoring and harvest

pilot_and_monitoring_po = StrictPartialOrder(nodes=[pilot_planting_po, monitoring_harvest_po])
pilot_and_monitoring_po.order.add_edge(pilot_planting_po, monitoring_harvest_po)

# Loop for continuous monitoring and harvesting trial:
# Loop(
#    A = Data Monitoring and Harvest Trial (concurrent),
#    B = Silent transition (tau) to loop again or exit
# )
skip = SilentTransition()
monitor_harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitoring_harvest_po, skip])

# Scale Planning after monitoring and harvest loop ends
scale_planning_po = StrictPartialOrder(nodes=[monitor_harvest_loop, Scale_Planning])
scale_planning_po.order.add_edge(monitor_harvest_loop, Scale_Planning)

# Waste Reuse can happen concurrently with Scale Planning (efficiency)
final_po = StrictPartialOrder(nodes=[scale_planning_po, Waste_Reuse])
# no order between scale planning and waste reuse

# Connect the main phases in order:
# structure_design_po after site_analysis_po done
# system_integration_po after structure_design_po
# automation_sensor_climate_po after system_integration_po
# pilot_and_monitoring_po after automation_sensor_climate_po
# scale_planning_po in final_po after monitoring loop (embedded in scale_planning_po)
# Waste reuse concurrent with scale planning

main_po_nodes = [
    site_analysis_po,
    structure_design_po,
    system_integration_po,
    automation_sensor_climate_po,
    pilot_and_monitoring_po,
    final_po,
]

root = StrictPartialOrder(nodes=main_po_nodes)
# Define the order between these main phases:
root.order.add_edge(site_analysis_po, structure_design_po)
root.order.add_edge(structure_design_po, system_integration_po)
root.order.add_edge(system_integration_po, automation_sensor_climate_po)
root.order.add_edge(automation_sensor_climate_po, pilot_and_monitoring_po)
root.order.add_edge(pilot_and_monitoring_po, final_po)