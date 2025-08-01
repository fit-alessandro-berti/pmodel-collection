# Generated from: bf70ebf0-094f-4f21-bf8b-69e865a1ee27.json
# Description: This process involves transforming underutilized urban rooftops into sustainable farming spaces that produce fresh produce for local communities. It includes initial site assessment, structural analysis, sourcing eco-friendly materials, soil preparation with organic compost, installing modular hydroponic systems, setting up rainwater harvesting, integrating renewable energy sources, training local workers on urban agriculture techniques, implementing pest control using natural methods, scheduling crop cycles to maximize yield, conducting regular maintenance and monitoring plant health, facilitating community engagement workshops, managing produce distribution channels, and evaluating environmental impact to ensure ongoing sustainability and scalability of the rooftop farms.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_assess = Transition(label="Site Assess")
structure_check = Transition(label="Structure Check")
material_sourcing = Transition(label="Material Sourcing")
soil_prep = Transition(label="Soil Prep")
hydroponic_install = Transition(label="Hydroponic Install")
water_harvest = Transition(label="Water Harvest")
energy_setup = Transition(label="Energy Setup")
worker_training = Transition(label="Worker Training")
pest_control = Transition(label="Pest Control")
crop_scheduling = Transition(label="Crop Scheduling")
maintenance = Transition(label="Maintenance")
health_monitor = Transition(label="Health Monitor")
community_workshop = Transition(label="Community Workshop")
produce_distrib = Transition(label="Produce Distrib")
impact_review = Transition(label="Impact Review")

# Inner concurrent phase for each crop cycle
inner_cycle = StrictPartialOrder(
    nodes=[
        pest_control,
        maintenance,
        health_monitor,
        produce_distrib
    ]
)
# Loop: schedule crop cycle, then do one cycle, repeat or exit
crop_cycle_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[crop_scheduling, inner_cycle]
)

# Root partial order
root = StrictPartialOrder(
    nodes=[
        site_assess,
        structure_check,
        material_sourcing,
        soil_prep,
        hydroponic_install,
        water_harvest,
        energy_setup,
        worker_training,
        community_workshop,
        crop_cycle_loop,
        impact_review
    ]
)

# Define the control-flow dependencies
root.order.add_edge(site_assess, structure_check)
root.order.add_edge(structure_check, material_sourcing)
root.order.add_edge(material_sourcing, soil_prep)
root.order.add_edge(soil_prep, hydroponic_install)
# Harvest and energy setup can proceed after hydroponic installation
root.order.add_edge(hydroponic_install, water_harvest)
root.order.add_edge(hydroponic_install, energy_setup)
# Worker training proceeds once the core systems are in place
root.order.add_edge(water_harvest, worker_training)
root.order.add_edge(energy_setup, worker_training)
# Community engagement and the crop-cycle loop begin after training
root.order.add_edge(worker_training, community_workshop)
root.order.add_edge(worker_training, crop_cycle_loop)
# Final impact review once workshops and crop cycles complete
root.order.add_edge(community_workshop, impact_review)
root.order.add_edge(crop_cycle_loop, impact_review)