# Generated from: cc6a0acc-edcb-405b-b949-ef30a817db08.json
# Description: This process outlines the complex steps involved in transforming underutilized urban rooftops into productive agricultural spaces. It covers site assessment, structural analysis, soil and water testing, modular bed installation, climate control setup, crop selection, pest management, community engagement, and ongoing maintenance. The workflow ensures sustainable food production within city environments by integrating technology, environmental considerations, and stakeholder collaboration to maximize yield and minimize ecological impact.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all atomic activities
site_survey    = Transition(label="Site Survey")
load_test      = Transition(label="Load Test")
soil_sample    = Transition(label="Soil Sample")
water_check    = Transition(label="Water Check")
design_plan    = Transition(label="Design Plan")
bed_setup      = Transition(label="Bed Setup")
irrigation     = Transition(label="Irrigation Install")
climate_setup  = Transition(label="Climate Setup")
seed_selection = Transition(label="Seed Selection")
planting       = Transition(label="Planting Phase")
pest_control   = Transition(label="Pest Control")
growth_monitor = Transition(label="Growth Monitor")
harvest_prep   = Transition(label="Harvest Prep")
community_meet = Transition(label="Community Meet")
waste_manage   = Transition(label="Waste Manage")
yield_report   = Transition(label="Yield Report")

# 1) Initial assessment & testing: SS → LT → {Soil,Water} → DP
initial = StrictPartialOrder(nodes=[site_survey, load_test, soil_sample, water_check, design_plan])
initial.order.add_edge(site_survey, load_test)
initial.order.add_edge(load_test, soil_sample)
initial.order.add_edge(load_test, water_check)
initial.order.add_edge(soil_sample, design_plan)
initial.order.add_edge(water_check, design_plan)

# 2) Installation & planting: DP → Bed → {Irrigation,Climate} → Seed Sel → Plant
install = StrictPartialOrder(nodes=[
    design_plan,
    bed_setup,
    irrigation,
    climate_setup,
    seed_selection,
    planting
])
install.order.add_edge(design_plan, bed_setup)
install.order.add_edge(bed_setup, irrigation)
install.order.add_edge(bed_setup, climate_setup)
install.order.add_edge(irrigation, seed_selection)
install.order.add_edge(climate_setup, seed_selection)
install.order.add_edge(seed_selection, planting)

# 3) Growth‐phase loop: concurrently do Growth Monitor & Pest Control, repeat until done
loop_body = StrictPartialOrder(nodes=[growth_monitor, pest_control])
# silent step for loop‐exit decision
skip = SilentTransition()
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, skip])

# 4) Harvest prep → parallel {Community meet, Waste manage} → Yield report
community_waste = StrictPartialOrder(nodes=[community_meet, waste_manage])
# no edges => they are concurrent

# 5) Assemble the global partial order
root = StrictPartialOrder(
    nodes=[initial, install, growth_loop, harvest_prep, community_waste, yield_report]
)
root.order.add_edge(initial, install)
root.order.add_edge(install, growth_loop)
root.order.add_edge(growth_loop, harvest_prep)
root.order.add_edge(harvest_prep, community_waste)
root.order.add_edge(community_waste, yield_report)