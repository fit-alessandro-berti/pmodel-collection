# Generated from: 879c8f2d-6f54-43b8-94bc-724715141cee.json
# Description: This process outlines the complex and interdisciplinary steps required to establish a fully operational urban vertical farm within a repurposed industrial building. It involves integrating agricultural science with urban planning, engineering, and sustainability practices. The workflow includes site assessment, modular system design, climate control calibration, nutrient solution formulation, automated planting schedules, real-time environmental monitoring, waste recycling protocols, energy optimization, and community engagement strategies. Each phase requires coordination between agronomists, engineers, IT specialists, and local authorities to ensure the farm meets productivity, safety, and environmental standards while adapting to the unique constraints of an urban setting. The process emphasizes innovative technology use, such as AI-driven crop health analysis and IoT-enabled resource management, to maximize yield and minimize resource consumption.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
system_design    = Transition(label='System Design')
climate_setup    = Transition(label='Climate Setup')
water_testing    = Transition(label='Water Testing')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_selection   = Transition(label='Seed Selection')
sensor_install   = Transition(label='Sensor Install')
automation_setup = Transition(label='Automation Setup')
planting_cycle   = Transition(label='Planting Cycle')
data_integration = Transition(label='Data Integration')
health_check     = Transition(label='Health Check')
yield_forecast   = Transition(label='Yield Forecast')
waste_sorting    = Transition(label='Waste Sorting')
energy_audit     = Transition(label='Energy Audit')
community_meet   = Transition(label='Community Meet')
maintenance_plan = Transition(label='Maintenance Plan')

# Build the cultivation‐cycle subgraph: plant → integrate → health check → forecast
cultivation_cycle = StrictPartialOrder(
    nodes=[planting_cycle, data_integration, health_check, yield_forecast]
)
cultivation_cycle.order.add_edge(planting_cycle,   data_integration)
cultivation_cycle.order.add_edge(data_integration,  health_check)
cultivation_cycle.order.add_edge(health_check,      yield_forecast)

# Build the cleanup subgraph: waste sorting → energy audit
cleanup = StrictPartialOrder(nodes=[waste_sorting, energy_audit])
cleanup.order.add_edge(waste_sorting, energy_audit)

# Loop: perform cultivation then cleanup, repeat until exit
loop_cultivation = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cultivation_cycle, cleanup]
)

# Top‐level partial order: from site assessment to final handover
root = StrictPartialOrder(
    nodes=[
        site_survey, structural_audit, system_design,
        climate_setup, water_testing, nutrient_mix,
        seed_selection, sensor_install, automation_setup,
        loop_cultivation,
        community_meet, maintenance_plan
    ]
)

# Initial parallel site assessment
root.order.add_edge(site_survey,      system_design)
root.order.add_edge(structural_audit, system_design)

# System design → setup/configuration tasks in parallel
root.order.add_edge(system_design, climate_setup)
root.order.add_edge(system_design, seed_selection)
root.order.add_edge(system_design, sensor_install)
root.order.add_edge(system_design, automation_setup)

# Climate setup → water test → nutrient preparation
root.order.add_edge(climate_setup, water_testing)
root.order.add_edge(water_testing, nutrient_mix)

# Once prep tasks complete → enter the cultivation loop
root.order.add_edge(nutrient_mix,     loop_cultivation)
root.order.add_edge(seed_selection,   loop_cultivation)
root.order.add_edge(sensor_install,   loop_cultivation)
root.order.add_edge(automation_setup, loop_cultivation)

# After finishing all cultivation cycles → community engagement → maintenance planning
root.order.add_edge(loop_cultivation, community_meet)
root.order.add_edge(community_meet,   maintenance_plan)