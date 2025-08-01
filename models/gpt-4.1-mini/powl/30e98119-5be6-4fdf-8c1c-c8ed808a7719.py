# Generated from: 30e98119-5be6-4fdf-8c1c-c8ed808a7719.json
# Description: This process involves establishing a sustainable urban beekeeping operation within a metropolitan area. It begins with site scouting to identify suitable rooftop or community garden locations, followed by local regulation assessment to ensure compliance with city ordinances. Next, hive selection and acquisition are conducted, choosing appropriate hive designs for urban environments. Installation requires careful placement and securing of hives, considering environmental factors and accessibility. Regular hive inspections and health monitoring are performed to detect pests or diseases early. Pollination tracking is integrated by mapping nearby flora and bee activity patterns. Honey extraction employs specialized urban-friendly equipment and methods to minimize disturbance. Packaging and labeling comply with local food safety standards. Community engagement includes educational workshops and collaboration with local farmers for crop pollination enhancement. Finally, waste management and equipment sterilization ensure sustainability and hive longevity in the urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Scouting = Transition(label='Site Scouting')
Regulation_Check = Transition(label='Regulation Check')
Hive_Selection = Transition(label='Hive Selection')
Hive_Purchase = Transition(label='Hive Purchase')
Hive_Installation = Transition(label='Hive Installation')
Health_Inspection = Transition(label='Health Inspection')
Pest_Control = Transition(label='Pest Control')
Flora_Mapping = Transition(label='Flora Mapping')
Pollination_Track = Transition(label='Pollination Track')
Honey_Extraction = Transition(label='Honey Extraction')
Honey_Packaging = Transition(label='Honey Packaging')
Label_Compliance = Transition(label='Label Compliance')
Community_Workshop = Transition(label='Community Workshop')
Farmer_Liaison = Transition(label='Farmer Liaison')
Waste_Disposal = Transition(label='Waste Disposal')
Equipment_Clean = Transition(label='Equipment Clean')

# Health Inspection loop: Health Inspection followed by choice to either exit or Pest Control then back to Health Inspection
health_loop = OperatorPOWL(operator=Operator.LOOP, children=[Health_Inspection, Pest_Control])

# Pollination tracking activities together as partial order (concurrent Flora Mapping and Pollination Track)
pollination_PO = StrictPartialOrder(nodes=[Flora_Mapping, Pollination_Track])

# Community engagement partial order: Community Workshop and Farmer Liaison concurrently
community_PO = StrictPartialOrder(nodes=[Community_Workshop, Farmer_Liaison])

# Honey packaging and label compliance partial order: they are sequential, so connect
honey_packaging_PO = StrictPartialOrder(nodes=[Honey_Packaging, Label_Compliance])
honey_packaging_PO.order.add_edge(Honey_Packaging, Label_Compliance)

# Waste disposal and equipment cleaning partial order: they are sequential, so connect
waste_PO = StrictPartialOrder(nodes=[Waste_Disposal, Equipment_Clean])
waste_PO.order.add_edge(Waste_Disposal, Equipment_Clean)

# Installation requires careful placement and securing, considered single activity Hive_Installation

# Define the full process partial order:

# First sequence: Site Scouting --> Regulation Check --> Hive Selection --> Hive Purchase --> Hive Installation
initial_PO = StrictPartialOrder(nodes=[Site_Scouting, Regulation_Check, Hive_Selection, Hive_Purchase, Hive_Installation])
initial_PO.order.add_edge(Site_Scouting, Regulation_Check)
initial_PO.order.add_edge(Regulation_Check, Hive_Selection)
initial_PO.order.add_edge(Hive_Selection, Hive_Purchase)
initial_PO.order.add_edge(Hive_Purchase, Hive_Installation)

# Next: After installation, we have the health loop (Health Inspection and Pest Control)
# Then the pollination activities (Flora Mapping and Pollination Track)
# Then honey extraction --> honey packaging and labeling (sequential)
# Then community engagement (Community Workshop and Farmer Liaison concurrently)
# Finally waste disposal and equipment cleaning (sequential)

# Compose the latter part partial order nodes:
# Combine health_loop, pollination_PO, Honey_Extraction, honey_packaging_PO, community_PO, waste_PO
latter_nodes = [
    health_loop,
    pollination_PO,
    Honey_Extraction,
    honey_packaging_PO,
    community_PO,
    waste_PO,
]

latter_PO = StrictPartialOrder(nodes=latter_nodes)

# Add order edges for the latter part:
# health_loop --> pollination_PO --> Honey_Extraction --> honey_packaging_PO --> community_PO --> waste_PO

latter_PO.order.add_edge(health_loop, pollination_PO)
latter_PO.order.add_edge(pollination_PO, Honey_Extraction)
latter_PO.order.add_edge(Honey_Extraction, honey_packaging_PO)
latter_PO.order.add_edge(honey_packaging_PO, community_PO)
latter_PO.order.add_edge(community_PO, waste_PO)

# Now combine initial_PO and latter_PO into final root PO
root = StrictPartialOrder(nodes=[initial_PO, latter_PO])

# The order edges:
# initial_PO --> latter_PO (meaning Hive Installation --> health_loop)
# To be precise Hive Installation is last in initial_PO, health_loop is first in latter_PO's nodes
root.order.add_edge(initial_PO, latter_PO)

# Note: To link Hive Installation to health_loop explicitly to ensure logical flow,
# we add edge Hive_Installation --> health_loop
# This is done by adding edge inside combined PO, which contains both initial_PO and latter_PO
# But initial_PO and latter_PO themselves are StrictPartialOrder objects (nodes),
# so edges between these nodes represent order between sub-processes.

# Everything is modeled as described.
