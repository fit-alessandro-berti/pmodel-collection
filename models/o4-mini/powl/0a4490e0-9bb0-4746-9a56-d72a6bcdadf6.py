# Generated from: 0a4490e0-9bb0-4746-9a56-d72a6bcdadf6.json
# Description: This process outlines the end-to-end workflow for designing, manufacturing, and deploying custom drones tailored for agricultural monitoring. It includes initial client consultation to determine specific needs, iterative prototype testing using AI-driven simulations, regulatory compliance verification, precision component sourcing from multiple suppliers, adaptive software integration for environmental data collection, multi-phase quality assurance checks, and final deployment with remote operational training. Post-deployment, the process incorporates continuous performance monitoring with automatic firmware updates and periodic feedback sessions to optimize drone functionality and client satisfaction, ensuring a sustainable and scalable drone service solution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
client_brief        = Transition(label='Client Brief')
needs_analysis      = Transition(label='Needs Analysis')
concept_design      = Transition(label='Concept Design')
ai_simulation       = Transition(label='AI Simulation')
prototype_build     = Transition(label='Prototype Build')
component_sourcing  = Transition(label='Component Sourcing')
supply_verification = Transition(label='Supply Verification')
software_coding     = Transition(label='Software Coding')
integration_test    = Transition(label='Integration Test')
regulatory_check    = Transition(label='Regulatory Check')
quality_audit       = Transition(label='Quality Audit')
field_trial         = Transition(label='Field Trial')
operator_training   = Transition(label='Operator Training')
deployment_launch   = Transition(label='Deployment Launch')
performance_monitor = Transition(label='Performance Monitor')
firmware_update     = Transition(label='Firmware Update')
feedback_review     = Transition(label='Feedback Review')

# Loop 1: iterative prototype testing (AI Simulation ↔ Prototype Build)
loop1 = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ai_simulation, prototype_build]
)

# Loop 2: continuous performance monitoring with firmware updates & feedback
feedback_cycle = StrictPartialOrder(
    nodes=[firmware_update, feedback_review]
)
# no order edges ⇒ firmware_update and feedback_review can occur in any order / concurrently

loop2 = OperatorPOWL(
    operator=Operator.LOOP,
    children=[performance_monitor, feedback_cycle]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    client_brief,
    needs_analysis,
    concept_design,
    loop1,
    component_sourcing,
    supply_verification,
    software_coding,
    integration_test,
    regulatory_check,
    quality_audit,
    field_trial,
    operator_training,
    deployment_launch,
    loop2
])

# Define the control-flow (happens-before) relations
root.order.add_edge(client_brief,        needs_analysis)
root.order.add_edge(needs_analysis,      concept_design)
root.order.add_edge(concept_design,      loop1)
root.order.add_edge(loop1,               component_sourcing)
root.order.add_edge(component_sourcing,  supply_verification)
root.order.add_edge(supply_verification, software_coding)
root.order.add_edge(software_coding,     integration_test)
root.order.add_edge(integration_test,    regulatory_check)
root.order.add_edge(regulatory_check,    quality_audit)
root.order.add_edge(quality_audit,       field_trial)
root.order.add_edge(field_trial,         operator_training)
root.order.add_edge(operator_training,   deployment_launch)
root.order.add_edge(deployment_launch,   loop2)