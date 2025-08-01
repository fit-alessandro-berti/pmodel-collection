# Generated from: e225a1da-d5d8-4dd5-9eca-148c85756035.json
# Description: This process details the establishment of a vertical farming facility within an urban environment, integrating advanced hydroponic systems with IoT monitoring, energy-efficient lighting, and automated nutrient delivery. It involves site assessment, modular system design, environmental calibration, crop selection based on market trends, installation of sensors, staff training on smart agriculture technology, regulatory compliance checks, trial cultivation cycles, data-driven yield optimization, and marketing launch strategies. The process ensures sustainable urban agriculture that maximizes space, reduces water usage, and provides fresh produce directly to local consumers while adapting dynamically to environmental feedback through continuous monitoring and system adjustments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities as Transitions with exact given names
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Select_Crops = Transition(label='Select Crops')
Install_Modules = Transition(label='Install Modules')
Setup_Sensors = Transition(label='Setup Sensors')
Calibrate_Climate = Transition(label='Calibrate Climate')
Configure_Lighting = Transition(label='Configure Lighting')
Integrate_IoT = Transition(label='Integrate IoT')
Train_Staff = Transition(label='Train Staff')
Run_Trials = Transition(label='Run Trials')
Analyze_Data = Transition(label='Analyze Data')
Optimize_Yield = Transition(label='Optimize Yield')
Check_Compliance = Transition(label='Check Compliance')
Plan_Marketing = Transition(label='Plan Marketing')
Launch_Facility = Transition(label='Launch Facility')

# Create partial orders for system design & installation steps
# Site Survey -> Design Layout -> Select Crops
preparation = StrictPartialOrder(nodes=[Site_Survey, Design_Layout, Select_Crops])
preparation.order.add_edge(Site_Survey, Design_Layout)
preparation.order.add_edge(Design_Layout, Select_Crops)

# Installation and integration: Install Modules -> Setup Sensors -> Calibrate Climate
# -> Configure Lighting -> Integrate IoT
installation_nodes = [
    Install_Modules,
    Setup_Sensors,
    Calibrate_Climate,
    Configure_Lighting,
    Integrate_IoT
]
installation = StrictPartialOrder(nodes=installation_nodes)
installation.order.add_edge(Install_Modules, Setup_Sensors)
installation.order.add_edge(Setup_Sensors, Calibrate_Climate)
installation.order.add_edge(Calibrate_Climate, Configure_Lighting)
installation.order.add_edge(Configure_Lighting, Integrate_IoT)

# Staff training and compliance checks are concurrent with Analyze Data & Optimize Yield, 
# but must happen after installation & integration
train_and_compliance = StrictPartialOrder(nodes=[Train_Staff, Check_Compliance])
# Trial cultivation cycle: Run Trials -> Analyze Data -> Optimize Yield (sequential)
trials_analysis = StrictPartialOrder(nodes=[Run_Trials, Analyze_Data, Optimize_Yield])
trials_analysis.order.add_edge(Run_Trials, Analyze_Data)
trials_analysis.order.add_edge(Analyze_Data, Optimize_Yield)

# Marketing planning before launch
marketing = StrictPartialOrder(nodes=[Plan_Marketing, Launch_Facility])
marketing.order.add_edge(Plan_Marketing, Launch_Facility)

# Combine Train Staff and Check Compliance and trials_analysis concurrently
post_install = StrictPartialOrder(nodes=[train_and_compliance, trials_analysis])
# To allow concurrency inside, we need to merge inner nodes

# Instead of nesting partial orders directly as nodes,
# flatten nodes for 'post_install' and add edges to enforce dependencies.

post_install = StrictPartialOrder(
    nodes=[
        Train_Staff,
        Check_Compliance,
        Run_Trials,
        Analyze_Data,
        Optimize_Yield,
    ]
)
# Run trials chain
post_install.order.add_edge(Run_Trials, Analyze_Data)
post_install.order.add_edge(Analyze_Data, Optimize_Yield)
# Train Staff and Check Compliance can happen concurrently with trials_analysis
# no edges needed between them

# Assemble the whole process:
# preparation -> installation -> post_install -> marketing

root = StrictPartialOrder(
    nodes=[preparation, installation, post_install, marketing]
)
root.order.add_edge(preparation, installation)
root.order.add_edge(installation, post_install)
root.order.add_edge(post_install, marketing)