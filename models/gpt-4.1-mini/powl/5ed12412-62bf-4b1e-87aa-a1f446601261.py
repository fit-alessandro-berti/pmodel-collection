# Generated from: 5ed12412-62bf-4b1e-87aa-a1f446601261.json
# Description: This process describes the complex supply chain and quality assurance workflow involved in the artisan cheese trade, from farm sourcing to boutique retail delivery. It includes unique activities such as milk terroir analysis, microbial culture selection, aging environment calibration, and sensory panel evaluation. The process integrates traditional craftsmanship with modern quality control, involving multiple stakeholders including dairy farmers, microbiologists, master cheesemakers, logistics coordinators, and specialty retailers. Each cheese batch undergoes rigorous testing and certification before packaging and distribution, ensuring product authenticity and premium quality for discerning customers across diverse markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
farm_audit = Transition(label='Farm Audit')
milk_testing = Transition(label='Milk Testing')
culture_prep = Transition(label='Culture Prep')
coagulation_start = Transition(label='Coagulation Start')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_press = Transition(label='Molding Press')
salting_bath = Transition(label='Salting Bath')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_profiling = Transition(label='Flavor Profiling')
microbe_check = Transition(label='Microbe Check')
packaging_prep = Transition(label='Packaging Prep')
label_printing = Transition(label='Label Printing')
order_sorting = Transition(label='Order Sorting')
transport_scheduling = Transition(label='Transport Scheduling')
retail_delivery = Transition(label='Retail Delivery')

# Build partial orders representing main flows with some concurrency where logical
# Initial supply chain quality checks happen sequentially
initial_checks = StrictPartialOrder(
    nodes=[farm_audit, milk_testing]
)
initial_checks.order.add_edge(farm_audit, milk_testing)

# Culture preparation and coagulation start sequential
prep_and_coag = StrictPartialOrder(
    nodes=[culture_prep, coagulation_start]
)
prep_and_coag.order.add_edge(culture_prep, coagulation_start)

# Cheese processing steps partially ordered:
# curd cutting -> whey draining -> molding press -> salting bath
cheese_processing = StrictPartialOrder(
    nodes=[curd_cutting, whey_draining, molding_press, salting_bath]
)
cheese_processing.order.add_edge(curd_cutting, whey_draining)
cheese_processing.order.add_edge(whey_draining, molding_press)
cheese_processing.order.add_edge(molding_press, salting_bath)

# Aging and quality controls partially ordered but concurrent where possible
aging_quality = StrictPartialOrder(
    nodes=[aging_setup, humidity_control, flavor_profiling, microbe_check]
)
aging_quality.order.add_edge(aging_setup, humidity_control)
aging_quality.order.add_edge(aging_setup, flavor_profiling)
aging_quality.order.add_edge(aging_setup, microbe_check)

# Packaging prep and label printing sequential
packaging = StrictPartialOrder(
    nodes=[packaging_prep, label_printing]
)
packaging.order.add_edge(packaging_prep, label_printing)

# Order sorting, transport scheduling, and retail delivery partially ordered:
# order sorting -> transport scheduling -> retail delivery
logistics = StrictPartialOrder(
    nodes=[order_sorting, transport_scheduling, retail_delivery]
)
logistics.order.add_edge(order_sorting, transport_scheduling)
logistics.order.add_edge(transport_scheduling, retail_delivery)

# Compose process top-level partial order integrating all above subprocesses

root = StrictPartialOrder(nodes=[
    initial_checks,
    prep_and_coag,
    cheese_processing,
    aging_quality,
    packaging,
    logistics
])

# Define global control flow order edges:
# 1. initial_checks -> prep_and_coag
root.order.add_edge(initial_checks, prep_and_coag)
# 2. prep_and_coag -> cheese_processing
root.order.add_edge(prep_and_coag, cheese_processing)
# 3. cheese_processing -> aging_quality
root.order.add_edge(cheese_processing, aging_quality)
# 4. aging_quality -> packaging
root.order.add_edge(aging_quality, packaging)
# 5. packaging -> logistics
root.order.add_edge(packaging, logistics)