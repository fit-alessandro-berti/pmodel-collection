# Generated from: 7ebdadd7-4f67-4a6c-b537-c81456b861a4.json
# Description: This process outlines the complex series of steps required to establish a fully operational urban vertical farm within a constrained city environment. It involves site selection based on environmental and zoning factors, modular infrastructure design, integration of hydroponic and aeroponic systems, automation setup for climate control and nutrient delivery, and implementation of sustainable energy sources. The process further includes staff training on specialized equipment, regulatory compliance checks, iterative crop trial cycles to optimize yield, and a digital supply chain integration to connect with local markets efficiently. Continuous monitoring and adaptive management ensure peak productivity and resource conservation in an atypical urban agricultural context.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
Site_Survey = Transition(label='Site Survey')
Zoning_Review = Transition(label='Zoning Review')
Modular_Design = Transition(label='Modular Design')
System_Integration = Transition(label='System Integration')
Climate_Setup = Transition(label='Climate Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Automation_Install = Transition(label='Automation Install')
Energy_Connect = Transition(label='Energy Connect')
Staff_Training = Transition(label='Staff Training')
Compliance_Check = Transition(label='Compliance Check')
Trial_Crops = Transition(label='Trial Crops')
Yield_Analysis = Transition(label='Yield Analysis')
Supply_Sync = Transition(label='Supply Sync')
Monitoring_Setup = Transition(label='Monitoring Setup')
Adaptive_Control = Transition(label='Adaptive Control')

# Define Trial Cycle loop body (Trial Crops then Yield Analysis)
trial_body = StrictPartialOrder(nodes=[Trial_Crops, Yield_Analysis])
trial_body.order.add_edge(Trial_Crops, Yield_Analysis)

# Loop operator: * (Trial Cycle body, tau)
trial_loop = OperatorPOWL(operator=Operator.LOOP, children=[trial_body, SilentTransition()])

# Partial order for initial site selection: Site Survey --> Zoning Review
site_selection = StrictPartialOrder(nodes=[Site_Survey, Zoning_Review])
site_selection.order.add_edge(Site_Survey, Zoning_Review)

# Partial order for modular infrastructure: Modular Design --> System Integration
modular_infra = StrictPartialOrder(nodes=[Modular_Design, System_Integration])
modular_infra.order.add_edge(Modular_Design, System_Integration)

# Partial order for automation: Climate Setup --> Nutrient Mix --> Automation Install
automation = StrictPartialOrder(nodes=[Climate_Setup, Nutrient_Mix, Automation_Install])
automation.order.add_edge(Climate_Setup, Nutrient_Mix)
automation.order.add_edge(Nutrient_Mix, Automation_Install)

# Energy Connect alone (can be concurrent with automation)
energy = Energy_Connect

# Partial order for staff and compliance: Staff Training --> Compliance Check
staff_comp = StrictPartialOrder(nodes=[Staff_Training, Compliance_Check])
staff_comp.order.add_edge(Staff_Training, Compliance_Check)

# Partial order for supply chain: Supply Sync --> Monitoring Setup --> Adaptive Control
supply_monitor = StrictPartialOrder(nodes=[Supply_Sync, Monitoring_Setup, Adaptive_Control])
supply_monitor.order.add_edge(Supply_Sync, Monitoring_Setup)
supply_monitor.order.add_edge(Monitoring_Setup, Adaptive_Control)

# Combine automation and energy: partial order (automation and energy in parallel)
automation_energy = StrictPartialOrder(nodes=[automation, energy])

# Combine staff and compliance with trial loop: partial order staff_comp --> trial_loop
staff_trial = StrictPartialOrder(nodes=[staff_comp, trial_loop])
staff_trial.order.add_edge(staff_comp, trial_loop)

# Combine supply_monitor after staff_trial
final_subprocess = StrictPartialOrder(nodes=[staff_trial, supply_monitor])
final_subprocess.order.add_edge(staff_trial, supply_monitor)

# Combine modular infrastructure before automation_energy
infra_auto_energy = StrictPartialOrder(nodes=[modular_infra, automation_energy])
infra_auto_energy.order.add_edge(modular_infra, automation_energy)

# Combine site selection before infra_auto_energy
site_to_infra = StrictPartialOrder(nodes=[site_selection, infra_auto_energy])
site_to_infra.order.add_edge(site_selection, infra_auto_energy)

# Combine whole process before final subprocess
root = StrictPartialOrder(nodes=[site_to_infra, final_subprocess])
root.order.add_edge(site_to_infra, final_subprocess)