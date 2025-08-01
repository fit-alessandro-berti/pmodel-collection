# Generated from: 766c9267-3879-4b0f-b1d3-1360c4a5bee6.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site evaluation, structural retrofitting, environmental system integration, and crop selection tailored to local climate and market demand. The process further encompasses automation implementation for irrigation and nutrient delivery, staff training on hydroponic techniques, and ongoing monitoring protocols to optimize yield. It concludes with regulatory compliance checks and launching a local distribution network to ensure fresh produce reaches urban consumers efficiently, balancing sustainability and profitability in a dense city environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey        = Transition(label='Site Survey')
load_analysis      = Transition(label='Load Analysis')
structure_retrofit = Transition(label='Structure Retrofit')
climate_study      = Transition(label='Climate Study')
crop_selection     = Transition(label='Crop Selection')
system_design      = Transition(label='System Design')
irrigation_setup   = Transition(label='Irrigation Setup')
nutrient_mix       = Transition(label='Nutrient Mix')
automation_install = Transition(label='Automation Install')
staff_training     = Transition(label='Staff Training')
growth_monitoring  = Transition(label='Growth Monitoring')
pest_control       = Transition(label='Pest Control')
regulation_audit   = Transition(label='Regulation Audit')
packaging_design   = Transition(label='Packaging Design')
distribution_plan  = Transition(label='Distribution Plan')

# Define a loop for ongoing monitoring and pest control
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[growth_monitoring, pest_control]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    load_analysis,
    structure_retrofit,
    climate_study,
    crop_selection,
    system_design,
    irrigation_setup,
    nutrient_mix,
    automation_install,
    staff_training,
    monitoring_loop,
    regulation_audit,
    packaging_design,
    distribution_plan
])

# Add the sequencing edges
root.order.add_edge(site_survey, load_analysis)
root.order.add_edge(load_analysis, structure_retrofit)
root.order.add_edge(structure_retrofit, climate_study)
root.order.add_edge(climate_study, crop_selection)
root.order.add_edge(crop_selection, system_design)

# After system design, three tasks can run in parallel, then join at staff training
for task in [irrigation_setup, nutrient_mix, automation_install]:
    root.order.add_edge(system_design, task)
    root.order.add_edge(task, staff_training)

# Staff training precedes the monitoring loop
root.order.add_edge(staff_training, monitoring_loop)

# After the monitoring loop, finish with audit, packaging, and distribution
root.order.add_edge(monitoring_loop, regulation_audit)
root.order.add_edge(regulation_audit, packaging_design)
root.order.add_edge(packaging_design, distribution_plan)