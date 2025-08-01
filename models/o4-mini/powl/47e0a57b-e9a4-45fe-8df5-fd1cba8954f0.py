# Generated from: 47e0a57b-e9a4-45fe-8df5-fd1cba8954f0.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a densely populated city. It includes site selection based on environmental factors, modular infrastructure design, integration of IoT sensors for climate control, hydroponic system assembly, automated nutrient delivery calibration, energy sourcing from renewables, pest management through biological agents, crop selection for optimal yield, staff training on technology use, regulatory compliance checks, real-time monitoring setup, harvest scheduling, packaging with sustainable materials, distribution logistics coordination, and continuous system optimization using AI analytics to maximize productivity and minimize environmental impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_select = Transition(label='Site Select')
design_modules = Transition(label='Design Modules')
install_sensors = Transition(label='Install Sensors')
assemble_hydroponics = Transition(label='Assemble Hydroponics')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
source_energy = Transition(label='Source Energy')
manage_pests = Transition(label='Manage Pests')
select_crops = Transition(label='Select Crops')
train_staff = Transition(label='Train Staff')
check_compliance = Transition(label='Check Compliance')
setup_monitoring = Transition(label='Setup Monitoring')
schedule_harvest = Transition(label='Schedule Harvest')
package_produce = Transition(label='Package Produce')
coordinate_logistics = Transition(label='Coordinate Logistics')
optimize_systems = Transition(label='Optimize Systems')

# Build the main workflow as a strict partial order (everything in sequence)
main_pipeline = StrictPartialOrder(nodes=[
    site_select,
    design_modules,
    install_sensors,
    assemble_hydroponics,
    calibrate_nutrients,
    source_energy,
    manage_pests,
    select_crops,
    train_staff,
    check_compliance,
    setup_monitoring,
    schedule_harvest,
    package_produce,
    coordinate_logistics
])

# Add the sequential edges
edges = [
    (site_select, design_modules),
    (design_modules, install_sensors),
    (install_sensors, assemble_hydroponics),
    (assemble_hydroponics, calibrate_nutrients),
    (calibrate_nutrients, source_energy),
    (source_energy, manage_pests),
    (manage_pests, select_crops),
    (select_crops, train_staff),
    (train_staff, check_compliance),
    (check_compliance, setup_monitoring),
    (setup_monitoring, schedule_harvest),
    (schedule_harvest, package_produce),
    (package_produce, coordinate_logistics)
]
for src, tgt in edges:
    main_pipeline.order.add_edge(src, tgt)

# Model continuous system optimization as a loop around the main pipeline
# LOOP(children=[A, B]) means: do A, then either exit or do B then A again, etc.
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_pipeline, optimize_systems]
)