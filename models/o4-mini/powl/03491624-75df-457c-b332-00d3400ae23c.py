# Generated from: 03491624-75df-457c-b332-00d3400ae23c.json
# Description: This process involves the intricate steps required to produce, certify, and export artisanal cheese from rural farms to international gourmet markets. It includes raw milk sourcing, traditional fermentation, quality control, packaging with unique branding, regulatory compliance checks for each target country, coordination with logistics partners specializing in perishable goods, managing customs documentation, and ensuring cold chain integrity throughout transit. The process also involves market feedback collection post-delivery to adjust production and marketing strategies for different regions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing      = Transition(label='Milk Sourcing')
fermentation_start = Transition(label='Fermentation Start')
curd_cutting       = Transition(label='Curd Cutting')
molding_cheese     = Transition(label='Molding Cheese')
salt_application   = Transition(label='Salt Application')
aging_check        = Transition(label='Aging Check')
quality_testing    = Transition(label='Quality Testing')
packaging_design   = Transition(label='Packaging Design')
label_printing     = Transition(label='Label Printing')
certify_origin     = Transition(label='Certify Origin')
customs_filing     = Transition(label='Customs Filing')
cold_chain         = Transition(label='Cold Chain')
logistics_booking  = Transition(label='Logistics Booking')
market_feedback    = Transition(label='Market Feedback')
adjust_production  = Transition(label='Adjust Production')

# Build the regulatory‐compliance partial order
compliance_po = StrictPartialOrder(nodes=[certify_origin, customs_filing])
compliance_po.order.add_edge(certify_origin, customs_filing)

# Silent transition for loop exit
skip = SilentTransition()

# Loop: do compliance_po at least once, then optionally repeat
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_po, skip])

# Root partial order for the entire process
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    fermentation_start,
    curd_cutting,
    molding_cheese,
    salt_application,
    aging_check,
    quality_testing,
    packaging_design,
    label_printing,
    compliance_loop,
    cold_chain,
    logistics_booking,
    market_feedback,
    adjust_production
])

# Sequence edges for production steps
root.order.add_edge(milk_sourcing,      fermentation_start)
root.order.add_edge(fermentation_start, curd_cutting)
root.order.add_edge(curd_cutting,       molding_cheese)
root.order.add_edge(molding_cheese,     salt_application)
root.order.add_edge(salt_application,   aging_check)
root.order.add_edge(aging_check,        quality_testing)
root.order.add_edge(quality_testing,    packaging_design)
root.order.add_edge(packaging_design,   label_printing)

# After labeling, do compliance loop
root.order.add_edge(label_printing, compliance_loop)

# After compliance (possibly repeated), run cold chain & logistics in parallel
root.order.add_edge(compliance_loop, cold_chain)
root.order.add_edge(compliance_loop, logistics_booking)

# Both must complete before collecting feedback
root.order.add_edge(cold_chain,        market_feedback)
root.order.add_edge(logistics_booking, market_feedback)

# Finally adjust production based on feedback
root.order.add_edge(market_feedback, adjust_production)