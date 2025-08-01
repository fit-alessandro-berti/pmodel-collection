# Generated from: 766c9267-3879-4b0f-b1d3-1360c4a5bee6.json
# Description: This process outlines the intricate steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site evaluation, structural retrofitting, environmental system integration, and crop selection tailored to local climate and market demand. The process further encompasses automation implementation for irrigation and nutrient delivery, staff training on hydroponic techniques, and ongoing monitoring protocols to optimize yield. It concludes with regulatory compliance checks and launching a local distribution network to ensure fresh produce reaches urban consumers efficiently, balancing sustainability and profitability in a dense city environment.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Site_Survey = Transition(label='Site Survey')
Load_Analysis = Transition(label='Load Analysis')
Structure_Retrofit = Transition(label='Structure Retrofit')
Climate_Study = Transition(label='Climate Study')
Crop_Selection = Transition(label='Crop Selection')
System_Design = Transition(label='System Design')
Irrigation_Setup = Transition(label='Irrigation Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automation_Install = Transition(label='Automation Install')
Staff_Training = Transition(label='Staff Training')
Growth_Monitoring = Transition(label='Growth Monitoring')
Pest_Control = Transition(label='Pest Control')
Regulation_Audit = Transition(label='Regulation Audit')
Packaging_Design = Transition(label='Packaging Design')
Distribution_Plan = Transition(label='Distribution Plan')

# Site evaluation partial order
site_eval = StrictPartialOrder(nodes=[Site_Survey, Load_Analysis])
site_eval.order.add_edge(Site_Survey, Load_Analysis)

# Structural retrofitting depends on load analysis
structural_retrofit = Structure_Retrofit

# Environmental system depends on climate study and system design depends on climate study
env_study = StrictPartialOrder(nodes=[Climate_Study, Crop_Selection])
# Climate study precedes crop selection (tailored to climate and market demand)
env_study.order.add_edge(Climate_Study, Crop_Selection)

system_design = System_Design

# System Design depends on climate study
# We'll create PO of climate study --> crop selection and system design happens after climate study (concurrent with crop selection)
env_and_design = StrictPartialOrder(nodes=[Crop_Selection, system_design])
env_and_design.order.add_edge(Crop_Selection, system_design)

# Automation components
automation_steps = StrictPartialOrder(nodes=[Irrigation_Setup, Nutrient_Mix, Automation_Install])
automation_steps.order.add_edge(Irrigation_Setup, Nutrient_Mix)
automation_steps.order.add_edge(Nutrient_Mix, Automation_Install)

# Staff training follows automation install
staff_training = Staff_Training

# Growth monitoring and pest control run concurrently after staff training
monitor_and_pest = StrictPartialOrder(nodes=[Growth_Monitoring, Pest_Control])

# Regulatory compliance
regulation = Regulation_Audit

# Packaging and distribution plans run concurrently after regulation audit
packaging_distribution = StrictPartialOrder(nodes=[Packaging_Design, Distribution_Plan])

# Build main flow edges:
# site_eval --> structure retrofit
# structure retrofit --> climate study
# climate study --> crop selection
# crop selection and system design run concurrently, but system design occurs after crop selection (from env_and_design)
# system design --> automation steps
# automation steps --> staff training
# staff training --> monitoring and pest control (concurrent)
# monitoring and pest control --> regulation audit
# regulation audit --> packaging and distribution (concurrent)

root = StrictPartialOrder(nodes=[
    site_eval, 
    structural_retrofit, 
    climate_study := Climate_Study,  # for explicit edge definition
    env_study,
    env_and_design,
    automation_steps,
    staff_training,
    monitor_and_pest,
    regulation,
    packaging_distribution
])

# Add partial order edges among these nodes:

# site_eval before structure retrofit
root.order.add_edge(site_eval, structural_retrofit)

# structure retrofit before climate study
root.order.add_edge(structural_retrofit, climate_study)

# climate study before env_study (which contains crop selection only after climate study)
root.order.add_edge(climate_study, env_study)

# env_study before env_and_design (crop selection and system design)
root.order.add_edge(env_study, env_and_design)

# env_and_design before automation steps
root.order.add_edge(env_and_design, automation_steps)

# automation steps before staff training
root.order.add_edge(automation_steps, staff_training)

# staff training before monitor and pest control
root.order.add_edge(staff_training, monitor_and_pest)

# monitor and pest control before regulation audit
root.order.add_edge(monitor_and_pest, regulation)

# regulation audit before packaging and distribution
root.order.add_edge(regulation, packaging_distribution)