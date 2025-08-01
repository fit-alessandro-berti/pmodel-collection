# Generated from: 7681640e-8dd6-4a87-ac5c-4c1c87d12954.json
# Description: This process outlines the end-to-end setup and deployment of a bespoke drone fleet designed for specialized industrial inspection tasks. It begins with requirement analysis and proceeds through custom hardware sourcing, firmware adaptation, and environmental simulation testing. After pilot training and regulatory compliance validation, the process includes dynamic route programming, real-time telemetry integration, and emergency protocol implementation. Finally, the process ensures continuous performance monitoring and adaptive maintenance scheduling to optimize operational longevity and safety in challenging environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
requirement_analysis = Transition(label='Requirement Analysis')
hardware_sourcing    = Transition(label='Hardware Sourcing')
firmware_adaptation  = Transition(label='Firmware Adaptation')
simulated_testing    = Transition(label='Simulated Testing')
pilot_training       = Transition(label='Pilot Training')
compliance_check     = Transition(label='Compliance Check')
route_programming    = Transition(label='Route Programming')
telemetry_setup      = Transition(label='Telemetry Setup')
emergency_setup      = Transition(label='Emergency Setup')
data_integration     = Transition(label='Data Integration')
risk_assessment      = Transition(label='Risk Assessment')
field_deployment     = Transition(label='Field Deployment')
feedback_loop        = Transition(label='Feedback Loop')
performance_audit    = Transition(label='Performance Audit')
maintenance_plan     = Transition(label='Maintenance Plan')

# Define the redo part of the loop (Feedback Loop -> Maintenance Plan)
redo_po = StrictPartialOrder(
    nodes=[feedback_loop, maintenance_plan]
)
redo_po.order.add_edge(feedback_loop, maintenance_plan)

# Define the loop: do a Performance Audit, then either exit or do redo_po then audit again
audit_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[performance_audit, redo_po]
)

# Assemble the main sequence as a partial order
root = StrictPartialOrder(
    nodes=[
        requirement_analysis,
        hardware_sourcing,
        firmware_adaptation,
        simulated_testing,
        pilot_training,
        compliance_check,
        route_programming,
        telemetry_setup,
        emergency_setup,
        data_integration,
        risk_assessment,
        field_deployment,
        audit_loop
    ]
)

# Add the sequential dependencies
r = root.order
r.add_edge(requirement_analysis, hardware_sourcing)
r.add_edge(hardware_sourcing, firmware_adaptation)
r.add_edge(firmware_adaptation, simulated_testing)
r.add_edge(simulated_testing, pilot_training)
r.add_edge(pilot_training, compliance_check)
r.add_edge(compliance_check, route_programming)
r.add_edge(route_programming, telemetry_setup)
r.add_edge(telemetry_setup, emergency_setup)
r.add_edge(emergency_setup, data_integration)
r.add_edge(data_integration, risk_assessment)
r.add_edge(risk_assessment, field_deployment)
r.add_edge(field_deployment, audit_loop)