# Generated from: 6f060d21-5a8f-4064-a468-3cafaf4e9523.json
# Description: This process describes the comprehensive cycle of urban vertical farming, integrating sustainable agriculture with advanced technology in densely populated environments. It begins with site analysis and environmental calibration, followed by automated seeding and nutrient optimization. Continuous monitoring through IoT sensors ensures ideal growth conditions. The system adapts lighting and irrigation dynamically based on plant health data. Pest detection is managed through AI-driven imaging, reducing chemical use. Harvesting is executed by robotic units, and produce is quality-checked before packaging. Finally, logistics coordinate rapid delivery to local markets, maintaining freshness and minimizing carbon footprint. This atypical but realistic process exemplifies future-forward urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
site_analysis      = Transition(label='Site Analysis')
env_calibration    = Transition(label='Env Calibration')
seed_automation    = Transition(label='Seed Automation')
nutrient_mix       = Transition(label='Nutrient Mix')
iot_monitoring     = Transition(label='IoT Monitoring')
light_adjustment   = Transition(label='Light Adjustment')
irrigation_control = Transition(label='Irrigation Control')
health_scanning    = Transition(label='Health Scanning')
pest_detection     = Transition(label='Pest Detection')
ai_imaging         = Transition(label='AI Imaging')
robotic_harvest    = Transition(label='Robotic Harvest')
quality_check      = Transition(label='Quality Check')
packaging_prep     = Transition(label='Packaging Prep')
cold_storage       = Transition(label='Cold Storage')
logistics_plan     = Transition(label='Logistics Plan')
market_delivery    = Transition(label='Market Delivery')

# Partial order for the adaptation steps: Light Adjustment -> Irrigation Control -> Health Scanning
adjustments = StrictPartialOrder(nodes=[
    light_adjustment,
    irrigation_control,
    health_scanning
])
adjustments.order.add_edge(light_adjustment, irrigation_control)
adjustments.order.add_edge(irrigation_control, health_scanning)

# Loop: IoT Monitoring, then either exit or perform adjustments and repeat monitoring
adaptation_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[iot_monitoring, adjustments]
)

# Root partial order for the entire process
root = StrictPartialOrder(nodes=[
    site_analysis,
    env_calibration,
    seed_automation,
    nutrient_mix,
    adaptation_loop,
    pest_detection,
    ai_imaging,
    robotic_harvest,
    quality_check,
    packaging_prep,
    cold_storage,
    logistics_plan,
    market_delivery
])

# Sequential dependencies
root.order.add_edge(site_analysis,      env_calibration)
root.order.add_edge(env_calibration,    seed_automation)
root.order.add_edge(seed_automation,    nutrient_mix)
root.order.add_edge(nutrient_mix,       adaptation_loop)
root.order.add_edge(adaptation_loop,    pest_detection)
root.order.add_edge(pest_detection,     ai_imaging)
root.order.add_edge(ai_imaging,         robotic_harvest)
root.order.add_edge(robotic_harvest,    quality_check)
root.order.add_edge(quality_check,      packaging_prep)
root.order.add_edge(packaging_prep,     cold_storage)
root.order.add_edge(cold_storage,       logistics_plan)
root.order.add_edge(logistics_plan,     market_delivery)