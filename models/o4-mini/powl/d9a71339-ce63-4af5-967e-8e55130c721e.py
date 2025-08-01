# Generated from: d9a71339-ce63-4af5-967e-8e55130c721e.json
# Description: This process outlines the establishment of an urban vertical farm integrating hydroponic systems and AI-driven environmental controls. Starting from site analysis and structural assessment, it involves modular unit installation, nutrient solution formulation, sensor calibration, and AI model training for growth optimization. The workflow includes ongoing data acquisition, predictive maintenance scheduling, pest detection via image recognition, and automated harvesting coordination. Final stages focus on yield quality assessment, packaging automation, and distribution logistics planning, ensuring sustainable urban agriculture with minimal resource consumption and maximized crop output.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
structural_check  = Transition(label='Structural Check')
modular_install   = Transition(label='Modular Install')
hydroponic_setup  = Transition(label='Hydroponic Setup')
nutrient_mix      = Transition(label='Nutrient Mix')
sensor_setup      = Transition(label='Sensor Setup')
ai_training       = Transition(label='AI Training')
data_capture      = Transition(label='Data Capture')
maintenance_plan  = Transition(label='Maintenance Plan')
pest_scan         = Transition(label='Pest Scan')
growth_monitor    = Transition(label='Growth Monitor')
harvest_sync      = Transition(label='Harvest Sync')
quality_test      = Transition(label='Quality Test')
package_prep      = Transition(label='Package Prep')
logistics_plan    = Transition(label='Logistics Plan')

# Define loop of ongoing tasks (concurrent within each iteration)
loop_tasks = StrictPartialOrder(nodes=[
    data_capture, maintenance_plan, pest_scan, growth_monitor, harvest_sync
])
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[loop_tasks, loop_tasks])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_check,
    modular_install,
    hydroponic_setup,
    nutrient_mix,
    sensor_setup,
    ai_training,
    loop_node,
    quality_test,
    package_prep,
    logistics_plan
])

# Sequence edges for the initial setup
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, modular_install)
root.order.add_edge(modular_install, hydroponic_setup)
root.order.add_edge(hydroponic_setup, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_setup)
root.order.add_edge(sensor_setup, ai_training)
root.order.add_edge(ai_training, loop_node)

# Sequence edges for the final stages
root.order.add_edge(loop_node, quality_test)
root.order.add_edge(quality_test, package_prep)
root.order.add_edge(package_prep, logistics_plan)