# Generated from: 56b8dd67-451f-4a64-bbe2-d681a2eed576.json
# Description: This process governs the intricate coordination required to facilitate international loans of valuable artworks between museums, galleries, and private collectors. It involves provenance verification, customs compliance, conditional insurance underwriting, climate-controlled transportation planning, and installation scheduling. The process also addresses risk mitigation, legal documentation, multi-party approvals, and real-time status reporting to ensure the artwork's integrity and security throughout transit and display. Stakeholders include conservators, legal teams, logistics providers, and curators, all collaborating to meet strict deadlines and maintain cultural heritage standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ProvenanceCheck = Transition(label='Provenance Check')
LoanRequest = Transition(label='Loan Request')
LegalReview = Transition(label='Legal Review')
InsuranceSetup = Transition(label='Insurance Setup')
CustomsFiling = Transition(label='Customs Filing')
ClimatePlan = Transition(label='Climate Plan')
TransportBooking = Transition(label='Transport Booking')
ConditionReport = Transition(label='Condition Report')
PackagingDesign = Transition(label='Packaging Design')
SecurityClearance = Transition(label='Security Clearance')
InstallationPrep = Transition(label='Installation Prep')
StakeholderSync = Transition(label='Stakeholder Sync')
RiskAssessment = Transition(label='Risk Assessment')
FinalApproval = Transition(label='Final Approval')
StatusUpdate = Transition(label='Status Update')
Deinstallation = Transition(label='Deinstallation')
ReturnLogistics = Transition(label='Return Logistics')

# Insurance Setup may be conditionally skipped (choice of insurance or skip)
skip = SilentTransition()
insurance_choice = OperatorPOWL(operator=Operator.XOR, children=[InsuranceSetup, skip])

# The loop might be status updates that repeat until final approval
# Loop with body: StatusUpdate, repeat until exit after FinalApproval
# According to the definition, loop = *(A,B) where A is done, then choice to exit or do B then A again.
# We want loop: do StatusUpdate, then choose exit or RiskAssessment (or other re-checks), then StatusUpdate again.
# But the problem mentions ongoing status reporting, risk mitigation, and approvals. Let's model a loop with:
# A = StatusUpdate
# B = a partial order of RiskAssessment and StakeholderSync (concurrent), then LegalReview (dependency)
# But better keep it simple: loop body B includes RiskAssessment and StakeholderSync (concurrent).
# Let's put LegalReview before FinalApproval (linear).

# Partial order of RiskAssessment and StakeholderSync concurrent
risk_stakeholder = StrictPartialOrder(nodes=[RiskAssessment, StakeholderSync])
# No order edges mean concurrent execution

# Loop body: do risk_stakeholder, then StatusUpdate again

# Loop children: A=StatusUpdate, B=risk_stakeholder
status_loop = OperatorPOWL(operator=Operator.LOOP, children=[StatusUpdate, risk_stakeholder])

# Main process partial order:
# The tasks occur in phases:

# Phase 1: Provenance Check -> Loan Request -> Legal Review

phase1 = StrictPartialOrder(nodes=[ProvenanceCheck, LoanRequest, LegalReview])
phase1.order.add_edge(ProvenanceCheck, LoanRequest)
phase1.order.add_edge(LoanRequest, LegalReview)

# Phase 2: After Legal Review, choice to do Insurance Setup or skip

# phase2 is insurance_choice defined above

# Phase 3: Customs Filing must occur after insurance_choice, then Climate Plan, Transport Booking

phase3 = StrictPartialOrder(nodes=[CustomsFiling, ClimatePlan, TransportBooking])
phase3.order.add_edge(CustomsFiling, ClimatePlan)
phase3.order.add_edge(ClimatePlan, TransportBooking)

# Phase 4: Condition Report, Packaging Design, Security Clearance (concurrent)

phase4 = StrictPartialOrder(nodes=[ConditionReport, PackagingDesign, SecurityClearance])
# no order edges = concurrent

# Phase 5: Installation Prep after phase4

phase5 = InstallationPrep

# Phase 6: Risk mitigation and approvals: modeled with the loop status_loop to cover ongoing Risk and Stakeholder Sync

# After loop completes, Final Approval

# Phase 7: Deinstallation and Return Logistics (after Final Approval)

phase7 = StrictPartialOrder(nodes=[Deinstallation, ReturnLogistics])
phase7.order.add_edge(Deinstallation, ReturnLogistics)

# Compose all phases into one main partial order with proper edges:

all_nodes = [phase1, insurance_choice, phase3, phase4, phase5, status_loop, FinalApproval, phase7]

root = StrictPartialOrder(nodes=all_nodes)

# Add ordering edges between phases:

# phase1 -> insurance_choice
root.order.add_edge(phase1, insurance_choice)

# insurance_choice -> phase3
root.order.add_edge(insurance_choice, phase3)

# phase3 -> phase4
root.order.add_edge(phase3, phase4)

# phase4 -> Installation Prep (phase5)
root.order.add_edge(phase4, phase5)

# Installation Prep -> status_loop
root.order.add_edge(phase5, status_loop)

# status_loop -> Final Approval
root.order.add_edge(status_loop, FinalApproval)

# FinalApproval -> phase7
root.order.add_edge(FinalApproval, phase7)