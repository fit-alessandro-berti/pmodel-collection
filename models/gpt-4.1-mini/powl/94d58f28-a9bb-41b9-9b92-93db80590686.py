# Generated from: 94d58f28-a9bb-41b9-9b92-93db80590686.json
# Description: This process encompasses the unique steps involved in producing and distributing artisanal cheese from farm to gourmet retailer. It begins with selecting rare milk breeds and monitoring animal diet to influence flavor profiles. The milk undergoes micro-filtering and custom fermentation using wild cultures. Aging occurs in controlled microclimates with periodic turning and humidity adjustments. Quality is assessed through sensory panels and microbial analysis. Packaging utilizes biodegradable materials with embedded QR codes detailing provenance. Finally, logistics involve temperature-monitored transport and boutique delivery, ensuring freshness and traceability throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Breed_Select = Transition(label='Breed Select')
Diet_Monitor = Transition(label='Diet Monitor')
Milk_Harvest = Transition(label='Milk Harvest')
Micro_Filter = Transition(label='Micro Filter')
Wild_Culture = Transition(label='Wild Culture')
Custom_Ferment = Transition(label='Custom Ferment')
Curd_Cut = Transition(label='Curd Cut')
Press_Form = Transition(label='Press Form')
Microclimate_Age = Transition(label='Microclimate Age')
Turn_Cheese = Transition(label='Turn Cheese')
Humidity_Adjust = Transition(label='Humidity Adjust')
Sensory_Panel = Transition(label='Sensory Panel')
Microbial_Test = Transition(label='Microbial Test')
Eco_Package = Transition(label='Eco Package')
QR_Code = Transition(label='QR Code')
Temp_Transport = Transition(label='Temp Transport')
Boutique_Deliver = Transition(label='Boutique Deliver')

# Parallel initial steps: Breed Select and Diet Monitor are concurrent before Milk Harvest
initial_PO = StrictPartialOrder(nodes=[Breed_Select, Diet_Monitor, Milk_Harvest])
initial_PO.order.add_edge(Breed_Select, Milk_Harvest)
initial_PO.order.add_edge(Diet_Monitor, Milk_Harvest)

# Milk processing sequence: Milk Harvest -> Micro Filter -> Custom Fermentation (Wild Culture + Custom Ferment in sequence)
fermentation_PO = StrictPartialOrder(nodes=[Wild_Culture, Custom_Ferment])
fermentation_PO.order.add_edge(Wild_Culture, Custom_Ferment)

processing_PO = StrictPartialOrder(
    nodes=[Micro_Filter, fermentation_PO]
)
processing_PO.order.add_edge(Micro_Filter, fermentation_PO)

milk_process_PO = StrictPartialOrder(
    nodes=[initial_PO, processing_PO]
)
milk_process_PO.order.add_edge(initial_PO, processing_PO)

# Cheese forming: Curd Cut -> Press Form
forming_PO = StrictPartialOrder(nodes=[Curd_Cut, Press_Form])
forming_PO.order.add_edge(Curd_Cut, Press_Form)

# Aging with periodic tasks in parallel: Microclimate Age, Turn Cheese, Humidity Adjust
# Turn Cheese and Humidity Adjust are concurrent and both must happen repeatedly during aging
aging_PO = StrictPartialOrder(nodes=[Microclimate_Age, Turn_Cheese, Humidity_Adjust])
# Microclimate Age happens first, then turning and humidity adjustments can occur concurrently during aging
aging_PO.order.add_edge(Microclimate_Age, Turn_Cheese)
aging_PO.order.add_edge(Microclimate_Age, Humidity_Adjust)

# Quality Assessment: Sensory Panel and Microbial Test concurrent
quality_PO = StrictPartialOrder(nodes=[Sensory_Panel, Microbial_Test])

# Packaging partial order: Eco Package -> QR Code
packaging_PO = StrictPartialOrder(nodes=[Eco_Package, QR_Code])
packaging_PO.order.add_edge(Eco_Package, QR_Code)

# Logistics partial order: Temp Transport -> Boutique Deliver
logistics_PO = StrictPartialOrder(nodes=[Temp_Transport, Boutique_Deliver])
logistics_PO.order.add_edge(Temp_Transport, Boutique_Deliver)

# Put everything in final order:
# milk_process_PO -> forming_PO -> aging_PO -> quality_PO -> packaging_PO -> logistics_PO

root = StrictPartialOrder(
    nodes=[milk_process_PO, forming_PO, aging_PO, quality_PO, packaging_PO, logistics_PO]
)
root.order.add_edge(milk_process_PO, forming_PO)
root.order.add_edge(forming_PO, aging_PO)
root.order.add_edge(aging_PO, quality_PO)
root.order.add_edge(quality_PO, packaging_PO)
root.order.add_edge(packaging_PO, logistics_PO)