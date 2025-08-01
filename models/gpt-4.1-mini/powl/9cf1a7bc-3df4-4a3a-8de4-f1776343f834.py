# Generated from: 9cf1a7bc-3df4-4a3a-8de4-f1776343f834.json
# Description: This process outlines the complex supply chain of artisanal cheese production, from sourcing rare milk varieties to aging cheese in controlled environments. It involves selecting heritage breeds, managing microflora cultures, monitoring environmental conditions, coordinating with local farmers, ensuring quality through sensory evaluation, packaging in sustainable materials, handling customs for international export, and managing direct-to-consumer logistics. The process requires intricate coordination between agricultural practices, microbial science, artisan craftsmanship, and niche marketing strategies to ensure the final product maintains its unique flavor profile and meets regulatory standards across different markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Breed_Selection = Transition(label='Breed Selection')
Milk_Harvest = Transition(label='Milk Harvest')
Culture_Prep = Transition(label='Culture Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Whey_Drain = Transition(label='Whey Drain')
Mold_Inoculate = Transition(label='Mold Inoculate')
Press_Cheese = Transition(label='Press Cheese')
Salt_Application = Transition(label='Salt Application')
Cave_Aging = Transition(label='Cave Aging')
Quality_Test = Transition(label='Quality Test')
Packaging_Prep = Transition(label='Packaging Prep')
Label_Design = Transition(label='Label Design')
Customs_Clear = Transition(label='Customs Clear')
Order_Dispatch = Transition(label='Order Dispatch')
Customer_Feedback = Transition(label='Customer Feedback')

# Agriculture and preparation (some concurrency):
# Breed Selection -> Milk Harvest and Culture Prep can run concurrently
# Culture Prep -> Milk Pasteurize -> Curd Formation -> Whey Drain

prep_PO = StrictPartialOrder(nodes=[Breed_Selection, Milk_Harvest, Culture_Prep,
                                    Milk_Pasteurize, Curd_Formation, Whey_Drain])
prep_PO.order.add_edge(Breed_Selection, Milk_Harvest)
prep_PO.order.add_edge(Breed_Selection, Culture_Prep)
prep_PO.order.add_edge(Culture_Prep, Milk_Pasteurize)
prep_PO.order.add_edge(Milk_Pasteurize, Curd_Formation)
prep_PO.order.add_edge(Curd_Formation, Whey_Drain)

# Cheese treatment steps in partial order with some concurrency:
# Mold Inoculate and Press Cheese start after Whey Drain but can be concurrent
# Salt Application after both Mold Inoculate and Press Cheese
treatment_PO = StrictPartialOrder(nodes=[Whey_Drain, Mold_Inoculate, Press_Cheese, Salt_Application])
treatment_PO.order.add_edge(Whey_Drain, Mold_Inoculate)
treatment_PO.order.add_edge(Whey_Drain, Press_Cheese)
treatment_PO.order.add_edge(Mold_Inoculate, Salt_Application)
treatment_PO.order.add_edge(Press_Cheese, Salt_Application)

# Aging and quality check:
# Cave Aging then Quality Test

aging_PO = StrictPartialOrder(nodes=[Salt_Application, Cave_Aging, Quality_Test])
aging_PO.order.add_edge(Salt_Application, Cave_Aging)
aging_PO.order.add_edge(Cave_Aging, Quality_Test)

# Packaging and labeling can be concurrent after Quality Test
packaging_PO = StrictPartialOrder(nodes=[Quality_Test, Packaging_Prep, Label_Design])
packaging_PO.order.add_edge(Quality_Test, Packaging_Prep)
packaging_PO.order.add_edge(Quality_Test, Label_Design)

# Export or direct sales path:
# After packaging and labeling join (we model this with XOR choice):
# Choice between Customs Clear (for international) or Order Dispatch (direct)
# Customer Feedback after both possible paths (join concurrency)

# Join Packaging and Label Design in a PO for concurrency before export/logistics
packaging_and_label_PO = StrictPartialOrder(nodes=[Packaging_Prep, Label_Design])
# packaging_and_label_PO.order is empty, means Packaging_Prep and Label_Design concurrent

# Export logistics
export_PO = StrictPartialOrder(nodes=[Customs_Clear])
# Direct sales logistics
direct_PO = StrictPartialOrder(nodes=[Order_Dispatch])

# Choice between export and direct distribution
distribution_choice = OperatorPOWL(operator=Operator.XOR, children=[export_PO, direct_PO])

# Customer feedback after distribution (join both paths)
post_distribution_PO = StrictPartialOrder(
    nodes=[distribution_choice, Customer_Feedback]
)
post_distribution_PO.order.add_edge(distribution_choice, Customer_Feedback)

# Assemble distribution and packaging:

# packaging_and_label_PO before distribution choice
packaging_to_distribution_PO = StrictPartialOrder(
    nodes=[packaging_and_label_PO, distribution_choice]
)
packaging_to_distribution_PO.order.add_edge(packaging_and_label_PO, distribution_choice)

# Full end section:
end_section_PO = StrictPartialOrder(
    nodes=[packaging_to_distribution_PO, Customer_Feedback]
)
end_section_PO.order.add_edge(packaging_to_distribution_PO, Customer_Feedback)

# Now build full model in correct order:

# Order: prep_PO -> treatment_PO -> aging_PO -> packaging_PO -> distribution_choice -> Customer_Feedback
# To link packaging_PO to packaging_and_label_PO, replace packaging_PO by packaging_and_label_PO since packaging_PO 
# includes Quality_Test from aging_PO; better to connect aging_PO -> packaging_and_label_PO skipping packaging_PO alone

# So connect aging_PO -> packaging_and_label_PO
full_PO = StrictPartialOrder(
    nodes=[prep_PO, treatment_PO, aging_PO, packaging_and_label_PO, distribution_choice, Customer_Feedback]
)
# Linking partial orders linear plus some concurrency inside:
full_PO.order.add_edge(prep_PO, treatment_PO)
full_PO.order.add_edge(treatment_PO, aging_PO)
full_PO.order.add_edge(aging_PO, packaging_and_label_PO)
full_PO.order.add_edge(packaging_and_label_PO, distribution_choice)
full_PO.order.add_edge(distribution_choice, Customer_Feedback)

root = full_PO