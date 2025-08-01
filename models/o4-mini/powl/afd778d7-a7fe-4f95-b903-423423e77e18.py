# Generated from: afd778d7-a7fe-4f95-b903-423423e77e18.json
# Description: This process outlines the comprehensive steps involved in establishing a fully operational urban rooftop farm on a commercial building. It begins with structural assessment and environmental analysis, followed by sourcing sustainable materials and soil alternatives. The process includes modular bed assembly, installation of automated irrigation systems, and integration of renewable energy sources. Crop selection is based on microclimate data and market demand, with seed procurement aligned accordingly. Subsequent activities cover planting schedules, pest management using organic methods, and periodic nutrient supplementation. The farm incorporates real-time monitoring via IoT sensors, data analysis for yield optimization, and community engagement initiatives to promote urban agriculture awareness. Finally, harvest logistics and distribution channels are managed to ensure fresh produce reaches local markets efficiently, completing a cycle that supports sustainability and urban food security.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
assess_structure     = Transition(label='Assess Structure')
analyze_climate      = Transition(label='Analyze Climate')
source_materials     = Transition(label='Source Materials')
prepare_soil         = Transition(label='Prepare Soil')
assemble_beds        = Transition(label='Assemble Beds')
install_irrigation   = Transition(label='Install Irrigation')
set_energy           = Transition(label='Set Energy')
select_crops         = Transition(label='Select Crops')
procure_seeds        = Transition(label='Procure Seeds')
schedule_planting    = Transition(label='Schedule Planting')
manage_pests         = Transition(label='Manage Pests')
supplement_nutrients = Transition(label='Supplement Nutrients')
monitor_sensors      = Transition(label='Monitor Sensors')
analyze_data         = Transition(label='Analyze Data')
engage_community     = Transition(label='Engage Community')
plan_harvest         = Transition(label='Plan Harvest')
distribute_produce   = Transition(label='Distribute Produce')

# Build the partial order
root = StrictPartialOrder(nodes=[
    assess_structure,
    analyze_climate,
    source_materials,
    prepare_soil,
    assemble_beds,
    install_irrigation,
    set_energy,
    select_crops,
    procure_seeds,
    schedule_planting,
    manage_pests,
    supplement_nutrients,
    monitor_sensors,
    analyze_data,
    engage_community,
    plan_harvest,
    distribute_produce
])

# Sequential dependencies
root.order.add_edge(assess_structure,     analyze_climate)
root.order.add_edge(analyze_climate,      source_materials)
root.order.add_edge(source_materials,     prepare_soil)
root.order.add_edge(prepare_soil,         assemble_beds)
root.order.add_edge(assemble_beds,        install_irrigation)
root.order.add_edge(install_irrigation,   set_energy)
root.order.add_edge(set_energy,           select_crops)
root.order.add_edge(select_crops,         procure_seeds)
root.order.add_edge(procure_seeds,        schedule_planting)
root.order.add_edge(schedule_planting,    manage_pests)
root.order.add_edge(manage_pests,         supplement_nutrients)
root.order.add_edge(supplement_nutrients, monitor_sensors)
root.order.add_edge(monitor_sensors,      analyze_data)
root.order.add_edge(analyze_data,         plan_harvest)
root.order.add_edge(plan_harvest,         distribute_produce)

# Community engagement can occur after the farm is established
root.order.add_edge(supplement_nutrients, engage_community)