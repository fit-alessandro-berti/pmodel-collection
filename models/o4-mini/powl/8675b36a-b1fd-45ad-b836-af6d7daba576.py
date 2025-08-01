# Generated from: 8675b36a-b1fd-45ad-b836-af6d7daba576.json
# Description: This process describes the complex integration of vertical farming systems within urban environments to optimize limited space and resources. It involves site assessment, modular system design, environmental calibration, crop selection based on microclimate, automated nutrient delivery, pest monitoring through AI sensors, energy consumption optimization, waste recycling, yield forecasting using predictive analytics, community engagement for local distribution, regulatory compliance checks, continuous system maintenance, data-driven growth adjustments, and final harvest logistics. The process aims to create a sustainable, scalable urban agriculture model that maximizes efficiency while minimizing environmental impact and fostering community participation.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey      = Transition(label='Site Survey')
design_module    = Transition(label='Design Module')
calibrate_sensors= Transition(label='Calibrate Sensors')
select_crops     = Transition(label='Select Crops')
setup_irrigation = Transition(label='Setup Irrigation')
install_ai       = Transition(label='Install AI')
monitor_pests    = Transition(label='Monitor Pests')
optimize_energy  = Transition(label='Optimize Energy')
recycle_waste    = Transition(label='Recycle Waste')
forecast_yield   = Transition(label='Forecast Yield')
engage_community = Transition(label='Engage Community')
check_compliance = Transition(label='Check Compliance')
maintain_systems = Transition(label='Maintain Systems')
adjust_growth    = Transition(label='Adjust Growth')
plan_harvest     = Transition(label='Plan Harvest')

# Loop for continuous maintenance and growth adjustment
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintain_systems, adjust_growth]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_module, calibrate_sensors, select_crops,
    setup_irrigation, install_ai, monitor_pests, optimize_energy,
    recycle_waste, forecast_yield, engage_community, check_compliance,
    loop, plan_harvest
])

# Define the control‐flow order
edges = [
    (site_survey, design_module),
    (design_module, calibrate_sensors),
    (calibrate_sensors, select_crops),
    (select_crops, setup_irrigation),
    (setup_irrigation, install_ai),
    (install_ai, monitor_pests),
    (monitor_pests, optimize_energy),
    (optimize_energy, recycle_waste),
    (recycle_waste, forecast_yield),
    (forecast_yield, engage_community),
    (engage_community, check_compliance),
    (check_compliance, loop),
    (loop, plan_harvest)
]

for src, tgt in edges:
    root.order.add_edge(src, tgt)