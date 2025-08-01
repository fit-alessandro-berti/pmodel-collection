# Generated from: 3c8221db-62bb-4c0a-b5d2-631e0417f77d.json
# Description: This process outlines the comprehensive steps required to establish a fully operational urban vertical farm within a repurposed warehouse. It involves initial site analysis, structural retrofitting, environmental control system installation, hydroponic and aeroponic system integration, nutrient solution calibration, automated monitoring deployment, staff training, and ongoing yield optimization. The process ensures sustainable resource usage, minimal environmental impact, and maximized crop output through precision agriculture technologies. It also includes regulatory compliance checks and community engagement initiatives to promote local food production and urban greening efforts.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
structural_audit  = Transition(label='Structural Audit')
design_layout     = Transition(label='Design Layout')
retrofitting      = Transition(label='Retrofitting')
system_install    = Transition(label='System Install')
climate_setup     = Transition(label='Climate Setup')
nutrient_prep     = Transition(label='Nutrient Prep')
plant_seeding     = Transition(label='Plant Seeding')
sensor_deploy     = Transition(label='Sensor Deploy')
automation_tune   = Transition(label='Automation Tune')
staff_training    = Transition(label='Staff Training')
compliance_check  = Transition(label='Compliance Check')
community_meet    = Transition(label='Community Meet')
waste_manage      = Transition(label='Waste Manage')
energy_audit      = Transition(label='Energy Audit')
yield_monitor     = Transition(label='Yield Monitor')
data_analysis     = Transition(label='Data Analysis')

# Define the ongoing yield‐optimization loop: Yield Monitor then optionally Data Analysis repeatedly
yield_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_monitor, data_analysis])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_audit,
    design_layout,
    retrofitting,
    system_install,
    climate_setup,
    nutrient_prep,
    plant_seeding,
    sensor_deploy,
    automation_tune,
    staff_training,
    compliance_check,
    community_meet,
    waste_manage,
    energy_audit,
    yield_loop
])

# Phase 1: Site survey to retrofitting
root.order.add_edge(site_survey, structural_audit)
root.order.add_edge(structural_audit, design_layout)
root.order.add_edge(design_layout, retrofitting)

# Phase 2: Installation & setup
root.order.add_edge(retrofitting, system_install)
root.order.add_edge(system_install, climate_setup)

# Phase 3: Planting preparation
root.order.add_edge(climate_setup, nutrient_prep)
root.order.add_edge(nutrient_prep, plant_seeding)

# Phase 4: Automation deployment
root.order.add_edge(plant_seeding, sensor_deploy)
root.order.add_edge(sensor_deploy, automation_tune)

# Phase 5: Staff training
root.order.add_edge(automation_tune, staff_training)

# After training: start compliance, community engagement, and yield‐optimization loop in parallel
root.order.add_edge(staff_training, compliance_check)
root.order.add_edge(staff_training, community_meet)
root.order.add_edge(staff_training, yield_loop)

# Compliance workflow
root.order.add_edge(compliance_check, waste_manage)
root.order.add_edge(waste_manage, energy_audit)