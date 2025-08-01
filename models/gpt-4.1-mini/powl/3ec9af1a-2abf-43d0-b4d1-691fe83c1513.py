# Generated from: 3ec9af1a-2abf-43d0-b4d1-691fe83c1513.json
# Description: This process outlines the establishment of an urban vertical farming system integrating advanced hydroponics and AI-driven environmental controls. The workflow begins with site analysis and structural assessment, followed by modular farm design and procurement of specialized equipment. Subsequent steps include installation of nutrient delivery systems, lighting calibration, and sensor network deployment. Once operational, the process covers seed selection, automated planting, and growth monitoring using machine learning algorithms. Harvest cycles are optimized through data analytics, while waste is minimized via composting and water recycling. Finally, produce packaging and distribution logistics ensure freshness and sustainability in urban markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_analysis = Transition(label='Site Analysis')
structure_check = Transition(label='Structure Check')
design_modules = Transition(label='Design Modules')
order_equipment = Transition(label='Order Equipment')
install_hydroponics = Transition(label='Install Hydroponics')
set_lighting = Transition(label='Set Lighting')
deploy_sensors = Transition(label='Deploy Sensors')
select_seeds = Transition(label='Select Seeds')
automate_planting = Transition(label='Automate Planting')
monitor_growth = Transition(label='Monitor Growth')
analyze_data = Transition(label='Analyze Data')
optimize_harvest = Transition(label='Optimize Harvest')
process_waste = Transition(label='Process Waste')
package_produce = Transition(label='Package Produce')
distribute_goods = Transition(label='Distribute Goods')

# Construction of the workflow partial orders according to the description

# Phase 1: site_analysis --> structure_check (sequential)
phase1 = StrictPartialOrder(nodes=[site_analysis, structure_check])
phase1.order.add_edge(site_analysis, structure_check)

# Phase 2: design_modules and order_equipment in parallel after structure_check
phase2 = StrictPartialOrder(nodes=[design_modules, order_equipment])  # no order => concurrent

# Phase 3: install_hydroponics --> set_lighting --> deploy_sensors (sequential)
phase3 = StrictPartialOrder(nodes=[install_hydroponics, set_lighting, deploy_sensors])
phase3.order.add_edge(install_hydroponics, set_lighting)
phase3.order.add_edge(set_lighting, deploy_sensors)

# Phase 4: select_seeds --> automate_planting --> monitor_growth (sequential)
phase4 = StrictPartialOrder(nodes=[select_seeds, automate_planting, monitor_growth])
phase4.order.add_edge(select_seeds, automate_planting)
phase4.order.add_edge(automate_planting, monitor_growth)

# Phase 5: analyze_data --> optimize_harvest (sequential)
phase5 = StrictPartialOrder(nodes=[analyze_data, optimize_harvest])
phase5.order.add_edge(analyze_data, optimize_harvest)

# Phase 6: process_waste (single node)
phase6 = process_waste

# Phase 7: package_produce --> distribute_goods (sequential)
phase7 = StrictPartialOrder(nodes=[package_produce, distribute_goods])
phase7.order.add_edge(package_produce, distribute_goods)

# Integrate phases according to dependencies and concurrency derived from description:

# After phase1 (structure_check):
# (phase2 concurrent: design_modules, order_equipment) must both complete before phase3 (install_hydroponics etc.)
# So phase3 depends on both phase2 activities

# After phase3 (deploy_sensors) --> phase4 (select_seeds...)
# After phase4 (monitor_growth) --> phase5 (analyze_data...)
# Then phases 5, 6 (process_waste), and 7 (packaging-distributing) run in order:
# phase5 --> phase6 --> phase7

# Create a big partial order including all phases, where some phases are POWL models or transitions

# Nodes of the final model:
nodes = [
    phase1,        # StrictPartialOrder(site_analysis, structure_check)
    phase2,        # StrictPartialOrder(design_modules, order_equipment)
    phase3,        # StrictPartialOrder(install_hydroponics, set_lighting, deploy_sensors)
    phase4,        # StrictPartialOrder(select_seeds, automate_planting, monitor_growth)
    phase5,        # StrictPartialOrder(analyze_data, optimize_harvest)
    phase6,        # process_waste (Transition)
    phase7         # StrictPartialOrder(package_produce, distribute_goods)
]

root = StrictPartialOrder(nodes=nodes)

# Adding edges according to described control flow dependencies:

# Within phase1 already ordered: site_analysis --> structure_check
# phase1 --> phase2 (both design_modules and order_equipment start after structure_check)
root.order.add_edge(phase1, phase2)

# phase2 --> phase3 (both design_modules and order_equipment must complete before install_hydroponics)
root.order.add_edge(phase2, phase3)

# phase3 --> phase4
root.order.add_edge(phase3, phase4)

# phase4 --> phase5
root.order.add_edge(phase4, phase5)

# phase5 --> phase6 (process_waste)
root.order.add_edge(phase5, phase6)

# phase6 --> phase7 (packaging and distribution)
root.order.add_edge(phase6, phase7)