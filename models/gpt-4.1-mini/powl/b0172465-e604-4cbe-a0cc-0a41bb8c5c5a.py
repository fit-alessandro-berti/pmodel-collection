# Generated from: b0172465-e604-4cbe-a0cc-0a41bb8c5c5a.json
# Description: This process outlines the comprehensive steps involved in establishing a sustainable urban rooftop farm. It includes site evaluation, structural analysis, soil testing, microclimate assessment, vendor sourcing for modular planting systems, installation of automated irrigation, integration of renewable energy sources, crop selection based on local demand, pest management planning, community engagement for shared maintenance, waste composting setup, yield forecasting, market channel development, and continuous monitoring to ensure productivity and environmental compliance. The process aims to transform underutilized urban rooftop spaces into productive agricultural hubs while addressing logistical, environmental, and social challenges uniquely inherent to urban farming.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
climate_study = Transition(label='Climate Study')
vendor_sourcing = Transition(label='Vendor Sourcing')
system_install = Transition(label='System Install')
irrigation_setup = Transition(label='Irrigation Setup')
energy_integrate = Transition(label='Energy Integrate')
crop_select = Transition(label='Crop Select')
pest_control = Transition(label='Pest Control')
community_meet = Transition(label='Community Meet')
waste_setup = Transition(label='Waste Setup')
yield_forecast = Transition(label='Yield Forecast')
market_plan = Transition(label='Market Plan')
monitor_growth = Transition(label='Monitor Growth')

# Construct partial orders to reflect dependencies and partial concurrency:
#
# Phase 1: Site evaluation: site_survey -> load_test, soil_sample, climate_study are concurrent after load_test
phase1 = StrictPartialOrder(
    nodes=[site_survey, load_test, soil_sample, climate_study]
)
phase1.order.add_edge(site_survey, load_test)
# load_test then soil_sample and climate_study can run concurrently
phase1.order.add_edge(load_test, soil_sample)
phase1.order.add_edge(load_test, climate_study)

# Phase 2: Vendor sourcing + system install + irrigation + energy integration
# Vendor sourcing must precede system install
# System install must precede irrigation setup and energy integrate (which are concurrent)
phase2 = StrictPartialOrder(
    nodes=[vendor_sourcing, system_install, irrigation_setup, energy_integrate]
)
phase2.order.add_edge(vendor_sourcing, system_install)
phase2.order.add_edge(system_install, irrigation_setup)
phase2.order.add_edge(system_install, energy_integrate)

# Phase 3: Crop select -> pest control -> community meet, waste setup (concurrent)
phase3 = StrictPartialOrder(
    nodes=[crop_select, pest_control, community_meet, waste_setup]
)
phase3.order.add_edge(crop_select, pest_control)
phase3.order.add_edge(pest_control, community_meet)
phase3.order.add_edge(pest_control, waste_setup)

# Phase 4: Yield forecast -> market plan -> monitor growth
phase4 = StrictPartialOrder(
    nodes=[yield_forecast, market_plan, monitor_growth]
)
phase4.order.add_edge(yield_forecast, market_plan)
phase4.order.add_edge(market_plan, monitor_growth)

# Organize the entire process as a partial order of these four phases,
# where phases happen in sequence:
# phase1 -> phase2 -> phase3 -> phase4
root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase4]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)