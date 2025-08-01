# Generated from: 26daf4f0-0673-4613-8683-5f71651a640e.json
# Description: This process outlines the complex and atypical supply chain management for sourcing, cultivating, and distributing specialized microbial cultures used in biotechnological applications. It involves initial strain identification from diverse environments, genetic optimization, controlled fermentation scaling, quality assurance through multi-stage bioassays, cryopreservation logistics, and regulatory compliance for international bio-material shipments. The process integrates real-time environmental monitoring, adaptive resource allocation based on microbial growth kinetics, and custom packaging solutions to maintain viability. Additionally, it incorporates feedback loops for strain performance data collected from end-users to inform continuous improvement and innovation in microbial product offerings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Strain_Sourcing = Transition(label='Strain Sourcing')
Genetic_Editing = Transition(label='Genetic Editing')
Culture_Initiation = Transition(label='Culture Initiation')
Growth_Monitoring = Transition(label='Growth Monitoring')
Fermentation_Scale = Transition(label='Fermentation Scale')
Bioassay_Testing = Transition(label='Bioassay Testing')
Viability_Check = Transition(label='Viability Check')
Cryo_Packaging = Transition(label='Cryo Packaging')
Cold_Chain = Transition(label='Cold Chain')
Regulatory_Review = Transition(label='Regulatory Review')
Custom_Labeling = Transition(label='Custom Labeling')
Shipment_Booking = Transition(label='Shipment Booking')
Environmental_Scan = Transition(label='Environmental Scan')
Data_Feedback = Transition(label='Data Feedback')
Resource_Adjust = Transition(label='Resource Adjust')
Performance_Audit = Transition(label='Performance Audit')

skip = SilentTransition()

# Build the loop for feedback of strain performance data
# Loop node: first child = Data Feedback (feedback activity),
# second child = Performance Audit --> Resource Adjust --> Growth Monitoring
# After monitoring, cycle back via loop

# Define the sequence inside the loop's B branch (Performance Audit -> Resource Adjust -> Growth Monitoring)
loop_B_PO = StrictPartialOrder(nodes=[Performance_Audit, Resource_Adjust, Growth_Monitoring])
loop_B_PO.order.add_edge(Performance_Audit, Resource_Adjust)
loop_B_PO.order.add_edge(Resource_Adjust, Growth_Monitoring)

loop = OperatorPOWL(operator=Operator.LOOP, children=[Data_Feedback, loop_B_PO])

# Partial order for the main process steps before the loop, and after the loop

# Controlled fermentation scaling follows growth monitoring in the loop branch,
# so we build the rest after Growth Monitoring (which is included in the loop)

# Chain for initial sourcing & genetic optimization
initial_PO = StrictPartialOrder(nodes=[Strain_Sourcing, Genetic_Editing, Culture_Initiation])
initial_PO.order.add_edge(Strain_Sourcing, Genetic_Editing)
initial_PO.order.add_edge(Genetic_Editing, Culture_Initiation)

# From Culture Initiation to Environmental Scan (real-time monitoring)
# Environmental Scan can run concurrently with loop (which includes Growth Monitoring)
env_scan_and_loop = StrictPartialOrder(nodes=[Environmental_Scan, loop])
# They start after Culture_Initiation
# So Culture_Initiation --> Environmental_Scan and Culture_Initiation --> loop
env_scan_and_loop.order.add_edge(Environmental_Scan, loop)  # Environmental Scan before loop? No, both start after Culture Initiation, they run concurrent.
# Actually better: partial order without dependency between Environmental Scan and loop (concurrent)
# Add edges: Culture_Initiation --> Environmental Scan, Culture_Initiation --> loop root node
env_scan_and_loop = StrictPartialOrder(nodes=[Environmental_Scan, loop])

# We'll join initial_PO and env_scan_and_loop with start edges from Culture_Initiation
# So Culture_Initiation --> Environmental_Scan
# Culture_Initiation --> loop
# To do this we put all nodes in a big PartialOrder

# Build the chain after Growth Monitoring (which is inside the loop B branch),
# The loop restarts Growth Monitoring, so after loop completes, proceed with:

# Fermentation Scale -> Bioassay Testing -> Viability Check -> Cryo Packaging -> Cold Chain
# -> Regulatory Review -> Custom Labeling -> Shipment Booking

post_loop_PO = StrictPartialOrder(nodes=[
    Fermentation_Scale,
    Bioassay_Testing,
    Viability_Check,
    Cryo_Packaging,
    Cold_Chain,
    Regulatory_Review,
    Custom_Labeling,
    Shipment_Booking,
])

post_loop_PO.order.add_edge(Fermentation_Scale, Bioassay_Testing)
post_loop_PO.order.add_edge(Bioassay_Testing, Viability_Check)
post_loop_PO.order.add_edge(Viability_Check, Cryo_Packaging)
post_loop_PO.order.add_edge(Cryo_Packaging, Cold_Chain)
post_loop_PO.order.add_edge(Cold_Chain, Regulatory_Review)
post_loop_PO.order.add_edge(Regulatory_Review, Custom_Labeling)
post_loop_PO.order.add_edge(Custom_Labeling, Shipment_Booking)

# Assemble everything into one big PO

root = StrictPartialOrder(
    nodes=[
        # initial chain activities
        Strain_Sourcing,
        Genetic_Editing,
        Culture_Initiation,
        # concurrent Environmental Scan and loop
        Environmental_Scan,
        loop,
        # post loop chain
        Fermentation_Scale,
        Bioassay_Testing,
        Viability_Check,
        Cryo_Packaging,
        Cold_Chain,
        Regulatory_Review,
        Custom_Labeling,
        Shipment_Booking,
    ]
)

# initial ordering: Strain_Sourcing -> Genetic_Editing -> Culture_Initiation
root.order.add_edge(Strain_Sourcing, Genetic_Editing)
root.order.add_edge(Genetic_Editing, Culture_Initiation)

# Culture_Initiation -> Environmental_Scan and Culture_Initiation -> loop (concurrent start)
root.order.add_edge(Culture_Initiation, Environmental_Scan)
root.order.add_edge(Culture_Initiation, loop)

# loop ends before post_loop_PO starts at Fermentation_Scale
root.order.add_edge(loop, Fermentation_Scale)

# Add post loop order edges
root.order.add_edge(Fermentation_Scale, Bioassay_Testing)
root.order.add_edge(Bioassay_Testing, Viability_Check)
root.order.add_edge(Viability_Check, Cryo_Packaging)
root.order.add_edge(Cryo_Packaging, Cold_Chain)
root.order.add_edge(Cold_Chain, Regulatory_Review)
root.order.add_edge(Regulatory_Review, Custom_Labeling)
root.order.add_edge(Custom_Labeling, Shipment_Booking)