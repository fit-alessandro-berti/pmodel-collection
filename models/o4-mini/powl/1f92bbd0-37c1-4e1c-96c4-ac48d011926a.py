# Generated from: 1f92bbd0-37c1-4e1c-96c4-ac48d011926a.json
# Description: This process outlines the complex and atypical steps involved in establishing an urban vertical farming operation within a constrained city environment. It includes initial site evaluation, modular system design, climate control calibration, nutrient optimization, and automated harvesting integration. The process further involves stakeholder engagement for local sourcing, regulatory compliance checks, energy consumption analysis, waste recycling protocols, and real-time growth monitoring through IoT sensors. Each activity ensures sustainability, scalability, and community impact while addressing unique urban agricultural challenges such as space limitations and environmental factors, making this a multifaceted and innovative business endeavor.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
design_modules   = Transition(label='Design Modules')
sensor_install   = Transition(label='Sensor Install')
climate_setup    = Transition(label='Climate Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
water_cycle      = Transition(label='Water Cycle')
lighting_tune    = Transition(label='Lighting Tune')
growth_monitor   = Transition(label='Growth Monitor')
data_analyze     = Transition(label='Data Analyze')
energy_audit     = Transition(label='Energy Audit')
waste_plan       = Transition(label='Waste Plan')
compliance_check = Transition(label='Compliance Check')
staff_training   = Transition(label='Staff Training')
community_meet   = Transition(label='Community Meet')
distribution_map = Transition(label='Distribution Map')
harvest_sync     = Transition(label='Harvest Sync')
scale_plan       = Transition(label='Scale Plan')

# Partial order for the monitoring & analysis step
monitor_po = StrictPartialOrder(nodes=[growth_monitor, data_analyze])
monitor_po.order.add_edge(growth_monitor, data_analyze)

# Partial order for the calibration steps (they can run concurrently)
calibration_po = StrictPartialOrder(
    nodes=[climate_setup, nutrient_mix, water_cycle, lighting_tune]
)

# Loop: run monitoring+analysis, then optionally run calibration and repeat
calibration_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[monitor_po, calibration_po]
)

# Build the top‐level workflow: survey → design → sensor install → calibration loop
# then fan‐out to the various sustainability/compliance/distribution tasks,
# finally converging to a scale plan.
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_modules,
        sensor_install,
        calibration_loop,
        energy_audit,
        waste_plan,
        compliance_check,
        staff_training,
        community_meet,
        distribution_map,
        harvest_sync,
        scale_plan
    ]
)

# Sequential dependencies
root.order.add_edge(site_survey, design_modules)
root.order.add_edge(design_modules, sensor_install)
root.order.add_edge(sensor_install, calibration_loop)

# After the loop, these tasks can proceed in parallel
for act in [
    energy_audit,
    waste_plan,
    compliance_check,
    staff_training,
    community_meet,
    distribution_map,
    harvest_sync
]:
    root.order.add_edge(calibration_loop, act)
    # each of these must complete before scaling up
    root.order.add_edge(act, scale_plan)