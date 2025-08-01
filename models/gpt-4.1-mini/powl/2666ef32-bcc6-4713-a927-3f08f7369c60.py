# Generated from: 2666ef32-bcc6-4713-a927-3f08f7369c60.json
# Description: This process outlines the complex and atypical workflow required to launch a new line of artisan microbrews that combines traditional brewing techniques with experimental ingredients sourced from local foragers. It involves intricate steps from ingredient scouting and seasonal recipe adaptation to regulatory compliance checks and community engagement events. Each activity ensures the product maintains authenticity while meeting safety standards and market demand. The process requires coordination between brewers, botanists, marketing teams, and distribution partners to create a unique product that stands out in a saturated craft beer market. Special attention is given to sustainability, quality control, and iterative feedback loops from tasting panels and early adopters to refine the final brew before mass release.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Ingredient_Scout = Transition(label='Ingredient Scout')
Recipe_Draft = Transition(label='Recipe Draft')
Forager_Meet = Transition(label='Forager Meet')
Lab_Testing = Transition(label='Lab Testing')
Batch_Brewing = Transition(label='Batch Brewing')
Quality_Audit = Transition(label='Quality Audit')
Label_Design = Transition(label='Label Design')
Reg_Compliance = Transition(label='Reg Compliance')
Tasting_Panel = Transition(label='Tasting Panel')
Feedback_Review = Transition(label='Feedback Review')
Packaging_Set = Transition(label='Packaging Set')
Market_Launch = Transition(label='Market Launch')
Event_Planning = Transition(label='Event Planning')
Sales_Training = Transition(label='Sales Training')
Distribution_Setup = Transition(label='Distribution Setup')
Sustainability_Check = Transition(label='Sustainability Check')
Customer_Survey = Transition(label='Customer Survey')

# Loop: Tasting Panel and Feedback Review iterative refinement
panel_feedback_loop = OperatorPOWL(
    operator=Operator.LOOP, 
    children=[Tasting_Panel, Feedback_Review]
)

# Initial ingredient and recipe preparation partial order
ingredient_and_recipe = StrictPartialOrder(
    nodes=[Ingredient_Scout, Forager_Meet, Recipe_Draft]
)
ingredient_and_recipe.order.add_edge(Ingredient_Scout, Recipe_Draft)
ingredient_and_recipe.order.add_edge(Forager_Meet, Recipe_Draft)

# Brewing, testing, and quality audit partial order
brewing_and_quality = StrictPartialOrder(
    nodes=[Batch_Brewing, Lab_Testing, Quality_Audit]
)
brewing_and_quality.order.add_edge(Batch_Brewing, Lab_Testing)
brewing_and_quality.order.add_edge(Lab_Testing, Quality_Audit)

# Packaging and launch partial order
packaging_and_launch = StrictPartialOrder(
    nodes=[Label_Design, Packaging_Set, Market_Launch]
)
packaging_and_launch.order.add_edge(Label_Design, Packaging_Set)
packaging_and_launch.order.add_edge(Packaging_Set, Market_Launch)

# Coordination partial order for regulatory, sustainability, and community
coordination = StrictPartialOrder(
    nodes=[Reg_Compliance, Sustainability_Check, Event_Planning, Sales_Training, Distribution_Setup, Customer_Survey]
)
coordination.order.add_edge(Reg_Compliance, Sales_Training)
coordination.order.add_edge(Sustainability_Check, Sales_Training)
coordination.order.add_edge(Event_Planning, Sales_Training)
coordination.order.add_edge(Sales_Training, Distribution_Setup)
coordination.order.add_edge(Distribution_Setup, Customer_Survey)

# Overall preparation order:
# 1) Ingredient and Recipe
# 2) Brewing and Quality
# 3) Loop of Tasting Panel and Feedback Review repeated until exit
# 4) Packaging and Launch
# 5) Coordination
root = StrictPartialOrder(
    nodes=[
        ingredient_and_recipe, 
        brewing_and_quality, 
        panel_feedback_loop, 
        packaging_and_launch, 
        coordination
    ]
)
root.order.add_edge(ingredient_and_recipe, brewing_and_quality)
root.order.add_edge(brewing_and_quality, panel_feedback_loop)
root.order.add_edge(panel_feedback_loop, packaging_and_launch)
root.order.add_edge(packaging_and_launch, coordination)