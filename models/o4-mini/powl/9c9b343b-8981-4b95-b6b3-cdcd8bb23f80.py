# Generated from: 9c9b343b-8981-4b95-b6b3-cdcd8bb23f80.json
# Description: This process outlines the comprehensive steps required to onboard new urban vertical farms into a smart city ecosystem. It involves site evaluation, integration with city utilities, real-time data synchronization, regulatory compliance verification, IoT sensor installation, automated climate calibration, supply chain linkage, waste recycling setup, and continuous performance monitoring. The goal is to ensure sustainable urban agriculture with optimized resource usage and seamless interaction with city infrastructure, enabling scalable, tech-driven food production within dense metropolitan environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
site_survey        = Transition(label='Site Survey')
utility_sync       = Transition(label='Utility Sync')
regulation_check   = Transition(label='Regulation Check')
sensor_install     = Transition(label='Sensor Install')
data_link          = Transition(label='Data Link')
climate_adjust     = Transition(label='Climate Adjust')
crop_scheduling    = Transition(label='Crop Scheduling')
waste_setup        = Transition(label='Waste Setup')
supply_link        = Transition(label='Supply Link')
energy_audit       = Transition(label='Energy Audit')
security_setup     = Transition(label='Security Setup')
staff_training     = Transition(label='Staff Training')
system_test        = Transition(label='System Test')
performance_review = Transition(label='Performance Review')
reporting_setup    = Transition(label='Reporting Setup')

# Build the partial‐order workflow
root = StrictPartialOrder(
    nodes=[
        site_survey, utility_sync, regulation_check, data_link,
        sensor_install, climate_adjust,
        crop_scheduling, waste_setup, supply_link, energy_audit, security_setup,
        staff_training, system_test,
        performance_review, reporting_setup
    ]
)

# Define dependencies
root.order.add_edge(site_survey, utility_sync)

root.order.add_edge(utility_sync, data_link)
root.order.add_edge(utility_sync, regulation_check)

root.order.add_edge(data_link, sensor_install)
root.order.add_edge(regulation_check, sensor_install)

root.order.add_edge(sensor_install, climate_adjust)

for nxt in [crop_scheduling, waste_setup, supply_link, energy_audit, security_setup]:
    root.order.add_edge(climate_adjust, nxt)

for prev in [crop_scheduling, waste_setup, supply_link, energy_audit, security_setup]:
    root.order.add_edge(prev, staff_training)

root.order.add_edge(staff_training, system_test)

root.order.add_edge(system_test, performance_review)
root.order.add_edge(system_test, reporting_setup)