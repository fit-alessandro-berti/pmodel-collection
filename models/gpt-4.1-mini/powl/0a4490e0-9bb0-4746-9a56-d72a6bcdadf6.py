# Generated from: 0a4490e0-9bb0-4746-9a56-d72a6bcdadf6.json
# Description: This process outlines the end-to-end workflow for designing, manufacturing, and deploying custom drones tailored for agricultural monitoring. It includes initial client consultation to determine specific needs, iterative prototype testing using AI-driven simulations, regulatory compliance verification, precision component sourcing from multiple suppliers, adaptive software integration for environmental data collection, multi-phase quality assurance checks, and final deployment with remote operational training. Post-deployment, the process incorporates continuous performance monitoring with automatic firmware updates and periodic feedback sessions to optimize drone functionality and client satisfaction, ensuring a sustainable and scalable drone service solution.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Client_Brief = Transition(label='Client Brief')
Needs_Analysis = Transition(label='Needs Analysis')
Concept_Design = Transition(label='Concept Design')
AI_Simulation = Transition(label='AI Simulation')
Prototype_Build = Transition(label='Prototype Build')
Component_Sourcing = Transition(label='Component Sourcing')
Supply_Verification = Transition(label='Supply Verification')
Software_Coding = Transition(label='Software Coding')
Integration_Test = Transition(label='Integration Test')
Regulatory_Check = Transition(label='Regulatory Check')
Quality_Audit = Transition(label='Quality Audit')
Field_Trial = Transition(label='Field Trial')
Operator_Training = Transition(label='Operator Training')
Deployment_Launch = Transition(label='Deployment Launch')
Performance_Monitor = Transition(label='Performance Monitor')
Firmware_Update = Transition(label='Firmware Update')
Feedback_Review = Transition(label='Feedback Review')

# The iterative prototype testing using AI-driven simulations is a loop:
# loop: Concept Design and Prototype Build, then choice to exit or AI Simulation then loop again
# But description states iterative prototype testing using AI Simulation, so likely a loop with Concept Design + Prototype Build executed once before loop starts
# Let's model the loop as:
# A = Concept Design + Prototype Build (in partial order)
# B = AI Simulation (which is prototype testing driven by AI)
# Loop executes A once, then chooses to exit, or B then A again, repeatedly.

design_and_build = StrictPartialOrder(nodes=[Concept_Design, Prototype_Build])
design_and_build.order.add_edge(Concept_Design, Prototype_Build)

prototype_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_and_build, AI_Simulation])

# Component sourcing involves sourcing and supply verification, supply verification must come after sourcing
component_procurement = StrictPartialOrder(nodes=[Component_Sourcing, Supply_Verification])
component_procurement.order.add_edge(Component_Sourcing, Supply_Verification)

# Software integration for environmental data collection:
# Software Coding then Integration Test in order
software_integration = StrictPartialOrder(nodes=[Software_Coding, Integration_Test])
software_integration.order.add_edge(Software_Coding, Integration_Test)

# Quality assurance multi-phase checks: Quality Audit and Field Trial
quality_checks = StrictPartialOrder(nodes=[Quality_Audit, Field_Trial])
quality_checks.order.add_edge(Quality_Audit, Field_Trial)

# Deployment with remote operational training: Operator Training then Deployment Launch
deployment_phase = StrictPartialOrder(nodes=[Operator_Training, Deployment_Launch])
deployment_phase.order.add_edge(Operator_Training, Deployment_Launch)

# Post-deployment continuous performance monitoring with automatic firmware updates and periodic feedback:
# Model as a loop with Performance Monitor then choice of exit or Firmware Update and Feedback Review then re-monitoring
post_deploy_loop_body = StrictPartialOrder(nodes=[Firmware_Update, Feedback_Review])
# Feedback Review and Firmware Update concurrent, order none implied, so just nodes in set

post_deploy_loop = OperatorPOWL(operator=Operator.LOOP, children=[Performance_Monitor, post_deploy_loop_body])

# Regulatory compliance verification: Regulatory Check after prototype loop ends and before component sourcing and software integration
# Let's assume Regulatory_Check after prototype_loop and before component_procurement and software_integration
# Component procurement and software integration likely concurrent after regulatory check

# Client consultation and needs analysis happen first, in order
client_phase = StrictPartialOrder(nodes=[Client_Brief, Needs_Analysis])
client_phase.order.add_edge(Client_Brief, Needs_Analysis)

# Now assemble the full process as partial order with control flows

# After client_phase: prototype_loop and regulatory_check in parallel but regulatory_check likely after prototype loop:
# However, as per description regulatory compliance verification happens probably after prototype testing as prototypes must comply
# So prototype_loop --> Regulatory_Check --> component_procurement and software_integration (concurrent)

# component_procurement and software_integration happen in parallel

# After these, quality_checks then deployment_phase

# Then post_deploy_loop

root = StrictPartialOrder(nodes=[
    client_phase,                    # Client Brief -> Needs Analysis
    prototype_loop,                 # Loop on Concept Design and Prototype Build with AI Simulation
    Regulatory_Check,
    component_procurement,          # Component Sourcing -> Supply Verification
    software_integration,           # Software Coding -> Integration Test
    quality_checks,                 # Quality Audit -> Field Trial
    deployment_phase,               # Operator Training -> Deployment Launch
    post_deploy_loop                # Performance Monitor loop with Firmware Update and Feedback Review
])

# Define order relations

# client_phase --> prototype_loop
root.order.add_edge(client_phase, prototype_loop)

# prototype_loop --> Regulatory_Check
root.order.add_edge(prototype_loop, Regulatory_Check)

# Regulatory_Check --> component_procurement and Regulatory_Check --> software_integration (concurrent branches)
root.order.add_edge(Regulatory_Check, component_procurement)
root.order.add_edge(Regulatory_Check, software_integration)

# component_procurement and software_integration both precede quality_checks
root.order.add_edge(component_procurement, quality_checks)
root.order.add_edge(software_integration, quality_checks)

# quality_checks --> deployment_phase
root.order.add_edge(quality_checks, deployment_phase)

# deployment_phase --> post_deploy_loop
root.order.add_edge(deployment_phase, post_deploy_loop)