# Generated from: 2fed960d-dbd4-4e80-be8b-f9ffae0e0aa7.json
# Description: This process outlines the complex steps involved in establishing an urban beekeeping operation on a city rooftop. It covers site assessment, regulatory compliance, hive installation, bee colony acquisition, ongoing health monitoring, honey extraction, and community engagement activities. The process requires coordination with local authorities for permits, environmental impact evaluations, and integration with urban agriculture initiatives. It also involves managing seasonal changes, pest control without harmful chemicals, and educating neighbors about bee safety. Ultimately, the process aims to create a sustainable, productive beekeeping environment that supports pollination and local biodiversity while producing quality honey products.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Site_Survey = Transition(label='Site Survey')
Permit_Check = Transition(label='Permit Check')
Risk_Assess = Transition(label='Risk Assess')
Hive_Design = Transition(label='Hive Design')
Material_Procure = Transition(label='Material Procure')
Rooftop_Prep = Transition(label='Rooftop Prep')
Hive_Install = Transition(label='Hive Install')
Colony_Order = Transition(label='Colony Order')
Bee_Release = Transition(label='Bee Release')
Health_Monitor = Transition(label='Health Monitor')
Pest_Control = Transition(label='Pest Control')
Honey_Harvest = Transition(label='Honey Harvest')
Wax_Clean = Transition(label='Wax Clean')
Community_Meet = Transition(label='Community Meet')
Seasonal_Adjust = Transition(label='Seasonal Adjust')
Data_Record = Transition(label='Data Record')
Education_Plan = Transition(label='Education Plan')

skip = SilentTransition()

# Part 1: Initial assessments & permits in partial order with concurrency where possible
initial_PO = StrictPartialOrder(nodes=[Site_Survey, Permit_Check, Risk_Assess])
initial_PO.order.add_edge(Site_Survey, Permit_Check)   # Survey before permit check
initial_PO.order.add_edge(Site_Survey, Risk_Assess)    # Survey before risk assess

# Part 2: Hive design and materials
design_PO = StrictPartialOrder(nodes=[Hive_Design, Material_Procure])
design_PO.order.add_edge(Hive_Design, Material_Procure)  # design before procuring materials

# Part 3: Rooftop prep + Hive install
install_PO = StrictPartialOrder(nodes=[Rooftop_Prep, Hive_Install])
install_PO.order.add_edge(Rooftop_Prep, Hive_Install)    # prep before install

# Part 4: Acquire colony and release bees (sequential)
colony_PO = StrictPartialOrder(nodes=[Colony_Order, Bee_Release])
colony_PO.order.add_edge(Colony_Order, Bee_Release)

# Part 5: Maintenance loop: Health monitor -> Pest control (no harmful chemicals) -> Seasonal adjust -> Data record
# Loop structure, looping over health monitoring and pest control with seasonal adjustments

maintenance_loop_body = StrictPartialOrder(nodes=[Health_Monitor, Pest_Control, Seasonal_Adjust, Data_Record])
maintenance_loop_body.order.add_edge(Health_Monitor, Pest_Control)
maintenance_loop_body.order.add_edge(Pest_Control, Seasonal_Adjust)
maintenance_loop_body.order.add_edge(Seasonal_Adjust, Data_Record)

loop_maintenance = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_loop_body, skip])

# Part 6: Honey harvest & wax clean sequential
harvest_PO = StrictPartialOrder(nodes=[Honey_Harvest, Wax_Clean])
harvest_PO.order.add_edge(Honey_Harvest, Wax_Clean)

# Part 7: Community engagement: community meet & education plan concurrent
community_PO = StrictPartialOrder(nodes=[Community_Meet, Education_Plan])

# Now, build the main flow with partial orders and edges to define order:

# Top-level partial order nodes:
# initial_PO -> design_PO -> install_PO -> colony_PO -> loop_maintenance -> harvest_PO -> community_PO

# We'll combine all partial orders and operators into one StrictPartialOrder, connecting them accordingly

root = StrictPartialOrder(
    nodes=[initial_PO, design_PO, install_PO, colony_PO, loop_maintenance, harvest_PO, community_PO]
)
root.order.add_edge(initial_PO, design_PO)
root.order.add_edge(design_PO, install_PO)
root.order.add_edge(install_PO, colony_PO)
root.order.add_edge(colony_PO, loop_maintenance)
root.order.add_edge(loop_maintenance, harvest_PO)
root.order.add_edge(harvest_PO, community_PO)