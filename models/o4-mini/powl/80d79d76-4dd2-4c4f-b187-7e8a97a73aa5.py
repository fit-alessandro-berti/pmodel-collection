# Generated from: 80d79d76-4dd2-4c4f-b187-7e8a97a73aa5.json
# Description: This process outlines the intricate steps involved in restoring antique artifacts to preserve historical value while ensuring structural integrity and aesthetic authenticity. It begins with detailed provenance research, followed by condition assessment and material analysis. Conservation planning is then developed to balance restoration with preservation ethics, after which specialized cleaning and stabilization techniques are applied. Subsequent activities include delicate repair, color matching, and surface finishing using historically accurate materials. Final stages involve documentation, client review, and long-term maintenance scheduling to ensure the artifact's longevity and compliance with museum standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
prov_check    = Transition(label='Provenance Check')
cond_scan     = Transition(label='Condition Scan')
mat_test      = Transition(label='Material Test')
plan_creation = Transition(label='Plan Creation')
ethics_review = Transition(label='Ethics Review')
surface_clean = Transition(label='Surface Clean')
struct_fix    = Transition(label='Structural Fix')
color_match   = Transition(label='Color Match')
paint_apply   = Transition(label='Paint Apply')
finish_polish = Transition(label='Finish Polish')
uv_cure       = Transition(label='UV Cure')
documentation = Transition(label='Documentation')
client_review = Transition(label='Client Review')
pack_prep     = Transition(label='Packaging Prep')
maint_plan    = Transition(label='Maintenance Plan')

# Build the partial order
root = StrictPartialOrder(nodes=[
    prov_check, cond_scan, mat_test, 
    plan_creation, ethics_review, 
    surface_clean, struct_fix, 
    color_match, paint_apply, finish_polish, uv_cure,
    documentation, client_review, pack_prep, maint_plan
])

# Define control-flow dependencies
root.order.add_edge(prov_check, cond_scan)
root.order.add_edge(prov_check, mat_test)
root.order.add_edge(cond_scan, plan_creation)
root.order.add_edge(mat_test, plan_creation)
root.order.add_edge(plan_creation, ethics_review)
root.order.add_edge(ethics_review, surface_clean)
root.order.add_edge(ethics_review, struct_fix)
root.order.add_edge(surface_clean, color_match)
root.order.add_edge(struct_fix, color_match)
root.order.add_edge(color_match, paint_apply)
root.order.add_edge(paint_apply, finish_polish)
root.order.add_edge(finish_polish, uv_cure)
root.order.add_edge(uv_cure, documentation)
root.order.add_edge(documentation, client_review)
root.order.add_edge(client_review, pack_prep)
root.order.add_edge(pack_prep, maint_plan)