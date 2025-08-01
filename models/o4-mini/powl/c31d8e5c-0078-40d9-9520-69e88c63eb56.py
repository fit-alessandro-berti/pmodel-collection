# Generated from: c31d8e5c-0078-40d9-9520-69e88c63eb56.json
# Description: This process outlines the complex steps involved in establishing an urban rooftop farming project within a metropolitan environment. It includes initial site assessment, structural analysis, securing permits, soil testing, irrigation system design, sourcing organic seeds, installing hydroponic units, integrating renewable energy sources, implementing pest control measures, setting up monitoring sensors, training staff, marketing produce, managing harvest cycles, waste recycling, and final reporting. The process requires coordination among architects, agronomists, city officials, and marketing teams to ensure a sustainable and profitable urban agriculture venture that maximizes limited rooftop space while adhering to city regulations and environmental standards.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey    = Transition(label='Site Survey')
load_test      = Transition(label='Load Test')
permit_apply   = Transition(label='Permit Apply')
soil_sample    = Transition(label='Soil Sample')
irrigation_plan= Transition(label='Irrigation Plan')
energy_setup   = Transition(label='Energy Setup')
install_units  = Transition(label='Install Units')
sensor_setup   = Transition(label='Sensor Setup')
pest_control   = Transition(label='Pest Control')
staff_training = Transition(label='Staff Training')
seed_order     = Transition(label='Seed Order')
crop_planting  = Transition(label='Crop Planting')
harvest_log    = Transition(label='Harvest Log')
waste_sort     = Transition(label='Waste Sort')
market_launch  = Transition(label='Market Launch')

# Build the body of the loop (harvest → waste sort → market)
harvest_cycle_po = StrictPartialOrder(
    nodes=[harvest_log, waste_sort, market_launch]
)
harvest_cycle_po.order.add_edge(harvest_log, waste_sort)
harvest_cycle_po.order.add_edge(waste_sort, market_launch)

# LOOP: plant crops, then do one cycle of harvest/marketing/waste, repeat until exit
harvest_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[crop_planting, harvest_cycle_po]
)

# Assemble the full process as a strict partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        load_test,
        permit_apply,
        soil_sample,
        irrigation_plan,
        energy_setup,
        install_units,
        sensor_setup,
        pest_control,
        staff_training,
        seed_order,
        harvest_loop
    ]
)

# Define the sequential control-flow
sequence = [
    site_survey,
    load_test,
    permit_apply,
    soil_sample,
    irrigation_plan,
    energy_setup,
    install_units,
    sensor_setup,
    pest_control,
    staff_training,
    seed_order,
    harvest_loop
]
for prev, nxt in zip(sequence, sequence[1:]):
    root.order.add_edge(prev, nxt)