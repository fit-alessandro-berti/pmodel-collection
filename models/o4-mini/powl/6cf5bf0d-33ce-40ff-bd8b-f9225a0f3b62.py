# Generated from: 6cf5bf0d-33ce-40ff-bd8b-f9225a0f3b62.json
# Description: This process manages the end-to-end supply chain of artisan cheese from milk sourcing to final delivery in specialty stores. It involves selecting unique dairy farms based on seasonal milk quality, coordinating traditional cheese aging in controlled environments, ensuring compliance with regional food safety standards, packaging with eco-friendly materials, and managing niche market demand forecasting. The process integrates quality testing, artisan certification, and logistics optimization to maintain product integrity and brand authenticity while adapting to fluctuating agricultural conditions and consumer trends.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
t_milk_sourcing   = Transition(label="Milk Sourcing")
t_quality_testing = Transition(label="Quality Testing")
t_farm_selection  = Transition(label="Farm Selection")

t_pasteurize      = Transition(label="Milk Pasteurize")
t_starter_culture = Transition(label="Starter Culture")
t_curd_formation  = Transition(label="Curd Formation")
t_whey_separation = Transition(label="Whey Separation")
t_molding_cheese  = Transition(label="Molding Cheese")

t_aging_control   = Transition(label="Aging Control")
t_humidity_check  = Transition(label="Humidity Check")
t_flavor_sampling = Transition(label="Flavor Sampling")

t_certification   = Transition(label="Certification")
t_packaging_eco   = Transition(label="Packaging Eco")

t_stock_mgmt      = Transition(label="Stock Management")
t_demand_forecast = Transition(label="Demand Forecast")

t_order_proc      = Transition(label="Order Processing")
t_store_delivery  = Transition(label="Store Delivery")

# 1) Farm sourcing & selection sequence
farm_proc = StrictPartialOrder(
    nodes=[t_milk_sourcing, t_quality_testing, t_farm_selection]
)
farm_proc.order.add_edge(t_milk_sourcing, t_quality_testing)
farm_proc.order.add_edge(t_quality_testing, t_farm_selection)

# 2) Cheese initial production sequence
prod_proc = StrictPartialOrder(
    nodes=[
        t_pasteurize,
        t_starter_culture,
        t_curd_formation,
        t_whey_separation,
        t_molding_cheese,
    ]
)
prod_proc.order.add_edge(t_pasteurize, t_starter_culture)
prod_proc.order.add_edge(t_starter_culture, t_curd_formation)
prod_proc.order.add_edge(t_curd_formation, t_whey_separation)
prod_proc.order.add_edge(t_whey_separation, t_molding_cheese)

# 3) Aging loop: A = one iteration, B = repeat body
aging_body_A = StrictPartialOrder(
    nodes=[t_aging_control, t_humidity_check, t_flavor_sampling]
)
aging_body_A.order.add_edge(t_aging_control, t_humidity_check)
aging_body_A.order.add_edge(t_humidity_check, t_flavor_sampling)

aging_body_B = StrictPartialOrder(
    nodes=[t_aging_control, t_humidity_check, t_flavor_sampling]
)
aging_body_B.order.add_edge(t_aging_control, t_humidity_check)
aging_body_B.order.add_edge(t_humidity_check, t_flavor_sampling)

aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_body_A, aging_body_B]
)

# 4) Packaging & certification
cert_and_pack = StrictPartialOrder(
    nodes=[t_certification, t_packaging_eco]
)
cert_and_pack.order.add_edge(t_certification, t_packaging_eco)

# 5) Parallel stock management and demand forecasting
stock_demand = StrictPartialOrder(
    nodes=[t_stock_mgmt, t_demand_forecast]
)
# no edges => they run in parallel

# 6) Final ordering & delivery
fulfillment = StrictPartialOrder(
    nodes=[t_order_proc, t_store_delivery]
)
fulfillment.order.add_edge(t_order_proc, t_store_delivery)

# 7) Assemble the root partial order
root = StrictPartialOrder(
    nodes=[
        farm_proc,
        prod_proc,
        aging_loop,
        cert_and_pack,
        stock_demand,
        fulfillment
    ]
)

# Establish the control-flow dependencies
root.order.add_edge(farm_proc, prod_proc)
root.order.add_edge(prod_proc, aging_loop)
root.order.add_edge(aging_loop, cert_and_pack)
root.order.add_edge(cert_and_pack, stock_demand)
root.order.add_edge(stock_demand, fulfillment)