# Generated from: f539c9ab-5eb3-445b-9dae-fb136a5c953c.json
# Description: This process outlines the complex steps involved in establishing an urban vertical farm within a repurposed industrial building. It includes site assessment, modular system design, hydroponic installation, climate control configuration, nutrient management, automated pest detection, energy optimization, labor training, local market integration, and continuous yield monitoring, all while complying with urban agricultural regulations and sustainability standards. The process ensures maximized crop output in limited space using advanced technology and data analytics to maintain optimal growth conditions and resource efficiency.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
site_survey       = Transition(label="Site Survey")
structural_audit  = Transition(label="Structural Audit")
modular_design    = Transition(label="Modular Design")
hydroponic_setup  = Transition(label="Hydroponic Setup")
climate_config    = Transition(label="Climate Config")
nutrient_mix      = Transition(label="Nutrient Mix")
pest_detect       = Transition(label="Pest Detect")
lighting_setup    = Transition(label="Lighting Setup")
energy_audit      = Transition(label="Energy Audit")
automation_install= Transition(label="Automation Install")
staff_training    = Transition(label="Staff Training")
regulation_check  = Transition(label="Regulation Check")
market_analysis   = Transition(label="Market Analysis")
waste_manage      = Transition(label="Waste Manage")
yield_monitor     = Transition(label="Yield Monitor")
data_analytics    = Transition(label="Data Analytics")

# Define the monitoring loop: first yield_monitor, then repeat (data_analytics ➔ yield_monitor)
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[yield_monitor, data_analytics]
)

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    site_survey,
    structural_audit,
    modular_design,
    hydroponic_setup,
    climate_config,
    nutrient_mix,
    pest_detect,
    lighting_setup,
    energy_audit,
    automation_install,
    staff_training,
    regulation_check,
    market_analysis,
    waste_manage,
    monitor_loop
])

# Add the control‐flow dependencies
o = root.order
o.add_edge(site_survey,       structural_audit)
o.add_edge(structural_audit,  modular_design)
o.add_edge(modular_design,    hydroponic_setup)
o.add_edge(modular_design,    climate_config)
o.add_edge(hydroponic_setup,  nutrient_mix)
o.add_edge(climate_config,    nutrient_mix)
o.add_edge(nutrient_mix,      pest_detect)
o.add_edge(pest_detect,       lighting_setup)
o.add_edge(pest_detect,       energy_audit)
o.add_edge(pest_detect,       automation_install)
o.add_edge(automation_install, staff_training)
o.add_edge(automation_install, regulation_check)
o.add_edge(automation_install, market_analysis)
o.add_edge(staff_training,    waste_manage)
o.add_edge(regulation_check,  waste_manage)
o.add_edge(market_analysis,   waste_manage)
o.add_edge(waste_manage,      monitor_loop)