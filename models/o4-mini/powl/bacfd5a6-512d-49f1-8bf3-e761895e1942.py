# Generated from: bacfd5a6-512d-49f1-8bf3-e761895e1942.json
# Description: This process manages the complex supply chain for an urban vertical farming operation that sources organic inputs, coordinates sensor-driven crop monitoring, adapts to microclimate variations, and delivers fresh produce directly to local consumers. It integrates IoT data analysis for predictive maintenance, dynamic inventory adjustment based on growth cycles, and last-mile delivery optimization within congested cityscapes. The process includes vendor coordination for sustainable packaging, regulatory compliance for urban agriculture, and real-time customer feedback loops to refine crop varieties and service quality, all while maintaining sustainability and minimizing waste in a highly dynamic environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
input_sourcing     = Transition(label='Input Sourcing')
sensor_sync        = Transition(label='Sensor Sync')
crop_monitor       = Transition(label='Crop Monitor')
climate_adjust     = Transition(label='Climate Adjust')
growth_forecast    = Transition(label='Growth Forecast')
inventory_check    = Transition(label='Inventory Check')
vendor_align       = Transition(label='Vendor Align')
packaging_prep     = Transition(label='Packaging Prep')
regulation_review  = Transition(label='Regulation Review')
quality_audit      = Transition(label='Quality Audit')
data_analysis      = Transition(label='Data Analysis')
maintenance_plan   = Transition(label='Maintenance Plan')
order_dispatch     = Transition(label='Order Dispatch')
route_optimize     = Transition(label='Route Optimize')
customer_feedback  = Transition(label='Customer Feedback')
waste_manage       = Transition(label='Waste Manage')

# Monitoring and inventory loop body
monitor_seq = StrictPartialOrder(nodes=[
    sensor_sync, crop_monitor, climate_adjust, growth_forecast, inventory_check
])
monitor_seq.order.add_edge(sensor_sync, crop_monitor)
monitor_seq.order.add_edge(crop_monitor, climate_adjust)
monitor_seq.order.add_edge(climate_adjust, growth_forecast)
monitor_seq.order.add_edge(growth_forecast, inventory_check)

# Analysis and maintenance loop repeat
analysis_plan = StrictPartialOrder(nodes=[data_analysis, maintenance_plan])
analysis_plan.order.add_edge(data_analysis, maintenance_plan)

# Loop: monitor_seq then either exit or do analysis_plan and repeat
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_seq, analysis_plan])

# Vendor coordination, packaging, compliance, audit
vendor_stage = StrictPartialOrder(nodes=[
    vendor_align, packaging_prep, regulation_review, quality_audit
])
vendor_stage.order.add_edge(vendor_align, packaging_prep)
vendor_stage.order.add_edge(packaging_prep, regulation_review)
vendor_stage.order.add_edge(regulation_review, quality_audit)

# Dispatch, routing, feedback and waste management (feedback and waste concurrent)
dispatch_stage = StrictPartialOrder(nodes=[
    order_dispatch, route_optimize, customer_feedback, waste_manage
])
dispatch_stage.order.add_edge(order_dispatch, route_optimize)
dispatch_stage.order.add_edge(route_optimize, customer_feedback)
dispatch_stage.order.add_edge(route_optimize, waste_manage)

# Root partial order
root = StrictPartialOrder(nodes=[
    input_sourcing, monitor_loop, vendor_stage, dispatch_stage
])
root.order.add_edge(input_sourcing, monitor_loop)
root.order.add_edge(monitor_loop, vendor_stage)
root.order.add_edge(vendor_stage, dispatch_stage)