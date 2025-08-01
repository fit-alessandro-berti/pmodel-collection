# Generated from: 255f6d81-d960-47a3-aca2-817f26554736.json
# Description: This process governs the acquisition, evaluation, and rotation of artwork leased to corporate offices for aesthetic enhancement and brand alignment. It involves curating pieces based on corporate culture, negotiating lease terms with artists or galleries, scheduling installation and maintenance, and periodically rotating collections to refresh environments. Feedback from employees is collected to assess impact on workplace ambiance and productivity. Additionally, the process includes managing insurance, provenance verification, and coordinating art events to engage stakeholders. The goal is to maintain a dynamic, inspiring visual environment while optimizing budget and compliance with corporate policies.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ts = Transition(label='Art Sourcing')
budget = Transition(label='Budget Approval')
artist = Transition(label='Artist Liaison')
lease = Transition(label='Lease Negotiation')
survey = Transition(label='Workplace Survey')
selection = Transition(label='Collection Selection')
contract = Transition(label='Contract Drafting')
insurance = Transition(label='Insurance Setup')
plan = Transition(label='Installation Plan')
delivery = Transition(label='Artwork Delivery')
setup = Transition(label='Display Setup')
maintenance = Transition(label='Maintenance Check')
feedback = Transition(label='Employee Feedback')
rotation = Transition(label='Collection Rotation')
event = Transition(label='Event Coordination')
provenance = Transition(label='Provenance Check')
compliance = Transition(label='Policy Compliance')

# Main process (A)
A = StrictPartialOrder(nodes=[
    ts, selection, artist, lease, contract, budget, provenance, compliance,
    insurance, plan, delivery, setup, maintenance, survey, feedback, event
])
# Acquisition & contracting
A.order.add_edge(ts, selection)
A.order.add_edge(selection, artist)
A.order.add_edge(artist, lease)
A.order.add_edge(lease, contract)
A.order.add_edge(contract, budget)
A.order.add_edge(budget, provenance)
A.order.add_edge(provenance, compliance)
# Installation preparation
A.order.add_edge(compliance, insurance)
A.order.add_edge(insurance, plan)
A.order.add_edge(plan, delivery)
A.order.add_edge(delivery, setup)
# Post‐installation activities
A.order.add_edge(setup, maintenance)
A.order.add_edge(setup, survey)
A.order.add_edge(survey, feedback)
A.order.add_edge(setup, event)

# Rotation step (B), to be repeated in a loop
B = StrictPartialOrder(nodes=[rotation])

# Loop: do A once, then either exit or do B then A again
root = OperatorPOWL(operator=Operator.LOOP, children=[A, B])