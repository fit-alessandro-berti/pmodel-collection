# Generated from: 7c63406a-8a53-49bf-bdfa-e0f1855c7868.json
# Description: This process outlines the complex supply chain management of artisanal cheese production, starting from sourcing rare milk varieties from small farms, through custom fermentation and aging stages in microclimate-controlled rooms, quality testing using sensory panels, to bespoke packaging and niche market distribution. It involves coordination among farmers, microbiologists, logistics experts, and marketing specialists to ensure product authenticity, maintain flavor profiles, and meet regulatory standards while catering to gourmet consumers worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
milk_sourcing       = Transition(label='Milk Sourcing')
farm_audit          = Transition(label='Farm Audit')
milk_testing        = Transition(label='Milk Testing')
starter_prep        = Transition(label='Starter Prep')
curd_formation      = Transition(label='Curd Formation')
pressing_cheese     = Transition(label='Pressing Cheese')
salting_stage       = Transition(label='Salting Stage')
microclimate_setup  = Transition(label='Microclimate Setup')
aging_control       = Transition(label='Aging Control')
sensory_panel       = Transition(label='Sensory Panel')
quality_review      = Transition(label='Quality Review')
packaging_design    = Transition(label='Packaging Design')
label_approval      = Transition(label='Label Approval')
custom_shipping     = Transition(label='Custom Shipping')
retail_onboarding   = Transition(label='Retail Onboarding')
market_feedback     = Transition(label='Market Feedback')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    milk_sourcing, farm_audit, milk_testing,
    starter_prep, curd_formation, pressing_cheese, salting_stage,
    microclimate_setup, aging_control,
    sensory_panel, quality_review,
    packaging_design, label_approval,
    custom_shipping, retail_onboarding,
    market_feedback
])

# Source‐farm‐milk‐testing branch
root.order.add_edge(milk_sourcing, farm_audit)
root.order.add_edge(farm_audit, milk_testing)

# Cheesemaking sequence
root.order.add_edge(milk_testing, starter_prep)
root.order.add_edge(starter_prep, curd_formation)
root.order.add_edge(curd_formation, pressing_cheese)
root.order.add_edge(pressing_cheese, salting_stage)

# Aging requires both salting_complete and microclimate_setup
root.order.add_edge(salting_stage, aging_control)
root.order.add_edge(microclimate_setup, aging_control)

# Quality checks
root.order.add_edge(aging_control, sensory_panel)
root.order.add_edge(sensory_panel, quality_review)

# Packaging and approval
root.order.add_edge(quality_review, packaging_design)
root.order.add_edge(packaging_design, label_approval)

# Distribution paths
root.order.add_edge(label_approval, custom_shipping)
root.order.add_edge(label_approval, retail_onboarding)

# Final market feedback after distribution
root.order.add_edge(custom_shipping, market_feedback)
root.order.add_edge(retail_onboarding, market_feedback)