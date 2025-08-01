# Generated from: c4d0932a-0550-47d9-bda9-d857c439a42a.json
# Description: This process details the end-to-end supply chain management of artisanal cheese production, starting from raw milk sourcing from small farms, through quality testing, fermentation monitoring, and aging in controlled environments. It includes packaging customization, seasonal demand forecasting, niche marketing strategies, distribution via boutique retailers, and feedback collection from connoisseurs to continuously refine the product. The process integrates traditional craftsmanship with modern traceability technology to ensure authenticity and compliance with food safety standards, while maintaining the unique characteristics that distinguish artisanal cheese in a competitive marketplace.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as Transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Starter_Culture = Transition(label='Starter Culture')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Cheese = Transition(label='Molding Cheese')
Pressing_Block = Transition(label='Pressing Block')
Brining_Bath = Transition(label='Brining Bath')
Aging_Control = Transition(label='Aging Control')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Design = Transition(label='Packaging Design')
Demand_Forecast = Transition(label='Demand Forecast')
Retail_Outreach = Transition(label='Retail Outreach')
Customer_Feedback = Transition(label='Customer Feedback')

# Define partial orders to represent sequential and partially concurrent tasks

# Milk Sourcing --> Quality Testing
sourcing_and_testing = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing])
sourcing_and_testing.order.add_edge(Milk_Sourcing, Quality_Testing)

# Starter Culture --> Coagulation --> Curd Cutting --> Whey Draining --> Molding Cheese --> Pressing Block --> Brining Bath --> Aging Control --> Flavor Profiling
# define fixed chain for cheese production steps
cheese_production_nodes = [
    Starter_Culture,
    Coagulation,
    Curd_Cutting,
    Whey_Draining,
    Molding_Cheese,
    Pressing_Block,
    Brining_Bath,
    Aging_Control,
    Flavor_Profiling
]
cheese_production = StrictPartialOrder(nodes=cheese_production_nodes)
for i in range(len(cheese_production_nodes)-1):
    cheese_production.order.add_edge(cheese_production_nodes[i], cheese_production_nodes[i+1])

# Packaging Design and Demand Forecast happen after Flavor Profiling, but can be parallel
packaging_and_demand = StrictPartialOrder(nodes=[Packaging_Design, Demand_Forecast, Flavor_Profiling])
packaging_and_demand.order.add_edge(Flavor_Profiling, Packaging_Design)
packaging_and_demand.order.add_edge(Flavor_Profiling, Demand_Forecast)

# Retail Outreach after Demand Forecast
retail_outreach = StrictPartialOrder(nodes=[Demand_Forecast, Retail_Outreach])
retail_outreach.order.add_edge(Demand_Forecast, Retail_Outreach)

# Customer Feedback after Retail Outreach and Packaging Design (both must be done)
feedback = StrictPartialOrder(nodes=[Packaging_Design, Retail_Outreach, Customer_Feedback])
feedback.order.add_edge(Packaging_Design, Customer_Feedback)
feedback.order.add_edge(Retail_Outreach, Customer_Feedback)

# Combine all partial orders maintaining order dependencies:

# Step 1: sourcing_and_testing
# Step 2: cheese_production starts only after Quality Testing finished (from sourcing_and_testing)
# Step 3: packaging_and_demand after Flavor Profiling (end of cheese_production)
# Step 4: retail_outreach after Demand Forecast (in packaging_and_demand)
# Step 5: feedback after Packaging Design and Retail Outreach

# Let's create a root PO combining all nodes
nodes = [
    Milk_Sourcing, Quality_Testing,
    Starter_Culture, Coagulation, Curd_Cutting, Whey_Draining,
    Molding_Cheese, Pressing_Block, Brining_Bath, Aging_Control, Flavor_Profiling,
    Packaging_Design, Demand_Forecast, Retail_Outreach, Customer_Feedback
]

root = StrictPartialOrder(nodes=nodes)

# Add order edges for sourcing_and_testing
root.order.add_edge(Milk_Sourcing, Quality_Testing)

# Link Quality Testing to Starter Culture (start cheese production only after testing)
root.order.add_edge(Quality_Testing, Starter_Culture)

# Cheese production edges in sequence
for i in range(len(cheese_production_nodes)-1):
    root.order.add_edge(cheese_production_nodes[i], cheese_production_nodes[i+1])

# From Flavor Profiling to Packaging Design and Demand Forecast (parallel after Flavor Profiling)
root.order.add_edge(Flavor_Profiling, Packaging_Design)
root.order.add_edge(Flavor_Profiling, Demand_Forecast)

# Demand Forecast to Retail Outreach
root.order.add_edge(Demand_Forecast, Retail_Outreach)

# Packaging Design and Retail Outreach to Customer Feedback
root.order.add_edge(Packaging_Design, Customer_Feedback)
root.order.add_edge(Retail_Outreach, Customer_Feedback)