# Generated from: ba3324a3-7cd2-45c5-aca5-7af611936a21.json
# Description: This process outlines the intricate creation of bespoke artisanal perfumes, combining traditional techniques with modern sensory analysis. It involves sourcing rare botanicals, maceration, multiple distillation steps, olfactory testing with expert panels, precise blending, aging in controlled environments, and custom packaging. The process ensures each fragrance is unique, balanced, and aligned with client preferences, requiring iterative adjustments and quality assurance before final delivery to niche markets or private collectors, emphasizing craftsmanship and exclusivity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
botanical = Transition(label='Botanical Sourcing')
raw_sorting = Transition(label='Raw Sorting')
initial_maceration = Transition(label='Initial Maceration')
steam_distill = Transition(label='Steam Distill')
solvent_extraction = Transition(label='Solvent Extraction')
olfactory_testing = Transition(label='Olfactory Testing')
blend_trial = Transition(label='Blend Trial')
concentration_adjust = Transition(label='Concentration Adjust')
aging_process = Transition(label='Aging Process')
quality_check = Transition(label='Quality Check')
client_feedback = Transition(label='Client Feedback')
blend_revision = Transition(label='Blend Revision')
final_dilution = Transition(label='Final Dilution')
bottle_filling = Transition(label='Bottle Filling')
custom_labeling = Transition(label='Custom Labeling')
packaging_design = Transition(label='Packaging Design')
dispatch_prep = Transition(label='Dispatch Prep')

# Build the loop body for iterative adjustments
adjustments = StrictPartialOrder(nodes=[
    concentration_adjust,
    aging_process,
    quality_check,
    client_feedback,
    blend_revision
])
adjustments.order.add_edge(concentration_adjust, aging_process)
adjustments.order.add_edge(aging_process, quality_check)
adjustments.order.add_edge(quality_check, client_feedback)
adjustments.order.add_edge(client_feedback, blend_revision)

# Define the loop: do a Blend Trial, then either exit or perform adjustments and repeat
iterative_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[blend_trial, adjustments]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    botanical,
    raw_sorting,
    initial_maceration,
    steam_distill,
    solvent_extraction,
    olfactory_testing,
    iterative_loop,
    final_dilution,
    bottle_filling,
    custom_labeling,
    packaging_design,
    dispatch_prep
])

# Initial sequence up to distillation
root.order.add_edge(botanical, raw_sorting)
root.order.add_edge(raw_sorting, initial_maceration)
# Parallel distillation branches
root.order.add_edge(initial_maceration, steam_distill)
root.order.add_edge(initial_maceration, solvent_extraction)
# Both distillations must complete before testing
root.order.add_edge(steam_distill, olfactory_testing)
root.order.add_edge(solvent_extraction, olfactory_testing)
# Testing leads into the iterative blending loop
root.order.add_edge(olfactory_testing, iterative_loop)
# After the loop, finalize and package
root.order.add_edge(iterative_loop, final_dilution)
root.order.add_edge(final_dilution, bottle_filling)
# Labeling and design can proceed in parallel after filling
root.order.add_edge(bottle_filling, custom_labeling)
root.order.add_edge(bottle_filling, packaging_design)
# Both must complete before dispatch preparation
root.order.add_edge(custom_labeling, dispatch_prep)
root.order.add_edge(packaging_design, dispatch_prep)