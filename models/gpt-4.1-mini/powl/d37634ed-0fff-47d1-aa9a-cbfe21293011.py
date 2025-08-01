# Generated from: d37634ed-0fff-47d1-aa9a-cbfe21293011.json
# Description: This process governs the end-to-end operations of an urban vertical farm that integrates hydroponic crop production with local distribution and waste recycling. Starting from seed selection, the process includes nutrient solution preparation, environmental monitoring, automated harvesting, quality inspection, packaging, and delivery to local markets. Additionally, it incorporates waste biomass processing for compost generation and energy recovery, ensuring a closed-loop sustainable system. Coordination with city regulations and community engagement programs also plays a vital role in optimizing farm output while minimizing ecological footprint and promoting urban food security.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Seed_Selection = Transition(label='Seed Selection')
Nutrient_Mix = Transition(label='Nutrient Mix')
Environment_Check = Transition(label='Environment Check')
Planting_Setup = Transition(label='Planting Setup')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Control = Transition(label='Pest Control')
Automated_Harvest = Transition(label='Automated Harvest')
Quality_Inspect = Transition(label='Quality Inspect')
Packaging_Prep = Transition(label='Packaging Prep')
Order_Fulfill = Transition(label='Order Fulfill')
Local_Delivery = Transition(label='Local Delivery')
Waste_Collect = Transition(label='Waste Collect')
Biomass_Process = Transition(label='Biomass Process')
Compost_Create = Transition(label='Compost Create')
Energy_Recover = Transition(label='Energy Recover')
Regulation_Review = Transition(label='Regulation Review')
Community_Engage = Transition(label='Community Engage')

# Define the waste processing loop: after Waste Collect, loop between Biomass Process -> (Compost or Energy Recover) -> repeat or exit
# Use XOR to choose between Compost_Create and Energy_Recover
compost_or_energy = OperatorPOWL(operator=Operator.XOR, children=[Compost_Create, Energy_Recover])

# Loop: Waste Collect followed by (Biomass Process then choice compost_or_energy), repeated zero or more times
# Loop structure: *(Waste Collect, Biomass Process then choice then back to Waste Collect or exit)
loop_body = StrictPartialOrder(nodes=[Biomass_Process, compost_or_energy])
loop_body.order.add_edge(Biomass_Process, compost_or_energy)
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[Waste_Collect, loop_body])

# Core production partial order:
# Sequential: Seed Selection -> Nutrient Mix -> Environment Check -> Planting Setup -> (Growth Monitoring and Pest Control concurrent) -> Automated Harvest -> Quality Inspect -> Packaging Prep -> Order Fulfill -> Local Delivery

core_nodes = [
    Seed_Selection,
    Nutrient_Mix,
    Environment_Check,
    Planting_Setup,
    Growth_Monitoring,
    Pest_Control,
    Automated_Harvest,
    Quality_Inspect,
    Packaging_Prep,
    Order_Fulfill,
    Local_Delivery
]

core_po = StrictPartialOrder(nodes=core_nodes)

core_po.order.add_edge(Seed_Selection, Nutrient_Mix)
core_po.order.add_edge(Nutrient_Mix, Environment_Check)
core_po.order.add_edge(Environment_Check, Planting_Setup)
# Growth Monitoring and Pest Control are concurrent, both after Planting Setup
core_po.order.add_edge(Planting_Setup, Growth_Monitoring)
core_po.order.add_edge(Planting_Setup, Pest_Control)
# Both Growth Monitoring and Pest Control must complete before Automated Harvest
core_po.order.add_edge(Growth_Monitoring, Automated_Harvest)
core_po.order.add_edge(Pest_Control, Automated_Harvest)
core_po.order.add_edge(Automated_Harvest, Quality_Inspect)
core_po.order.add_edge(Quality_Inspect, Packaging_Prep)
core_po.order.add_edge(Packaging_Prep, Order_Fulfill)
core_po.order.add_edge(Order_Fulfill, Local_Delivery)

# The coordination activities can be modeled as concurrent activities happening alongside the core production and waste loop
coordination_nodes = [Regulation_Review, Community_Engage]
coordination_po = StrictPartialOrder(nodes=coordination_nodes)
# No order edges, concurrency implied

# Combine core production, waste_loop, and coordination into a top-level partial order
root_nodes = [core_po, waste_loop, coordination_po]

root = StrictPartialOrder(nodes=root_nodes)
# Core production precedes local delivery already inside core_po
# Link core production and waste loop: no explicit temporal dependency, run concurrently
# Link core production and coordination: concurrent with no ordering
# No order edges needed between core_po, waste_loop, and coordination_po to show concurrency

# The model is now:
# root = PO( nodes={core_po, waste_loop, coordination_po}, order={} )
