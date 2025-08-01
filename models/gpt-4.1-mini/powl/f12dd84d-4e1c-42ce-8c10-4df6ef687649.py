# Generated from: f12dd84d-4e1c-42ce-8c10-4df6ef687649.json
# Description: This process outlines the intricate supply chain and quality assurance workflow for artisan cheese production, starting from sourcing rare raw milk varieties to aging in controlled environments. It includes activities such as microbial testing, traditional curdling, seasonal staff coordination, and niche market distribution. The process also covers sustainable packaging decisions, traceability logging, and customer feedback integration to maintain authenticity and meet artisanal standards while navigating regulatory compliance and fluctuating seasonal yields.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
curd_processing = Transition(label='Curd Processing')
salt_application = Transition(label='Salt Application')
mold_inoculation = Transition(label='Mold Inoculation')
press_molding = Transition(label='Press Molding')
brine_soaking = Transition(label='Brine Soaking')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
microbial_check = Transition(label='Microbial Check')
packaging_design = Transition(label='Packaging Design')
label_printing = Transition(label='Label Printing')
trace_logging = Transition(label='Trace Logging')
distribution_plan = Transition(label='Distribution Plan')
customer_review = Transition(label='Customer Review')
inventory_audit = Transition(label='Inventory Audit')
sustainability_audit = Transition(label='Sustainability Audit')

# Construct partial orders and control structures

# Initial sourcing and testing sequence
initial_po = StrictPartialOrder(nodes=[milk_sourcing, quality_testing])
initial_po.order.add_edge(milk_sourcing, quality_testing)

# Traditional curdling and salting sequence
curd_po = StrictPartialOrder(nodes=[curd_processing, salt_application])
curd_po.order.add_edge(curd_processing, salt_application)

# Molding sequence after salting: mold inoculation -> press molding -> brine soaking
molding_po = StrictPartialOrder(
    nodes=[mold_inoculation, press_molding, brine_soaking]
)
molding_po.order.add_edge(mold_inoculation, press_molding)
molding_po.order.add_edge(press_molding, brine_soaking)

# Aging process with environmental controls: aging setup and humidity control can be concurrent
aging_po = StrictPartialOrder(
    nodes=[aging_setup, humidity_control]
)
# No order edges between aging_setup and humidity_control, concurrent

# Microbial check happens after aging controls
aging_and_check_po = StrictPartialOrder(
    nodes=[aging_po, microbial_check]
)
aging_and_check_po.order.add_edge(aging_po, microbial_check)  # Loop expects Transition or OperatorPOWL as nodes
# but StrictPartialOrder expects nodes as Transition or OperatorPOWL - 
# we consider aging_po as node here - is possible if aging_po is wrapped as OperatorPOWL or we flatten

# To keep POWL nodes consistent, treat aging_po as node inside another PO
# So, create an OperatorPOWL with aging_po and microbial_check in partial order

# Packaging decision: packaging design and label printing concurrent
packaging_po = StrictPartialOrder(nodes=[packaging_design, label_printing])
# concurrent, no edges

# Trace logging after packaging
packaging_and_trace_po = StrictPartialOrder(
    nodes=[packaging_po, trace_logging]
)
packaging_and_trace_po.order.add_edge(packaging_po, trace_logging)

# Distribution plan after trace logging
dist_po = StrictPartialOrder(nodes=[distribution_plan])
# single node

# Feedback loop: customer review and audits (inventory and sustainability)
audits_po = StrictPartialOrder(nodes=[inventory_audit, sustainability_audit])
# audits concurrent, no edges

feedback_po = StrictPartialOrder(
    nodes=[customer_review, audits_po]
)
feedback_po.order.add_edge(customer_review, audits_po)

# Loop structure on feedback to model repeated seasonal staff coordination (abstracted here as loop on feedback)
# Since no explicit seasonal staff coordination activity was given, 
# model feedback as loop body and exit is a silent transition (skip)

skip = SilentTransition()

feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_review, audits_po])
# But LOOP requires two children: first body (A), second "repetitive" part (B)
# We interpret the feedback loop as: first do customer_review then audits, then choose exit or repeat audits & customer review

# For LOOP operator, children = [A, B]
# So let A = customer_review, B = audits_po (audits repeated before going back to customer review)
# This fits LOOP: A then (exit or B then A again)

feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[customer_review,
              audits_po]
)

# Now assemble top-level model connecting all parts in PROCESS logical order:
# milk_sourcing -> quality_testing -> curd_processing -> salt_application -> molding_po ->
# aging_po + microbial_check -> packaging_po -> trace_logging -> distribution_plan -> feedback_loop

# We need to ensure proper ordering with nodes being:
# initial_po, curd_po, molding_po, aging_po, microbial_check, packaging_po, trace_logging, distribution_plan, feedback_loop

# However, since initial_po, curd_po, molding_po, aging_po, packaging_po, audits_po,
# these are StrictPartialOrder objects or Transition objects or OperatorPOWL;
# StrictPartialOrder nodes expect only Transition, SilentTransition or OperatorPOWL as nodes.
# To nest StrictPartialOrder inside another, better flatten or wrap them into OperatorPOWL if needed.

# Instead, build all as OperatorPOWL with operator=Operator.PO (partial order)
# but Operator.PO not in specification; so use StrictPartialOrder at top and place all smaller orders as nodes.

# So to keep consistent, make these nested parts OperatorPOWL of type XOR or LOOP only, else partial orders are StrictPartialOrder.

# We'll define intermediate steps as StrictPartialOrder nodes, with transitions inside, and use these nodes in the final top-level StrictPartialOrder

# First, wrap partial orders that are needed as individual nodes:

# For those that are already PartialOrders with multiple nodes: keep them as is

# For applying ordering among them, use final PO with nodes:
# [initial_po, curd_po, molding_po, aging_po, microbial_check, packaging_po, trace_logging, distribution_plan, feedback_loop]

# microbial_check is Transition

# Build aging_po as partial order with aging_setup and humidity_control

aging_po = StrictPartialOrder(nodes=[aging_setup, humidity_control])  # concurrent

# Create a partial order for aging_po and microbial_check: microbial_check depends on aging_po

aging_with_check = StrictPartialOrder(nodes=[aging_po, microbial_check])
aging_with_check.order.add_edge(aging_po, microbial_check)

# Create packaging_and_trace as partial order: packaging_po -> trace_logging

packaging_and_trace = StrictPartialOrder(nodes=[packaging_po, trace_logging])
packaging_and_trace.order.add_edge(packaging_po, trace_logging)

# Now final top-level PO nodes:

root = StrictPartialOrder(
    nodes=[
        initial_po,
        curd_po,
        molding_po,
        aging_with_check,
        packaging_and_trace,
        distribution_plan,
        feedback_loop,
    ]
)

# Add ordering edges reflecting the process flow

root.order.add_edge(initial_po, curd_po)
root.order.add_edge(curd_po, molding_po)
root.order.add_edge(molding_po, aging_with_check)
root.order.add_edge(aging_with_check, packaging_and_trace)
root.order.add_edge(packaging_and_trace, distribution_plan)
root.order.add_edge(distribution_plan, feedback_loop)