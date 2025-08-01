# Generated from: ef4c7e9b-2e50-4a92-9d87-411a39fe63cb.json
# Description: This process describes the intricate operations involved in managing an urban vertical farming facility, integrating advanced hydroponics, AI-based growth monitoring, and automated logistics. Starting from seed selection and nutrient mixing, the cycle includes environmental calibration, pest detection using machine vision, dynamic lighting adjustment, and robotic harvesting. Post-harvest activities involve quality inspection, data logging, and packaging optimization. The process also covers waste recycling, energy consumption analysis, and supply chain coordination with local retailers, ensuring sustainability while maximizing yield and freshness in a confined urban environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
seed_selection   = Transition(label="Seed Selection")
nutrient_mix     = Transition(label="Nutrient Mix")
environment_setup = Transition(label="Environment Setup")
pest_scan        = Transition(label="Pest Scan")
light_control    = Transition(label="Light Control")
growth_monitor   = Transition(label="Growth Monitor")
water_cycle      = Transition(label="Water Cycle")
air_quality      = Transition(label="Air Quality")
robotic_harvest  = Transition(label="Robotic Harvest")
quality_check    = Transition(label="Quality Check")
data_logging     = Transition(label="Data Logging")
packaging        = Transition(label="Packaging")
waste_sort       = Transition(label="Waste Sort")
energy_audit     = Transition(label="Energy Audit")
retail_sync      = Transition(label="Retail Sync")

# Build the monitoring sub‐cycle as a partial order (concurrent)
monitor_cycle = StrictPartialOrder(
    nodes=[pest_scan, light_control, growth_monitor, water_cycle, air_quality]
)
# No edges → all monitoring tasks can run concurrently

# Build the loop: do environment setup, then zero or more repetitions of the monitor cycle
loop_node = OperatorPOWL(
    operator=Operator.LOOP,
    children=[environment_setup, monitor_cycle]
)

# Root partial order: sequence of major phases, ending with concurrent wrap‐up tasks
root = StrictPartialOrder(
    nodes=[
        seed_selection,
        nutrient_mix,
        loop_node,
        robotic_harvest,
        quality_check,
        data_logging,
        packaging,
        waste_sort,
        energy_audit,
        retail_sync
    ]
)

# Add control‐flow edges to enforce the intended ordering
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, loop_node)
root.order.add_edge(loop_node, robotic_harvest)
root.order.add_edge(robotic_harvest, quality_check)
root.order.add_edge(quality_check, data_logging)
root.order.add_edge(data_logging, packaging)

# After packaging, the last three tasks run concurrently
root.order.add_edge(packaging, waste_sort)
root.order.add_edge(packaging, energy_audit)
root.order.add_edge(packaging, retail_sync)