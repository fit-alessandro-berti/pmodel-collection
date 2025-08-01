# Generated from: 7b4bc1bc-c193-4508-b9bc-447481d9c69f.json
# Description: This process outlines the complex operational cycle of an urban vertical farm that integrates hydroponics, automated environmental controls, and real-time data analytics to maximize crop yield and sustainability. It begins with seed selection and preparation, followed by nutrient solution formulation and automated planting in multi-layered growth trays. Continuous monitoring of microclimate conditions such as humidity, temperature, and light intensity is conducted using IoT sensors. Data is analyzed to adjust parameters dynamically via AI-driven controls. Pollination is simulated mechanically or via controlled introduction of pollinator insects. Harvesting robots selectively pick mature produce, which is then quality-checked and sorted by automated vision systems. Post-harvest processing includes washing, packaging in biodegradable materials, and cold storage. The process concludes with logistics coordination for local distribution, waste recycling, and system maintenance to ensure sustainability and minimize downtime.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define transitions for each activity
seed_prep = Transition(label="Seed Prep")
nutrient_mix = Transition(label="Nutrient Mix")
automated_plant = Transition(label="Automated Plant")
microclimate_check = Transition(label="Microclimate Check")
data_capture = Transition(label="Data Capture")
ai_adjustments = Transition(label="AI Adjustments")
pollination_step = Transition(label="Pollination Step")
harvest_robots = Transition(label="Harvest Robots")
quality_scan = Transition(label="Quality Scan")
produce_sort = Transition(label="Produce Sort")
wash_cycle = Transition(label="Wash Cycle")
eco_packaging = Transition(label="Eco Packaging")
cold_storage = Transition(label="Cold Storage")
local_dispatch = Transition(label="Local Dispatch")
waste_recycle = Transition(label="Waste Recycle")
system_cleanup = Transition(label="System Cleanup")

# Build the partial‐order workflow
root = StrictPartialOrder(
    nodes=[
        seed_prep, nutrient_mix, automated_plant,
        microclimate_check, data_capture, ai_adjustments,
        pollination_step, harvest_robots, quality_scan,
        produce_sort, wash_cycle, eco_packaging,
        cold_storage, local_dispatch, waste_recycle,
        system_cleanup
    ]
)

# Sequential dependencies
root.order.add_edge(seed_prep, nutrient_mix)
root.order.add_edge(nutrient_mix, automated_plant)

# After planting, monitoring activities run in parallel
root.order.add_edge(automated_plant, microclimate_check)
root.order.add_edge(automated_plant, data_capture)

# Monitoring feeds into AI adjustments
root.order.add_edge(microclimate_check, ai_adjustments)
root.order.add_edge(data_capture, ai_adjustments)

# Continue linearly after AI adjustments
root.order.add_edge(ai_adjustments, pollination_step)
root.order.add_edge(pollination_step, harvest_robots)
root.order.add_edge(harvest_robots, quality_scan)
root.order.add_edge(quality_scan, produce_sort)
root.order.add_edge(produce_sort, wash_cycle)
root.order.add_edge(wash_cycle, eco_packaging)
root.order.add_edge(eco_packaging, cold_storage)

# After cold storage, dispatch runs in parallel with recycling & cleanup
root.order.add_edge(cold_storage, local_dispatch)
root.order.add_edge(cold_storage, waste_recycle)
root.order.add_edge(waste_recycle, system_cleanup)