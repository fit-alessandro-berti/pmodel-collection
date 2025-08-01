# Generated from: 67b6bc49-7d25-485d-b414-132e5919e2e3.json
# Description: This process involves the careful evaluation, documentation, and restoration of antique artifacts to preserve their historical integrity while enhancing their aesthetic appeal. It includes detailed condition assessments, sourcing of period-accurate materials, delicate cleaning procedures, and expert craftsmanship to repair damages without compromising originality. Continuous consultation with historians and material scientists ensures authenticity. The process concludes with final quality checks, certification, and preparation for display or sale, balancing conservation ethics with market demands.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities as POWL transitions
intake = Transition(label='Artifact Intake')
hist_research = Transition(label='Historical Research')
cond_survey = Transition(label='Condition Survey')
material_sourcing = Transition(label='Material Sourcing')
cleaning_prep = Transition(label='Cleaning Prep')
surface_cleaning = Transition(label='Surface Cleaning')
structural_repair = Transition(label='Structural Repair')
finish_restoration = Transition(label='Finish Restoration')
expert_consultation = Transition(label='Expert Consultation')
documentation = Transition(label='Documentation')
quality_review = Transition(label='Quality Review')
certification = Transition(label='Certification')
packaging = Transition(label='Packaging')
display_setup = Transition(label='Display Setup')
client_handover = Transition(label='Client Handover')

# Build the partial order (root)
root = StrictPartialOrder(nodes=[
    intake,
    hist_research,
    cond_survey,
    material_sourcing,
    cleaning_prep,
    surface_cleaning,
    structural_repair,
    finish_restoration,
    expert_consultation,
    documentation,
    quality_review,
    certification,
    packaging,
    display_setup,
    client_handover
])

# Artifact Intake precedes Research and Survey
root.order.add_edge(intake, hist_research)
root.order.add_edge(intake, cond_survey)

# Research and Survey both precede Documentation
root.order.add_edge(hist_research, documentation)
root.order.add_edge(cond_survey, documentation)

# Research precedes Material Sourcing
root.order.add_edge(hist_research, material_sourcing)

# Documentation, Sourcing, and Expert Consultation precede Cleaning Prep
root.order.add_edge(documentation, cleaning_prep)
root.order.add_edge(material_sourcing, cleaning_prep)
root.order.add_edge(expert_consultation, cleaning_prep)

# Expert Consultation requires Research, Survey, and Sourcing
root.order.add_edge(hist_research, expert_consultation)
root.order.add_edge(cond_survey, expert_consultation)
root.order.add_edge(material_sourcing, expert_consultation)

# Cleaning workflow
root.order.add_edge(cleaning_prep, surface_cleaning)
root.order.add_edge(surface_cleaning, structural_repair)
root.order.add_edge(structural_repair, finish_restoration)

# Finalization workflow
root.order.add_edge(finish_restoration, quality_review)
root.order.add_edge(quality_review, certification)
root.order.add_edge(certification, packaging)
root.order.add_edge(packaging, display_setup)
root.order.add_edge(display_setup, client_handover)