# Generated from: 6f060d21-5a8f-4064-a468-3cafaf4e9523.json
# Description: This process describes the comprehensive cycle of urban vertical farming, integrating sustainable agriculture with advanced technology in densely populated environments. It begins with site analysis and environmental calibration, followed by automated seeding and nutrient optimization. Continuous monitoring through IoT sensors ensures ideal growth conditions. The system adapts lighting and irrigation dynamically based on plant health data. Pest detection is managed through AI-driven imaging, reducing chemical use. Harvesting is executed by robotic units, and produce is quality-checked before packaging. Finally, logistics coordinate rapid delivery to local markets, maintaining freshness and minimizing carbon footprint. This atypical but realistic process exemplifies future-forward urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
env_calibration = Transition(label='Env Calibration')
seed_automation = Transition(label='Seed Automation')
nutrient_mix = Transition(label='Nutrient Mix')
iot_monitoring = Transition(label='IoT Monitoring')
light_adjustment = Transition(label='Light Adjustment')
irrigation_control = Transition(label='Irrigation Control')
health_scanning = Transition(label='Health Scanning')
pest_detection = Transition(label='Pest Detection')
ai_imaging = Transition(label='AI Imaging')
robotic_harvest = Transition(label='Robotic Harvest')
quality_check = Transition(label='Quality Check')
packaging_prep = Transition(label='Packaging Prep')
cold_storage = Transition(label='Cold Storage')
logistics_plan = Transition(label='Logistics Plan')
market_delivery = Transition(label='Market Delivery')

# Construct partial order reflecting the described process

# Start with site analysis and env calibration (in sequence)
# Then seed automation and nutrient mix (in parallel)
# Then IoT Monitoring
# Then Light Adjustment and Irrigation Control (in parallel)
# Then Health Scanning
# Then Pest Detection and AI Imaging (in parallel)
# Then Robotic Harvest
# Then Quality Check and Packaging Prep (in parallel)
# Then Cold Storage
# Then Logistics Plan
# Then Market Delivery

root = StrictPartialOrder(
    nodes=[
        site_analysis,
        env_calibration,
        seed_automation,
        nutrient_mix,
        iot_monitoring,
        light_adjustment,
        irrigation_control,
        health_scanning,
        pest_detection,
        ai_imaging,
        robotic_harvest,
        quality_check,
        packaging_prep,
        cold_storage,
        logistics_plan,
        market_delivery
    ]
)

# Define order edges

# Sequential: site_analysis -> env_calibration
root.order.add_edge(site_analysis, env_calibration)
# After env_calibration: seed_automation and nutrient_mix are concurrent, so both depend on env_calibration
root.order.add_edge(env_calibration, seed_automation)
root.order.add_edge(env_calibration, nutrient_mix)
# After seed_automation and nutrient_mix, iot_monitoring starts
root.order.add_edge(seed_automation, iot_monitoring)
root.order.add_edge(nutrient_mix, iot_monitoring)
# After iot_monitoring: light_adjustment and irrigation_control concurrent
root.order.add_edge(iot_monitoring, light_adjustment)
root.order.add_edge(iot_monitoring, irrigation_control)
# After both light_adjustment and irrigation_control: health_scanning
root.order.add_edge(light_adjustment, health_scanning)
root.order.add_edge(irrigation_control, health_scanning)
# After health_scanning: pest_detection and ai_imaging concurrent
root.order.add_edge(health_scanning, pest_detection)
root.order.add_edge(health_scanning, ai_imaging)
# Both pest_detection and ai_imaging precede robotic_harvest
root.order.add_edge(pest_detection, robotic_harvest)
root.order.add_edge(ai_imaging, robotic_harvest)
# After robotic_harvest: quality_check and packaging_prep concurrent
root.order.add_edge(robotic_harvest, quality_check)
root.order.add_edge(robotic_harvest, packaging_prep)
# After quality_check and packaging_prep: cold_storage
root.order.add_edge(quality_check, cold_storage)
root.order.add_edge(packaging_prep, cold_storage)
# Then cold_storage -> logistics_plan -> market_delivery
root.order.add_edge(cold_storage, logistics_plan)
root.order.add_edge(logistics_plan, market_delivery)