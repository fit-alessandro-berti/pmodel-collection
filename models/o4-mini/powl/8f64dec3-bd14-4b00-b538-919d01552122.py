# Generated from: 8f64dec3-bd14-4b00-b538-919d01552122.json
# Description: This process involves the careful restoration of antique artifacts, combining historical research, material analysis, and precision craftsmanship to preserve original features while ensuring structural integrity. The workflow begins with artifact assessment and documentation, followed by controlled cleaning, selective material consolidation, and surface stabilization. Specialized activities include micro-crack repair, color matching, and period-accurate repainting. Throughout the process, environmental controls are maintained to prevent further degradation. Final steps include quality inspection, provenance updating, and preparing detailed restoration reports for archival purposes. This atypical process ensures antiques retain both their aesthetic and historical values through a multidisciplinary approach.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
artifact_assess    = Transition(label='Artifact Assess')
documentation     = Transition(label='Documentation')
historical_check  = Transition(label='Historical Check')
material_test     = Transition(label='Material Test')
condition_map     = Transition(label='Condition Map')
surface_clean     = Transition(label='Surface Clean')
consolidate_frag  = Transition(label='Consolidate Fragile')
structural_fix    = Transition(label='Structural Fix')
micro_crack       = Transition(label='Micro Crack')
color_match       = Transition(label='Color Match')
repaint_period    = Transition(label='Repaint Period')
quality_inspect   = Transition(label='Quality Inspect')
provenance_update = Transition(label='Provenance Update')
report_prep       = Transition(label='Report Prep')
archive_store     = Transition(label='Archive Store')
environmental_set = Transition(label='Environmental Set')

# Build a partial order: environmental_set is left unconnected to model its
# concurrent, ongoing role; all other steps form a strict sequence
root = StrictPartialOrder(nodes=[
    artifact_assess, documentation, historical_check, material_test, condition_map,
    surface_clean, consolidate_frag, structural_fix,
    micro_crack, color_match, repaint_period,
    quality_inspect, provenance_update, report_prep, archive_store,
    environmental_set
])

# Sequence edges for the main workflow
root.order.add_edge(artifact_assess,    documentation)
root.order.add_edge(documentation,     historical_check)
root.order.add_edge(historical_check,  material_test)
root.order.add_edge(material_test,     condition_map)
root.order.add_edge(condition_map,     surface_clean)
root.order.add_edge(surface_clean,     consolidate_frag)
root.order.add_edge(consolidate_frag,  structural_fix)
root.order.add_edge(structural_fix,    micro_crack)
root.order.add_edge(micro_crack,       color_match)
root.order.add_edge(color_match,       repaint_period)
root.order.add_edge(repaint_period,    quality_inspect)
root.order.add_edge(quality_inspect,   provenance_update)
root.order.add_edge(provenance_update, report_prep)
root.order.add_edge(report_prep,       archive_store)