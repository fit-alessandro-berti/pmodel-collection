# Generated from: 7c63406a-8a53-49bf-bdfa-e0f1855c7868.json
# Description: This process outlines the complex supply chain management of artisanal cheese production, starting from sourcing rare milk varieties from small farms, through custom fermentation and aging stages in microclimate-controlled rooms, quality testing using sensory panels, to bespoke packaging and niche market distribution. It involves coordination among farmers, microbiologists, logistics experts, and marketing specialists to ensure product authenticity, maintain flavor profiles, and meet regulatory standards while catering to gourmet consumers worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Farm_Audit = Transition(label='Farm Audit')
Milk_Testing = Transition(label='Milk Testing')

Starter_Prep = Transition(label='Starter Prep')
Curd_Formation = Transition(label='Curd Formation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Stage = Transition(label='Salting Stage')

Microclimate_Setup = Transition(label='Microclimate Setup')
Aging_Control = Transition(label='Aging Control')

Sensory_Panel = Transition(label='Sensory Panel')
Quality_Review = Transition(label='Quality Review')

Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')

Custom_Shipping = Transition(label='Custom Shipping')
Retail_Onboarding = Transition(label='Retail Onboarding')
Market_Feedback = Transition(label='Market Feedback')

# Build partial orders reflecting partial order and concurrency

# Milk sourcing related - start: Milk_Sourcing -> Farm_Audit -> Milk_Testing
milk_proc = StrictPartialOrder(
    nodes=[Milk_Sourcing, Farm_Audit, Milk_Testing]
)
milk_proc.order.add_edge(Milk_Sourcing, Farm_Audit)
milk_proc.order.add_edge(Farm_Audit, Milk_Testing)

# Cheese production fermentation sequence
cheese_prod_seq = StrictPartialOrder(
    nodes=[Starter_Prep, Curd_Formation, Pressing_Cheese, Salting_Stage]
)
cheese_prod_seq.order.add_edge(Starter_Prep, Curd_Formation)
cheese_prod_seq.order.add_edge(Curd_Formation, Pressing_Cheese)
cheese_prod_seq.order.add_edge(Pressing_Cheese, Salting_Stage)

# Aging and microclimate setup run concurrently but Aging_Control depends on Microclimate_Setup
aging_setup = StrictPartialOrder(
    nodes=[Microclimate_Setup, Aging_Control]
)
aging_setup.order.add_edge(Microclimate_Setup, Aging_Control)

# Sensory panel and Quality review sequential
quality_seq = StrictPartialOrder(
    nodes=[Sensory_Panel, Quality_Review]
)
quality_seq.order.add_edge(Sensory_Panel, Quality_Review)

# Packaging design and label approval sequential
packaging_approval = StrictPartialOrder(
    nodes=[Packaging_Design, Label_Approval]
)
packaging_approval.order.add_edge(Packaging_Design, Label_Approval)

# Distribution sequence:
distribution_seq = StrictPartialOrder(
    nodes=[Custom_Shipping, Retail_Onboarding, Market_Feedback]
)
distribution_seq.order.add_edge(Custom_Shipping, Retail_Onboarding)
distribution_seq.order.add_edge(Retail_Onboarding, Market_Feedback)

# Combine all major blocks into a global partial order:
# Start with milk_proc first,
# then cheese_prod_seq and aging_setup can run concurrently (senior experts work parallel),
# after which quality_seq,
# then packaging_approval,
# finally distribution_seq

root = StrictPartialOrder(
    nodes=[
        milk_proc,
        cheese_prod_seq,
        aging_setup,
        quality_seq,
        packaging_approval,
        distribution_seq
    ]
)
# Add edges to reflect dependencies between these blocks
root.order.add_edge(milk_proc, cheese_prod_seq)
root.order.add_edge(milk_proc, aging_setup)
root.order.add_edge(cheese_prod_seq, quality_seq)
root.order.add_edge(aging_setup, quality_seq)
root.order.add_edge(quality_seq, packaging_approval)
root.order.add_edge(packaging_approval, distribution_seq)