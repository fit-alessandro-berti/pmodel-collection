# Generated from: ec9aec90-0174-4e31-a649-c752527fd227.json
# Description: This process outlines the intricate workflow involved in restoring antique artifacts for museums or private collectors. It begins with artifact assessment and provenance verification to ensure authenticity. Following that, condition analysis identifies damage and material composition. Conservation planning is then developed, balancing preservation with restoration goals. Next, delicate cleaning and stabilization treatments are performed, often requiring custom tools. Missing parts are fabricated or sourced from archival materials. After structural repairs, surface treatments including patina preservation or color matching are applied. Documentation throughout ensures traceability. Final quality review and client approval precede careful packaging and transport arrangements to prevent damage during delivery. This atypical but realistic process demands expertise across multiple disciplines to return artifacts to display condition while respecting their historical integrity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Atomic activities
t_assess        = Transition(label='Assess Artifact')
t_verify        = Transition(label='Verify Provenance')
t_analyze       = Transition(label='Analyze Condition')
t_plan          = Transition(label='Plan Conservation')
t_clean         = Transition(label='Clean Surface')
t_stabilize     = Transition(label='Stabilize Structure')
t_source        = Transition(label='Source Materials')
t_fabricate     = Transition(label='Fabricate Parts')
t_repairs       = Transition(label='Perform Repairs')
t_patina        = Transition(label='Apply Patina')
t_match         = Transition(label='Match Colors')
t_document      = Transition(label='Document Process')
t_review        = Transition(label='Review Quality')
t_approve       = Transition(label='Obtain Approval')
t_package       = Transition(label='Package Securely')
t_transport     = Transition(label='Arrange Transport')

# Choice between sourcing or fabricating missing parts
xor_parts = OperatorPOWL(operator=Operator.XOR,
                         children=[t_source, t_fabricate])
# Choice between patina preservation or color matching
xor_surface = OperatorPOWL(operator=Operator.XOR,
                          children=[t_patina, t_match])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    t_assess, t_verify, t_analyze, t_plan,
    t_clean, t_stabilize, xor_parts, t_repairs,
    xor_surface, t_document, t_review, t_approve,
    t_package, t_transport
])

# Define the sequence/control‐flow edges
root.order.add_edge(t_assess,    t_verify)
root.order.add_edge(t_verify,    t_analyze)
root.order.add_edge(t_analyze,   t_plan)
root.order.add_edge(t_plan,      t_clean)
root.order.add_edge(t_clean,     t_stabilize)
root.order.add_edge(t_stabilize, xor_parts)
root.order.add_edge(xor_parts,   t_repairs)
root.order.add_edge(t_repairs,   xor_surface)
root.order.add_edge(xor_surface, t_review)
root.order.add_edge(t_review,    t_approve)
root.order.add_edge(t_approve,   t_package)
root.order.add_edge(t_package,   t_transport)

# 'Document Process' is concurrent with the rest (no ordering constraints)