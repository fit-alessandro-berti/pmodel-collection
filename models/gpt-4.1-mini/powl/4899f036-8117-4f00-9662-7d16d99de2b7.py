# Generated from: 4899f036-8117-4f00-9662-7d16d99de2b7.json
# Description: This process details the complex orchestration required to establish a sustainable urban rooftop farm in a densely populated city. It involves evaluating structural integrity, securing permits, sourcing organic soil and seeds, designing efficient irrigation systems, integrating renewable energy solutions, coordinating with local suppliers, managing seasonal crop rotation, and implementing pest control without chemicals. Continuous monitoring of plant health and environmental data is essential. Additionally, the process requires community engagement initiatives and educational workshops to promote urban agriculture awareness and participation. The entire workflow balances regulatory compliance, environmental sustainability, and economic viability, ensuring the rooftop farm thrives as a model of urban green innovation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Load_Testing = Transition(label='Load Testing')
Permit_Filing = Transition(label='Permit Filing')
Soil_Sourcing = Transition(label='Soil Sourcing')
Seed_Selection = Transition(label='Seed Selection')
Irrigation_Plan = Transition(label='Irrigation Plan')
Energy_Setup = Transition(label='Energy Setup')
Supplier_Vetting = Transition(label='Supplier Vetting')
Crop_Rotation = Transition(label='Crop Rotation')
Pest_Control = Transition(label='Pest Control')
Health_Monitor = Transition(label='Health Monitor')
Data_Logging = Transition(label='Data Logging')
Community_Meet = Transition(label='Community Meet')
Workshop_Plan = Transition(label='Workshop Plan')
Compliance_Check = Transition(label='Compliance Check')
Harvest_Prep = Transition(label='Harvest Prep')
Waste_Manage = Transition(label='Waste Manage')

# Define partial orders and choices reflecting the process description.

# Phase 1: Structural and regulatory checks
structure_PO = StrictPartialOrder(nodes=[Site_Survey, Load_Testing, Permit_Filing])
structure_PO.order.add_edge(Site_Survey, Load_Testing)
structure_PO.order.add_edge(Load_Testing, Permit_Filing)

# Phase 2: Materials sourcing, can happen in partial order: soil and seed sourcing can be concurrent after permit filing
soil_seed_PO = StrictPartialOrder(nodes=[Soil_Sourcing, Seed_Selection])
# no order edges here, concurrent

# Phase 3: Design and supply preparation can start after permit filing and sourcing
design_PO = StrictPartialOrder(nodes=[Irrigation_Plan, Energy_Setup, Supplier_Vetting])
# irrigation plan and energy setup are design activities, supplier vetting separate but concurrent
# all start after permit filing and sourcing (enforced at root level by order edges)

# Phase 4: Crop management loop - Crop Rotation and Pest Control looped
crop_loop = OperatorPOWL(operator=Operator.LOOP, children=[Crop_Rotation, Pest_Control])

# Phase 5: Monitoring and data logging run concurrently after crop management starts
monitoring_PO = StrictPartialOrder(nodes=[Health_Monitor, Data_Logging])
# no order edges, concurrent

# Phase 6: Community engagement: meet and workshops concurrent
community_PO = StrictPartialOrder(nodes=[Community_Meet, Workshop_Plan])

# Phase 7: Compliance check before harvest prep and waste management
pre_harvest_PO = StrictPartialOrder(nodes=[Compliance_Check, Harvest_Prep, Waste_Manage])
pre_harvest_PO.order.add_edge(Compliance_Check, Harvest_Prep)
pre_harvest_PO.order.add_edge(Compliance_Check, Waste_Manage)

# Build the root model by integrating the phases with partial order edges representing dependencies

root = StrictPartialOrder(
    nodes=[
        structure_PO,
        soil_seed_PO,
        design_PO,
        crop_loop,
        monitoring_PO,
        community_PO,
        pre_harvest_PO
    ]
)

# Add cross-partial order edges to reflect global order dependencies:

# Permit Filing must complete before Soil/Seed sourcing & design
root.order.add_edge(structure_PO, soil_seed_PO)
root.order.add_edge(structure_PO, design_PO)

# Soil and seed sourcing must complete before design starts (to represent dependency)
root.order.add_edge(soil_seed_PO, design_PO)

# Design must complete before crop rotation loop starts
root.order.add_edge(design_PO, crop_loop)

# Crop rotation loop before monitoring can effectively run (monitoring runs alongside crop rotation)
# According to description continuous monitoring is essential - can be concurrent or after crop_loop start
# We'll allow monitoring to happen concurrently with crop_loop by letting monitoring start after crop_loop starts
root.order.add_edge(crop_loop, monitoring_PO)

# Community engagement can happen after crop loop (crop growth ongoing) and monitoring start
root.order.add_edge(crop_loop, community_PO)
root.order.add_edge(monitoring_PO, community_PO)  # community after monitoring start

# Pre-harvest activities after crop rotation loop and community engagement
root.order.add_edge(crop_loop, pre_harvest_PO)
root.order.add_edge(community_PO, pre_harvest_PO)

# That's the entire complex process modeled
