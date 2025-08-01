# Generated from: f23f42e0-cf33-4472-9f50-92811cfbd4e6.json
# Description: This process encompasses the end-to-end supply chain of artisan cheese production, involving niche activities such as microbial culture selection, milk sourcing from specific regional farms, controlled aging in microclimates, quality tasting panels, and coordinated distribution to specialty retailers and exclusive gastronomic events. The process requires precise timing, temperature control, and regulatory compliance checks to maintain product uniqueness and safety. It integrates traditional craftsmanship with modern traceability technology, ensuring provenance and enhancing brand value in a competitive, small-batch market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
activities = [
    'Milk Sourcing', 'Culture Selection', 'Milk Testing', 'Curd Cutting',
    'Whey Draining', 'Mold Inoculation', 'Forming Cheese', 'Salting Stage',
    'Aging Setup', 'Climate Control', 'Quality Tasting', 'Packaging Prep',
    'Label Printing', 'Regulatory Audit', 'Distribution Plan',
    'Retail Delivery', 'Event Coordination'
]
transitions = {act: Transition(label=act) for act in activities}

# Create the root partial order with all nodes
root = StrictPartialOrder(nodes=list(transitions.values()))

# Define the main sequence of edges
sequence = [
    ('Milk Sourcing', 'Culture Selection'),
    ('Culture Selection', 'Milk Testing'),
    ('Milk Testing', 'Curd Cutting'),
    ('Curd Cutting', 'Whey Draining'),
    ('Whey Draining', 'Mold Inoculation'),
    ('Mold Inoculation', 'Forming Cheese'),
    ('Forming Cheese', 'Salting Stage'),
    ('Salting Stage', 'Aging Setup'),
    ('Aging Setup', 'Climate Control'),
    ('Climate Control', 'Quality Tasting'),
    ('Quality Tasting', 'Packaging Prep'),
    ('Packaging Prep', 'Label Printing'),
    ('Label Printing', 'Regulatory Audit'),
    ('Regulatory Audit', 'Distribution Plan')
]
for src, tgt in sequence:
    root.order.add_edge(transitions[src], transitions[tgt])

# Split into concurrent distribution paths
root.order.add_edge(transitions['Distribution Plan'], transitions['Retail Delivery'])
root.order.add_edge(transitions['Distribution Plan'], transitions['Event Coordination'])