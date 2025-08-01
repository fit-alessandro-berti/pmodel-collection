# Generated from: 2666ef32-bcc6-4713-a927-3f08f7369c60.json
# Description: This process outlines the complex and atypical workflow required to launch a new line of artisan microbrews that combines traditional brewing techniques with experimental ingredients sourced from local foragers. It involves intricate steps from ingredient scouting and seasonal recipe adaptation to regulatory compliance checks and community engagement events. Each activity ensures the product maintains authenticity while meeting safety standards and market demand. The process requires coordination between brewers, botanists, marketing teams, and distribution partners to create a unique product that stands out in a saturated craft beer market. Special attention is given to sustainability, quality control, and iterative feedback loops from tasting panels and early adopters to refine the final brew before mass release.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transition objects
ingredient_scout     = Transition(label="Ingredient Scout")
forager_meet        = Transition(label="Forager Meet")
recipe_draft        = Transition(label="Recipe Draft")
lab_testing         = Transition(label="Lab Testing")
batch_brewing       = Transition(label="Batch Brewing")
quality_audit       = Transition(label="Quality Audit")
tasting_panel       = Transition(label="Tasting Panel")
feedback_review     = Transition(label="Feedback Review")
label_design        = Transition(label="Label Design")
sustainability_check= Transition(label="Sustainability Check")
reg_compliance      = Transition(label="Reg Compliance")
packaging_set       = Transition(label="Packaging Set")
event_planning      = Transition(label="Event Planning")
sales_training      = Transition(label="Sales Training")
distribution_setup  = Transition(label="Distribution Setup")
market_launch       = Transition(label="Market Launch")
customer_survey     = Transition(label="Customer Survey")

# Core brewing/testing sequence
core_seq = StrictPartialOrder(nodes=[lab_testing, batch_brewing, quality_audit])
core_seq.order.add_edge(lab_testing, batch_brewing)
core_seq.order.add_edge(batch_brewing, quality_audit)

# Feedback branch sequence
feedback_seq = StrictPartialOrder(nodes=[tasting_panel, feedback_review])
feedback_seq.order.add_edge(tasting_panel, feedback_review)

# Loop: do core_seq, then optionally do feedback_seq and repeat core_seq, until exit
brew_loop = OperatorPOWL(operator=Operator.LOOP, children=[core_seq, feedback_seq])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ingredient_scout,
    forager_meet,
    recipe_draft,
    brew_loop,
    label_design,
    sustainability_check,
    reg_compliance,
    packaging_set,
    event_planning,
    sales_training,
    distribution_setup,
    market_launch,
    customer_survey
])

# Define the control-flow dependencies
root.order.add_edge(ingredient_scout, forager_meet)
root.order.add_edge(forager_meet, recipe_draft)
root.order.add_edge(recipe_draft, brew_loop)

root.order.add_edge(brew_loop, label_design)
root.order.add_edge(label_design, sustainability_check)
root.order.add_edge(sustainability_check, reg_compliance)

root.order.add_edge(reg_compliance, packaging_set)
root.order.add_edge(packaging_set, event_planning)
root.order.add_edge(event_planning, sales_training)
root.order.add_edge(sales_training, distribution_setup)
root.order.add_edge(distribution_setup, market_launch)
root.order.add_edge(market_launch, customer_survey)