# Generated from: c619c6d9-c45c-4ad5-8992-4bd4e48841f7.json
# Description: This process involves the bespoke assembly of unmanned aerial vehicles tailored to specific client requirements. Starting from initial design consultation, the workflow includes component sourcing from multiple specialized suppliers, precision calibration of sensors, custom firmware integration, iterative flight testing in controlled environments, and compliance verification with aviation regulations. The process demands cross-functional coordination among engineering, quality assurance, software development, and logistics teams to ensure timely delivery of fully operational drones equipped with client-specific payloads and optimized flight parameters.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Design_Consult = Transition(label='Design Consult')

# Component sourcing from multiple specialized suppliers can be seen as concurrent subtasks:
Component_Sourcing = Transition(label='Component Sourcing')

# Precision calibration of sensors
Sensor_Calibrate = Transition(label='Sensor Calibrate')

# Custom firmware integration, software load and payload configure can be concurrent or partially ordered:
Firmware_Integrate = Transition(label='Firmware Integrate')
Software_Load = Transition(label='Software Load')
Payload_Configure = Transition(label='Payload Configure')

# Assembly setup, wiring connect, chassis build are assembly tasks that likely have order:
Assembly_Setup = Transition(label='Assembly Setup')
Wiring_Connect = Transition(label='Wiring Connect')
Chassis_Build = Transition(label='Chassis Build')

# Flight testing and Data analyze in iterative loop - because it's iterative flight testing and analysis:
Flight_Testing = Transition(label='Flight Testing')
Data_Analyze = Transition(label='Data Analyze')

# Regulation Check and Quality Inspect and Packaging Prep are sequential:
Regulation_Check = Transition(label='Regulation Check')
Quality_Inspect = Transition(label='Quality Inspect')
Packaging_Prep = Transition(label='Packaging Prep')

# Logistics Plan and Client Review final steps:
Logistics_Plan = Transition(label='Logistics Plan')
Client_Review = Transition(label='Client Review')

# Build assembly partial order:
assembly_nodes = [Assembly_Setup, Wiring_Connect, Chassis_Build]
assembly = StrictPartialOrder(nodes=assembly_nodes)
assembly.order.add_edge(Assembly_Setup, Wiring_Connect)
assembly.order.add_edge(Wiring_Connect, Chassis_Build)

# Firmware_Integrate, Software_Load, Payload_Configure can be done in parallel:
firmware_parallel = StrictPartialOrder(nodes=[Firmware_Integrate, Software_Load, Payload_Configure])
# no order edges means these three can run concurrently

# Flight testing loop: flight testing followed by data analyze, then choice to loop again or exit
flight_testing_loop_body = StrictPartialOrder(nodes=[Flight_Testing, Data_Analyze])
flight_testing_loop_body.order.add_edge(Flight_Testing, Data_Analyze)
flight_testing = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing_loop_body, flight_testing_loop_body])

# After flight testing loop: Regulation check -> Quality inspect -> Packaging prep
quality_sequence = StrictPartialOrder(nodes=[Regulation_Check, Quality_Inspect, Packaging_Prep])
quality_sequence.order.add_edge(Regulation_Check, Quality_Inspect)
quality_sequence.order.add_edge(Quality_Inspect, Packaging_Prep)

# Parallel block after Design Consult:
# - Component Sourcing
# - Sensor Calibrate
# - firmware_parallel
# - assembly
parallel_after_design = StrictPartialOrder(
    nodes=[Component_Sourcing, Sensor_Calibrate, firmware_parallel, assembly]
)
# no edges = concurrent

# Connect Design Consult to parallel block:
root = StrictPartialOrder(
    nodes=[Design_Consult, parallel_after_design, flight_testing, quality_sequence, Logistics_Plan, Client_Review]
)
root.order.add_edge(Design_Consult, parallel_after_design)

# After parallel block finishes, flight testing loop starts:
root.order.add_edge(parallel_after_design, flight_testing)

# After flight testing loop, quality_sequence:
root.order.add_edge(flight_testing, quality_sequence)

# After quality_sequence, logistics plan, then client review:
root.order.add_edge(quality_sequence, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Client_Review)