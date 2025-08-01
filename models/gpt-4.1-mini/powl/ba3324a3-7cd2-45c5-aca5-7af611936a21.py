# Generated from: ba3324a3-7cd2-45c5-aca5-7af611936a21.json
# Description: This process outlines the intricate creation of bespoke artisanal perfumes, combining traditional techniques with modern sensory analysis. It involves sourcing rare botanicals, maceration, multiple distillation steps, olfactory testing with expert panels, precise blending, aging in controlled environments, and custom packaging. The process ensures each fragrance is unique, balanced, and aligned with client preferences, requiring iterative adjustments and quality assurance before final delivery to niche markets or private collectors, emphasizing craftsmanship and exclusivity.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Botanical_Sourcing = Transition(label='Botanical Sourcing')
Raw_Sorting = Transition(label='Raw Sorting')
Initial_Maceration = Transition(label='Initial Maceration')
Steam_Distill = Transition(label='Steam Distill')
Solvent_Extraction = Transition(label='Solvent Extraction')
Olfactory_Testing = Transition(label='Olfactory Testing')
Blend_Trial = Transition(label='Blend Trial')
Concentration_Adjust = Transition(label='Concentration Adjust')
Aging_Process = Transition(label='Aging Process')
Quality_Check = Transition(label='Quality Check')
Client_Feedback = Transition(label='Client Feedback')
Blend_Revision = Transition(label='Blend Revision')
Final_Dilution = Transition(label='Final Dilution')
Bottle_Filling = Transition(label='Bottle Filling')
Custom_Labeling = Transition(label='Custom Labeling')
Packaging_Design = Transition(label='Packaging Design')
Dispatch_Prep = Transition(label='Dispatch Prep')

# Loop body: blend trial -> concentration adjust -> aging process -> quality check -> client feedback -> blend revision
# After blend revision, loop back to blend trial for iteration
loop_body_nodes = [
    Blend_Trial,
    Concentration_Adjust,
    Aging_Process,
    Quality_Check,
    Client_Feedback,
    Blend_Revision
]
loop_body = StrictPartialOrder(nodes=loop_body_nodes)
loop_body.order.add_edge(Blend_Trial, Concentration_Adjust)
loop_body.order.add_edge(Concentration_Adjust, Aging_Process)
loop_body.order.add_edge(Aging_Process, Quality_Check)
loop_body.order.add_edge(Quality_Check, Client_Feedback)
loop_body.order.add_edge(Client_Feedback, Blend_Revision)

# The loop operator:
# A = Blend_Trial (the "do" part)
# B = rest of loop_body without Blend_Trial (the "redo" part)
# According to POWL LOOP definition, loop = *(A, B)
# but B should be the sequence after A excluding A itself
# So split loop_body: 
# A = Blend_Trial
# B = Concentration_Adjust -> Aging_Process -> Quality_Check -> Client_Feedback -> Blend_Revision

# Build B partial order
B_nodes = [
    Concentration_Adjust,
    Aging_Process,
    Quality_Check,
    Client_Feedback,
    Blend_Revision
]
B = StrictPartialOrder(nodes=B_nodes)
B.order.add_edge(Concentration_Adjust, Aging_Process)
B.order.add_edge(Aging_Process, Quality_Check)
B.order.add_edge(Quality_Check, Client_Feedback)
B.order.add_edge(Client_Feedback, Blend_Revision)

loop = OperatorPOWL(operator=Operator.LOOP, children=[Blend_Trial, B])

# Partial order before loop:
# Botanical sourcing -> raw sorting -> initial maceration
# Then two parallel distillation ways: steam distill and solvent extraction (concurrent)
# After which Olfactory Testing starts (which depends on both distillation methods)
# Then loop starts
# After loop finishes, final dilution, bottle filling, custom labeling, packaging design, dispatch prep in strict order

root_nodes = [
    Botanical_Sourcing, Raw_Sorting, Initial_Maceration,
    Steam_Distill, Solvent_Extraction,
    Olfactory_Testing,
    loop,
    Final_Dilution, Bottle_Filling, Custom_Labeling,
    Packaging_Design, Dispatch_Prep
]

root = StrictPartialOrder(nodes=root_nodes)

# sequence edges before parallel distillation:
root.order.add_edge(Botanical_Sourcing, Raw_Sorting)
root.order.add_edge(Raw_Sorting, Initial_Maceration)

# initial maceration enables steam distill and solvent extraction (concurrent)
root.order.add_edge(Initial_Maceration, Steam_Distill)
root.order.add_edge(Initial_Maceration, Solvent_Extraction)

# both distillation must finish before olfactory testing
root.order.add_edge(Steam_Distill, Olfactory_Testing)
root.order.add_edge(Solvent_Extraction, Olfactory_Testing)

# olfactory testing before loop
root.order.add_edge(Olfactory_Testing, loop)

# after loop, continue strictly
root.order.add_edge(loop, Final_Dilution)
root.order.add_edge(Final_Dilution, Bottle_Filling)
root.order.add_edge(Bottle_Filling, Custom_Labeling)
root.order.add_edge(Custom_Labeling, Packaging_Design)
root.order.add_edge(Packaging_Design, Dispatch_Prep)