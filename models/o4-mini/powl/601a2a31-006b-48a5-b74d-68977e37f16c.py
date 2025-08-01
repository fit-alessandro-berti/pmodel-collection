# Generated from: 601a2a31-006b-48a5-b74d-68977e37f16c.json
# Description: This process outlines the establishment of an urban vertical farm within a repurposed industrial warehouse. It begins with site evaluation and structural reinforcement, followed by modular rack assembly and installation of hydroponic systems. Specialized lighting calibration is conducted to optimize plant growth cycles. Nutrient solution formulation and water recycling integration ensure sustainable cultivation. Crop selection is aligned with local demand forecasting. Continuous environmental monitoring and pest management protocols are implemented via IoT devices. Harvest scheduling coordinates with automated packaging and distribution logistics, ensuring freshness and reducing waste. The process concludes with regular data analysis for yield optimization and adaptive system maintenance to sustain productivity in an urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
site_eval       = Transition(label='Site Eval')
structure_check = Transition(label='Structure Check')
rack_install    = Transition(label='Rack Install')
hydroponic_setup= Transition(label='Hydroponic Setup')
light_calibrate = Transition(label='Light Calibrate')
nutrient_mix    = Transition(label='Nutrient Mix')
water_cycle     = Transition(label='Water Cycle')
demand_forecast = Transition(label='Demand Forecast')
crop_select     = Transition(label='Crop Select')
enviro_monitor  = Transition(label='Enviro Monitor')
pest_control    = Transition(label='Pest Control')
harvest_plan    = Transition(label='Harvest Plan')
auto_package    = Transition(label='Auto Package')
logistics_setup = Transition(label='Logistics Setup')

# Final ongoing loop: Data Analyze then System Maintain
data_analyze    = Transition(label='Data Analyze')
system_maintain = Transition(label='System Maintain')
analysis_loop   = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, system_maintain])

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    site_eval, structure_check, rack_install, hydroponic_setup,
    light_calibrate, nutrient_mix, water_cycle, demand_forecast,
    crop_select, enviro_monitor, pest_control, harvest_plan,
    auto_package, logistics_setup, analysis_loop
])

# Add the control‐flow (partial‐order) edges
o = root.order
o.add_edge(site_eval,       structure_check)
o.add_edge(structure_check, rack_install)
o.add_edge(rack_install,    hydroponic_setup)
o.add_edge(hydroponic_setup, light_calibrate)

o.add_edge(light_calibrate, nutrient_mix)
o.add_edge(light_calibrate, water_cycle)

o.add_edge(nutrient_mix,    demand_forecast)
o.add_edge(water_cycle,     demand_forecast)
o.add_edge(demand_forecast, crop_select)

o.add_edge(hydroponic_setup, enviro_monitor)
o.add_edge(hydroponic_setup, pest_control)

o.add_edge(enviro_monitor,  harvest_plan)
o.add_edge(pest_control,    harvest_plan)
o.add_edge(crop_select,     harvest_plan)

o.add_edge(harvest_plan,    auto_package)
o.add_edge(harvest_plan,    logistics_setup)

o.add_edge(auto_package,    analysis_loop)
o.add_edge(logistics_setup, analysis_loop)