# Generated from: dcc961c5-86a2-44f2-a5d9-420d123b4bb9.json
# Description: This process outlines the complex setup and operational workflow for establishing an urban vertical farm within a densely populated city environment. It involves site assessment, modular design, climate control calibration, hydroponic nutrient balancing, automated seeding, integrated pest management, energy optimization, data-driven growth monitoring, waste recycling, and community engagement initiatives. The process requires coordination between architects, agronomists, engineers, and local authorities to ensure sustainable production, regulatory compliance, and minimal ecological footprint while maximizing yield and quality of fresh produce in a constrained urban space.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_acquire = Transition(label='Permit Acquire')
modular_build = Transition(label='Modular Build')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_automation = Transition(label='Seed Automation')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
sensor_install = Transition(label='Sensor Install')
growth_monitor = Transition(label='Growth Monitor')
waste_process = Transition(label='Waste Process')
data_analysis = Transition(label='Data Analysis')
staff_train = Transition(label='Staff Train')
community_link = Transition(label='Community Link')
yield_report = Transition(label='Yield Report')

# Phase 1: Initial assessment and design with permits
phase1 = StrictPartialOrder(nodes=[site_survey, design_layout, permit_acquire])
phase1.order.add_edge(site_survey, design_layout)
phase1.order.add_edge(site_survey, permit_acquire)
phase1.order.add_edge(design_layout, permit_acquire)

# Phase 2: Construction and calibration
phase2 = StrictPartialOrder(nodes=[modular_build, climate_setup, nutrient_mix])
phase2.order.add_edge(modular_build, climate_setup)
phase2.order.add_edge(climate_setup, nutrient_mix)

# Phase 3: Installation of automation and control systems
phase3 = StrictPartialOrder(nodes=[seed_automation, pest_control, energy_audit, sensor_install])
phase3.order.add_edge(seed_automation, pest_control)
phase3.order.add_edge(pest_control, energy_audit)
phase3.order.add_edge(energy_audit, sensor_install)

# Phase 4: Monitoring, waste, and analysis running in parallel with data and operations close coordination
phase4 = StrictPartialOrder(nodes=[growth_monitor, waste_process, data_analysis])
# growth_monitor and waste_process can run concurrently, data_analysis depends on growth_monitor and waste_process
phase4.order.add_edge(growth_monitor, data_analysis)
phase4.order.add_edge(waste_process, data_analysis)

# Phase 5: Training, community, and reporting
phase5 = StrictPartialOrder(nodes=[staff_train, community_link, yield_report])
phase5.order.add_edge(staff_train, community_link)
phase5.order.add_edge(community_link, yield_report)

# Compose whole process: phases ordered, some concurrency internally
root = StrictPartialOrder(
    nodes=[phase1, phase2, phase3, phase4, phase5]
)
root.order.add_edge(phase1, phase2)
root.order.add_edge(phase2, phase3)
root.order.add_edge(phase3, phase4)
root.order.add_edge(phase4, phase5)