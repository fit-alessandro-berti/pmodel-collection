# Generated from: 0c1f9bfe-a114-45bf-afb8-985999331140.json
# Description: This process outlines the establishment of an urban vertical farm within a multi-story building in a dense city environment. It involves initial site assessment for structural integrity, followed by modular hydroponic system installation. Climate control calibration is performed to optimize plant growth, including lighting and humidity adjustments. Nutrient solution recipes are developed and tested for various crops. Automation systems integrate sensor data for real-time monitoring. Workforce training is conducted to manage technology and manual tasks. Waste recycling strategies are implemented to minimize environmental impact. Finally, distribution channels are coordinated with local markets and restaurants, ensuring fresh produce delivery within tight urban logistics constraints.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for activities
Site_Assess = Transition(label='Site Assess')
Load_Test = Transition(label='Load Test')
Modular_Install = Transition(label='Modular Install')
Hydro_Setup = Transition(label='Hydro Setup')
Climate_Tune = Transition(label='Climate Tune')
Light_Adjust = Transition(label='Light Adjust')
Nutrient_Mix = Transition(label='Nutrient Mix')
Crop_Trial = Transition(label='Crop Trial')
Sensor_Deploy = Transition(label='Sensor Deploy')
System_Sync = Transition(label='System Sync')
Staff_Train = Transition(label='Staff Train')
Waste_Plan = Transition(label='Waste Plan')
Market_Link = Transition(label='Market Link')
Route_Plan = Transition(label='Route Plan')
Delivery_Set = Transition(label='Delivery Set')

# First phase: Initial site assessment for structural integrity: Site Assess -> Load Test (sequential)
site_assessment_PO = StrictPartialOrder(
    nodes=[Site_Assess, Load_Test],
)
site_assessment_PO.order.add_edge(Site_Assess, Load_Test)

# Second phase: Modular hydroponic system installation (single activity after assessment)
# Hydro Setup depends on Modular Install (modular install before hydro setup)
installation_PO = StrictPartialOrder(
    nodes=[Modular_Install, Hydro_Setup],
)
installation_PO.order.add_edge(Modular_Install, Hydro_Setup)

# Larger phase: after site assessment and load test complete, modular install + hydro setup sequential
installation_phase = StrictPartialOrder(
    nodes=[site_assessment_PO, installation_PO]
)
installation_phase.order.add_edge(site_assessment_PO, installation_PO)

# Third phase: Climate control calibration including lighting and humidity adjustments.
# Climate Tune -> Light Adjust (sequential)
climate_PO = StrictPartialOrder(
    nodes=[Climate_Tune, Light_Adjust],
)
climate_PO.order.add_edge(Climate_Tune, Light_Adjust)

# Fourth phase: Nutrient mixing and crop trial (Nutrient Mix -> Crop Trial)
nutrient_PO = StrictPartialOrder(
    nodes=[Nutrient_Mix, Crop_Trial],
)
nutrient_PO.order.add_edge(Nutrient_Mix, Crop_Trial)

# The two calibration subphases can be done concurrently (climate control and nutrients)
calibration_PO = StrictPartialOrder(
    nodes=[climate_PO, nutrient_PO]
)
# No order edges between these two means concurrent

# Fifth phase: Automation integration: Sensor Deploy -> System Sync
automation_PO = StrictPartialOrder(
    nodes=[Sensor_Deploy, System_Sync],
)
automation_PO.order.add_edge(Sensor_Deploy, System_Sync)

# Sixth phase: Workforce training
# Staff Train alone
workforce_PO = Staff_Train  # single activity

# Seventh phase: Waste recycling plan alone
waste_PO = Waste_Plan

# Eighth phase: Distribution channel coordination:
# Market Link -> Route Plan -> Delivery Set
distribution_PO = StrictPartialOrder(
    nodes=[Market_Link, Route_Plan, Delivery_Set],
)
distribution_PO.order.add_edge(Market_Link, Route_Plan)
distribution_PO.order.add_edge(Route_Plan, Delivery_Set)

# Now, we organize all the major phases in order:
# After installation phase, do calibration, then automation, then workforce and waste plan can be concurrent,
# then distribution phase finalizes.

# Combine workforce_PO and waste_PO concurrent:
workforce_waste_PO = StrictPartialOrder(
    nodes=[workforce_PO, waste_PO],
)
# No edges between workforce and waste, thus concurrent

# Combine automation, then workforce_waste_PO:
automation_and_workforce_waste_PO = StrictPartialOrder(
    nodes=[automation_PO, workforce_waste_PO],
)
automation_and_workforce_waste_PO.order.add_edge(automation_PO, workforce_waste_PO)

# Combine calibration, then automation_and_workforce_waste_PO
calibration_to_automation_PO = StrictPartialOrder(
    nodes=[calibration_PO, automation_and_workforce_waste_PO],
)
calibration_to_automation_PO.order.add_edge(calibration_PO, automation_and_workforce_waste_PO)

# Combine all phases in order:
root = StrictPartialOrder(
    nodes=[installation_phase, calibration_to_automation_PO, distribution_PO],
)
root.order.add_edge(installation_phase, calibration_to_automation_PO)
root.order.add_edge(calibration_to_automation_PO, distribution_PO)