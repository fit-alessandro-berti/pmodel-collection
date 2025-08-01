# Generated from: 0ddef569-63db-4f3b-92fe-11e57a1988b3.json
# Description: This process governs the end-to-end supply chain for specialized microbial cultures used in biotechnological research and pharmaceutical production. It begins with strain acquisition, followed by genetic verification, controlled cultivation, contamination monitoring, biomass harvesting, preservation through lyophilization, packaging under sterile conditions, cold chain logistics coordination, quality validation at multiple checkpoints, inventory management with real-time tracking, regulatory documentation compliance, customer-specific formulation adjustments, and finally, delivery with post-dispatch support for culture revival and viability confirmation. The process integrates scientific rigor with logistical precision to ensure live cultures arrive viable and uncontaminated at research or production facilities worldwide.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition, OperatorPOWL
from pm4py.objects.process_tree.obj import Operator

# Define activities
Strain_Acquire = Transition(label='Strain Acquire')
Genetic_Verify = Transition(label='Genetic Verify')
Culture_Initiate = Transition(label='Culture Initiate')
Growth_Monitor = Transition(label='Growth Monitor')
Contam_Check = Transition(label='Contam Check')
Biomass_Harvest = Transition(label='Biomass Harvest')
Lyophilize_Sample = Transition(label='Lyophilize Sample')
Sterile_Package = Transition(label='Sterile Package')
Cold_Chain = Transition(label='Cold Chain')
Quality_Validate = Transition(label='Quality Validate')
Inventory_Track = Transition(label='Inventory Track')
Regulatory_Review = Transition(label='Regulatory Review')
Formulation_Adjust = Transition(label='Formulation Adjust')
Dispatch_Prepare = Transition(label='Dispatch Prepare')
Client_Support = Transition(label='Client Support')

# Build partial order sequentially according to description

# First sequence: Strain Acquire --> Genetic Verify --> Culture Initiate
seq1 = StrictPartialOrder(nodes=[Strain_Acquire, Genetic_Verify, Culture_Initiate])
seq1.order.add_edge(Strain_Acquire, Genetic_Verify)
seq1.order.add_edge(Genetic_Verify, Culture_Initiate)

# Second part: Growth Monitor and Contam Check run in parallel after Culture Initiate
# So include these nodes with partial order Culture_Initiate --> Growth Monitor and Culture_Initiate --> Contam Check

# Create partial order for these three nodes (Culture_Initiate, Growth_Monitor, Contam_Check)
seq2 = StrictPartialOrder(nodes=[Culture_Initiate, Growth_Monitor, Contam_Check])
seq2.order.add_edge(Culture_Initiate, Growth_Monitor)
seq2.order.add_edge(Culture_Initiate, Contam_Check)

# Third step after both Growth Monitor and Contam Check: Biomass Harvest
# So Biomass Harvest depends on both Growth Monitor and Contam Check
# Build partial order including these four nodes: Growth Monitor, Contam Check, Biomass Harvest
# with edges Growth Monitor --> Biomass Harvest, Contam Check --> Biomass Harvest

seq3 = StrictPartialOrder(nodes=[Growth_Monitor, Contam_Check, Biomass_Harvest])
seq3.order.add_edge(Growth_Monitor, Biomass_Harvest)
seq3.order.add_edge(Contam_Check, Biomass_Harvest)

# Fourth: after Biomass Harvest -> Lyophilize Sample -> Sterile Package -> Cold Chain
seq4 = StrictPartialOrder(nodes=[Biomass_Harvest, Lyophilize_Sample, Sterile_Package, Cold_Chain])
seq4.order.add_edge(Biomass_Harvest, Lyophilize_Sample)
seq4.order.add_edge(Lyophilize_Sample, Sterile_Package)
seq4.order.add_edge(Sterile_Package, Cold_Chain)

# Fifth: parallel activities after Cold Chain: Quality Validate and Inventory Track run concurrently
# Both depend on Cold Chain
seq5 = StrictPartialOrder(nodes=[Cold_Chain, Quality_Validate, Inventory_Track])
seq5.order.add_edge(Cold_Chain, Quality_Validate)
seq5.order.add_edge(Cold_Chain, Inventory_Track)

# Sixth: after these two, Regulatory Review
seq6 = StrictPartialOrder(nodes=[Quality_Validate, Inventory_Track, Regulatory_Review])
seq6.order.add_edge(Quality_Validate, Regulatory_Review)
seq6.order.add_edge(Inventory_Track, Regulatory_Review)

# Seventh: Formulation Adjust after Regulatory Review
seq7 = StrictPartialOrder(nodes=[Regulatory_Review, Formulation_Adjust])
seq7.order.add_edge(Regulatory_Review, Formulation_Adjust)

# Eighth: Dispatch Prepare after Formulation Adjust
seq8 = StrictPartialOrder(nodes=[Formulation_Adjust, Dispatch_Prepare])
seq8.order.add_edge(Formulation_Adjust, Dispatch_Prepare)

# Finally: Client Support after Dispatch Prepare
seq9 = StrictPartialOrder(nodes=[Dispatch_Prepare, Client_Support])
seq9.order.add_edge(Dispatch_Prepare, Client_Support)

# Combine all sequences into one bigger partial order including all nodes:
# Note some nodes appear repeatedly in above partial orders - to build overall model, create a StrictPartialOrder with all nodes
# Then add edges between all dependencies collected above

all_nodes = [
    Strain_Acquire,
    Genetic_Verify,
    Culture_Initiate,
    Growth_Monitor,
    Contam_Check,
    Biomass_Harvest,
    Lyophilize_Sample,
    Sterile_Package,
    Cold_Chain,
    Quality_Validate,
    Inventory_Track,
    Regulatory_Review,
    Formulation_Adjust,
    Dispatch_Prepare,
    Client_Support,
]

root = StrictPartialOrder(nodes=all_nodes)

# Add all edges gathered above:

# seq1 edges
root.order.add_edge(Strain_Acquire, Genetic_Verify)
root.order.add_edge(Genetic_Verify, Culture_Initiate)

# seq2 edges
root.order.add_edge(Culture_Initiate, Growth_Monitor)
root.order.add_edge(Culture_Initiate, Contam_Check)

# seq3 edges
root.order.add_edge(Growth_Monitor, Biomass_Harvest)
root.order.add_edge(Contam_Check, Biomass_Harvest)

# seq4 edges
root.order.add_edge(Biomass_Harvest, Lyophilize_Sample)
root.order.add_edge(Lyophilize_Sample, Sterile_Package)
root.order.add_edge(Sterile_Package, Cold_Chain)

# seq5 edges
root.order.add_edge(Cold_Chain, Quality_Validate)
root.order.add_edge(Cold_Chain, Inventory_Track)

# seq6 edges
root.order.add_edge(Quality_Validate, Regulatory_Review)
root.order.add_edge(Inventory_Track, Regulatory_Review)

# seq7 edge
root.order.add_edge(Regulatory_Review, Formulation_Adjust)

# seq8 edge
root.order.add_edge(Formulation_Adjust, Dispatch_Prepare)

# seq9 edge
root.order.add_edge(Dispatch_Prepare, Client_Support)