# Generated from: d227f68d-91ef-4a5d-9122-edcc9ca30f4a.json
# Description: This process outlines the comprehensive steps involved in establishing an urban vertical farm within a metropolitan environment. It begins with site evaluation and proceeds through modular infrastructure assembly, hydroponic system installation, and climate control calibration. The process includes seed selection tailored to urban microclimates, nutrient solution formulation, and automated growth monitoring integration. It also involves compliance verification with local zoning laws, energy optimization for sustainability, pest management through biological controls, and logistics planning for distribution. Finally, the process concludes with staff training on advanced cultivation techniques and ongoing performance analysis to maximize yield and resource efficiency in a constrained urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permits_check = Transition(label='Permits Check')
foundation_prep = Transition(label='Foundation Prep')
frame_assembly = Transition(label='Frame Assembly')
hydro_setup = Transition(label='Hydro Setup')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
system_calibration = Transition(label='System Calibration')
pest_control = Transition(label='Pest Control')
automation_link = Transition(label='Automation Link')
staff_training = Transition(label='Staff Training')
yield_tracking = Transition(label='Yield Tracking')
distribution_plan = Transition(label='Distribution Plan')

# Define partial orders for main sequences
# Site evaluation and infrastructure assembly
po1 = StrictPartialOrder(nodes=[site_survey, design_layout, permits_check, foundation_prep, frame_assembly])
po1.order.add_edge(site_survey, design_layout)
po1.order.add_edge(design_layout, permits_check)
po1.order.add_edge(permits_check, foundation_prep)
po1.order.add_edge(foundation_prep, frame_assembly)

# Hydroponic system installation and climate control calibration in partial order
po2 = StrictPartialOrder(nodes=[hydro_setup, climate_setup])
# no order between hydro_setup and climate_setup to allow concurrency

# Seed selection and nutrient mix with system calibration
po3 = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, system_calibration])
po3.order.add_edge(seed_selection, nutrient_mix)
po3.order.add_edge(nutrient_mix, system_calibration)

# Pest control and automation link concurrent
po4 = StrictPartialOrder(nodes=[pest_control, automation_link])
# no order between pest_control and automation_link

# Staff training and yield tracking concurrent with distribution plan after them
po5_inner = StrictPartialOrder(nodes=[staff_training, yield_tracking])
# no order between staff_training and yield_tracking

po5 = StrictPartialOrder(nodes=[po5_inner, distribution_plan])
po5.order.add_edge(po5_inner, distribution_plan)

# Combine the parts in a partial order with edges connecting main phases
root = StrictPartialOrder(nodes=[po1, po2, po3, po4, po5])
root.order.add_edge(po1, po2)
root.order.add_edge(po1, po3)
root.order.add_edge(po2, po4)
root.order.add_edge(po3, po4)
root.order.add_edge(po4, po5)