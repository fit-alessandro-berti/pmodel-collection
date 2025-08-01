# Generated from: fbd0a280-a097-4b20-bd85-a45e775b26c9.json
# Description: This process outlines the complex operational cycle of an urban vertical farming enterprise that integrates advanced hydroponics, AI-driven climate control, and community engagement. The workflow begins with seed selection and germination optimization, followed by nutrient formulation and precise water management. Real-time monitoring through IoT sensors enables adaptive lighting and airflow adjustments. Concurrently, crop health assessments using multispectral imaging guide pest control and disease prevention strategies without chemicals. Harvesting is carefully timed to maximize yield quality, after which produce undergoes immediate cold storage and packaging within the facility. Finally, logistics coordination ensures same-day delivery to local markets and subscription customers, while feedback loops from sales and customer input drive continuous process improvements and sustainability initiatives.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
seed_selection    = Transition(label='Seed Selection')
germination_setup = Transition(label='Germination Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
water_control     = Transition(label='Water Control')
sensor_monitor    = Transition(label='Sensor Monitor')
climate_adjust    = Transition(label='Climate Adjust')
lighting_tune     = Transition(label='Lighting Tune')
airflow_manage    = Transition(label='Airflow Manage')
health_scan       = Transition(label='Health Scan')
pest_control      = Transition(label='Pest Control')
harvest_timing    = Transition(label='Harvest Timing')
cold_storage      = Transition(label='Cold Storage')
package_prep      = Transition(label='Package Prep')
delivery_plan     = Transition(label='Delivery Plan')
feedback_loop     = Transition(label='Feedback Loop')

# Build the main partial‐order of the process
main_seq = StrictPartialOrder(nodes=[
    seed_selection, germination_setup,
    nutrient_mix, water_control,
    sensor_monitor,
    climate_adjust, lighting_tune, airflow_manage,
    health_scan, pest_control,
    harvest_timing, cold_storage,
    package_prep, delivery_plan
])

# Define the ordering (dependencies)
# 1. Seed -> Germination
main_seq.order.add_edge(seed_selection, germination_setup)
# 2. Germination -> Nutrient Mix -> Water Control
main_seq.order.add_edge(germination_setup, nutrient_mix)
main_seq.order.add_edge(nutrient_mix, water_control)
# 3. Water Control -> Sensor Monitor
main_seq.order.add_edge(water_control, sensor_monitor)
# 4. Sensor Monitor -> Climate Adjust, Lighting Tune, Airflow Manage, Health Scan
for tgt in (climate_adjust, lighting_tune, airflow_manage, health_scan):
    main_seq.order.add_edge(sensor_monitor, tgt)
# 5. Health Scan -> Pest Control
main_seq.order.add_edge(health_scan, pest_control)
# 6. After environmental & health tasks -> Harvest Timing
for src in (climate_adjust, lighting_tune, airflow_manage, pest_control):
    main_seq.order.add_edge(src, harvest_timing)
# 7. Harvest -> Cold Storage -> Package Prep -> Delivery Plan
main_seq.order.add_edge(harvest_timing, cold_storage)
main_seq.order.add_edge(cold_storage, package_prep)
main_seq.order.add_edge(package_prep, delivery_plan)

# Wrap in a loop with feedback
root = OperatorPOWL(
    operator=Operator.LOOP,
    children=[main_seq, feedback_loop]
)