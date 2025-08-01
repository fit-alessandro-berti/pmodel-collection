# Generated from: 24d2b147-4f6c-4a1c-9eee-37cf87fe70be.json
# Description: This process outlines the comprehensive steps involved in assembling custom drones tailored to specific client requirements. It begins with component sourcing based on specialized criteria, followed by firmware customization to match unique operational parameters. Quality assurance includes both automated and manual inspections to ensure compliance with safety and performance standards. The assembly incorporates modular parts to allow for future upgrades. After initial assembly, drones undergo environmental stress testing simulating various weather conditions. Post-testing, final calibration adjusts sensors and flight controls. Documentation is generated for maintenance and client training. The process concludes with packaging optimized for fragile electronics and coordinating logistics with specialized carriers to ensure secure delivery.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
component_sourcing = Transition(label='Component Sourcing')
firmware_setup = Transition(label='Firmware Setup')
module_assembly = Transition(label='Module Assembly')

preliminary_testing = Transition(label='Preliminary Testing')

calibration_adjust = Transition(label='Calibration Adjust')

stress_testing = Transition(label='Stress Testing')

sensor_check = Transition(label='Sensor Check')
flight_control = Transition(label='Flight Control')

quality_audit = Transition(label='Quality Audit')

documentation = Transition(label='Documentation')
client_review = Transition(label='Client Review')

packaging_prep = Transition(label='Packaging Prep')

logistics_plan = Transition(label='Logistics Plan')
shipping_arrange = Transition(label='Shipping Arrange')

after_sales_support = Transition(label='After-Sales Support')

# Build Quality Assurance partial order with concurrent sensor_check and flight_control preceding quality_audit
qa_po = StrictPartialOrder(
    nodes=[sensor_check, flight_control, quality_audit],
)
qa_po.order.add_edge(sensor_check, quality_audit)
qa_po.order.add_edge(flight_control, quality_audit)

# Build Packaging and Shipping partial order: logistics_plan before shipping_arrange
pack_ship_po = StrictPartialOrder(
    nodes=[packaging_prep, logistics_plan, shipping_arrange],
)
pack_ship_po.order.add_edge(logistics_plan, shipping_arrange)

# Client review possibly after documentation
doc_review_po = StrictPartialOrder(
    nodes=[documentation, client_review],
)
doc_review_po.order.add_edge(documentation, client_review)

# Partial order of module assembly: module_assembly then preliminary_testing then stress_testing then calibration_adjust
assembly_po = StrictPartialOrder(
    nodes=[module_assembly, preliminary_testing, stress_testing, calibration_adjust],
)
assembly_po.order.add_edge(module_assembly, preliminary_testing)
assembly_po.order.add_edge(preliminary_testing, stress_testing)
assembly_po.order.add_edge(stress_testing, calibration_adjust)

# Overall process order:
# component_sourcing -> firmware_setup -> assembly_po -> qa_po -> doc_review_po -> pack_ship_po -> after_sales_support

root = StrictPartialOrder(
    nodes=[
        component_sourcing,
        firmware_setup,
        assembly_po,
        qa_po,
        doc_review_po,
        pack_ship_po,
        after_sales_support
    ],
)
root.order.add_edge(component_sourcing, firmware_setup)
root.order.add_edge(firmware_setup, assembly_po)
root.order.add_edge(assembly_po, qa_po)
root.order.add_edge(qa_po, doc_review_po)
root.order.add_edge(doc_review_po, pack_ship_po)
root.order.add_edge(pack_ship_po, after_sales_support)