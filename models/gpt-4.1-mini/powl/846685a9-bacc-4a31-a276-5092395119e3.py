# Generated from: 846685a9-bacc-4a31-a276-5092395119e3.json
# Description: This process outlines the complex steps involved in establishing a sustainable urban vertical farm within a repurposed commercial building. It includes site assessment, environmental control system design, modular planting unit installation, nutrient solution preparation, and integration of IoT monitoring devices. The process also covers labor scheduling for planting cycles, pest management using biological controls, and data analytics for yield optimization. Additionally, it involves community engagement for local produce distribution, energy consumption audits, and continuous improvement through feedback loops, making it a multifaceted and atypical business operation in the agricultural technology sector.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
Site_Survey = Transition(label='Site Survey')
Design_Layout = Transition(label='Design Layout')
Install_Modules = Transition(label='Install Modules')
Setup_Lighting = Transition(label='Setup Lighting')
Configure_Sensors = Transition(label='Configure Sensors')
Prepare_Nutrients = Transition(label='Prepare Nutrients')
Seed_Planting = Transition(label='Seed Planting')
Monitor_Growth = Transition(label='Monitor Growth')
Pest_Control = Transition(label='Pest Control')
Data_Collection = Transition(label='Data Collection')
Analyze_Metrics = Transition(label='Analyze Metrics')
Schedule_Labor = Transition(label='Schedule Labor')
Energy_Audit = Transition(label='Energy Audit')
Community_Outreach = Transition(label='Community Outreach')
Feedback_Review = Transition(label='Feedback Review')
Yield_Packaging = Transition(label='Yield Packaging')
Distribution_Plan = Transition(label='Distribution Plan')

# Model the feedback loop: after Feedback Review, choose either to exit or to go back to Schedule Labor
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[Schedule_Labor, Feedback_Review])

# Modular planting unit and environmental control installations run in parallel after layout design
env_install = StrictPartialOrder(nodes=[Setup_Lighting, Configure_Sensors])
mod_planting = StrictPartialOrder(nodes=[Install_Modules])

install_phase = StrictPartialOrder(nodes=[Design_Layout, env_install, mod_planting])
install_phase.order.add_edge(Design_Layout, env_install)
install_phase.order.add_edge(Design_Layout, mod_planting)

# Nutrient preparation and seed planting are sequential after installations
nutrients_and_planting = StrictPartialOrder(nodes=[Prepare_Nutrients, Seed_Planting])
nutrients_and_planting.order.add_edge(Prepare_Nutrients, Seed_Planting)

# Monitoring and pest control with partial order (can be concurrent)
monitor_pest = StrictPartialOrder(nodes=[Monitor_Growth, Pest_Control])

# Data collection and analysis sequential
data_and_analysis = StrictPartialOrder(nodes=[Data_Collection, Analyze_Metrics])
data_and_analysis.order.add_edge(Data_Collection, Analyze_Metrics)

# Packaging and distribution sequential
pack_dist = StrictPartialOrder(nodes=[Yield_Packaging, Distribution_Plan])
pack_dist.order.add_edge(Yield_Packaging, Distribution_Plan)

# Community outreach and energy audit can occur concurrently, both before or during monitoring
comm_energy = StrictPartialOrder(nodes=[Community_Outreach, Energy_Audit])

# Final overall process partial order
root = StrictPartialOrder(nodes=[
    Site_Survey,
    install_phase,
    nutrients_and_planting,
    monitor_pest,
    data_and_analysis,
    feedback_loop,
    comm_energy,
    pack_dist
])

# Define order edges
root.order.add_edge(Site_Survey, install_phase)
root.order.add_edge(install_phase, nutrients_and_planting)
root.order.add_edge(nutrients_and_planting, monitor_pest)
root.order.add_edge(monitor_pest, data_and_analysis)
root.order.add_edge(data_and_analysis, feedback_loop)
root.order.add_edge(feedback_loop, pack_dist)

# Comm and energy audit concurrent but after Site Survey and can occur before or during monitor_pest
root.order.add_edge(Site_Survey, comm_energy)
root.order.add_edge(comm_energy, monitor_pest)