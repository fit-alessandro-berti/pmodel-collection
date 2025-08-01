# Generated from: f16cf946-8543-4dee-9400-18c79ef7478b.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farming facility within a repurposed industrial building. It involves site assessment, environmental analysis, modular system design, seed selection based on microclimate, installation of hydroponic and aeroponic units, integration of IoT sensors for real-time monitoring, automation of nutrient delivery, energy optimization via renewable sources, pest management without pesticides, periodic crop rotation planning, quality control checks, yield forecasting using AI models, supply chain coordination for local distribution, employee training on system maintenance, and continuous process improvement through data analytics. The process ensures sustainable food production with minimal environmental impact in dense urban areas.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey   = Transition(label='Site Survey')
climate_study = Transition(label='Climate Study')
system_design = Transition(label='System Design')
energy_audit  = Transition(label='Energy Audit')
seed_select   = Transition(label='Seed Selection')
unit_install  = Transition(label='Unit Install')
sensor_setup  = Transition(label='Sensor Setup')
nutrient_mix  = Transition(label='Nutrient Mix')
pest_control  = Transition(label='Pest Control')
crop_plan     = Transition(label='Crop Plan')
quality_check = Transition(label='Quality Check')
yield_forecast= Transition(label='Yield Forecast')
supply_sync   = Transition(label='Supply Sync')
staff_train   = Transition(label='Staff Train')
data_review   = Transition(label='Data Review')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey, climate_study, system_design, energy_audit,
    seed_select, unit_install, sensor_setup, nutrient_mix,
    pest_control, crop_plan, quality_check, yield_forecast,
    supply_sync, staff_train, data_review
])

# Add dependencies
root.order.add_edge(site_survey,   system_design)
root.order.add_edge(climate_study, system_design)
root.order.add_edge(site_survey,   energy_audit)
root.order.add_edge(climate_study, seed_select)
root.order.add_edge(system_design, unit_install)
root.order.add_edge(system_design, sensor_setup)
root.order.add_edge(unit_install,  nutrient_mix)
root.order.add_edge(sensor_setup,  nutrient_mix)
root.order.add_edge(system_design, pest_control)
root.order.add_edge(seed_select,   crop_plan)
root.order.add_edge(nutrient_mix,  quality_check)
root.order.add_edge(pest_control,  quality_check)
root.order.add_edge(quality_check, yield_forecast)
root.order.add_edge(crop_plan,     yield_forecast)
root.order.add_edge(yield_forecast,supply_sync)
root.order.add_edge(unit_install,  staff_train)
root.order.add_edge(sensor_setup,  staff_train)
root.order.add_edge(supply_sync,   data_review)
root.order.add_edge(staff_train,   data_review)