# Generated from: ba10c964-d8ba-4cc0-bf55-b049daa2ca6a.json
# Description: This process outlines the end-to-end supply chain for artisan cheese, beginning with milk sourcing from local farms, quality testing, and fermentation monitoring. It includes unique steps such as microbial culture selection, aging environment control, and flavor profiling. The process also covers packaging with sustainable materials, direct-to-consumer marketing, and inventory rotation based on sensory evaluation. Additionally, it handles regulatory compliance specific to dairy and organic certifications, coordinates seasonal production variations, and integrates customer feedback for continuous recipe refinement, ensuring a premium product that balances tradition and innovation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Culture_Selection = Transition(label='Culture Selection')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Formation = Transition(label='Curd Formation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Process = Transition(label='Salting Process')
Fermentation_Check = Transition(label='Fermentation Check')
Aging_Control = Transition(label='Aging Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Prep = Transition(label='Packaging Prep')
Sustainable_Wrap = Transition(label='Sustainable Wrap')
Inventory_Rotate = Transition(label='Inventory Rotate')
Marketing_Launch = Transition(label='Marketing Launch')
Customer_Feedback = Transition(label='Customer Feedback')
Compliance_Review = Transition(label='Compliance Review')
Seasonal_Adjust = Transition(label='Seasonal Adjust')
Recipe_Update = Transition(label='Recipe Update')

# Partial order for initial milk treatment and cheese formation
milk_treatment = StrictPartialOrder(
    nodes=[Milk_Sourcing, Quality_Testing, Culture_Selection, Milk_Pasteurize,
           Curd_Formation, Pressing_Cheese, Salting_Process])
milk_treatment.order.add_edge(Milk_Sourcing, Quality_Testing)
milk_treatment.order.add_edge(Quality_Testing, Culture_Selection)
milk_treatment.order.add_edge(Culture_Selection, Milk_Pasteurize)
milk_treatment.order.add_edge(Milk_Pasteurize, Curd_Formation)
milk_treatment.order.add_edge(Curd_Formation, Pressing_Cheese)
milk_treatment.order.add_edge(Pressing_Cheese, Salting_Process)

# Partial order for fermentation and aging with checks and profiling
fermentation_aging = StrictPartialOrder(
    nodes=[Fermentation_Check, Aging_Control, Flavor_Profiling])
fermentation_aging.order.add_edge(Fermentation_Check, Aging_Control)
fermentation_aging.order.add_edge(Aging_Control, Flavor_Profiling)

# Packaging partial order (Packaging Prep and Sustainable Wrap concurrent)
packaging = StrictPartialOrder(
    nodes=[Packaging_Prep, Sustainable_Wrap])
# no order between Packaging Prep and Sustainable Wrap (concurrent)

# Marketing and Inventory partial order
marketing_inventory = StrictPartialOrder(
    nodes=[Inventory_Rotate, Marketing_Launch])
# no order between Inventory Rotate and Marketing Launch (concurrent)

# Compliance Review is before Seasonal Adjust and Recipe Update
compliance_seasonal_recipe = StrictPartialOrder(
    nodes=[Compliance_Review, Seasonal_Adjust, Recipe_Update])
compliance_seasonal_recipe.order.add_edge(Compliance_Review, Seasonal_Adjust)
compliance_seasonal_recipe.order.add_edge(Compliance_Review, Recipe_Update)

# Customer Feedback precedes Recipe Update for continuous refinement
customer_feedback_loop = StrictPartialOrder(
    nodes=[Customer_Feedback, Recipe_Update])
customer_feedback_loop.order.add_edge(Customer_Feedback, Recipe_Update)

# Combine recipe update with a loop to model continuous refinement with feedback
recipe_refinement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Recipe_Update,
        Customer_Feedback
    ])

# Now build the overall process partial order
# Structure:

# Start: milk_treatment
# then fermentation_aging
# then packaging
# then marketing_inventory
# Concurrent with marketing_inventory are compliance_seasonal_recipe and recipe_refinement_loop

root = StrictPartialOrder(
    nodes=[milk_treatment, fermentation_aging, packaging,
           marketing_inventory, compliance_seasonal_recipe, recipe_refinement_loop])

# Add edges according to described ordering
root.order.add_edge(milk_treatment, fermentation_aging)
root.order.add_edge(fermentation_aging, packaging)
root.order.add_edge(packaging, marketing_inventory)
# compliance_seasonal_recipe and recipe_refinement_loop start after packaging, concurrent with marketing_inventory
root.order.add_edge(packaging, compliance_seasonal_recipe)
root.order.add_edge(packaging, recipe_refinement_loop)

# No edge between marketing_inventory, compliance_seasonal_recipe, recipe_refinement_loop to allow concurrency