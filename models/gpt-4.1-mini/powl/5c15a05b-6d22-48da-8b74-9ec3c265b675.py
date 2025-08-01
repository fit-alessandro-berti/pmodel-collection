# Generated from: 5c15a05b-6d22-48da-8b74-9ec3c265b675.json
# Description: This process outlines the establishment of a fully automated urban vertical farm within a repurposed industrial building. It involves initial site analysis, environmental impact assessments, integration of IoT sensors for microclimate control, modular hydroponic rack installation, nutrient solution calibration, AI-driven crop scheduling, automated seeding and harvesting, waste recycling loops, and sustainability reporting. The procedure ensures optimized space utilization, energy efficiency, and maximized crop yield while adhering to local regulations and community engagement protocols, making it a complex yet innovative approach to urban agriculture.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
site_survey = Transition(label='Site Survey')
impact_study = Transition(label='Impact Study')
iot_setup = Transition(label='IoT Setup')
rack_install = Transition(label='Rack Install')
nutrient_mix = Transition(label='Nutrient Mix')
crop_schedule = Transition(label='Crop Schedule')
seed_automation = Transition(label='Seed Automation')
harvest_cycle = Transition(label='Harvest Cycle')
waste_process = Transition(label='Waste Process')
energy_audit = Transition(label='Energy Audit')
data_sync = Transition(label='Data Sync')
quality_check = Transition(label='Quality Check')
regulation_review = Transition(label='Regulation Review')
community_meet = Transition(label='Community Meet')
report_generate = Transition(label='Report Generate')

# Waste recycling loop: repeat waste_process then data_sync
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_process, data_sync])

# After IoT Setup and Rack Install, Nutrient Mix is done, then Crop Scheduling
crop_prep = StrictPartialOrder(nodes=[nutrient_mix, crop_schedule])
crop_prep.order.add_edge(nutrient_mix, crop_schedule)

# Automation sequence: Seed Automation then Harvest Cycle
automation_seq = StrictPartialOrder(nodes=[seed_automation, harvest_cycle])
automation_seq.order.add_edge(seed_automation, harvest_cycle)

# Site preparation partial order: Site Survey -> Impact Study -> IoT Setup and Rack Install concurrent
site_prep = StrictPartialOrder(nodes=[site_survey, impact_study, iot_setup, rack_install])
site_prep.order.add_edge(site_survey, impact_study)
site_prep.order.add_edge(impact_study, iot_setup)
site_prep.order.add_edge(impact_study, rack_install)

# Quality and compliance partial order: Energy Audit, Quality Check, Regulation Review, Community Meet in sequence
quality_compliance = StrictPartialOrder(nodes=[energy_audit, quality_check, regulation_review, community_meet])
quality_compliance.order.add_edge(energy_audit, quality_check)
quality_compliance.order.add_edge(quality_check, regulation_review)
quality_compliance.order.add_edge(regulation_review, community_meet)

# Reporting after above
report_and_sync = StrictPartialOrder(nodes=[report_generate, data_sync])
report_and_sync.order.add_edge(report_generate, data_sync)

# Full process partial order nodes:
# - site_prep
# - crop_prep
# - automation_seq
# - waste_loop
# - quality_compliance
# - report_and_sync

# Note: data_sync occurs in waste_loop as looping activity and at end for final sync, 
# treat these as separate instances (waste_loop uses data_sync node, final uses separate data_sync node)
# To avoid confusion, redefine final data_sync as distinct Transition with same label
final_data_sync = Transition(label='Data Sync')

# Build partial order connecting everything logically:

# Overall nodes
root_nodes = [
    site_prep,
    crop_prep,
    automation_seq,
    waste_loop,
    quality_compliance,
    report_generate,
    final_data_sync
]

root = StrictPartialOrder(nodes=root_nodes)

# Define ordering between main phases:

# 1) Site preparation before crop preparation
root.order.add_edge(site_prep, crop_prep)

# 2) Crop preparation before automation sequence
root.order.add_edge(crop_prep, automation_seq)

# 3) Automation sequence before waste loop
root.order.add_edge(automation_seq, waste_loop)

# 4) Waste loop before quality compliance
root.order.add_edge(waste_loop, quality_compliance)

# 5) Quality compliance before final report and sync
# report_generate node already in root, tie quality_compliance --> report_generate
root.order.add_edge(quality_compliance, report_generate)

# 6) Report generate before final data sync
root.order.add_edge(report_generate, final_data_sync)