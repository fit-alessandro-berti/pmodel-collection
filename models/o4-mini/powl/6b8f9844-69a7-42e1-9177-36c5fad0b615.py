# Generated from: 6b8f9844-69a7-42e1-9177-36c5fad0b615.json
# Description: This process outlines the establishment of an urban vertical farming system that integrates hydroponics, IoT monitoring, and renewable energy sources to maximize crop yield in limited city spaces. It involves site evaluation, modular system design, nutrient solution preparation, environmental control calibration, and ongoing crop health analysis to ensure sustainable and efficient food production within urban environments. The process also includes waste recycling, energy optimization, and community engagement to promote local food security and reduce carbon footprint.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activity transitions
t_site_survey        = Transition(label='Site Survey')
t_design_module      = Transition(label='Design Module')
t_install_frames     = Transition(label='Install Frames')
t_setup_hydroponics  = Transition(label='Setup Hydroponics')
t_prepare_nutrients  = Transition(label='Prepare Nutrients')
t_configure_sensors  = Transition(label='Configure Sensors')
t_calibrate_climate  = Transition(label='Calibrate Climate')
t_plant_seeding      = Transition(label='Plant Seeding')
t_monitor_growth     = Transition(label='Monitor Growth')
t_analyze_data       = Transition(label='Analyze Data')
t_adjust_lighting    = Transition(label='Adjust Lighting')
t_recycle_waste      = Transition(label='Recycle Waste')
t_optimize_energy    = Transition(label='Optimize Energy')
t_maintenance_check  = Transition(label='Maintenance Check')
t_harvest_crops      = Transition(label='Harvest Crops')
t_community_outreach = Transition(label='Community Outreach')
t_report_metrics     = Transition(label='Report Metrics')

# Build the monitoring sub‐process (to be looped)
monitor_bundle = StrictPartialOrder(nodes=[
    t_monitor_growth,
    t_analyze_data,
    t_adjust_lighting,
    t_recycle_waste,
    t_optimize_energy,
    t_maintenance_check
])
monitor_bundle.order.add_edge(t_monitor_growth,    t_analyze_data)
monitor_bundle.order.add_edge(t_analyze_data,      t_adjust_lighting)
monitor_bundle.order.add_edge(t_adjust_lighting,   t_recycle_waste)
monitor_bundle.order.add_edge(t_recycle_waste,     t_optimize_energy)
monitor_bundle.order.add_edge(t_optimize_energy,   t_maintenance_check)

# A silent transition to allow loop exit/continuation
skip = SilentTransition()

# Loop operator: repeat the monitoring bundle until exit
loop_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[monitor_bundle, skip])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    t_site_survey,
    t_design_module,
    t_install_frames,
    t_setup_hydroponics,
    t_prepare_nutrients,
    t_configure_sensors,
    t_calibrate_climate,
    t_plant_seeding,
    loop_monitoring,
    t_harvest_crops,
    t_community_outreach,
    t_report_metrics
])

# Sequence edges
root.order.add_edge(t_site_survey,       t_design_module)
root.order.add_edge(t_design_module,     t_install_frames)
root.order.add_edge(t_install_frames,    t_setup_hydroponics)
root.order.add_edge(t_setup_hydroponics, t_prepare_nutrients)
root.order.add_edge(t_setup_hydroponics, t_configure_sensors)
root.order.add_edge(t_prepare_nutrients, t_calibrate_climate)
root.order.add_edge(t_configure_sensors, t_calibrate_climate)
root.order.add_edge(t_calibrate_climate, t_plant_seeding)
root.order.add_edge(t_plant_seeding,     loop_monitoring)
root.order.add_edge(loop_monitoring,     t_harvest_crops)
root.order.add_edge(t_harvest_crops,     t_community_outreach)
root.order.add_edge(t_community_outreach, t_report_metrics)