# Generated from: 28a8eed7-648f-4454-8c4c-54342b4626dc.json
# Description: This process details the complex steps involved in importing artisan cheeses from remote European farms to boutique stores in North America. It involves sourcing rare cheese varieties, verifying organic certifications, coordinating with local customs agents, managing temperature-controlled logistics, handling quarantine inspections, and ensuring compliance with strict FDA regulations. The process also includes quality sampling, labeling adjustments for different markets, marketing coordination for product launch, and final distribution to specialty retailers, all while maintaining traceability and minimizing spoilage risks throughout the supply chain.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
farm_sourcing     = Transition(label='Farm Sourcing')
certify_organic   = Transition(label='Certify Organic')
contract_signing  = Transition(label='Contract Signing')
customs_liaison   = Transition(label='Customs Liaison')
logistics_planning= Transition(label='Logistics Planning')
temp_monitoring   = Transition(label='Temp Monitoring')
spoilage_control  = Transition(label='Spoilage Control')
traceability_setup= Transition(label='Traceability Setup')
quarantine_check  = Transition(label='Quarantine Check')
fda_compliance    = Transition(label='FDA Compliance')
import_clearance  = Transition(label='Import Clearance')
sample_testing    = Transition(label='Sample Testing')
quality_audit     = Transition(label='Quality Audit')
label_revision    = Transition(label='Label Revision')
marketing_prep    = Transition(label='Marketing Prep')
retail_scheduling = Transition(label='Retail Scheduling')
distribution_setup= Transition(label='Distribution Setup')
skip              = SilentTransition()

# Loop: Sample Testing then choose to exit or do Quality Audit then Sample Testing again
loop_testing = OperatorPOWL(operator=Operator.LOOP, children=[sample_testing, quality_audit])

# Optional label revision: either revise or skip
label_choice = OperatorPOWL(operator=Operator.XOR, children=[label_revision, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    farm_sourcing, certify_organic, contract_signing,
    customs_liaison, logistics_planning,
    temp_monitoring, spoilage_control, traceability_setup,
    quarantine_check, fda_compliance, import_clearance,
    loop_testing, label_choice,
    marketing_prep, retail_scheduling, distribution_setup
])

# Define the control-flow dependencies
# Initial sequence
root.order.add_edge(farm_sourcing, certify_organic)
root.order.add_edge(certify_organic, contract_signing)

# After contract: two concurrent branches
root.order.add_edge(contract_signing, customs_liaison)
root.order.add_edge(contract_signing, logistics_planning)

# Customs branch: liaison -> quarantine -> FDA -> import clearance
root.order.add_edge(customs_liaison, quarantine_check)
root.order.add_edge(quarantine_check, fda_compliance)
root.order.add_edge(fda_compliance, import_clearance)

# Logistics branch: planning -> temp monitoring -> spoilage control -> traceability
root.order.add_edge(logistics_planning, temp_monitoring)
root.order.add_edge(temp_monitoring, spoilage_control)
root.order.add_edge(spoilage_control, traceability_setup)

# Both branches join before testing loop
root.order.add_edge(import_clearance, loop_testing)
root.order.add_edge(traceability_setup, loop_testing)

# After testing loop: optional label revision -> marketing -> retail scheduling -> distribution
root.order.add_edge(loop_testing, label_choice)
root.order.add_edge(label_choice, marketing_prep)
root.order.add_edge(marketing_prep, retail_scheduling)
root.order.add_edge(retail_scheduling, distribution_setup)