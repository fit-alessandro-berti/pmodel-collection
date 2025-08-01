# Generated from: 0e544013-f632-4b0c-9203-060c9e06658b.json
# Description: This process outlines the complex and atypical steps required to establish an urban vertical farm within a repurposed industrial building. It involves site assessment, modular system design, environmental control integration, seed selection, and nutrient solution formulation. The process further includes automated planting, multi-tier crop monitoring using IoT sensors, adaptive lighting adjustments, pest management through biological controls, and dynamic harvesting schedules. Post-harvest, produce is cleaned, quality checked, packaged, and routed through a local distribution network optimized for freshness and minimal carbon footprint. Continuous data analysis and machine learning are applied to optimize growth cycles and resource consumption, ensuring sustainable urban agriculture operations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_assess     = Transition(label="Site Assess")
system_design   = Transition(label="System Design")
env_control     = Transition(label="Env Control")
seed_select     = Transition(label="Seed Select")
nutrient_prep   = Transition(label="Nutrient Prep")
auto_plant      = Transition(label="Auto Plant")
sensor_deploy   = Transition(label="Sensor Deploy")
growth_monitor  = Transition(label="Growth Monitor")
light_adjust    = Transition(label="Light Adjust")
pest_control    = Transition(label="Pest Control")
harvest_plan    = Transition(label="Harvest Plan")
produce_clean   = Transition(label="Produce Clean")
quality_check   = Transition(label="Quality Check")
package_goods   = Transition(label="Package Goods")
local_ship      = Transition(label="Local Ship")
data_analyze    = Transition(label="Data Analyze")
cycle_optimize  = Transition(label="Cycle Optimize")

# Define the end‐of‐process loop for continuous improvement
improvement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[data_analyze, cycle_optimize]
)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_assess,
    system_design,
    env_control,
    seed_select,
    nutrient_prep,
    auto_plant,
    sensor_deploy,
    growth_monitor,
    light_adjust,
    pest_control,
    harvest_plan,
    produce_clean,
    quality_check,
    package_goods,
    local_ship,
    improvement_loop
])

# Sequential setup steps
root.order.add_edge(site_assess,   system_design)
root.order.add_edge(system_design, env_control)
root.order.add_edge(env_control,   seed_select)
root.order.add_edge(seed_select,   nutrient_prep)
root.order.add_edge(nutrient_prep, auto_plant)
root.order.add_edge(auto_plant,    sensor_deploy)

# After sensors are deployed, monitoring, lighting, and pest control can proceed in parallel
root.order.add_edge(sensor_deploy, growth_monitor)
root.order.add_edge(sensor_deploy, light_adjust)
root.order.add_edge(sensor_deploy, pest_control)

# All three must complete before planning harvest
root.order.add_edge(growth_monitor, harvest_plan)
root.order.add_edge(light_adjust,   harvest_plan)
root.order.add_edge(pest_control,   harvest_plan)

# Post‐harvest steps
root.order.add_edge(harvest_plan,   produce_clean)
root.order.add_edge(produce_clean,  quality_check)
root.order.add_edge(quality_check,  package_goods)
root.order.add_edge(package_goods,  local_ship)

# Hand off to the continuous improvement loop
root.order.add_edge(local_ship, improvement_loop)