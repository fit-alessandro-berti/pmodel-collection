# Generated from: 6cf5bf0d-33ce-40ff-bd8b-f9225a0f3b62.json
# Description: This process manages the end-to-end supply chain of artisan cheese from milk sourcing to final delivery in specialty stores. It involves selecting unique dairy farms based on seasonal milk quality, coordinating traditional cheese aging in controlled environments, ensuring compliance with regional food safety standards, packaging with eco-friendly materials, and managing niche market demand forecasting. The process integrates quality testing, artisan certification, and logistics optimization to maintain product integrity and brand authenticity while adapting to fluctuating agricultural conditions and consumer trends.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transition objects
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Farm_Selection = Transition(label='Farm Selection')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Starter_Culture = Transition(label='Starter Culture')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Molding_Cheese = Transition(label='Molding Cheese')
Aging_Control = Transition(label='Aging Control')
Humidity_Check = Transition(label='Humidity Check')
Flavor_Sampling = Transition(label='Flavor Sampling')
Certification = Transition(label='Certification')
Packaging_Eco = Transition(label='Packaging Eco')
Stock_Management = Transition(label='Stock Management')
Demand_Forecast = Transition(label='Demand Forecast')
Order_Processing = Transition(label='Order Processing')
Store_Delivery = Transition(label='Store Delivery')

# Build partial orders respecting the described process

# Initial sourcing and selection - Milk Sourcing -> Quality Testing -> Farm Selection
initial_PO = StrictPartialOrder(nodes=[Milk_Sourcing, Quality_Testing, Farm_Selection])
initial_PO.order.add_edge(Milk_Sourcing, Quality_Testing)
initial_PO.order.add_edge(Quality_Testing, Farm_Selection)

# Milk processing through pasteurization and starter culture, then curd and whey
milk_process_PO = StrictPartialOrder(nodes=[Milk_Pasteurize, Starter_Culture, Curd_Formation, Whey_Separation])
milk_process_PO.order.add_edge(Milk_Pasteurize, Starter_Culture)
milk_process_PO.order.add_edge(Starter_Culture, Curd_Formation)
milk_process_PO.order.add_edge(Curd_Formation, Whey_Separation)

# Molding, aging control including humidity check and flavor sampling (parallel)
aging_checks_PO = StrictPartialOrder(nodes=[Humidity_Check, Flavor_Sampling])
# Humidity_Check and Flavor_Sampling are concurrent (no edges)

aging_PO = StrictPartialOrder(nodes=[Molding_Cheese, Aging_Control, aging_checks_PO])
aging_PO.order.add_edge(Molding_Cheese, Aging_Control)
aging_PO.order.add_edge(Aging_Control, aging_checks_PO)

# Certification must happen after aging checks complete (both Humidity_Check and Flavor_Sampling done)
cert_PO = StrictPartialOrder(nodes=[aging_PO, Certification])
cert_PO.order.add_edge(aging_PO, Certification)

# Packaging eco is after certification
packaging_PO = StrictPartialOrder(nodes=[cert_PO, Packaging_Eco])
packaging_PO.order.add_edge(cert_PO, Packaging_Eco)

# Stock management and demand forecast run in parallel after packaging
stock_and_demand_PO = StrictPartialOrder(nodes=[Stock_Management, Demand_Forecast])
# They are concurrent (no edges)

# Order Processing after both stock management and demand forecast
order_proc_PO = StrictPartialOrder(nodes=[stock_and_demand_PO, Order_Processing])
order_proc_PO.order.add_edge(stock_and_demand_PO, Order_Processing)

# Delivery after order processing
delivery_PO = StrictPartialOrder(nodes=[order_proc_PO, Store_Delivery])
delivery_PO.order.add_edge(order_proc_PO, Store_Delivery)

# Combine the main flows in sequence using a big PO:
root = StrictPartialOrder(
    nodes=[
        initial_PO,
        milk_process_PO,
        packaging_PO,
        order_proc_PO,
        delivery_PO
    ]
)

# Define ordering between main phases:
root.order.add_edge(initial_PO, milk_process_PO)
root.order.add_edge(milk_process_PO, packaging_PO)
root.order.add_edge(packaging_PO, order_proc_PO)
root.order.add_edge(order_proc_PO, delivery_PO)