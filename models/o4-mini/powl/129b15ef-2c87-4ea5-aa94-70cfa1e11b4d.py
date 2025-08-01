# Generated from: 129b15ef-2c87-4ea5-aa94-70cfa1e11b4d.json
# Description: This process outlines the detailed steps involved in authenticating rare historical artifacts brought in by collectors or museums. It involves initial inspection, provenance research, scientific testing, expert consultation, and final certification. The workflow ensures that each item undergoes rigorous validation combining physical examination and digital verification methods, including spectral analysis and blockchain tracking, to prevent forgery and establish authenticity before public or private acquisition.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
item_intake = Transition(label='Item Intake')
visual_scan = Transition(label='Visual Scan')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
provenance_check = Transition(label='Provenance Check')
historical_review = Transition(label='Historical Review')
material_sampling = Transition(label='Material Sampling')
spectral_test = Transition(label='Spectral Test')
blockchain_log = Transition(label='Blockchain Log')
database_match = Transition(label='Database Match')
expert_review = Transition(label='Expert Review')
forgery_analysis = Transition(label='Forgery Analysis')
cert_prep = Transition(label='Certification Prep')
final_approval = Transition(label='Final Approval')
client_notification = Transition(label='Client Notification')
archive_update = Transition(label='Archive Update')

# Build the partial order
root = StrictPartialOrder(nodes=[
    item_intake,
    visual_scan,
    digital_scan,
    condition_report,
    provenance_check,
    historical_review,
    material_sampling,
    spectral_test,
    blockchain_log,
    database_match,
    expert_review,
    forgery_analysis,
    cert_prep,
    final_approval,
    client_notification,
    archive_update
])

# After intake, four branches run in parallel
root.order.add_edge(item_intake, visual_scan)
root.order.add_edge(item_intake, digital_scan)
root.order.add_edge(item_intake, provenance_check)
root.order.add_edge(item_intake, material_sampling)

# Visual scan produces the condition report
root.order.add_edge(visual_scan, condition_report)

# Provenance research chain
root.order.add_edge(provenance_check, historical_review)

# Scientific testing chain
root.order.add_edge(material_sampling, spectral_test)

# Digital verification chain
root.order.add_edge(digital_scan, blockchain_log)
root.order.add_edge(blockchain_log, database_match)

# All research & testing converge into expert review
root.order.add_edge(historical_review, expert_review)
root.order.add_edge(spectral_test, expert_review)
root.order.add_edge(database_match, expert_review)

# Expert review -> forgery analysis
root.order.add_edge(expert_review, forgery_analysis)

# Condition report and forgery analysis feed into certification prep
root.order.add_edge(condition_report, cert_prep)
root.order.add_edge(forgery_analysis, cert_prep)

# Final certification sequence
root.order.add_edge(cert_prep, final_approval)
root.order.add_edge(final_approval, client_notification)
root.order.add_edge(client_notification, archive_update)