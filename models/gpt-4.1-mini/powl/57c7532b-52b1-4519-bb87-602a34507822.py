# Generated from: 57c7532b-52b1-4519-bb87-602a34507822.json
# Description: This process outlines the intricate supply chain of artisan cheese production, from sourcing rare milk varieties from remote farms to aging cheese in specialized microclimates. It involves quality testing at multiple stages, customized packaging based on cheese type, coordinating with boutique retailers, managing seasonal demand fluctuations, and ensuring traceability for food safety compliance. The process also includes collaborative recipe refinement with cheesemakers, digital inventory reconciliation, and international shipping logistics under controlled temperature conditions to maintain product integrity and enhance customer satisfaction in niche markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Recipe_Refinement = Transition(label='Recipe Refinement')
Curd_Formation = Transition(label='Curd Formation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salting_Stage = Transition(label='Salting Stage')
Aging_Setup = Transition(label='Aging Setup')
Microclimate_Control = Transition(label='Microclimate Control')
Inventory_Check = Transition(label='Inventory Check')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Order_Processing = Transition(label='Order Processing')
Retail_Coordination = Transition(label='Retail Coordination')
Shipping_Prep = Transition(label='Shipping Prep')
Temperature_Monitor = Transition(label='Temperature Monitor')
Compliance_Audit = Transition(label='Compliance Audit')
Sales_Feedback = Transition(label='Sales Feedback')
Demand_Forecast = Transition(label='Demand Forecast')

# Loop: Recipe Refinement <--> Milk Sourcing (collaborative refinement and sourcing cycle)
refinement_loop = OperatorPOWL(operator=Operator.LOOP, children=[Milk_Sourcing, Recipe_Refinement])

# Aging partial order: Aging Setup --> Microclimate Control
aging_po = StrictPartialOrder(nodes=[Aging_Setup, Microclimate_Control])
aging_po.order.add_edge(Aging_Setup, Microclimate_Control)

# Packaging partial order: Packaging Design --> Label Printing
packaging_po = StrictPartialOrder(nodes=[Packaging_Design, Label_Printing])
packaging_po.order.add_edge(Packaging_Design, Label_Printing)

# Shipping partial order: Shipping Prep --> Temperature Monitor --> Compliance Audit
shipping_po = StrictPartialOrder(
    nodes=[Shipping_Prep, Temperature_Monitor, Compliance_Audit]
)
shipping_po.order.add_edge(Shipping_Prep, Temperature_Monitor)
shipping_po.order.add_edge(Temperature_Monitor, Compliance_Audit)

# Demand Forecast and Sales Feedback are concurrent, both follow Retail Coordination
# Retail Coordination before Demand Forecast and Sales Feedback
retail_po = StrictPartialOrder(
    nodes=[Retail_Coordination, Demand_Forecast, Sales_Feedback]
)
retail_po.order.add_edge(Retail_Coordination, Demand_Forecast)
retail_po.order.add_edge(Retail_Coordination, Sales_Feedback)

# Inventory Check before Packaging Design and Order Processing
inventory_po = StrictPartialOrder(
    nodes=[Inventory_Check, Packaging_Design, Order_Processing]
)
inventory_po.order.add_edge(Inventory_Check, Packaging_Design)
inventory_po.order.add_edge(Inventory_Check, Order_Processing)

# Cheese production sequence:
# Milk Sourcing & Refinement Loop done first (refinement_loop)
# then Quality Testing
# then Curd Formation --> Pressing Cheese --> Salting Stage --> Aging (aging_po)
production_po = StrictPartialOrder(
    nodes=[refinement_loop, Quality_Testing, Curd_Formation, Pressing_Cheese, Salting_Stage, aging_po]
)
production_po.order.add_edge(refinement_loop, Quality_Testing)
production_po.order.add_edge(Quality_Testing, Curd_Formation)
production_po.order.add_edge(Curd_Formation, Pressing_Cheese)
production_po.order.add_edge(Pressing_Cheese, Salting_Stage)
production_po.order.add_edge(Salting_Stage, aging_po)

# After production comes inventory and retail coordination
post_prod_po = StrictPartialOrder(
    nodes=[production_po, inventory_po, retail_po, packaging_po, Order_Processing, shipping_po]
)
post_prod_po.order.add_edge(production_po, inventory_po)
post_prod_po.order.add_edge(inventory_po, retail_po)
post_prod_po.order.add_edge(inventory_po, packaging_po)
post_prod_po.order.add_edge(packaging_po, Order_Processing)
post_prod_po.order.add_edge(Order_Processing, shipping_po)
post_prod_po.order.add_edge(retail_po, shipping_po)

root = post_prod_po