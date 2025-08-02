# Generated from: cc6a0acc-edcb-405b-b949-ef30a817db08.json
# Description: This process outlines the complex steps involved in transforming underutilized urban rooftops into productive agricultural spaces. It covers site assessment, structural analysis, soil and water testing, modular bed installation, climate control setup, crop selection, pest management, community engagement, and ongoing maintenance. The workflow ensures sustainable food production within city environments by integrating technology, environmental considerations, and stakeholder collaboration to maximize yield and minimize ecological impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
water_check = Transition(label='Water Check')
design_plan = Transition(label='Design Plan')
bed_setup = Transition(label='Bed Setup')
irrigation_install = Transition(label='Irrigation Install')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
planting_phase = Transition(label='Planting Phase')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_prep = Transition(label='Harvest Prep')
community_meet = Transition(label='Community Meet')
waste_manage = Transition(label='Waste Manage')
yield_report = Transition(label='Yield Report')

# Site assessment partial order: Site Survey --> Load Test --> Soil Sample & Water Check (parallel)
site_assessment = StrictPartialOrder(
    nodes=[site_survey, load_test, soil_sample, water_check]
)
site_assessment.order.add_edge(site_survey, load_test)
site_assessment.order.add_edge(load_test, soil_sample)
site_assessment.order.add_edge(load_test, water_check)
# soil_sample and water_check concurrent because no edge between them

# Design plan after soil and water testing
design = design_plan

# Modular bed installation partial order: Bed Setup --> Irrigation Install & Climate Setup (parallel)
modular_bed_install = StrictPartialOrder(
    nodes=[bed_setup, irrigation_install, climate_setup]
)
modular_bed_install.order.add_edge(bed_setup, irrigation_install)
modular_bed_install.order.add_edge(bed_setup, climate_setup)
# irrigation_install and climate_setup concurrent

# Crop selection and planting partial order
crop_and_plant = StrictPartialOrder(
    nodes=[seed_selection, planting_phase]
)
crop_and_plant.order.add_edge(seed_selection, planting_phase)

# Pest management and growth monitor partial order (concurrent)
# They can be concurrent
pest_growth = StrictPartialOrder(
    nodes=[pest_control, growth_monitor]
)
# no order edges -> concurrent

# Harvest prep after pest and growth
harvest = harvest_prep

# Community engagement and waste management are considered parallel activities around harvest
community_waste = StrictPartialOrder(
    nodes=[community_meet, waste_manage]
)
# no edges, concurrent

# Yield report is last
yield_rpt = yield_report

# Build the full partial order stepwise

# 1. After site_assessment, come design_plan
phase1 = StrictPartialOrder(
    nodes=[site_assessment, design]
)
phase1.order.add_edge(site_assessment, design)

# 2. After design plan, modular bed install
phase2 = StrictPartialOrder(
    nodes=[phase1, modular_bed_install]
)
phase2.order.add_edge(phase1, modular_bed_install)

# 3. After modular bed install, crop and plant
phase3 = StrictPartialOrder(
    nodes=[phase2, crop_and_plant]
)
phase3.order.add_edge(phase2, crop_and_plant)

# 4. After crop and plant, pest and growth in parallel
phase4 = StrictPartialOrder(
    nodes=[phase3, pest_growth]
)
phase4.order.add_edge(phase3, pest_growth)

# 5. After pest and growth, harvest prep
phase5 = StrictPartialOrder(
    nodes=[phase4, harvest]
)
phase5.order.add_edge(phase4, harvest)

# 6. After harvest prep, community engagement and waste manage in parallel
phase6 = StrictPartialOrder(
    nodes=[phase5, community_waste]
)
phase6.order.add_edge(phase5, community_waste)

# 7. After community & waste, yield report
root = StrictPartialOrder(
    nodes=[phase6, yield_rpt]
)
root.order.add_edge(phase6, yield_rpt)