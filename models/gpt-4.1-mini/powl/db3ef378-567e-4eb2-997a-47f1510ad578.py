# Generated from: db3ef378-567e-4eb2-997a-47f1510ad578.json
# Description: This process outlines the complex and atypical supply chain for artisan cheese production, emphasizing the coordination between small-scale dairy farms, quality-controlled aging facilities, and niche distribution channels. The process involves raw milk collection from specialized breeds, microbial culture preparation, curd formation, controlled aging under precise humidity and temperature, artisanal packaging, and direct-to-consumer marketing through exclusive events and subscription models. It integrates traceability at each step, ensuring compliance with regional food safety laws while maintaining the unique flavor profiles that distinguish the product in a competitive market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions
Milk_Collection = Transition(label='Milk Collection')
Culture_Prep = Transition(label='Culture Prep')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Initial_Aging = Transition(label='Initial Aging')
Humidity_Control = Transition(label='Humidity Control')
Temperature_Check = Transition(label='Temperature Check')
Flavor_Testing = Transition(label='Flavor Testing')
Final_Aging = Transition(label='Final Aging')
Packaging_Artisanal = Transition(label='Packaging Artisanal')
Label_Printing = Transition(label='Label Printing')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Fulfillment = Transition(label='Order Fulfillment')
Subscription_Setup = Transition(label='Subscription Setup')
Event_Marketing = Transition(label='Event Marketing')

# Partial order for initial milk processing
milk_processing = StrictPartialOrder(
    nodes=[
        Milk_Collection,
        Culture_Prep,
        Curd_Formation,
        Whey_Separation,
        Molding_Cheese,
        Salting_Process
    ]
)
milk_processing.order.add_edge(Milk_Collection, Culture_Prep)
milk_processing.order.add_edge(Culture_Prep, Curd_Formation)
milk_processing.order.add_edge(Curd_Formation, Whey_Separation)
milk_processing.order.add_edge(Whey_Separation, Molding_Cheese)
milk_processing.order.add_edge(Molding_Cheese, Salting_Process)

# Partial order for controlled aging conditions
aging_conditions = StrictPartialOrder(
    nodes=[Humidity_Control, Temperature_Check]
)
# These two can be concurrent, so no edges

# Partial order for aging and quality testing
aging_and_testing = StrictPartialOrder(
    nodes=[Initial_Aging, aging_conditions, Flavor_Testing, Final_Aging]
)
aging_and_testing.order.add_edge(Initial_Aging, aging_conditions)
aging_and_testing.order.add_edge(aging_conditions, Flavor_Testing)
aging_and_testing.order.add_edge(Flavor_Testing, Final_Aging)

# Partial order for packaging and labeling
packaging_and_labeling = StrictPartialOrder(
    nodes=[Packaging_Artisanal, Label_Printing]
)
packaging_and_labeling.order.add_edge(Packaging_Artisanal, Label_Printing)

# Partial order for distribution channels (concurrent)
distribution = StrictPartialOrder(
    nodes=[Inventory_Audit, Order_Fulfillment, Subscription_Setup, Event_Marketing]
)
# no edges: all concurrent

# Build overall partial order with ordering between phases
root = StrictPartialOrder(
    nodes=[
        milk_processing,
        aging_and_testing,
        packaging_and_labeling,
        distribution
    ]
)

# Define execution order between phases
root.order.add_edge(milk_processing, aging_and_testing)
root.order.add_edge(aging_and_testing, packaging_and_labeling)
root.order.add_edge(packaging_and_labeling, distribution)