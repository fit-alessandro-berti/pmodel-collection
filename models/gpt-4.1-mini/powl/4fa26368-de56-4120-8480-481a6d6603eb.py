# Generated from: 4fa26368-de56-4120-8480-481a6d6603eb.json
# Description: This process involves the intricate steps required to produce, certify, package, and export artisanal cheese from a local farm to international gourmet markets. It begins with careful milk selection and fermentation, followed by quality inspections and aging under controlled conditions. After maturation, the cheese undergoes sensory evaluation and microbiological testing to comply with export regulations. Packaging is done using eco-friendly materials, accompanied by detailed labeling that meets destination country standards. Logistics coordination ensures timely shipment while maintaining cold chain integrity. Finally, customs clearance and distributor onboarding complete the process, enabling the cheese to reach connoisseurs worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
Milk_Selection = Transition(label='Milk Selection')
Fermentation_Start = Transition(label='Fermentation Start')
Quality_Check = Transition(label='Quality Check')
Cheese_Aging = Transition(label='Cheese Aging')
Sensory_Test = Transition(label='Sensory Test')
Microbial_Test = Transition(label='Microbial Test')
Certification_Prep = Transition(label='Certification Prep')
Eco_Packaging = Transition(label='Eco Packaging')
Label_Design = Transition(label='Label Design')
Label_Approval = Transition(label='Label Approval')
Cold_Storage = Transition(label='Cold Storage')
Logistics_Plan = Transition(label='Logistics Plan')
Customs_Filing = Transition(label='Customs Filing')
Distributor_Setup = Transition(label='Distributor Setup')
Shipment_Dispatch = Transition(label='Shipment Dispatch')

# Sensory and Microbial tests run concurrently after aging
sens_micro_PO = StrictPartialOrder(nodes=[Sensory_Test, Microbial_Test])
# No order edges between them: concurrent execution

# Label Design and Label Approval in sequence
label_PO = StrictPartialOrder(nodes=[Label_Design, Label_Approval])
label_PO.order.add_edge(Label_Design, Label_Approval)

# Packaging includes Eco Packaging and labeling (the label_PO)
packaging_PO = StrictPartialOrder(nodes=[Eco_Packaging, label_PO])
packaging_PO.order.add_edge(Eco_Packaging, label_PO)

# Logistics coordination includes Cold Storage and Logistics Plan in parallel
logistics_PO = StrictPartialOrder(nodes=[Cold_Storage, Logistics_Plan])
# No order edges: concurrent

# Final export partial order: Customs Filing, Distributor Setup, Shipment Dispatch in sequence
export_PO = StrictPartialOrder(nodes=[Customs_Filing, Distributor_Setup, Shipment_Dispatch])
export_PO.order.add_edge(Customs_Filing, Distributor_Setup)
export_PO.order.add_edge(Distributor_Setup, Shipment_Dispatch)

# Beginning steps partial order: Milk Selection -> Fermentation Start -> Quality Check -> Cheese Aging
begin_PO = StrictPartialOrder(nodes=[Milk_Selection, Fermentation_Start, Quality_Check, Cheese_Aging])
begin_PO.order.add_edge(Milk_Selection, Fermentation_Start)
begin_PO.order.add_edge(Fermentation_Start, Quality_Check)
begin_PO.order.add_edge(Quality_Check, Cheese_Aging)

# After Cheese Aging, Sensory and Microbial tests run concurrently
# Then Certification Prep
# Then Packaging (Eco Packaging and labeling)
# Then Logistics (Cold Storage and Logistics Plan concurrent)
# Then Export (Customs Filing, Distributor Setup, Shipment Dispatch)

# Create main PO with all steps and their ordering dependencies
root = StrictPartialOrder(
    nodes=[
        begin_PO,                 # first phase
        sens_micro_PO,            # tests concurrent
        Certification_Prep,       # single activity
        packaging_PO,             # packaging + labeling
        logistics_PO,             # logistics concurrent
        export_PO                 # final export
    ]
)

# Add order edges to chain these phases
root.order.add_edge(begin_PO, sens_micro_PO)
root.order.add_edge(sens_micro_PO, Certification_Prep)
root.order.add_edge(Certification_Prep, packaging_PO)
root.order.add_edge(packaging_PO, logistics_PO)
root.order.add_edge(logistics_PO, export_PO)