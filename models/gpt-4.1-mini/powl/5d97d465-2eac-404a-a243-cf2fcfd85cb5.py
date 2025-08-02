# Generated from: 5d97d465-2eac-404a-a243-cf2fcfd85cb5.json
# Description: This process outlines the intricate steps involved in producing and distributing high-quality artisanal cheese from small-scale farms to niche gourmet shops. It begins with raw milk sourcing from selected herds, followed by precise fermentation control and handcrafted curd formation. The cheese undergoes aging in controlled environments with specific humidity and temperature settings, monitored regularly for flavor development. Packaging involves eco-friendly materials with unique branding, after which the product is distributed through specialty logistics channels prioritizing freshness. Marketing targets connoisseurs via curated events and digital storytelling, while customer feedback loops help refine future batches. Regulatory compliance, seasonal variations, and artisanal authenticity checks are integrated throughout to maintain product integrity and exclusivity in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Herd_Selection = Transition(label='Herd Selection')
Milk_Testing = Transition(label='Milk Testing')
Curd_Formation = Transition(label='Curd Formation')
Fermentation_Check = Transition(label='Fermentation Check')
Pressing_Stage = Transition(label='Pressing Stage')
Aging_Control = Transition(label='Aging Control')
Humidity_Monitor = Transition(label='Humidity Monitor')
Temperature_Adjust = Transition(label='Temperature Adjust')
Flavor_Sampling = Transition(label='Flavor Sampling')
Eco_Packaging = Transition(label='Eco Packaging')
Brand_Labeling = Transition(label='Brand Labeling')
Specialty_Shipping = Transition(label='Specialty Shipping')
Event_Marketing = Transition(label='Event Marketing')
Customer_Feedback = Transition(label='Customer Feedback')
Quality_Audits = Transition(label='Quality Audits')
Regulation_Review = Transition(label='Regulation Review')

# Milk sourcing subprocess with Herd Selection and Milk Testing concurrent after Milk Sourcing
milk_sub_po = StrictPartialOrder(nodes=[Milk_Sourcing, Herd_Selection, Milk_Testing])
milk_sub_po.order.add_edge(Milk_Sourcing, Herd_Selection)
milk_sub_po.order.add_edge(Milk_Sourcing, Milk_Testing)

# Fermentation and curd formation sequence: Fermentation Check before Curd Formation
fermentation_curd_po = StrictPartialOrder(nodes=[Fermentation_Check, Curd_Formation])
fermentation_curd_po.order.add_edge(Fermentation_Check, Curd_Formation)

# Pressing Stage after Curd Formation
curd_press_po = StrictPartialOrder(nodes=[fermentation_curd_po, Pressing_Stage])
curd_press_po.order.add_edge(fermentation_curd_po, Pressing_Stage)

# Aging process with monitors and sampling:
# Aging Control -> Humidity Monitor & Temperature Adjust concurrent -> Flavor Sampling
aging_monitor_po = StrictPartialOrder(nodes=[Humidity_Monitor, Temperature_Adjust])
# No order edges between Humidity Monitor and Temperature Adjust (concurrent)

aging_seq1 = StrictPartialOrder(nodes=[Aging_Control, aging_monitor_po])
aging_seq1.order.add_edge(Aging_Control, aging_monitor_po)

aging_seq2 = StrictPartialOrder(nodes=[aging_seq1, Flavor_Sampling])
aging_seq2.order.add_edge(aging_seq1, Flavor_Sampling)

# Packaging: Eco Packaging -> Brand Labeling
packaging_po = StrictPartialOrder(nodes=[Eco_Packaging, Brand_Labeling])
packaging_po.order.add_edge(Eco_Packaging, Brand_Labeling)

# Distribution step after packaging
distribution_po = Specialty_Shipping

# Marketing: Event Marketing and Customer Feedback concurrent (feedback loops to refinement)
# Model feedback loop as LOOP: execute Event Marketing then choose exit or Customer Feedback then Event Marketing again
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Event_Marketing, Customer_Feedback])

# Quality and compliance checks concurrent with most steps
quality_compliance_po = StrictPartialOrder(nodes=[Quality_Audits, Regulation_Review])
# No edges between Quality_Audits and Regulation_Review (concurrent)

# Assemble main partial order with flows:
# milk_sub_po -> fermentation_curd_po -> Pressing Stage (curd_press_po)
# then aging subsequence (aging_seq2)
# then packaging (packaging_po)
# then distribution (Specialty_Shipping)
# marketing feedback loop concurrent after distribution
# quality_compliance_po concurrent with (overall process steps) we add edges to model concurrency without strict ordering

# Define main linear sequence nodes
main_seq_nodes = [
    milk_sub_po,
    curd_press_po,
    aging_seq2,
    packaging_po,
    distribution_po
]

# Build the main sequence partial order
main_seq_po = StrictPartialOrder(nodes=main_seq_nodes)
main_seq_po.order.add_edge(milk_sub_po, curd_press_po)
main_seq_po.order.add_edge(curd_press_po, aging_seq2)
main_seq_po.order.add_edge(aging_seq2, packaging_po)
main_seq_po.order.add_edge(packaging_po, distribution_po)

# Now compose root PO with:
# - main_seq_po
# - feedback_loop (marketing and feedback)
# - quality_compliance_po (quality and compliance)
# Feedback loop and quality_compliance_po run concurrently after distribution

root = StrictPartialOrder(nodes=[main_seq_po, feedback_loop, quality_compliance_po])
root.order.add_edge(main_seq_po, feedback_loop)
root.order.add_edge(main_seq_po, quality_compliance_po)