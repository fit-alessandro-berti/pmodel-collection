# Generated from: 75fe7266-8387-400c-98f9-3f7d788c05a4.json
# Description: This process outlines the detailed steps involved in restoring antique furniture to preserve its historical value while ensuring structural integrity and aesthetic appeal. It begins with initial assessment and authentication, followed by careful disassembly and cleaning. Specialized treatments are applied to repair wood damage and remove old finishes. Surface refinishing involves matching original paint or varnish tones. Reassembly requires precise fitting of components, sometimes fabricating missing parts based on historical research. The final phase includes quality control, documentation of restoration techniques, and client approval. This atypical process demands expertise in conservation science, craftsmanship, and historical knowledge, balancing preservation with usability and market valuation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
assess_item       = Transition(label='Assess Item')
authenticate_piece= Transition(label='Authenticate Piece')
disassemble_parts = Transition(label='Disassemble Parts')
clean_surfaces    = Transition(label='Clean Surfaces')
remove_finish     = Transition(label='Remove Finish')
treat_wood        = Transition(label='Treat Wood')
repair_damage     = Transition(label='Repair Damage')
refinish_surface  = Transition(label='Refinish Surface')
research_history  = Transition(label='Research History')
fabricate_parts   = Transition(label='Fabricate Parts')
reassemble_item   = Transition(label='Reassemble Item')
quality_check     = Transition(label='Quality Check')
document_process  = Transition(label='Document Process')
client_review     = Transition(label='Client Review')
finalize_rest     = Transition(label='Finalize Restoration')
store_securely    = Transition(label='Store Securely')
skip              = SilentTransition()

# Optional fabrication branch: either do research+fabrication or skip
fab_seq = StrictPartialOrder(nodes=[research_history, fabricate_parts])
fab_seq.order.add_edge(research_history, fabricate_parts)
xor_fabrication = OperatorPOWL(operator=Operator.XOR, children=[fab_seq, skip])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    assess_item, authenticate_piece,
    disassemble_parts, clean_surfaces,
    remove_finish, treat_wood, repair_damage,
    refinish_surface, xor_fabrication,
    reassemble_item, quality_check,
    document_process, client_review,
    finalize_rest, store_securely
])

# Define ordering constraints
# Initial assessment and authentication before disassembly
root.order.add_edge(assess_item,       disassemble_parts)
root.order.add_edge(authenticate_piece,disassemble_parts)
# Disassembly before cleaning
root.order.add_edge(disassemble_parts,  clean_surfaces)
# Cleaning before specialized treatments
root.order.add_edge(clean_surfaces,     remove_finish)
root.order.add_edge(clean_surfaces,     treat_wood)
root.order.add_edge(clean_surfaces,     repair_damage)
# All treatments before refinishing
root.order.add_edge(remove_finish,      refinish_surface)
root.order.add_edge(treat_wood,         refinish_surface)
root.order.add_edge(repair_damage,      refinish_surface)
# Refinishing before optional fabrication branch
root.order.add_edge(refinish_surface,   xor_fabrication)
# After fabrication (or skip) reassemble
root.order.add_edge(xor_fabrication,    reassemble_item)
# Reassembly before quality check
root.order.add_edge(reassemble_item,    quality_check)
# Quality check before documentation and client review
root.order.add_edge(quality_check,      document_process)
root.order.add_edge(quality_check,      client_review)
# Documentation and client review before finalization
root.order.add_edge(document_process,   finalize_rest)
root.order.add_edge(client_review,      finalize_rest)
# Finalization before storage
root.order.add_edge(finalize_rest,      store_securely)