# Generated from: d03d25d4-2b2a-4c5d-9e33-de54c815b114.json
# Description: This process ensures complete traceability and quality control in the artisanal coffee supply chain, from farm to cup. It involves unique steps like micro-lot identification, sensory profiling, blockchain recording, and dynamic pricing based on real-time market demand and quality metrics. The process also integrates direct farmer feedback, environmental impact assessment, and adaptive roasting schedules to optimize flavor profiles while maintaining sustainability and ethical sourcing. Each batch undergoes rigorous testing and certification before distribution, enabling transparency and consumer trust in a highly competitive specialty coffee market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as labeled transitions
farm_registration = Transition(label='Farm Registration')
lot_tagging = Transition(label='Lot Tagging')
soil_testing = Transition(label='Soil Testing')
harvest_logging = Transition(label='Harvest Logging')
coffee_sorting = Transition(label='Coffee Sorting')
sensory_profiling = Transition(label='Sensory Profiling')
quality_scoring = Transition(label='Quality Scoring')
blockchain_entry = Transition(label='Blockchain Entry')
environmental_audit = Transition(label='Environmental Audit')
farmer_feedback = Transition(label='Farmer Feedback')
dynamic_pricing = Transition(label='Dynamic Pricing')
roast_scheduling = Transition(label='Roast Scheduling')
batch_testing = Transition(label='Batch Testing')
certification_review = Transition(label='Certification Review')
distribution_prep = Transition(label='Distribution Prep')
consumer_feedback = Transition(label='Consumer Feedback')

# Build the partial order according to the described process:

# From farm registration to lot tagging and soil testing (concurrent)
# Then harvest logging after lot tagging and soil testing
# Coffee sorting follows harvest logging
# Then sensory profiling and quality scoring run concurrently after sorting
# Blockchain entry happens after both sensory profiling and quality scoring
# Environmental audit and farmer feedback happen concurrently after blockchain entry
# Dynamic pricing and roast scheduling run concurrently after farmer feedback
# Batch testing follows both environmental audit and roast scheduling (both must finish)
# Certification review follows batch testing
# Distribution preparation follows certification review
# Consumer feedback after distribution prep

root = StrictPartialOrder(nodes=[
    farm_registration,
    lot_tagging,
    soil_testing,
    harvest_logging,
    coffee_sorting,
    sensory_profiling,
    quality_scoring,
    blockchain_entry,
    environmental_audit,
    farmer_feedback,
    dynamic_pricing,
    roast_scheduling,
    batch_testing,
    certification_review,
    distribution_prep,
    consumer_feedback
])

order = root.order
order.add_edge(farm_registration, lot_tagging)
order.add_edge(farm_registration, soil_testing)

order.add_edge(lot_tagging, harvest_logging)
order.add_edge(soil_testing, harvest_logging)

order.add_edge(harvest_logging, coffee_sorting)

order.add_edge(coffee_sorting, sensory_profiling)
order.add_edge(coffee_sorting, quality_scoring)

order.add_edge(sensory_profiling, blockchain_entry)
order.add_edge(quality_scoring, blockchain_entry)

order.add_edge(blockchain_entry, environmental_audit)
order.add_edge(blockchain_entry, farmer_feedback)

order.add_edge(farmer_feedback, dynamic_pricing)
order.add_edge(farmer_feedback, roast_scheduling)

order.add_edge(environmental_audit, batch_testing)
order.add_edge(roast_scheduling, batch_testing)

order.add_edge(batch_testing, certification_review)
order.add_edge(certification_review, distribution_prep)
order.add_edge(distribution_prep, consumer_feedback)