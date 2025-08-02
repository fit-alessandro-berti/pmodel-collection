# Generated from: 4bafa746-7cd3-40ad-b921-fe364b2331ed.json
# Description: This process involves the sourcing, aging, quality testing, and distribution of handcrafted artisan cheeses from small farms to specialty retailers and exclusive restaurants. It includes selecting raw milk suppliers based on seasonal yield, managing aging conditions with precise humidity and temperature controls, performing microbial assessments, coordinating packaging with unique branding, and arranging logistics that ensure freshness while complying with international food safety regulations. The process also incorporates feedback loops from retailers on flavor profiles and demand forecasting to adjust production volumes and diversify cheese varieties offered in the market.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for activities
Milk_Sourcing = Transition(label='Milk Sourcing')
Supplier_Vetting = Transition(label='Supplier Vetting')
Milk_Testing = Transition(label='Milk Testing')
Curd_Preparation = Transition(label='Curd Preparation')
Pressing_Cheese = Transition(label='Pressing Cheese')
Salt_Application = Transition(label='Salt Application')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Microbial_Testing = Transition(label='Microbial Testing')
Flavor_Sampling = Transition(label='Flavor Sampling')
Packaging_Design = Transition(label='Packaging Design')
Label_Printing = Transition(label='Label Printing')
Order_Processing = Transition(label='Order Processing')
Transport_Scheduling = Transition(label='Transport Scheduling')
Retail_Feedback = Transition(label='Retail Feedback')
Demand_Forecast = Transition(label='Demand Forecast')
Inventory_Audit = Transition(label='Inventory Audit')

# Partial order for the initial sourcing and checking raw milk
sourcing_PO = StrictPartialOrder(
    nodes=[Milk_Sourcing, Supplier_Vetting, Milk_Testing],
)
sourcing_PO.order.add_edge(Milk_Sourcing, Supplier_Vetting)
sourcing_PO.order.add_edge(Supplier_Vetting, Milk_Testing)

# Partial order for cheese preparation steps
cheese_prep_PO = StrictPartialOrder(
    nodes=[Curd_Preparation, Pressing_Cheese, Salt_Application],
)
cheese_prep_PO.order.add_edge(Curd_Preparation, Pressing_Cheese)
cheese_prep_PO.order.add_edge(Pressing_Cheese, Salt_Application)

# Loop for aging with control and microbial testing with feedback loop
aging_control_PO = StrictPartialOrder(
    nodes=[Aging_Setup, Humidity_Control, Microbial_Testing],
)
aging_control_PO.order.add_edge(Aging_Setup, Humidity_Control)
aging_control_PO.order.add_edge(Humidity_Control, Microbial_Testing)

# Feedback loop from Retail Feedback and Demand Forecast with Inventory Audit influences production
# Define feedback activities as a sequential PO
feedback_PO = StrictPartialOrder(
    nodes=[Retail_Feedback, Demand_Forecast, Inventory_Audit],
)
feedback_PO.order.add_edge(Retail_Feedback, Demand_Forecast)
feedback_PO.order.add_edge(Demand_Forecast, Inventory_Audit)

# Loop node: After Microbial Testing, decide to exit loop or perform flavor sampling and feedback then loop again
loop_body_PO = StrictPartialOrder(
    nodes=[Flavor_Sampling, feedback_PO],
)
loop_body_PO.order.add_edge(Flavor_Sampling, feedback_PO)

# Loop: execute Aging_Control_PO, then choose to exit or do flavor sampling & feedback then aging again
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control_PO, loop_body_PO])

# Packaging partial order (design and label printing concurrent)
packaging_PO = StrictPartialOrder(
    nodes=[Packaging_Design, Label_Printing],
)
# Packaging_Design and Label_Printing are concurrent, no edges

# Distribution partial order (order processing -> transport scheduling)
distribution_PO = StrictPartialOrder(
    nodes=[Order_Processing, Transport_Scheduling],
)
distribution_PO.order.add_edge(Order_Processing, Transport_Scheduling)

# Construct full process partial order:
# sourcing_PO -> cheese_prep_PO -> loop (aging with feedback) -> packaging_PO & distribution_PO concurrent
root = StrictPartialOrder(
    nodes=[sourcing_PO, cheese_prep_PO, loop, packaging_PO, distribution_PO],
)
root.order.add_edge(sourcing_PO, cheese_prep_PO)
root.order.add_edge(cheese_prep_PO, loop)
root.order.add_edge(loop, packaging_PO)
root.order.add_edge(loop, distribution_PO)