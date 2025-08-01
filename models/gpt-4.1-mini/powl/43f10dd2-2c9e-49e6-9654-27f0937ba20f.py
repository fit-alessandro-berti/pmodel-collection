# Generated from: 43f10dd2-2c9e-49e6-9654-27f0937ba20f.json
# Description: This process outlines the complex integration of urban vertical farming systems within existing city infrastructure to optimize food production and sustainability. It involves selecting suitable building sites, retrofitting structures, installing hydroponic and aeroponic systems, integrating IoT sensors for climate control, managing energy consumption, coordinating with local supply chains, and ensuring regulatory compliance. The process also includes workforce training on new agricultural technologies, ongoing maintenance, real-time data analysis for crop optimization, and community engagement to promote urban agriculture awareness. This atypical business process bridges agriculture, technology, and urban planning to create a scalable model for sustainable city farming.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the labeled transitions (activities)
site_select = Transition(label='Site Select')
structure_assess = Transition(label='Structure Assess')
retrofit_plan = Transition(label='Retrofit Plan')
system_install = Transition(label='System Install')
hydroponic_setup = Transition(label='Hydroponic Setup')
aeroponic_setup = Transition(label='Aeroponic Setup')
sensor_deploy = Transition(label='Sensor Deploy')
climate_adjust = Transition(label='Climate Adjust')
energy_manage = Transition(label='Energy Manage')
supply_coordinate = Transition(label='Supply Coordinate')
compliance_check = Transition(label='Compliance Check')
staff_train = Transition(label='Staff Train')
maintenance_run = Transition(label='Maintenance Run')
data_analyze = Transition(label='Data Analyze')
community_engage = Transition(label='Community Engage')
crop_optimize = Transition(label='Crop Optimize')

# Choice between Hydroponic and Aeroponic setup (concurrent alternatives)
systems_choice = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, aeroponic_setup])

# Loop for Crop Optimization and Maintenance with Data Analyze
# According to problem: Crop Optimize depends on real-time Data Analysis
# and Maintenance is ongoing and interacts with Crop Optimize and Data Analyze,
# model loop: perform Maintenance, then choose to exit or do Data Analyze + Crop Optimize again + back to Maintenance
loop_maintenance = OperatorPOWL(
    operator=Operator.LOOP,
    children=[
        maintenance_run,
        OperatorPOWL(operator=Operator.XOR, children=[SilentTransition(), StrictPartialOrder(nodes=[data_analyze, crop_optimize])])
    ],
)

# Partial order for infrastructure setup and installation activities before system install
infrastructure = StrictPartialOrder(
    nodes=[site_select, structure_assess, retrofit_plan]
)
infrastructure.order.add_edge(site_select, structure_assess)
infrastructure.order.add_edge(structure_assess, retrofit_plan)

# Partial order for system install that comes after retrofit plan and before systems_choice (hydroponic/aeroponic)
install_phase = StrictPartialOrder(
    nodes=[retrofit_plan, system_install]
)
install_phase.order.add_edge(retrofit_plan, system_install)

# Partial order for sensor deploy, climate adjust, energy manage, supply coordinate, compliance check, staff train
# These happen after system install and systems choice, some concurrent, some partial order:
# Sensor deploy before climate adjust,
# Energy manage concurrent
# Supply coordinate and compliance check after install and possibly concurrent with above,
# Staff train can happen in parallel after system install but before loop_maintenance.

setup_monitoring = StrictPartialOrder(
    nodes=[sensor_deploy, climate_adjust, energy_manage, supply_coordinate, compliance_check, staff_train]
)
setup_monitoring.order.add_edge(sensor_deploy, climate_adjust)

# Combine infrastructure and install_phase in sequence
infra_and_install = StrictPartialOrder(
    nodes=[infrastructure, system_install]
)
infra_and_install.order.add_edge(infrastructure, system_install)

# Since infrastructure is already defined, and install_phase includes retrofit_plan and system_install,
# we define a PO merging them properly:

# Instead of combining infra_and_install, refining:
# Full installation and initial configuration partial order:
install_and_setup = StrictPartialOrder(
    nodes=[site_select, structure_assess, retrofit_plan, system_install, systems_choice, sensor_deploy,
           climate_adjust, energy_manage, supply_coordinate, compliance_check, staff_train]
)
# Define edges for installations and setup:
install_and_setup.order.add_edge(site_select, structure_assess)
install_and_setup.order.add_edge(structure_assess, retrofit_plan)
install_and_setup.order.add_edge(retrofit_plan, system_install)
install_and_setup.order.add_edge(system_install, systems_choice)
install_and_setup.order.add_edge(systems_choice, sensor_deploy)
install_and_setup.order.add_edge(sensor_deploy, climate_adjust)

# Staff train can happen after system install concurrently with setup_monitoring
install_and_setup.order.add_edge(system_install, staff_train)

# Energy manage, supply coordinate, compliance check concurrent after system install
install_and_setup.order.add_edge(system_install, energy_manage)
install_and_setup.order.add_edge(system_install, supply_coordinate)
install_and_setup.order.add_edge(system_install, compliance_check)

# Nodes of loop + install_and_setup + community engage (which can be concurrent with loop and monitoring)
# Community engage is an outreach activity, likely after initial setup but partially concurrent with ongoing loop

# Final root partial order combining:
# - install_and_setup partial order
# - loop_maintenance (maintenance -> optionally data analyze + crop optimize repeated)
# - community_engage (concurrent with loop and after install_and_setup)

root = StrictPartialOrder(
    nodes=[install_and_setup, loop_maintenance, community_engage]
)

# Define the ordering edges between these 3 nodes:
# install_and_setup precedes loop_maintenance and community_engage
root.order.add_edge(install_and_setup, loop_maintenance)
root.order.add_edge(install_and_setup, community_engage)