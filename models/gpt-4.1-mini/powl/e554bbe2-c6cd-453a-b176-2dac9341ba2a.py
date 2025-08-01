# Generated from: e554bbe2-c6cd-453a-b176-2dac9341ba2a.json
# Description: This process outlines the intricate steps involved in sourcing rare cheeses from small-scale artisanal farms, ensuring quality through custom aging, managing seasonal variations, and coordinating with niche gourmet retailers. It includes unique tasks such as microbial profiling, traditional hand-wrapping, climate-controlled transport logistics, and consumer feedback integration to maintain authenticity and exclusivity. The process demands close collaboration between farmers, microbiologists, logistics experts, and marketing teams to preserve the cheese's heritage while scaling distribution sustainably across diverse markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Farm_Selection = Transition(label='Farm Selection')
Milk_Testing = Transition(label='Milk Testing')
Starter_Culture = Transition(label='Starter Culture')
Curd_Formation = Transition(label='Curd Formation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Microbial_Profiling = Transition(label='Microbial Profiling')
Aging_Control = Transition(label='Aging Control')
Hand_Wrapping = Transition(label='Hand Wrapping')
Quality_Audit = Transition(label='Quality Audit')
Packaging_Prep = Transition(label='Packaging Prep')
Climate_Shipping = Transition(label='Climate Shipping')
Retail_Coordination = Transition(label='Retail Coordination')
Seasonal_Review = Transition(label='Seasonal Review')
Consumer_Survey = Transition(label='Consumer Survey')
Feedback_Analysis = Transition(label='Feedback Analysis')
Market_Adjustment = Transition(label='Market Adjustment')

# Process model structure analysis:
# 1) Core production flow: Farm Selection -> Milk Testing -> Starter Culture -> Curd Formation -> Pressing Cheese
core_production = StrictPartialOrder(nodes=[
    Farm_Selection, Milk_Testing, Starter_Culture, Curd_Formation, Pressing_Cheese
])
core_production.order.add_edge(Farm_Selection, Milk_Testing)
core_production.order.add_edge(Milk_Testing, Starter_Culture)
core_production.order.add_edge(Starter_Culture, Curd_Formation)
core_production.order.add_edge(Curd_Formation, Pressing_Cheese)

# 2) Quality and aging branch: Microbial Profiling -> Aging Control -> Hand Wrapping -> Quality Audit
# This branch starts after Pressing Cheese
quality_branch = StrictPartialOrder(nodes=[
    Microbial_Profiling, Aging_Control, Hand_Wrapping, Quality_Audit
])
quality_branch.order.add_edge(Microbial_Profiling, Aging_Control)
quality_branch.order.add_edge(Aging_Control, Hand_Wrapping)
quality_branch.order.add_edge(Hand_Wrapping, Quality_Audit)

# Connect core production to quality branch
core_to_quality = StrictPartialOrder(nodes=[core_production, quality_branch])
core_to_quality.order.add_edge(core_production, quality_branch)

# 3) Packaging and logistics branch after quality audit
packaging_branch = StrictPartialOrder(nodes=[
    Packaging_Prep, Climate_Shipping, Retail_Coordination
])
packaging_branch.order.add_edge(Packaging_Prep, Climate_Shipping)
packaging_branch.order.add_edge(Climate_Shipping, Retail_Coordination)

# Connect quality branch to packaging branch
quality_to_packaging = StrictPartialOrder(nodes=[core_to_quality, packaging_branch])
quality_to_packaging.order.add_edge(core_to_quality, packaging_branch)

# 4) Seasonal variation and market adjustment loop:
# Seasonal Review triggers a loop with Consumer Survey, Feedback Analysis and Market Adjustment
# Loop: execute Seasonal Review, then choice to exit or do (Consumer Survey -> Feedback Analysis -> Market Adjustment) then again Seasonal Review
consumer_branch = StrictPartialOrder(nodes=[
    Consumer_Survey, Feedback_Analysis, Market_Adjustment
])
consumer_branch.order.add_edge(Consumer_Survey, Feedback_Analysis)
consumer_branch.order.add_edge(Feedback_Analysis, Market_Adjustment)

seasonal_feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Seasonal_Review, consumer_branch]
)

# The seasonal_feedback_loop runs concurrently / parallel after packaging branch (distribution)
root = StrictPartialOrder(
    nodes=[quality_to_packaging, seasonal_feedback_loop]
)
root.order.add_edge(quality_to_packaging, seasonal_feedback_loop)