# Generated from: e9759ed7-771a-49ab-add7-c2b5dbd165e6.json
# Description: This process details the intricate steps involved in creating a bespoke artisanal perfume, starting from sourcing rare natural ingredients globally, through careful extraction and blending techniques, to aging and final packaging. The workflow requires coordination between botanists, chemists, and marketing teams to ensure the scent's uniqueness, quality, and market appeal. It includes testing for allergen compliance, custom bottle design, and limited edition release scheduling, making it a complex, multi-disciplinary process that balances creativity with regulatory and commercial considerations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Ingredient_Sourcing = Transition(label='Ingredient Sourcing')
Sample_Testing = Transition(label='Sample Testing')
Oil_Extraction = Transition(label='Oil Extraction')
Blend_Formulation = Transition(label='Blend Formulation')
Quality_Control = Transition(label='Quality Control')
Aging_Process = Transition(label='Aging Process')
Allergen_Check = Transition(label='Allergen Check')
Market_Research = Transition(label='Market Research')
Bottle_Design = Transition(label='Bottle Design')
Label_Approval = Transition(label='Label Approval')
Packaging_Setup = Transition(label='Packaging Setup')
Batch_Mixing = Transition(label='Batch Mixing')
Scent_Profiling = Transition(label='Scent Profiling')
Client_Feedback = Transition(label='Client Feedback')
Release_Scheduling = Transition(label='Release Scheduling')
Regulatory_Review = Transition(label='Regulatory Review')
Sales_Training = Transition(label='Sales Training')

# Create partial orders for sub-processes
# 1. Ingredient sourcing and initial testing
sourcing_testing = StrictPartialOrder(nodes=[Ingredient_Sourcing, Sample_Testing])
sourcing_testing.order.add_edge(Ingredient_Sourcing, Sample_Testing)

# 2. Oil extraction after testing
extraction = StrictPartialOrder(nodes=[sourcing_testing, Oil_Extraction])
extraction.order.add_edge(sourcing_testing, Oil_Extraction)

# 3. Blend formulation after extraction
blend = StrictPartialOrder(nodes=[extraction, Blend_Formulation])
blend.order.add_edge(extraction, Blend_Formulation)

# 4. Batch mixing in parallel with quality control and allergen check after blend formulation
batch_mixing = Batch_Mixing
quality_control = Quality_Control
allergen_check = Allergen_Check
mix_quality_allergen = StrictPartialOrder(
    nodes=[batch_mixing, quality_control, allergen_check])
# They start concurrently after blend formulation
po_mix_quality_allergen = StrictPartialOrder(
    nodes=[blend, mix_quality_allergen])
po_mix_quality_allergen.order.add_edge(blend, mix_quality_allergen)

# 5. Aging process after batch mixing
aging_after_mix = StrictPartialOrder(
    nodes=[batch_mixing, Aging_Process])
aging_after_mix.order.add_edge(batch_mixing, Aging_Process)

# Adjust to combine batch mixing -> aging, and quality control/allergen check parallel
# Build a partial order where:
# blend -> batch_mixing -> aging_process
# blend -> quality_control (parallel)
# blend -> allergen_check (parallel)

blend_and_follow = StrictPartialOrder(
    nodes=[blend, batch_mixing, Aging_Process, quality_control, allergen_check])
blend_and_follow.order.add_edge(blend, batch_mixing)
blend_and_follow.order.add_edge(batch_mixing, Aging_Process)
blend_and_follow.order.add_edge(blend, quality_control)
blend_and_follow.order.add_edge(blend, allergen_check)
# quality_control and allergen_check are concurrent with (batch_mixing->aging)

# 6. Scent profiling and client feedback after aging
profiling = StrictPartialOrder(
    nodes=[Aging_Process, Scent_Profiling])
profiling.order.add_edge(Aging_Process, Scent_Profiling)

feedback = StrictPartialOrder(
    nodes=[profiling, Client_Feedback])
feedback.order.add_edge(profiling, Client_Feedback)

# 7. Market research and regulatory review in parallel after blend formulation
market_and_regulatory = StrictPartialOrder(nodes=[Market_Research, Regulatory_Review])
# after blend formulation
blend_to_marketreg = StrictPartialOrder(
    nodes=[blend, market_and_regulatory])
blend_to_marketreg.order.add_edge(blend, market_and_regulatory)

# 8. Bottle design after market research
bottle_after_market = StrictPartialOrder(
    nodes=[Market_Research, Bottle_Design])
bottle_after_market.order.add_edge(Market_Research, Bottle_Design)

# 9. Label approval after bottle design and allergen check
label_approval_po = StrictPartialOrder(
    nodes=[Bottle_Design, Allergen_Check, Label_Approval])
label_approval_po.order.add_edge(Bottle_Design, Label_Approval)
label_approval_po.order.add_edge(Allergen_Check, Label_Approval)

# 10. Packaging setup after label approval and aging process
packaging_setup_po = StrictPartialOrder(
    nodes=[Label_Approval, Aging_Process, Packaging_Setup])
packaging_setup_po.order.add_edge(Label_Approval, Packaging_Setup)
packaging_setup_po.order.add_edge(Aging_Process, Packaging_Setup)

# 11. Release scheduling after client feedback and regulatory review
release_sched_po = StrictPartialOrder(
    nodes=[Client_Feedback, Regulatory_Review, Release_Scheduling])
release_sched_po.order.add_edge(Client_Feedback, Release_Scheduling)
release_sched_po.order.add_edge(Regulatory_Review, Release_Scheduling)

# 12. Sales training after release scheduling
sales_training_po = StrictPartialOrder(
    nodes=[Release_Scheduling, Sales_Training])
