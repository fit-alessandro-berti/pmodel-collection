# Generated from: 5446dd11-a6f8-4479-87d3-d82632dba1db.json
# Description: This process outlines the complex supply chain of artisanal cheese production, starting from sourcing rare local milk varieties, ensuring microbial cultures are cultivated in controlled environments, and managing precise aging conditions. It involves batch testing for quality, coordinating with seasonal farmers, integrating traditional handcraft techniques with modern hygiene standards, managing niche market orders, and handling export regulatory compliance. The process also covers waste management, packaging optimization for delicate transport, and consumer feedback integration to continuously refine cheese profiles while preserving artisanal authenticity and sustainability goals.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Prep = Transition(label='Culture Prep')
Batch_Testing = Transition(label='Batch Testing')
Coagulation = Transition(label='Coagulation')
Curd_Cutting = Transition(label='Curd Cutting')
Mold_Inoculation = Transition(label='Mold Inoculation')
Pressing = Transition(label='Pressing')
Salting = Transition(label='Salting')
Aging_Setup = Transition(label='Aging Setup')
Humidity_Control = Transition(label='Humidity Control')
Quality_Check = Transition(label='Quality Check')
Packaging = Transition(label='Packaging')
Order_Processing = Transition(label='Order Processing')
Export_Compliance = Transition(label='Export Compliance')
Waste_Disposal = Transition(label='Waste Disposal')
Market_Analysis = Transition(label='Market Analysis')
Feedback_Review = Transition(label='Feedback Review')

# Construct partial orders reflecting the supply chain sequence
# Start: Milk Sourcing -> Culture Prep -> Batch Testing

start_PO = StrictPartialOrder(nodes=[Milk_Sourcing, Culture_Prep, Batch_Testing])
start_PO.order.add_edge(Milk_Sourcing, Culture_Prep)
start_PO.order.add_edge(Culture_Prep, Batch_Testing)

# Cheese production order: Coagulation -> Curd Cutting -> Mold Inoculation -> Pressing -> Salting
production_PO = StrictPartialOrder(
    nodes=[Coagulation, Curd_Cutting, Mold_Inoculation, Pressing, Salting]
)
production_PO.order.add_edge(Coagulation, Curd_Cutting)
production_PO.order.add_edge(Curd_Cutting, Mold_Inoculation)
production_PO.order.add_edge(Mold_Inoculation, Pressing)
production_PO.order.add_edge(Pressing, Salting)

# Aging process loop including Aging Setup and Humidity Control, with Quality Check

aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        Aging_Setup,  # A in loop
        OperatorPOWL(
            operator=Operator.XOR,
            children=[Humidity_Control, Quality_Check],  # B in loop alternative choices
        ),
    ],
)

# Packaging after aging loop
packaging_PO = StrictPartialOrder(nodes=[aging_loop, Packaging])
packaging_PO.order.add_edge(aging_loop, Packaging)

# Order processing and export compliance after packaging
order_export_PO = StrictPartialOrder(nodes=[Packaging, Order_Processing, Export_Compliance])
order_export_PO.order.add_edge(Packaging, Order_Processing)
order_export_PO.order.add_edge(Order_Processing, Export_Compliance)

# Waste disposal can run concurrently after Salting and Packaging processes finish
waste_PO = StrictPartialOrder(nodes=[Salting, Packaging, Waste_Disposal])
waste_PO.order.add_edge(Salting, Waste_Disposal)
waste_PO.order.add_edge(Packaging, Waste_Disposal)

# Market analysis and feedback review run after export compliance, in partial order
market_feedback_PO = StrictPartialOrder(nodes=[Export_Compliance, Market_Analysis, Feedback_Review])
market_feedback_PO.order.add_edge(Export_Compliance, Market_Analysis)
market_feedback_PO.order.add_edge(Market_Analysis, Feedback_Review)

# Combine main parts via partial order: start_PO -> production_PO -> packaging_PO -> order_export_PO -> market_feedback_PO and include waste_PO concurrency

root = StrictPartialOrder(
    nodes=[start_PO, production_PO, packaging_PO, order_export_PO, market_feedback_PO, waste_PO]
)
root.order.add_edge(start_PO, production_PO)
root.order.add_edge(production_PO, packaging_PO)
root.order.add_edge(packaging_PO, order_export_PO)
root.order.add_edge(order_export_PO, market_feedback_PO)

# waste_PO depends concurrently on production_PO and packaging_PO (Salting and Packaging)
root.order.add_edge(production_PO, waste_PO)
root.order.add_edge(packaging_PO, waste_PO)