# Generated from: 5ed12412-62bf-4b1e-87aa-a1f446601261.json
# Description: This process describes the complex supply chain and quality assurance workflow involved in the artisan cheese trade, from farm sourcing to boutique retail delivery. It includes unique activities such as milk terroir analysis, microbial culture selection, aging environment calibration, and sensory panel evaluation. The process integrates traditional craftsmanship with modern quality control, involving multiple stakeholders including dairy farmers, microbiologists, master cheesemakers, logistics coordinators, and specialty retailers. Each cheese batch undergoes rigorous testing and certification before packaging and distribution, ensuring product authenticity and premium quality for discerning customers across diverse markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
farm_audit           = Transition(label='Farm Audit')
milk_testing        = Transition(label='Milk Testing')
culture_prep        = Transition(label='Culture Prep')
coagulation_start   = Transition(label='Coagulation Start')
curd_cutting        = Transition(label='Curd Cutting')
whey_draining       = Transition(label='Whey Draining')
molding_press       = Transition(label='Molding Press')
salting_bath        = Transition(label='Salting Bath')
aging_setup         = Transition(label='Aging Setup')
humidity_control    = Transition(label='Humidity Control')
microbe_check       = Transition(label='Microbe Check')
flavor_profiling    = Transition(label='Flavor Profiling')
packaging_prep      = Transition(label='Packaging Prep')
label_printing      = Transition(label='Label Printing')
order_sorting       = Transition(label='Order Sorting')
transport_scheduling= Transition(label='Transport Scheduling')
retail_delivery     = Transition(label='Retail Delivery')

# Loop for environment calibration + microbe check
loop_env = OperatorPOWL(
    operator=Operator.LOOP,
    children=[humidity_control, microbe_check]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    farm_audit,
    milk_testing,
    culture_prep,
    coagulation_start,
    curd_cutting,
    whey_draining,
    molding_press,
    salting_bath,
    aging_setup,
    loop_env,
    flavor_profiling,
    packaging_prep,
    label_printing,
    order_sorting,
    transport_scheduling,
    retail_delivery
])

# Define the control-flow dependencies
root.order.add_edge(farm_audit,            milk_testing)
root.order.add_edge(milk_testing,          culture_prep)
root.order.add_edge(culture_prep,          coagulation_start)
root.order.add_edge(coagulation_start,     curd_cutting)
root.order.add_edge(coagulation_start,     whey_draining)
root.order.add_edge(curd_cutting,          molding_press)
root.order.add_edge(whey_draining,         molding_press)
root.order.add_edge(molding_press,         salting_bath)
root.order.add_edge(salting_bath,          aging_setup)
root.order.add_edge(aging_setup,           loop_env)
root.order.add_edge(loop_env,              flavor_profiling)
root.order.add_edge(flavor_profiling,      packaging_prep)
root.order.add_edge(packaging_prep,        label_printing)
root.order.add_edge(label_printing,        order_sorting)
root.order.add_edge(order_sorting,         transport_scheduling)
root.order.add_edge(transport_scheduling,  retail_delivery)