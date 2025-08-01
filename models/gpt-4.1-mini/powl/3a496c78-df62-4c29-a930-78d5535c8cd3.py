# Generated from: 3a496c78-df62-4c29-a930-78d5535c8cd3.json
# Description: This process details the establishment of an urban vertical farming system within a repurposed commercial building. It involves site evaluation, structural modifications, installation of hydroponic systems, climate control setup, automated nutrient delivery configuration, and integration of AI-driven monitoring tools. Additionally, it includes staff training, regulatory compliance verification, crop planning, and marketing strategy development to ensure sustainable and efficient production of fresh produce in limited urban spaces while minimizing environmental impact and maximizing yield.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
site_survey = Transition(label='Site Survey')
structural_eval = Transition(label='Structural Eval')
permit_obtain = Transition(label='Permit Obtain')
system_design = Transition(label='System Design')
hydroponic_install = Transition(label='Hydroponic Install')
climate_setup = Transition(label='Climate Setup')
lighting_config = Transition(label='Lighting Config')
nutrient_setup = Transition(label='Nutrient Setup')
automation_setup = Transition(label='Automation Setup')
ai_integration = Transition(label='AI Integration')
staff_training = Transition(label='Staff Training')
compliance_check = Transition(label='Compliance Check')
crop_planning = Transition(label='Crop Planning')
yield_testing = Transition(label='Yield Testing')
market_launch = Transition(label='Market Launch')

# We interpret the process as follows:
# 1) Preliminary site and structural evaluation and permits:
prelim_po = StrictPartialOrder(
    nodes=[site_survey, structural_eval, permit_obtain],
)
prelim_po.order.add_edge(site_survey, structural_eval)
prelim_po.order.add_edge(structural_eval, permit_obtain)

# 2) System design and installation (order and some concurrency):
# System Design before Hydroponic Install and Climate Setup
install_po = StrictPartialOrder(
    nodes=[system_design, hydroponic_install, climate_setup, lighting_config, nutrient_setup, automation_setup, ai_integration],
)
install_po.order.add_edge(system_design, hydroponic_install)
install_po.order.add_edge(system_design, climate_setup)

# hydroponic_install before lighting_config and nutrient_setup
install_po.order.add_edge(hydroponic_install, lighting_config)
install_po.order.add_edge(hydroponic_install, nutrient_setup)

# climate_setup before automation_setup and ai_integration
install_po.order.add_edge(climate_setup, automation_setup)
install_po.order.add_edge(climate_setup, ai_integration)

# lighting_config, nutrient_setup before automation_setup (automation depends on them)
install_po.order.add_edge(lighting_config, automation_setup)
install_po.order.add_edge(nutrient_setup, automation_setup)

# ai_integration can happen concurrently with staff_training later (we'll connect that later)

# 3) Staff training, compliance check (after installations)
staff_and_compliance_po = StrictPartialOrder(
    nodes=[staff_training, compliance_check],
)
staff_and_compliance_po.order.add_edge(staff_training, compliance_check)

# 4) Crop planning and yield testing in order
crop_yield_po = StrictPartialOrder(
    nodes=[crop_planning, yield_testing],
)
crop_yield_po.order.add_edge(crop_planning, yield_testing)

# 5) Market launch last
market_launch_po = StrictPartialOrder(nodes=[market_launch])

# Now combine all parts reflecting probable order:
root = StrictPartialOrder(
    nodes=[prelim_po, install_po, staff_and_compliance_po, crop_yield_po, market_launch_po]
)
# prelim_po before install_po
root.order.add_edge(prelim_po, install_po)
# install_po before staff_and_compliance_po
root.order.add_edge(install_po, staff_and_compliance_po)
# install_po also before crop_planning (since AI integration can run concurrently with staff_training,
# to maintain order, put crop_planning after staff_and_compliance_po for workflow)
root.order.add_edge(staff_and_compliance_po, crop_yield_po)
# crop_yield_po before market launch
root.order.add_edge(crop_yield_po, market_launch_po)