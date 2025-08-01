# Generated from: 7f94bf10-9334-463e-b495-ab492a8e095a.json
# Description: This process manages the entire lifecycle of an urban vertical farm, integrating advanced hydroponics, automated environmental controls, and real-time data analytics to optimize crop yield within confined city spaces. It begins with site analysis and design customization, proceeds through seed selection and nutrient calibration, followed by growth monitoring using AI-driven sensors. The process includes pest management via biological controls, energy consumption optimization, and waste recycling. Harvesting is synchronized with distribution logistics to ensure freshness, and feedback loops from consumer data help refine subsequent cycles, making the system adaptive and sustainable in complex urban ecosystems.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
Site_Analysis    = Transition(label='Site Analysis')
Design_Layout    = Transition(label='Design Layout')
Seed_Selection   = Transition(label='Seed Selection')
Nutrient_Mix     = Transition(label='Nutrient Mix')
System_Setup     = Transition(label='System Setup')
Planting_Seeds   = Transition(label='Planting Seeds')
Growth_Monitor   = Transition(label='Growth Monitor')
Pest_Control     = Transition(label='Pest Control')
Climate_Adjust   = Transition(label='Climate Adjust')
Water_Recycling  = Transition(label='Water Recycling')
Energy_Audit     = Transition(label='Energy Audit')
Harvest_Plan     = Transition(label='Harvest Plan')
Quality_Check    = Transition(label='Quality Check')
Pack_Produce     = Transition(label='Pack Produce')
Distribute_Goods = Transition(label='Distribute Goods')
Data_Feedback    = Transition(label='Data Feedback')

# Build the core production cycle as a strict partial order
cycle = StrictPartialOrder(nodes=[
    Seed_Selection, Nutrient_Mix, System_Setup,
    Planting_Seeds, Growth_Monitor, Pest_Control,
    Climate_Adjust, Water_Recycling, Energy_Audit,
    Harvest_Plan, Quality_Check, Pack_Produce,
    Distribute_Goods
])
cycle.order.add_edge(Seed_Selection,   Nutrient_Mix)
cycle.order.add_edge(Nutrient_Mix,     System_Setup)
cycle.order.add_edge(System_Setup,     Planting_Seeds)
cycle.order.add_edge(Planting_Seeds,   Growth_Monitor)
cycle.order.add_edge(Growth_Monitor,   Pest_Control)
cycle.order.add_edge(Pest_Control,     Climate_Adjust)
cycle.order.add_edge(Climate_Adjust,   Water_Recycling)
cycle.order.add_edge(Water_Recycling,  Energy_Audit)
cycle.order.add_edge(Energy_Audit,     Harvest_Plan)
cycle.order.add_edge(Harvest_Plan,     Quality_Check)
cycle.order.add_edge(Quality_Check,    Pack_Produce)
cycle.order.add_edge(Pack_Produce,     Distribute_Goods)

# Wrap the cycle in a LOOP with Data Feedback feeding back into the next iteration
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cycle, Data_Feedback]
)

# Top‐level workflow: site analysis → design layout → looped production cycle
root = StrictPartialOrder(nodes=[Site_Analysis, Design_Layout, loop])
root.order.add_edge(Site_Analysis, Design_Layout)
root.order.add_edge(Design_Layout, loop)