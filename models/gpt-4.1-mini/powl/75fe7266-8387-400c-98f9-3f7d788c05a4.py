# Generated from: 75fe7266-8387-400c-98f9-3f7d788c05a4.json
# Description: This process outlines the detailed steps involved in restoring antique furniture to preserve its historical value while ensuring structural integrity and aesthetic appeal. It begins with initial assessment and authentication, followed by careful disassembly and cleaning. Specialized treatments are applied to repair wood damage and remove old finishes. Surface refinishing involves matching original paint or varnish tones. Reassembly requires precise fitting of components, sometimes fabricating missing parts based on historical research. The final phase includes quality control, documentation of restoration techniques, and client approval. This atypical process demands expertise in conservation science, craftsmanship, and historical knowledge, balancing preservation with usability and market valuation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Activities
Assess_Item = Transition(label='Assess Item')
Authenticate_Piece = Transition(label='Authenticate Piece')
Disassemble_Parts = Transition(label='Disassemble Parts')
Clean_Surfaces = Transition(label='Clean Surfaces')
Remove_Finish = Transition(label='Remove Finish')
Treat_Wood = Transition(label='Treat Wood')
Repair_Damage = Transition(label='Repair Damage')
Research_History = Transition(label='Research History')
Fabricate_Parts = Transition(label='Fabricate Parts')
Refinish_Surface = Transition(label='Refinish Surface')
Reassemble_Item = Transition(label='Reassemble Item')
Quality_Check = Transition(label='Quality Check')
Document_Process = Transition(label='Document Process')
Client_Review = Transition(label='Client Review')
Finalize_Restoration = Transition(label='Finalize Restoration')
Store_Securely = Transition(label='Store Securely')

# Structure:
# Initial assessment and authentication
assessment = StrictPartialOrder(nodes=[Assess_Item, Authenticate_Piece])
assessment.order.add_edge(Assess_Item, Authenticate_Piece)

# Disassembly and cleaning (disassembly before cleaning)
disassembly_cleaning = StrictPartialOrder(nodes=[Disassemble_Parts, Clean_Surfaces])
disassembly_cleaning.order.add_edge(Disassemble_Parts, Clean_Surfaces)

# Specialized treatments: remove finish --> repair via treat wood and repair damage (these two concurrent)
treatments_inner = StrictPartialOrder(nodes=[Treat_Wood, Repair_Damage])
# no edges between Treat_Wood and Repair_Damage (concurrent)
treatments = StrictPartialOrder(nodes=[Remove_Finish, treatments_inner])
treatments.order.add_edge(Remove_Finish, treatments_inner)

# Surface refinishing after treatments
surface_refinishing = RefInish = Refinish_Surface  # shorthand

# Reassembly: may fabricate parts based on historical research first (research and fabricate concurrent)
research_fabricate = StrictPartialOrder(nodes=[Research_History, Fabricate_Parts])
# concurrent, no edges

reassembly = StrictPartialOrder(nodes=[research_fabricate, Reassemble_Item])
reassembly.order.add_edge(research_fabricate, Reassemble_Item)

# Final phase: quality check --> documentation --> client review (choice: finalize or store securely)

final_review = StrictPartialOrder(nodes=[Quality_Check, Document_Process, Client_Review])
final_review.order.add_edge(Quality_Check, Document_Process)
final_review.order.add_edge(Document_Process, Client_Review)

final_choice = OperatorPOWL(operator=Operator.XOR, children=[Finalize_Restoration, Store_Securely])

final_phase = StrictPartialOrder(nodes=[final_review, final_choice])
final_phase.order.add_edge(final_review, final_choice)

# Combine all main phases in order
nodes = [
    assessment,
    disassembly_cleaning,
    treatments,
    Refinish_Surface,
    reassembly,
    final_phase
]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(assessment, disassembly_cleaning)
root.order.add_edge(disassembly_cleaning, treatments)
root.order.add_edge(treatments, Refinish_Surface)
root.order.add_edge(Refinish_Surface, reassembly)
root.order.add_edge(reassembly, final_phase)