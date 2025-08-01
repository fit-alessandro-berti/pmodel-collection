# Generated from: 26daf4f0-0673-4613-8683-5f71651a640e.json
# Description: This process outlines the complex and atypical supply chain management for sourcing, cultivating, and distributing specialized microbial cultures used in biotechnological applications. It involves initial strain identification from diverse environments, genetic optimization, controlled fermentation scaling, quality assurance through multi-stage bioassays, cryopreservation logistics, and regulatory compliance for international bio-material shipments. The process integrates real-time environmental monitoring, adaptive resource allocation based on microbial growth kinetics, and custom packaging solutions to maintain viability. Additionally, it incorporates feedback loops for strain performance data collected from end-users to inform continuous improvement and innovation in microbial product offerings.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
strain_sourcing    = Transition(label='Strain Sourcing')
genetic_editing   = Transition(label='Genetic Editing')
culture_initiation = Transition(label='Culture Initiation')
growth_monitoring  = Transition(label='Growth Monitoring')
resource_adjust    = Transition(label='Resource Adjust')
fermentation_scale = Transition(label='Fermentation Scale')
bioassay_testing   = Transition(label='Bioassay Testing')
viability_check    = Transition(label='Viability Check')
cryo_packaging     = Transition(label='Cryo Packaging')
cold_chain         = Transition(label='Cold Chain')
regulatory_review  = Transition(label='Regulatory Review')
custom_labeling    = Transition(label='Custom Labeling')
shipment_booking   = Transition(label='Shipment Booking')
environmental_scan = Transition(label='Environmental Scan')
data_feedback      = Transition(label='Data Feedback')
performance_audit  = Transition(label='Performance Audit')

# Loop for real‐time growth monitoring + adaptive resource adjustment
growth_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitoring, resource_adjust]
)

# The main pipeline from Genetic Editing down to Shipment Booking
inner_pipeline = StrictPartialOrder(nodes=[
    genetic_editing,
    culture_initiation,
    growth_loop,
    fermentation_scale,
    bioassay_testing,
    viability_check,
    cryo_packaging,
    cold_chain,
    regulatory_review,
    custom_labeling,
    shipment_booking
])
inner_pipeline.order.add_edge(genetic_editing,   culture_initiation)
inner_pipeline.order.add_edge(culture_initiation, growth_loop)
inner_pipeline.order.add_edge(growth_loop,        fermentation_scale)
inner_pipeline.order.add_edge(fermentation_scale, bioassay_testing)
inner_pipeline.order.add_edge(bioassay_testing,   viability_check)
inner_pipeline.order.add_edge(viability_check,    cryo_packaging)
inner_pipeline.order.add_edge(cryo_packaging,     cold_chain)
inner_pipeline.order.add_edge(cold_chain,         regulatory_review)
inner_pipeline.order.add_edge(regulatory_review,  custom_labeling)
inner_pipeline.order.add_edge(custom_labeling,    shipment_booking)

# Feedback subprocess: Data Feedback → Performance Audit
feedback_loop = StrictPartialOrder(nodes=[data_feedback, performance_audit])
feedback_loop.order.add_edge(data_feedback, performance_audit)

# Outer loop tying the main pipeline back to Genetic Editing via feedback
outer_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[inner_pipeline, feedback_loop]
)

# Root POWL: start with Strain Sourcing, then the outer loop; 
# Environmental Scan happens concurrently
root = StrictPartialOrder(nodes=[
    strain_sourcing,
    outer_loop,
    environmental_scan
])
root.order.add_edge(strain_sourcing, outer_loop)