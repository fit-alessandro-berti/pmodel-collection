# Generated from: 234fa21f-4e24-4e0c-8f9d-af034426352a.json
# Description: This process involves the planning, construction, and operational setup of a multi-layered urban vertical farm within a repurposed commercial building. It begins with site analysis and environmental assessment, followed by structural modifications and installation of hydroponic systems. Subsequent activities include climate control calibration, nutrient solution preparation, seed selection and planting, automated monitoring integration, and workforce training. The process concludes with trial harvests, quality control assessments, and adjustments to optimize yield while minimizing resource consumption and environmental impact in a dense urban setting.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
permitting       = Transition(label='Permitting')
hydro_setup      = Transition(label='Hydro Setup')
climate_setup    = Transition(label='Climate Setup')
nutrient_mix     = Transition(label='Nutrient Mix')
seed_selection   = Transition(label='Seed Selection')
planting         = Transition(label='Planting')
sensor_install   = Transition(label='Sensor Install')
automation_config= Transition(label='Automation Config')
staff_hiring     = Transition(label='Staff Hiring')
training         = Transition(label='Training')
trial_harvest    = Transition(label='Trial Harvest')
quality_check    = Transition(label='Quality Check')
yield_review     = Transition(label='Yield Review')
resource_audit   = Transition(label='Resource Audit')

# Build the loop for iterative adjustments: do Harvest->QC, then optionally do Review->Audit and repeat
A_loop = StrictPartialOrder(nodes=[trial_harvest, quality_check])
A_loop.order.add_edge(trial_harvest, quality_check)

B_loop = StrictPartialOrder(nodes=[yield_review, resource_audit])
B_loop.order.add_edge(yield_review, resource_audit)

loop = OperatorPOWL(operator=Operator.LOOP, children=[A_loop, B_loop])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    site_survey, structural_check, permitting, hydro_setup,
    climate_setup, nutrient_mix, seed_selection, planting,
    sensor_install, automation_config, staff_hiring, training,
    loop
])

# Site survey → Structural check → Permitting → Hydro setup
root.order.add_edge(site_survey, structural_check)
root.order.add_edge(structural_check, permitting)
root.order.add_edge(permitting, hydro_setup)

# After hydro_system is ready, parallel preparatory tasks
root.order.add_edge(hydro_setup, climate_setup)
root.order.add_edge(hydro_setup, nutrient_mix)
root.order.add_edge(hydro_setup, sensor_install)
root.order.add_edge(hydro_setup, staff_hiring)

# Sensor installation before automation configuration
root.order.add_edge(sensor_install, automation_config)

# Nutrient mix → Seed selection → Planting
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, planting)

# Staff hiring → Training
root.order.add_edge(staff_hiring, training)

# Before starting trial harvest, ensure planting, climate, automation, and training are done
root.order.add_edge(planting, loop)
root.order.add_edge(climate_setup, loop)
root.order.add_edge(automation_config, loop)
root.order.add_edge(training, loop)