# Generated from: 4b34ce4e-742b-425c-bb7c-05d289ba4720.json
# Description: This business process manages the end-to-end supply chain activities for a large-scale event involving multiple vendors, fluctuating demand, and last-minute changes. It includes sourcing unique materials, coordinating with international logistics, handling custom regulations, real-time inventory adjustments, and ensuring timely setup on-site. The process must also integrate unexpected disruptions like weather delays or vendor cancellations, requiring dynamic rescheduling and resource reallocation while maintaining cost controls and stakeholder communication throughout the event lifecycle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Vendor_Sourcing = Transition(label='Vendor Sourcing')
Contract_Review = Transition(label='Contract Review')
Material_Ordering = Transition(label='Material Ordering')
Customs_Clearance = Transition(label='Customs Clearance')
Inventory_Check = Transition(label='Inventory Check')
Demand_Forecast = Transition(label='Demand Forecast')
Logistics_Planning = Transition(label='Logistics Planning')
Transport_Booking = Transition(label='Transport Booking')
Quality_Inspect = Transition(label='Quality Inspect')
Real_time_Tracking = Transition(label='Real-time Tracking')
Risk_Assessment = Transition(label='Risk Assessment')
Reschedule_Tasks = Transition(label='Reschedule Tasks')
Resource_Allocate = Transition(label='Resource Allocate')
Setup_Coordination = Transition(label='Setup Coordination')
Stakeholder_Update = Transition(label='Stakeholder Update')
Cost_Monitoring = Transition(label='Cost Monitoring')
Contingency_Plan = Transition(label='Contingency Plan')

# Define silent transition for exiting loops
skip = SilentTransition()

# Loop for handling disruptions: risk assessment -> choice between rescheduling or contingency plan -> loop back
disruption_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Risk_Assessment,
    OperatorPOWL(operator=Operator.XOR, children=[Reschedule_Tasks, Contingency_Plan])
])

# Partial order for supply chain core flow:
# Vendor Sourcing -> Contract Review -> Material Ordering
# Material Ordering branches into Customs Clearance and Demand Forecast concurrently (no order between these)
# Both lead into Inventory Check -> Logistics Planning -> Transport Booking
# Then to Quality Inspect -> Real-time Tracking
core_supply_PO = StrictPartialOrder(nodes=[
    Vendor_Sourcing,
    Contract_Review,
    Material_Ordering,
    Customs_Clearance,
    Demand_Forecast,
    Inventory_Check,
    Logistics_Planning,
    Transport_Booking,
    Quality_Inspect,
    Real_time_Tracking
])

# Add order edges
core_supply_PO.order.add_edge(Vendor_Sourcing, Contract_Review)
core_supply_PO.order.add_edge(Contract_Review, Material_Ordering)

# Material Ordering precedes Customs Clearance and Demand Forecast (both concurrent)
core_supply_PO.order.add_edge(Material_Ordering, Customs_Clearance)
core_supply_PO.order.add_edge(Material_Ordering, Demand_Forecast)

# Both Customs Clearance and Demand Forecast precede Inventory Check
core_supply_PO.order.add_edge(Customs_Clearance, Inventory_Check)
core_supply_PO.order.add_edge(Demand_Forecast, Inventory_Check)

core_supply_PO.order.add_edge(Inventory_Check, Logistics_Planning)
core_supply_PO.order.add_edge(Logistics_Planning, Transport_Booking)
core_supply_PO.order.add_edge(Transport_Booking, Quality_Inspect)
core_supply_PO.order.add_edge(Quality_Inspect, Real_time_Tracking)

# After Real-time Tracking, Risk Assessment loop runs concurrently with Resource Allocation and Setup Coordination
# Also, Stakeholder Update and Cost Monitoring must follow Resource Allocation and Setup Coordination

post_tracking_PO = StrictPartialOrder(nodes=[
    disruption_loop,
    Resource_Allocate,
    Setup_Coordination,
    Stakeholder_Update,
    Cost_Monitoring
])

# No order between disruption_loop, Resource Allocate and Setup Coordination (can proceed concurrently)
# But Stakeholder Update and Cost Monitoring depend on Resource Allocation and Setup Coordination finishing

post_tracking_PO.order.add_edge(Resource_Allocate, Stakeholder_Update)
post_tracking_PO.order.add_edge(Setup_Coordination, Stakeholder_Update)
post_tracking_PO.order.add_edge(Resource_Allocate, Cost_Monitoring)
post_tracking_PO.order.add_edge(Setup_Coordination, Cost_Monitoring)

# Compose the full process partial order of two parts: core_supply_PO -> post_tracking_PO sequentially

root = StrictPartialOrder(nodes=[
    core_supply_PO,
    post_tracking_PO
])

root.order.add_edge(core_supply_PO, post_tracking_PO)