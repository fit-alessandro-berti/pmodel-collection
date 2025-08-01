# Generated from: 8945476a-7638-479b-802a-23e6bd1f8544.json
# Description: This process manages the end-to-end handling of custom art commissions for a boutique studio specializing in mixed media pieces. It involves initial client consultation to understand artistic preferences, followed by concept sketching and iterative feedback cycles. Once approved, materials sourcing is conducted considering sustainability and cost. The creation phase includes layering of diverse media, drying periods, and quality checks. Post-production involves framing options, documentation of artwork provenance, and final client presentation. Payment scheduling aligns with milestone completions, and after-delivery support includes care instructions and potential restoration services. The workflow ensures personalized client engagement while maintaining artistic integrity and operational efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
client_meet        = Transition(label='Client Meet')
preference_survey  = Transition(label='Preference Survey')
concept_sketch     = Transition(label='Concept Sketch')
feedback_loop      = Transition(label='Feedback Loop')
material_sourcing  = Transition(label='Material Sourcing')
cost_analysis      = Transition(label='Cost Analysis')
layer_application  = Transition(label='Layer Application')
drying_period      = Transition(label='Drying Period')
quality_check      = Transition(label='Quality Check')
frame_selection    = Transition(label='Frame Selection')
provenance_doc     = Transition(label='Provenance Doc')
final_presentation = Transition(label='Final Presentation')
payment_setup      = Transition(label='Payment Setup')
delivery_schedule  = Transition(label='Delivery Schedule')
aftercare_support  = Transition(label='Aftercare Support')
restoration_plan   = Transition(label='Restoration Plan')

# Concept sketch & feedback iterative loop: do sketch, then either exit or feedback→sketch again
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[concept_sketch, feedback_loop])

# Materials sourcing and cost analysis can proceed concurrently
po_sourcing = StrictPartialOrder(nodes=[material_sourcing, cost_analysis])
# (no edges = concurrency)

# Creation phase: layer → dry → quality check
po_creation = StrictPartialOrder(nodes=[layer_application, drying_period, quality_check])
po_creation.order.add_edge(layer_application, drying_period)
po_creation.order.add_edge(drying_period, quality_check)

# Post‐production: framing → provenance doc → final presentation
po_postproduction = StrictPartialOrder(nodes=[frame_selection, provenance_doc, final_presentation])
po_postproduction.order.add_edge(frame_selection, provenance_doc)
po_postproduction.order.add_edge(provenance_doc, final_presentation)

# Payment: setup → schedule delivery
po_payment = StrictPartialOrder(nodes=[payment_setup, delivery_schedule])
po_payment.order.add_edge(payment_setup, delivery_schedule)

# Aftercare support with optional restoration plan
skip      = SilentTransition()  # if no restoration is needed
xor_rest  = OperatorPOWL(operator=Operator.XOR, children=[skip, restoration_plan])
po_after  = StrictPartialOrder(nodes=[aftercare_support, xor_rest])
po_after.order.add_edge(aftercare_support, xor_rest)

# Root partial order connecting all phases
root = StrictPartialOrder(nodes=[
    client_meet,
    preference_survey,
    loop_feedback,
    po_sourcing,
    po_creation,
    po_postproduction,
    po_payment,
    po_after
])
root.order.add_edge(client_meet,       preference_survey)
root.order.add_edge(preference_survey, loop_feedback)
root.order.add_edge(loop_feedback,     po_sourcing)
root.order.add_edge(po_sourcing,       po_creation)
root.order.add_edge(po_creation,       po_postproduction)
root.order.add_edge(po_postproduction, po_payment)
root.order.add_edge(po_payment,        po_after)