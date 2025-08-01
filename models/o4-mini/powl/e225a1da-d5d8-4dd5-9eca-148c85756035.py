# Generated from: e225a1da-d5d8-4dd5-9eca-148c85756035.json
# Description: This process details the establishment of a vertical farming facility within an urban environment, integrating advanced hydroponic systems with IoT monitoring, energy-efficient lighting, and automated nutrient delivery. It involves site assessment, modular system design, environmental calibration, crop selection based on market trends, installation of sensors, staff training on smart agriculture technology, regulatory compliance checks, trial cultivation cycles, data-driven yield optimization, and marketing launch strategies. The process ensures sustainable urban agriculture that maximizes space, reduces water usage, and provides fresh produce directly to local consumers while adapting dynamically to environmental feedback through continuous monitoring and system adjustments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey        = Transition(label="Site Survey")
design_layout      = Transition(label="Design Layout")
select_crops       = Transition(label="Select Crops")
install_modules    = Transition(label="Install Modules")
setup_sensors      = Transition(label="Setup Sensors")
calibrate_climate  = Transition(label="Calibrate Climate")
configure_lighting = Transition(label="Configure Lighting")
integrate_iot      = Transition(label="Integrate IoT")
train_staff        = Transition(label="Train Staff")
run_trials         = Transition(label="Run Trials")
analyze_data       = Transition(label="Analyze Data")
optimize_yield     = Transition(label="Optimize Yield")
check_compliance   = Transition(label="Check Compliance")
plan_marketing     = Transition(label="Plan Marketing")
launch_facility    = Transition(label="Launch Facility")

# Define the loop body: analysis → optimization
trial_body = StrictPartialOrder(nodes=[analyze_data, optimize_yield])
trial_body.order.add_edge(analyze_data, optimize_yield)

# Define the trial loop: run_trials, then either exit or do (analyze → optimize) then run_trials again
trial_loop = OperatorPOWL(operator=Operator.LOOP, children=[run_trials, trial_body])

# Build the top‐level partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_layout,
        select_crops,
        install_modules,
        setup_sensors,
        calibrate_climate,
        configure_lighting,
        integrate_iot,
        train_staff,
        check_compliance,
        plan_marketing,
        trial_loop,
        launch_facility
    ]
)

# Sequence the initial setup
root.order.add_edge(site_survey,        design_layout)
root.order.add_edge(design_layout,      select_crops)
root.order.add_edge(select_crops,       install_modules)
root.order.add_edge(install_modules,    setup_sensors)
root.order.add_edge(setup_sensors,      calibrate_climate)
root.order.add_edge(calibrate_climate,  configure_lighting)
root.order.add_edge(configure_lighting, integrate_iot)

# After IoT integration, train staff, check compliance, and plan marketing can run in parallel
root.order.add_edge(integrate_iot, train_staff)
root.order.add_edge(integrate_iot, check_compliance)
root.order.add_edge(integrate_iot, plan_marketing)

# Only once training and compliance are done does the trial loop start
root.order.add_edge(train_staff,      trial_loop)
root.order.add_edge(check_compliance, trial_loop)

# After the loop and marketing planning, launch the facility
root.order.add_edge(trial_loop,    launch_facility)
root.order.add_edge(plan_marketing, launch_facility)