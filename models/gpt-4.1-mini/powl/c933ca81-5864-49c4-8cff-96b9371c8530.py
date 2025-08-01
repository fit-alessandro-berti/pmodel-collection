# Generated from: c933ca81-5864-49c4-8cff-96b9371c8530.json
# Description: This process outlines the specialized steps involved in the custom manufacturing of drones tailored to unique client specifications. It begins with client consultation to define precise requirements, followed by design iteration incorporating advanced aerodynamics and AI integration. Components procurement involves sourcing rare materials and bespoke electronics. Subsequent phases include precision assembly, multi-layer firmware installation, and rigorous environmental testing under varying conditions. Quality assurance ensures compliance with international aviation standards before packaging with custom branding. Finally, logistics coordination manages secure delivery and post-sale technical support to ensure optimal drone performance and customer satisfaction.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for all activities
Client_Consult = Transition(label='Client Consult')
Spec_Finalize = Transition(label='Spec Finalize')
Design_Draft = Transition(label='Design Draft')
Aerodynamics_Test = Transition(label='Aerodynamics Test')
AI_Integration = Transition(label='AI Integration')
Material_Sourcing = Transition(label='Material Sourcing')
Component_Order = Transition(label='Component Order')
Assembly_Line = Transition(label='Assembly Line')
Firmware_Install = Transition(label='Firmware Install')
Environmental_Test = Transition(label='Environmental Test')
Quality_Check = Transition(label='Quality Check')
Brand_Packaging = Transition(label='Brand Packaging')
Shipping_Prep = Transition(label='Shipping Prep')
Delivery_Schedule = Transition(label='Delivery Schedule')
Post_Sale_Support = Transition(label='Post-Sale Support')

# Build the partial order according to the description:
# Order: Client Consult -> Spec Finalize -> Design iteration (Design Draft, Aerodynamics Test, AI Integration)
# Design Draft --> Aerodynamics Test --> AI Integration (strict order as "integration" after tests)
# Component procurement (Material Sourcing -> Component Order) after design iteration
# Assembly Line after component procurement
# Then Firmware Install after assembly
# Then Environmental Test after firmware install
# Quality Check after environmental test
# Brand Packaging after quality check
# Shipping Prep after packaging
# Delivery Schedule after shipping prep
# Post-Sale Support after delivery schedule

# Design iteration from description suggests linear: Design Draft -> Aerodynamics Test -> AI Integration

root = StrictPartialOrder(nodes=[Client_Consult, Spec_Finalize,
                                 Design_Draft, Aerodynamics_Test, AI_Integration,
                                 Material_Sourcing, Component_Order,
                                 Assembly_Line, Firmware_Install,
                                 Environmental_Test, Quality_Check,
                                 Brand_Packaging, Shipping_Prep,
                                 Delivery_Schedule, Post_Sale_Support])

root.order.add_edge(Client_Consult, Spec_Finalize)
root.order.add_edge(Spec_Finalize, Design_Draft)
root.order.add_edge(Design_Draft, Aerodynamics_Test)
root.order.add_edge(Aerodynamics_Test, AI_Integration)

root.order.add_edge(AI_Integration, Material_Sourcing)
root.order.add_edge(Material_Sourcing, Component_Order)
root.order.add_edge(Component_Order, Assembly_Line)
root.order.add_edge(Assembly_Line, Firmware_Install)
root.order.add_edge(Firmware_Install, Environmental_Test)
root.order.add_edge(Environmental_Test, Quality_Check)
root.order.add_edge(Quality_Check, Brand_Packaging)
root.order.add_edge(Brand_Packaging, Shipping_Prep)
root.order.add_edge(Shipping_Prep, Delivery_Schedule)
root.order.add_edge(Delivery_Schedule, Post_Sale_Support)