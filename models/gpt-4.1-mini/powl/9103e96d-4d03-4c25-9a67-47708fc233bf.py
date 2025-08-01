# Generated from: 9103e96d-4d03-4c25-9a67-47708fc233bf.json
# Description: This process involves the intricate creation of bespoke artisanal perfumes, combining rare natural ingredients sourced globally with advanced blending techniques. It starts with raw material selection, followed by scent profiling, experimental formulation, and iterative refinement. Quality assessments are performed through sensory evaluation panels and chemical analysis to ensure complexity and harmony. Packaging design integrates sustainable materials while reflecting the brand identity. Finally, limited batch production is coordinated with exclusive distribution channels targeting niche luxury markets, ensuring each perfume embodies uniqueness and craftsmanship in every bottle.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Material_Sourcing = Transition(label='Material Sourcing')
Scent_Profiling = Transition(label='Scent Profiling')
Formula_Drafting = Transition(label='Formula Drafting')
Blend_Testing = Transition(label='Blend Testing')
Sensory_Panel = Transition(label='Sensory Panel')
Chemical_Analysis = Transition(label='Chemical Analysis')
Refinement_Loop = Transition(label='Refinement Loop')
Stability_Check = Transition(label='Stability Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Approval = Transition(label='Label Approval')
Batch_Mixing = Transition(label='Batch Mixing')
Quality_Audit = Transition(label='Quality Audit')
Limited_Edition = Transition(label='Limited Edition')
Distribution_Setup = Transition(label='Distribution Setup')
Market_Launch = Transition(label='Market Launch')
Customer_Feedback = Transition(label='Customer Feedback')

# Refinement loop between Refinement_Loop and Stability_Check (represents iterative refinement)
inner_loop = OperatorPOWL(operator=Operator.LOOP, children=[Refinement_Loop, Stability_Check])

# Quality assessment is a partial order of Sensory_Panel and Chemical_Analysis (perform assessments concurrently)
quality_assessment = StrictPartialOrder(nodes=[Sensory_Panel, Chemical_Analysis])
# no ordering edges = concurrent

# Packaging design includes Label Approval after Packaging Design
packaging = StrictPartialOrder(nodes=[Packaging_Design, Label_Approval])
packaging.order.add_edge(Packaging_Design, Label_Approval)

# Batch production includes Batch Mixing and Quality Audit in order
batch_production = StrictPartialOrder(nodes=[Batch_Mixing, Quality_Audit])
batch_production.order.add_edge(Batch_Mixing, Quality_Audit)

# Limited Edition and Distribution Setup are concurrent after batch production
limited_and_distribution = StrictPartialOrder(nodes=[Limited_Edition, Distribution_Setup])
# no order between them

# Market Launch after limited_and_distribution
# Customer Feedback after Market Launch
launch_and_feedback = StrictPartialOrder(nodes=[Market_Launch, Customer_Feedback])
launch_and_feedback.order.add_edge(Market_Launch, Customer_Feedback)

# Full quality check after the inner loop (meaning after iterative refinement)
quality_check_after_loop = StrictPartialOrder(nodes=[inner_loop, quality_assessment])
quality_check_after_loop.order.add_edge(inner_loop, quality_assessment)

# Packaging after quality assessment
packaging_after_quality = StrictPartialOrder(nodes=[quality_assessment, packaging])
packaging_after_quality.order.add_edge(quality_assessment, packaging)

# Batch production after packaging
batch_after_packaging = StrictPartialOrder(nodes=[packaging, batch_production])
batch_after_packaging.order.add_edge(packaging, batch_production)

# Limited edition and distribution setup after batch production
limited_dist_after_batch = StrictPartialOrder(nodes=[batch_production, limited_and_distribution])
limited_dist_after_batch.order.add_edge(batch_production, limited_and_distribution)

# Market launch and customer feedback after limited edition and distribution
final = StrictPartialOrder(nodes=[limited_and_distribution, launch_and_feedback])
final.order.add_edge(limited_and_distribution, launch_and_feedback)

# Initial sequential process from Material_Sourcing to Blend_Testing
initial_sequence = StrictPartialOrder(nodes=[Material_Sourcing, Scent_Profiling, Formula_Drafting, Blend_Testing])
initial_sequence.order.add_edge(Material_Sourcing, Scent_Profiling)
initial_sequence.order.add_edge(Scent_Profiling, Formula_Drafting)
initial_sequence.order.add_edge(Formula_Drafting, Blend_Testing)

# Full process: initial_sequence -> refinement & quality -> packaging -> batch -> limited+distribution -> launch+feedback
root = StrictPartialOrder(nodes=[
    initial_sequence,
    quality_check_after_loop,
    packaging_after_quality,
    batch_after_packaging,
    limited_dist_after_batch,
    final
])

# Add order edges between these sub-processes to represent the flow
root.order.add_edge(initial_sequence, quality_check_after_loop)
root.order.add_edge(quality_check_after_loop, packaging_after_quality)
root.order.add_edge(packaging_after_quality, batch_after_packaging)
root.order.add_edge(batch_after_packaging, limited_dist_after_batch)
root.order.add_edge(limited_dist_after_batch, final)