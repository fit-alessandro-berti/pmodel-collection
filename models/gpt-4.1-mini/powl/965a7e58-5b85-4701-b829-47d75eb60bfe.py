# Generated from: 965a7e58-5b85-4701-b829-47d75eb60bfe.json
# Description: This process outlines the complex and atypical supply chain involved in producing and distributing artisanal cheeses. It begins with selecting rare milk sources, followed by unique fermentation techniques that require constant environmental adjustments. Quality assessment includes sensory tests alongside lab analysis to ensure flavor profiles meet niche market demands. Packaging is customized per region with biodegradable materials. Distribution involves coordination between local farmers, specialty retailers, and international gourmet markets, incorporating cold chain logistics and real-time tracking. Customer feedback loops influence future batch variations, creating a dynamic production cycle balancing tradition and innovation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Milk_Testing = Transition(label='Milk Testing')
Starter_Culture = Transition(label='Starter Culture')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Drain = Transition(label='Whey Drain')
Mold_Inoculate = Transition(label='Mold Inoculate')
Aging_Control = Transition(label='Aging Control')
Flavor_Tasting = Transition(label='Flavor Tasting')
Lab_Analysis = Transition(label='Lab Analysis')
Packaging_Design = Transition(label='Packaging Design')
Eco_Packaging = Transition(label='Eco Packaging')
Cold_Storage = Transition(label='Cold Storage')
Logistics_Plan = Transition(label='Logistics Plan')
Retail_Coordination = Transition(label='Retail Coordination')
Feedback_Review = Transition(label='Feedback Review')

# Silent transition for optional choice/exit in loop
skip = SilentTransition()

# Step 1: Milk Sourcing, milk testing, starter culture and pasteurize in partial order:
milk_preparation = StrictPartialOrder(nodes=[Milk_Sourcing, Milk_Testing, Starter_Culture, Milk_Pasteurize])
milk_preparation.order.add_edge(Milk_Sourcing, Milk_Testing)       # Test milk after sourcing
milk_preparation.order.add_edge(Milk_Testing, Starter_Culture)     # Starter culture after testing
milk_preparation.order.add_edge(Starter_Culture, Milk_Pasteurize)  # Pasteurize after starter culture

# Step 2: Curd formation activities sequentially:
curd_process = StrictPartialOrder(nodes=[Curd_Formation, Curd_Cutting, Whey_Drain])
curd_process.order.add_edge(Curd_Formation, Curd_Cutting)
curd_process.order.add_edge(Curd_Cutting, Whey_Drain)

# Step 3: Mold inoculate and aging control in partial order(concurrent)
aging = StrictPartialOrder(nodes=[Mold_Inoculate, Aging_Control])
# no edges, concurrent execution

# Step 4: Quality assessment - flavor tasting and lab analysis in XOR choice (sensory or lab can be done first exclusively)
quality_assessment = OperatorPOWL(operator=Operator.XOR, children=[Flavor_Tasting, Lab_Analysis])

# Step 5: Packaging design then choice for eco/standard packaging
packaging_design = Packaging_Design
packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[Eco_Packaging, skip])  # optionally skip Eco Packaging

packaging = StrictPartialOrder(nodes=[packaging_design, packaging_choice])
packaging.order.add_edge(packaging_design, packaging_choice)

# Step 6: Distribution partial order between cold storage, logistics plan, retail coordination:
distribution = StrictPartialOrder(nodes=[Cold_Storage, Logistics_Plan, Retail_Coordination])
# Concurrent, no ordering edges

# Step 7: Feedback review loops back to start of production (milk preparation)
# Loop: 
#   body A = feedback review
#   body B = complete process from milk preparation up to distribution

# Complete process before feedback:
before_feedback = StrictPartialOrder(
    nodes=[milk_preparation, curd_process, aging, quality_assessment, packaging, distribution]
)
# Build partial order edges for process flow:
# milk_preparation before curd_process
before_feedback.order.add_edge(milk_preparation, curd_process)
# curd_process before aging
before_feedback.order.add_edge(curd_process, aging)
# aging before quality assessment
before_feedback.order.add_edge(aging, quality_assessment)
# quality assessment before packaging
before_feedback.order.add_edge(quality_assessment, packaging)
# packaging before distribution
before_feedback.order.add_edge(packaging, distribution)

# Loop: execute before_feedback, then feedback_review, then choose to exit or loop again
loop = OperatorPOWL(operator=Operator.LOOP, children=[before_feedback, Feedback_Review])

root = loop