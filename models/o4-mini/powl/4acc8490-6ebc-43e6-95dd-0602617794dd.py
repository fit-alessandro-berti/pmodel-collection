# Generated from: 4acc8490-6ebc-43e6-95dd-0602617794dd.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban rooftop farm. It integrates environmental assessments, structural evaluations, community engagement, and regulatory compliance. Starting from site analysis to crop selection, irrigation planning, and installation of renewable energy systems, the process ensures optimized resource use and maximizes yield while fostering urban green spaces. The workflow also includes ongoing monitoring, pest management, and periodic yield assessment to maintain long-term productivity and environmental benefits within a city setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
t_site      = Transition(label='Site Survey')
t_load      = Transition(label='Load Testing')
t_soil      = Transition(label='Soil Sampling')
t_water     = Transition(label='Water Analysis')
t_crop      = Transition(label='Crop Research')
t_energy    = Transition(label='Energy Audit')
t_permit    = Transition(label='Permit Filing')
t_design    = Transition(label='Design Layout')
t_irrig     = Transition(label='Irrigation Setup')
t_solar     = Transition(label='Solar Install')
t_community = Transition(label='Community Meet')
t_supplier  = Transition(label='Supplier Sourcing')
t_plant     = Transition(label='Planting Plan')
t_pest      = Transition(label='Pest Control')
t_yield     = Transition(label='Yield Monitor')
t_waste     = Transition(label='Waste Manage')
t_harvest   = Transition(label='Harvest Schedule')

# Step 2: concurrent structural & environmental assessments
po1 = StrictPartialOrder(nodes=[t_load, t_soil, t_water])
# Step 3: concurrent research, energy audit, permit filing
po2 = StrictPartialOrder(nodes=[t_crop, t_energy, t_permit])
# Step 5: concurrent irrigation & solar installation
po3 = StrictPartialOrder(nodes=[t_irrig, t_solar])
# Step 6: concurrent community engagement & supplier sourcing
po4 = StrictPartialOrder(nodes=[t_community, t_supplier])
# Loop body: ongoing monitoring tasks (concurrent within each iteration)
po_monitor = StrictPartialOrder(nodes=[t_pest, t_yield, t_waste])
# Loop operator: Planting Plan, then zero-or-more iterations of monitoring + re-planting
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[t_plant, po_monitor])

# Assemble the root partial order
root = StrictPartialOrder(
    nodes=[t_site, po1, po2, t_design, po3, po4, loop_monitor, t_harvest]
)

# Define the control-flow dependencies
root.order.add_edge(t_site,      po1)
root.order.add_edge(po1,        po2)
root.order.add_edge(po2,        t_design)
root.order.add_edge(t_design,    po3)
root.order.add_edge(po3,        po4)
root.order.add_edge(po4,        loop_monitor)
root.order.add_edge(loop_monitor, t_harvest)