# Generated from: 3ec9af1a-2abf-43d0-b4d1-691fe83c1513.json
# Description: This process outlines the establishment of an urban vertical farming system integrating advanced hydroponics and AI-driven environmental controls. The workflow begins with site analysis and structural assessment, followed by modular farm design and procurement of specialized equipment. Subsequent steps include installation of nutrient delivery systems, lighting calibration, and sensor network deployment. Once operational, the process covers seed selection, automated planting, and growth monitoring using machine learning algorithms. Harvest cycles are optimized through data analytics, while waste is minimized via composting and water recycling. Finally, produce packaging and distribution logistics ensure freshness and sustainability in urban markets.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the activities as POWL transitions
site_analysis      = Transition(label='Site Analysis')
structure_check    = Transition(label='Structure Check')
design_modules     = Transition(label='Design Modules')
order_equipment    = Transition(label='Order Equipment')
install_hydroponics = Transition(label='Install Hydroponics')
set_lighting       = Transition(label='Set Lighting')
deploy_sensors     = Transition(label='Deploy Sensors')
select_seeds       = Transition(label='Select Seeds')
automate_planting  = Transition(label='Automate Planting')
monitor_growth     = Transition(label='Monitor Growth')
analyze_data       = Transition(label='Analyze Data')
optimize_harvest   = Transition(label='Optimize Harvest')
process_waste      = Transition(label='Process Waste')
package_produce    = Transition(label='Package Produce')
distribute_goods   = Transition(label='Distribute Goods')

# Build a strictly sequential partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    structure_check,
    design_modules,
    order_equipment,
    install_hydroponics,
    set_lighting,
    deploy_sensors,
    select_seeds,
    automate_planting,
    monitor_growth,
    analyze_data,
    optimize_harvest,
    process_waste,
    package_produce,
    distribute_goods
])

# Add edges to represent the sequence
root.order.add_edge(site_analysis, structure_check)
root.order.add_edge(structure_check, design_modules)
root.order.add_edge(design_modules, order_equipment)
root.order.add_edge(order_equipment, install_hydroponics)
root.order.add_edge(install_hydroponics, set_lighting)
root.order.add_edge(set_lighting, deploy_sensors)
root.order.add_edge(deploy_sensors, select_seeds)
root.order.add_edge(select_seeds, automate_planting)
root.order.add_edge(automate_planting, monitor_growth)
root.order.add_edge(monitor_growth, analyze_data)
root.order.add_edge(analyze_data, optimize_harvest)
root.order.add_edge(optimize_harvest, process_waste)
root.order.add_edge(process_waste, package_produce)
root.order.add_edge(package_produce, distribute_goods)