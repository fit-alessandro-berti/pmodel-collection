# Generated from: 0bb6a448-b0d1-489f-aff5-1c6992335e25.json
# Description: This process outlines the intricate steps involved in launching an urban vertical farm, integrating advanced hydroponics, renewable energy, and IoT monitoring systems. It begins with site analysis and regulatory approval, followed by system design, vendor selection, and infrastructure setup. Subsequent phases include seed sourcing, climate calibration, and automation programming. Quality control and pest management run concurrently with staff training and community outreach to ensure sustainability and local engagement. The final stages focus on trial harvests, data analysis, and iterative optimization before full commercial production begins, ensuring a resilient urban agriculture ecosystem.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_analysis         = Transition(label='Site Analysis')
permit_filing         = Transition(label='Permit Filing')
system_design         = Transition(label='System Design')
vendor_selection      = Transition(label='Vendor Selection')
infrastructure_setup  = Transition(label='Infrastructure Setup')
seed_sourcing         = Transition(label='Seed Sourcing')
climate_setup         = Transition(label='Climate Setup')
automation_code       = Transition(label='Automation Code')
quality_control       = Transition(label='Quality Control')
pest_monitoring       = Transition(label='Pest Monitoring')
staff_training        = Transition(label='Staff Training')
community_outreach    = Transition(label='Community Outreach')
trial_harvest         = Transition(label='Trial Harvest')
data_review           = Transition(label='Data Review')
process_optimize      = Transition(label='Process Optimize')
launch_prep           = Transition(label='Launch Prep')
commercial_start      = Transition(label='Commercial Start')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_analysis,
    permit_filing,
    system_design,
    vendor_selection,
    infrastructure_setup,
    seed_sourcing,
    climate_setup,
    automation_code,
    quality_control,
    pest_monitoring,
    staff_training,
    community_outreach,
    trial_harvest,
    data_review,
    process_optimize,
    launch_prep,
    commercial_start
])

# Define the sequence and concurrency relations
root.order.add_edge(site_analysis, permit_filing)
root.order.add_edge(permit_filing, system_design)
root.order.add_edge(system_design, vendor_selection)
root.order.add_edge(vendor_selection, infrastructure_setup)
root.order.add_edge(infrastructure_setup, seed_sourcing)
root.order.add_edge(seed_sourcing, climate_setup)
root.order.add_edge(climate_setup, automation_code)

# After automation, four activities run concurrently
for next_task in [quality_control, pest_monitoring, staff_training, community_outreach]:
    root.order.add_edge(automation_code, next_task)

# All four must complete before trial harvest
for prev_task in [quality_control, pest_monitoring, staff_training, community_outreach]:
    root.order.add_edge(prev_task, trial_harvest)

# Final sequence
root.order.add_edge(trial_harvest, data_review)
root.order.add_edge(data_review, process_optimize)
root.order.add_edge(process_optimize, launch_prep)
root.order.add_edge(launch_prep, commercial_start)