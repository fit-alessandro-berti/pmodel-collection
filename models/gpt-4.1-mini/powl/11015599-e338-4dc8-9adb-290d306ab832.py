# Generated from: 11015599-e338-4dc8-9adb-290d306ab832.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site assessment, environmental impact analysis, modular system design, hydroponic and aeroponic integration, climate control calibration, nutrient cycle optimization, automation system installation, workforce training, regulatory compliance checks, pilot crop testing, data-driven yield forecasting, waste recycling implementation, community engagement strategy, and scaling plans. The goal is to create a sustainable, high-efficiency farming operation that maximizes limited urban space while minimizing environmental footprint and ensuring regulatory adherence.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
impact_study = Transition(label='Impact Study')
system_design = Transition(label='System Design')
hydroponics_setup = Transition(label='Hydroponics Setup')
aeroponics_setup = Transition(label='Aeroponics Setup')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
automation_install = Transition(label='Automation Install')
staff_training = Transition(label='Staff Training')
regulation_check = Transition(label='Regulation Check')
pilot_crops = Transition(label='Pilot Crops')
yield_forecast = Transition(label='Yield Forecast')
waste_cycle = Transition(label='Waste Cycle')
community_plan = Transition(label='Community Plan')
scale_strategy = Transition(label='Scale Strategy')

# Phases inferred from the description and activity names:
# 1. Site assessment phase: Site Survey --> Impact Study
# 2. Design phase: System Design
# 3. Setup phase: Hydroponics Setup and Aeroponics Setup (can run concurrently)
# 4. Calibration & optimization phase: Climate Setup --> Nutrient Mix
# 5. Automation & training: Automation Install --> Staff Training
# 6. Compliance: Regulation Check
# 7. Pilot and forecast: Pilot Crops --> Yield Forecast
# 8. Sustainability and community: Waste Cycle --> Community Plan
# 9. Final scaling: Scale Strategy

# Setup concurrent setup technologies:
setup_parallel = StrictPartialOrder(nodes=[hydroponics_setup, aeroponics_setup])
# no order edges => concurrent execution

# Calibration and optimization sequential:
calib_opt = StrictPartialOrder(nodes=[climate_setup, nutrient_mix])
calib_opt.order.add_edge(climate_setup, nutrient_mix)

# Automation and training sequential:
auto_train = StrictPartialOrder(nodes=[automation_install, staff_training])
auto_train.order.add_edge(automation_install, staff_training)

# Pilot and forecast sequential:
pilot_forecast = StrictPartialOrder(nodes=[pilot_crops, yield_forecast])
pilot_forecast.order.add_edge(pilot_crops, yield_forecast)

# Waste cycle and community plan sequential:
waste_community = StrictPartialOrder(nodes=[waste_cycle, community_plan])
waste_community.order.add_edge(waste_cycle, community_plan)

# Combine all major phases in partial order with dependencies:
# Site Survey --> Impact Study --> System Design --> Setup (hydroponics + aeroponics) --> Calibration & Optimization --> Automation & Training
# --> Regulation Check --> Pilot & Forecast --> Waste & Community --> Scale Strategy

root = StrictPartialOrder(
    nodes=[site_survey, impact_study, system_design, setup_parallel, calib_opt,
           auto_train, regulation_check, pilot_forecast, waste_community, scale_strategy]
)

# Add order edges between phases
root.order.add_edge(site_survey, impact_study)
root.order.add_edge(impact_study, system_design)
root.order.add_edge(system_design, setup_parallel)
root.order.add_edge(setup_parallel, calib_opt)
root.order.add_edge(calib_opt, auto_train)
root.order.add_edge(auto_train, regulation_check)
root.order.add_edge(regulation_check, pilot_forecast)
root.order.add_edge(pilot_forecast, waste_community)
root.order.add_edge(waste_community, scale_strategy)