sales_training_po.order.add_edge(Release_Scheduling, Sales_Training)

# Combine Bottle Design subtree with Label Approval subtree:
bottle_label = StrictPartialOrder(
    nodes=[bottle_after_market, label_approval_po])
bottle_label.order.add_edge(bottle_after_market, label_approval_po)

# Combine Packaging with Bottle/Label subtree
packaging_full = StrictPartialOrder(
    nodes=[bottle_label, packaging_setup_po])
packaging_full.order.add_edge(bottle_label, packaging_setup_po)

# Now combine main parallel branches after blend formulation:
# blend_and_follow (batch mixing, aging, quality, allergen)
# market_and_regulatory (market research, regulatory review)
# profiling and feedback (after aging)
# release scheduling and sales training (after feedback and regulatory)

# Create parallel nodes following blend:
# We already have blend_and_follow and blend_to_marketreg including blend

# Let's merge blend_and_follow and blend_to_marketreg into blend_extended:
blend_extended = StrictPartialOrder(
    nodes=[blend_and_follow, market_and_regulatory])
blend_extended.order.add_edge(blend_and_follow, market_and_regulatory)  # To serialize these, or leave concurrent?

# Actually they can be concurrent after blend:
# So create a PO with blend node and two concurrent nodes after it
blend_after = StrictPartialOrder(nodes=[blend, blend_and_follow, market_and_regulatory])
blend_after.order.add_edge(blend, blend_and_follow)
blend_after.order.add_edge(blend, market_and_regulatory)
# blend_and_follow and market_and_regulatory run concurrently after blend

# Now attach Profiling+Client Feedback after Aging_Process inside blend_and_follow
# Aging_Process is inside blend_and_follow.nodes

# Instead attach profiling and feedback sequences after Aging_Process node in blend_and_follow
# So merge blend_and_follow and profiling feedback into one PO with edges aging->scent profiling->client feedback

# Build a new PO for that:

aging_profiling_feedback = StrictPartialOrder(
    nodes=[Aging_Process, Scent_Profiling, Client_Feedback])
aging_profiling_feedback.order.add_edge(Aging_Process, Scent_Profiling)
aging_profiling_feedback.order.add_edge(Scent_Profiling, Client_Feedback)

# blend_and_follow is:
# blend -> batch_mixing -> Aging_Process
# blend -> quality_control
# blend -> allergen_check

# Replace Aging_Process node in blend_and_follow by aging_profiling_feedback

# So instead of Aging_Process as separate, integrate aging_profiling_feedback

# New blend_and_follow_extended PO

blend_and_follow_extended = StrictPartialOrder(
    nodes=[blend, Batch_Mixing, quality_control, allergen_check,
           aging_profiling_feedback])
blend_and_follow_extended.order.add_edge(blend, Batch_Mixing)
blend_and_follow_extended.order.add_edge(Batch_Mixing, aging_profiling_feedback)
blend_and_follow_extended.order.add_edge(blend, quality_control)
blend_and_follow_extended.order.add_edge(blend, allergen_check)

# Now parallel branches after blend are blend_and_follow_extended and market_and_regulatory, running concurrently

# Assemble final PO from blend, two parallel branches, bottle_label (which includes market research), packaging_full (which depends on label_approval and aging), and release + sales

# Actually market research and regulatory review are in market_and_regulatory

# bottle_label depends on Market_Research and Allergen_Check

# packaging_full depends on label_approval and Aging_Process (aging part is in aging_profiling_feedback)

# release_sched_po depends on Client_Feedback and Regulatory_Review (Regulatory_Review in market_and_regulatory)

# Assemble the entire structure with correct edges:

root = StrictPartialOrder(nodes=[
    Ingredient_Sourcing,
    Sample_Testing,
    Oil_Extraction,
    Blend_Formulation,
    blend_and_follow_extended,
    market_and_regulatory,
    bottle_label,
    packaging_setup_po,
    release_sched_po,
    sales_training_po
])

# Set edges according to dependencies:

# Ingredient_Sourcing -> Sample_Testing -> Oil_Extraction -> Blend_Formulation
root.order.add_edge(Ingredient_Sourcing, Sample_Testing)
root.order.add_edge(Sample_Testing, Oil_Extraction)
root.order.add_edge(Oil_Extraction, Blend_Formulation)

# Blend_Formulation -> blend_and_follow_extended (contains batch mixing etc.)
root.order.add_edge(Blend_Formulation, blend_and_follow_extended)

# Blend_Formulation -> market_and_regulatory (Market Research and Regulatory Review)
root.order.add_edge(Blend_Formulation, market_and_regulatory)

# Market Research inside market_and_regulatory -> Bottle Design (bottle_label subtree)
root.order.add_edge(market_and_regulatory, bottle_label)

# Allergen Check inside blend_and_follow_extended -> Label Approval (inside bottle_label)
root.order.add_edge(blend_and_follow_extended, bottle_label)

# Label Approval -> Packaging Setup (packaging_setup_po)
root.order.add_edge(bottle_label, packaging_setup_po)

# Aging Process inside blend_and_follow_extended (via aging_profiling_feedback) -> Packaging Setup
root.order.add_edge(blend_and_follow_extended, packaging_setup_po)

# Client Feedback inside blend_and_follow_extended (aging_profiling_feedback node Client Feedback) -> Release Scheduling (release_sched_po)
root.order.add_edge(blend_and_follow_extended, release_sched_po)

# Regulatory Review inside market_and_regulatory -> Release Scheduling (release_sched_po)
root.order.add_edge(market_and_regulatory, release_sched_po)

# Release Scheduling -> Sales Training
root.order.add_edge(release_sched_po, sales_training_po)