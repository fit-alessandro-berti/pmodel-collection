# Generated from: 03491624-75df-457c-b332-00d3400ae23c.json
# Description: This process involves the intricate steps required to produce, certify, and export artisanal cheese from rural farms to international gourmet markets. It includes raw milk sourcing, traditional fermentation, quality control, packaging with unique branding, regulatory compliance checks for each target country, coordination with logistics partners specializing in perishable goods, managing customs documentation, and ensuring cold chain integrity throughout transit. The process also involves market feedback collection post-delivery to adjust production and marketing strategies for different regions.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
fermentation_start = Transition(label='Fermentation Start')
curd_cutting = Transition(label='Curd Cutting')
molding_cheese = Transition(label='Molding Cheese')
salt_application = Transition(label='Salt Application')
aging_check = Transition(label='Aging Check')
quality_testing = Transition(label='Quality Testing')
packaging_design = Transition(label='Packaging Design')
label_printing = Transition(label='Label Printing')
certify_origin = Transition(label='Certify Origin')
customs_filing = Transition(label='Customs Filing')
cold_chain = Transition(label='Cold Chain')
logistics_booking = Transition(label='Logistics Booking')
market_feedback = Transition(label='Market Feedback')
adjust_production = Transition(label='Adjust Production')

# Create the partial order for the cheese production phases up to certification
production_po = StrictPartialOrder(nodes=[
    milk_sourcing,
    fermentation_start,
    curd_cutting,
    molding_cheese,
    salt_application,
    aging_check,
    quality_testing,
    packaging_design,
    label_printing,
    certify_origin
])
production_po.order.add_edge(milk_sourcing, fermentation_start)
production_po.order.add_edge(fermentation_start, curd_cutting)
production_po.order.add_edge(curd_cutting, molding_cheese)
production_po.order.add_edge(molding_cheese, salt_application)
production_po.order.add_edge(salt_application, aging_check)
production_po.order.add_edge(aging_check, quality_testing)
production_po.order.add_edge(quality_testing, packaging_design)
production_po.order.add_edge(packaging_design, label_printing)
production_po.order.add_edge(label_printing, certify_origin)

# Create the partial order representing export & logistics steps, which partially order customs, cold chain, and logistics booking in parallel
export_po = StrictPartialOrder(nodes=[customs_filing, cold_chain, logistics_booking])
# Partial order: customs_filing --> cold_chain, customs_filing --> logistics_booking (customs before transit and logistics)
export_po.order.add_edge(customs_filing, cold_chain)
export_po.order.add_edge(customs_filing, logistics_booking)

# Market feedback and adjustment steps happen after logistics booking and cold chain
feedback_po = StrictPartialOrder(nodes=[market_feedback, adjust_production])
feedback_po.order.add_edge(market_feedback, adjust_production)

# Combine export and feedback steps in a partial order:
# export_po must finish before feedback_po starts
export_feedback_po = StrictPartialOrder(nodes=[export_po, feedback_po])
export_feedback_po.order.add_edge(export_po, feedback_po)

# Overall root partial order combining production --> export_feedback_po
root = StrictPartialOrder(nodes=[production_po, export_feedback_po])
root.order.add_edge(production_po, export_feedback_po)