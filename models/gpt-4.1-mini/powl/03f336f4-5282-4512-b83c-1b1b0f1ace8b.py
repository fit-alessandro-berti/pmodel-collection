# Generated from: 03f336f4-5282-4512-b83c-1b1b0f1ace8b.json
# Description: This complex business process involves the systematic authentication of historical artifacts acquired through various channels. It begins with initial artifact intake and proceeds through multi-disciplinary expert evaluations including material analysis, provenance verification, and stylistic assessment. The process integrates scientific testing such as radiocarbon dating and spectroscopic examination alongside archival research and expert interviews. Discrepancies trigger secondary review loops and risk assessment protocols. Once authenticated, the artifact undergoes documentation, cataloging, and secure storage preparations. The workflow concludes with compliance reporting and preparation for either exhibition or controlled sale, ensuring legal and ethical standards are maintained throughout. This atypical process demands coordination across curatorial, scientific, legal, and logistical teams to guarantee authenticity and integrity in artifact handling.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
IntakeCheck = Transition(label='Intake Check')
MaterialTest = Transition(label='Material Test')
ProvenanceScan = Transition(label='Provenance Scan')
StylisticReview = Transition(label='Stylistic Review')

RadiocarbonDate = Transition(label='Radiocarbon Date')
SpectroAnalysis = Transition(label='Spectro Analysis')
ArchiveResearch = Transition(label='Archive Research')
ExpertInterview = Transition(label='Expert Interview')

DiscrepancyFlag = Transition(label='Discrepancy Flag')
SecondaryReview = Transition(label='Secondary Review')
RiskAssess = Transition(label='Risk Assess')

Documentation = Transition(label='Documentation')
CatalogUpdate = Transition(label='Catalog Update')
StoragePrep = Transition(label='Storage Prep')

ComplianceReport = Transition(label='Compliance Report')

ExhibitPrep = Transition(label='Exhibit Prep')
SaleApproval = Transition(label='Sale Approval')

# Scientific Testing partial order (Radiocarbon Date, Spectro Analysis concurrent)
scientific_testing = StrictPartialOrder(nodes=[RadiocarbonDate, SpectroAnalysis])

# Expert Investigations partial order (Archive Research, Expert Interview concurrent)
expert_investigation = StrictPartialOrder(nodes=[ArchiveResearch, ExpertInterview])

# Multi-disciplinary evaluations partial order:
# Material Test, Provenance Scan, Stylistic Review concurrent,
# then combined with scientific testing and expert investigation concurrently

# First the three evaluations concurrent
evals = StrictPartialOrder(nodes=[MaterialTest, ProvenanceScan, StylisticReview])

# Create a joint partial order with scientific testing and expert investigation concurrent with evals
# We combine evals, scientific_testing and expert_investigation at same level (all concurrent)
multi_eval = StrictPartialOrder(nodes=[evals, scientific_testing, expert_investigation])

# Add no order edges between these three nodes (evals, scientific_testing, expert_investigation) means fully concurrent

# Define the secondary review loop (execute DiscrepancyFlag, then loop on SecondaryReview and RiskAssess then back)
# DiscrepancyFlag activates a loop with SecondaryReview and RiskAssess repeated

# Loop children: A = SecondaryReview, B = RiskAssess
# * (SecondaryReview, RiskAssess)
secondary_loop = OperatorPOWL(operator=Operator.LOOP, children=[SecondaryReview, RiskAssess])

# Choice node: after secondary loop all end or escalate
# There is no direct mention of choice after secondary loop, so after loop ends flows forward

# Let's assume the control flow after initial evals combines results and if DiscrepancyFlag triggered,
# then loop, else continue

# So after multi_eval, one can have DiscrepancyFlag; 
# We'll model that DiscrepancyFlag is concurrent with multi_eval end 
# Or more precisely, the discrepancy check is after these evaluations (order edges)

# Build a partial order:
# IntakeCheck --> multi_eval --> DiscrepancyFlag --> secondary_loop --> Documentation

# Create strict partial order covering these steps:

# First level: IntakeCheck
# Second level: multi_eval
# Third level: DiscrepancyFlag
# Fourth level: secondary_loop (loop on SecondaryReview and RiskAssess)
# Fifth level: Documentation, CatalogUpdate, StoragePrep concurrent
# Sixth level: ComplianceReport
# Seventh level: exclusive choice between ExhibitPrep and SaleApproval

# Define documentation phase concurrent nodes
documentation_phase = StrictPartialOrder(nodes=[Documentation, CatalogUpdate, StoragePrep])

# Define final choice XOR between ExhibitPrep and SaleApproval
final_choice = OperatorPOWL(operator=Operator.XOR, children=[ExhibitPrep, SaleApproval])

# Build overall partial order with all components as nodes and edges for sequence

# nodes:
# IntakeCheck, multi_eval, DiscrepancyFlag, secondary_loop, documentation_phase, ComplianceReport, final_choice

# Create the partial orders as nodes:
# multi_eval itself has 3 sub POs inside, so multi_eval is node representing the evals cluster

# We'll treat them as nodes that are themselves partial orders or operators

# Now build the top-level PO with these nodes and edges

root = StrictPartialOrder(
    nodes=[
        IntakeCheck,
        multi_eval,
        DiscrepancyFlag,
        secondary_loop,
        documentation_phase,
        ComplianceReport,
        final_choice
    ]
)

# Add order edges for sequence
root.order.add_edge(IntakeCheck, multi_eval)
root.order.add_edge(multi_eval, DiscrepancyFlag)
root.order.add_edge(DiscrepancyFlag, secondary_loop)
root.order.add_edge(secondary_loop, documentation_phase)
root.order.add_edge(documentation_phase, ComplianceReport)
root.order.add_edge(ComplianceReport, final_choice)