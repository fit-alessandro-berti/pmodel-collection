# Generated from: bacfd5a6-512d-49f1-8bf3-e761895e1942.json
# Description: This process manages the complex supply chain for an urban vertical farming operation that sources organic inputs, coordinates sensor-driven crop monitoring, adapts to microclimate variations, and delivers fresh produce directly to local consumers. It integrates IoT data analysis for predictive maintenance, dynamic inventory adjustment based on growth cycles, and last-mile delivery optimization within congested cityscapes. The process includes vendor coordination for sustainable packaging, regulatory compliance for urban agriculture, and real-time customer feedback loops to refine crop varieties and service quality, all while maintaining sustainability and minimizing waste in a highly dynamic environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Input_Sourcing = Transition(label='Input Sourcing')
Sensor_Sync = Transition(label='Sensor Sync')
Crop_Monitor = Transition(label='Crop Monitor')
Climate_Adjust = Transition(label='Climate Adjust')
Growth_Forecast = Transition(label='Growth Forecast')
Inventory_Check = Transition(label='Inventory Check')
Vendor_Align = Transition(label='Vendor Align')
Packaging_Prep = Transition(label='Packaging Prep')
Regulation_Review = Transition(label='Regulation Review')
Data_Analysis = Transition(label='Data Analysis')
Maintenance_Plan = Transition(label='Maintenance Plan')
Order_Dispatch = Transition(label='Order Dispatch')
Route_Optimize = Transition(label='Route Optimize')
Customer_Feedback = Transition(label='Customer Feedback')
Waste_Manage = Transition(label='Waste Manage')
Quality_Audit = Transition(label='Quality Audit')

# Define a loop node for Customer feedback refinement:
# After initial Quality Audit, Customer Feedback is gathered, then may refine Quality Audit repeatedly
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Audit, Customer_Feedback])

# Packaging and regulation compliance in parallel and then vendor alignment (vendor coordination)
packaging_regulation_po = StrictPartialOrder(nodes=[Packaging_Prep, Regulation_Review])
# No direct order, concurrent

vendor_align_after_pack_reg = StrictPartialOrder(nodes=[packaging_regulation_po, Vendor_Align])
vendor_align_after_pack_reg.order.add_edge(packaging_regulation_po, Vendor_Align)

# IoT data analysis leading to maintenance plan
analysis_maintenance = StrictPartialOrder(nodes=[Data_Analysis, Maintenance_Plan])
analysis_maintenance.order.add_edge(Data_Analysis, Maintenance_Plan)

# Inventory Check depends on Growth Forecast which depends on Crop Monitoring and Climate Adjust together:
crop_climate_po = StrictPartialOrder(nodes=[Crop_Monitor, Climate_Adjust])
# Crop Monitor and Climate Adjust concurrent
growth_forecast_po = StrictPartialOrder(nodes=[crop_climate_po, Growth_Forecast])
growth_forecast_po.order.add_edge(crop_climate_po, Growth_Forecast)

# Inventory check after Growth Forecast
growth_inventory_po = StrictPartialOrder(nodes=[growth_forecast_po, Inventory_Check])
growth_inventory_po.order.add_edge(growth_forecast_po, Inventory_Check)

# Sensor Sync after Input Sourcing
input_sensor_po = StrictPartialOrder(nodes=[Input_Sourcing, Sensor_Sync])
input_sensor_po.order.add_edge(Input_Sourcing, Sensor_Sync)

# Assemble the early chain: Input Sourcing -> Sensor Sync -> (Crop Monitor || Climate Adjust) -> Growth Forecast -> Inventory Check
early_stage_po = StrictPartialOrder(nodes=[input_sensor_po, growth_inventory_po])
early_stage_po.order.add_edge(input_sensor_po, growth_inventory_po)

# Chain for delivery: Order Dispatch -> Route Optimize
delivery_po = StrictPartialOrder(nodes=[Order_Dispatch, Route_Optimize])
delivery_po.order.add_edge(Order_Dispatch, Route_Optimize)

# Waste manage and sustainability with Quality Audit (Quality Audit is in feedback_loop)
waste_quality_po = StrictPartialOrder(nodes=[Waste_Manage, feedback_loop])

# Compose all main parts together:
# 1. Early supply and monitoring (early_stage_po)
# 2. Vendor/package/regulation (vendor_align_after_pack_reg)
# 3. IoT analysis and maintenance (analysis_maintenance)
# 4. Delivery (delivery_po)
# 5. Waste and quality feedback loop (waste_quality_po)

root = StrictPartialOrder(nodes=[early_stage_po, vendor_align_after_pack_reg, analysis_maintenance, delivery_po, waste_quality_po])

# Define partial order edges between these compound nodes to reflect natural dependencies:

# Early stage before vendor/vendor-align activities (sourcing before packaging/vendor align)
root.order.add_edge(early_stage_po, vendor_align_after_pack_reg)

# Vendor align before Data Analysis (e.g. vendor inputs support IoT data analysis)
root.order.add_edge(vendor_align_after_pack_reg, analysis_maintenance)

# Analysis/maintenance before order dispatch (predictive maintenance supports dispatch readiness)
root.order.add_edge(analysis_maintenance, delivery_po)

# Delivery before Waste manage and Quality feedback (delivery finished before waste & feedback loop)
root.order.add_edge(delivery_po, waste_quality_po)