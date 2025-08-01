# Generated from: 8463a482-1b7b-4e92-9574-86c6f6ad416a.json
# Description: This process involves managing a multi-level urban vertical farm that integrates hydroponic and aeroponic systems to optimize crop yield within limited city spaces. It covers seed selection based on seasonal data, nutrient solution preparation, automated climate control adjustments, pest detection through AI imaging, and yield forecasting. Additionally, it includes waste recycling mechanisms, labor scheduling, real-time monitoring dashboards, and coordination with local markets for distribution. The process ensures sustainability by balancing energy consumption with renewable sources and maintaining strict quality standards through continuous sensor feedback and manual inspections.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
seed_sel      = Transition(label="Seed Selection")
nutrient_mix  = Transition(label="Nutrient Mix")
climate_setup = Transition(label="Climate Setup")
labor_assign  = Transition(label="Labor Assign")

planting        = Transition(label="Planting Cycle")
growth_monitor  = Transition(label="Growth Monitor")
pest_scan       = Transition(label="Pest Scan")

waste_sorting  = Transition(label="Waste Sorting")
energy_audit   = Transition(label="Energy Audit")
water_recycle  = Transition(label="Water Recycle")

yield_forecast = Transition(label="Yield Forecast")
market_sync    = Transition(label="Market Sync")
quality_check  = Transition(label="Quality Check")
inventory_log  = Transition(label="Inventory Log")
data_backup    = Transition(label="Data Backup")

# Build the monitoring sub‐process: Growth Monitor --> Pest Scan
monitoring = StrictPartialOrder(nodes=[growth_monitor, pest_scan])
monitoring.order.add_edge(growth_monitor, pest_scan)

# Build the planting loop: Planting Cycle; then repeat Growth Monitor & Pest Scan
plant_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting, monitoring])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        seed_sel, nutrient_mix, climate_setup, labor_assign,
        plant_loop,
        yield_forecast, waste_sorting, energy_audit, water_recycle,
        market_sync, quality_check, inventory_log, data_backup
    ]
)

# Initial setup ordering
root.order.add_edge(seed_sel,      nutrient_mix)
root.order.add_edge(nutrient_mix,  climate_setup)
root.order.add_edge(climate_setup, labor_assign)
root.order.add_edge(labor_assign,  plant_loop)

# After the planting loop: four activities can start in parallel
root.order.add_edge(plant_loop, yield_forecast)
root.order.add_edge(plant_loop, waste_sorting)
root.order.add_edge(plant_loop, energy_audit)
root.order.add_edge(plant_loop, water_recycle)

# Dependencies in post‐processing
root.order.add_edge(yield_forecast, market_sync)
root.order.add_edge(yield_forecast, quality_check)
root.order.add_edge(quality_check,   inventory_log)
root.order.add_edge(inventory_log,   data_backup)