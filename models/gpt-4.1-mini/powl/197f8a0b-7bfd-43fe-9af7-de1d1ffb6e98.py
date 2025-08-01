# Generated from: 197f8a0b-7bfd-43fe-9af7-de1d1ffb6e98.json
# Description: This process outlines the comprehensive steps required to establish an urban vertical farm within a repurposed industrial building. It covers initial site assessment, environmental impact analysis, structural modifications, hydroponic system design, nutrient cycle planning, automation integration, staff training, regulatory compliance, and market launch strategies. The approach uniquely combines architectural retrofitting with advanced agricultural technology to maximize yield in limited urban spaces, addressing sustainability and fresh local produce demand while navigating complex zoning laws and community engagement requirements.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
Site_Survey = Transition(label='Site Survey')
Impact_Study = Transition(label='Impact Study')
Design_Layout = Transition(label='Design Layout')
Permit_Filing = Transition(label='Permit Filing')
Structure_Mod = Transition(label='Structure Mod')
System_Install = Transition(label='System Install')
Nutrient_Plan = Transition(label='Nutrient Plan')
Water_Setup = Transition(label='Water Setup')
Lighting_Config = Transition(label='Lighting Config')
Automation_Test = Transition(label='Automation Test')
Staff_Onboard = Transition(label='Staff Onboard')
Compliance_Check = Transition(label='Compliance Check')
Trial_Grow = Transition(label='Trial Grow')
Harvest_Eval = Transition(label='Harvest Eval')
Market_Launch = Transition(label='Market Launch')

# According to the description and typical process:
# 1. Initial site assessment and environmental impact analysis are sequential and mandatory:
# Site Survey --> Impact Study

# 2. Design layout and permit filing are sequential and mandatory (design precedes permit):
# Design Layout --> Permit Filing

# 3. Structural modifications after permits:
# Permit Filing --> Structure Mod

# 4. Parallel advanced agricultural system installations happen after structural mods:
# System Install, Nutrient Plan, Water Setup, Lighting Config, Automation Test

# These five activities are done in partial order or concurrency:
# Let's represent these five as a StrictPartialOrder without order edges to mean concurrent

# 5. Staff training follows automation test and system install components:
# Staff Onboard depends on System Install and Automation Test being finished
# Nutrient Plan, Water Setup, Lighting Config do not block Staff Onboard directly

# 6. Compliance Check must be done after Staff Onboard
# 7. Trial Grow and Harvest Eval come after Compliance Check (sequential)
# 8. Market Launch after Harvest Eval

# Build partial order for the parallel install phase
install_nodes = [
    System_Install,
    Nutrient_Plan,
    Water_Setup,
    Lighting_Config,
    Automation_Test
]
install_phase = StrictPartialOrder(nodes=install_nodes)
# No order edges inside install phase (all concurrent)

# Now build the main backbone partial order:
# Site Survey --> Impact Study --> Design Layout --> Permit Filing --> Structure Mod --> install_phase --> Staff Onboard --> Compliance Check --> Trial Grow --> Harvest Eval --> Market Launch

# Because install_phase is a node itself, order edges connect structure_mod to install_phase, and install_phase to Staff Onboard

nodes = [
    Site_Survey,
    Impact_Study,
    Design_Layout,
    Permit_Filing,
    Structure_Mod,
    install_phase,
    Staff_Onboard,
    Compliance_Check,
    Trial_Grow,
    Harvest_Eval,
    Market_Launch
]

root = StrictPartialOrder(nodes=nodes)
root.order.add_edge(Site_Survey, Impact_Study)
root.order.add_edge(Impact_Study, Design_Layout)
root.order.add_edge(Design_Layout, Permit_Filing)
root.order.add_edge(Permit_Filing, Structure_Mod)
root.order.add_edge(Structure_Mod, install_phase)
root.order.add_edge(install_phase, Staff_Onboard)
root.order.add_edge(Staff_Onboard, Compliance_Check)
root.order.add_edge(Compliance_Check, Trial_Grow)
root.order.add_edge(Trial_Grow, Harvest_Eval)
root.order.add_edge(Harvest_Eval, Market_Launch)