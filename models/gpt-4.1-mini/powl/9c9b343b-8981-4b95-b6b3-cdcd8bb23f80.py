# Generated from: 9c9b343b-8981-4b95-b6b3-cdcd8bb23f80.json
# Description: This process outlines the comprehensive steps required to onboard new urban vertical farms into a smart city ecosystem. It involves site evaluation, integration with city utilities, real-time data synchronization, regulatory compliance verification, IoT sensor installation, automated climate calibration, supply chain linkage, waste recycling setup, and continuous performance monitoring. The goal is to ensure sustainable urban agriculture with optimized resource usage and seamless interaction with city infrastructure, enabling scalable, tech-driven food production within dense metropolitan environments.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as Transitions
SiteSurvey = Transition(label='Site Survey')
UtilitySync = Transition(label='Utility Sync')
RegulationCheck = Transition(label='Regulation Check')
SensorInstall = Transition(label='Sensor Install')
DataLink = Transition(label='Data Link')
ClimateAdjust = Transition(label='Climate Adjust')
CropScheduling = Transition(label='Crop Scheduling')
WasteSetup = Transition(label='Waste Setup')
SupplyLink = Transition(label='Supply Link')
EnergyAudit = Transition(label='Energy Audit')
SecuritySetup = Transition(label='Security Setup')
StaffTraining = Transition(label='Staff Training')
SystemTest = Transition(label='System Test')
PerformanceReview = Transition(label='Performance Review')
ReportingSetup = Transition(label='Reporting Setup')

# The process outline (partial order) based on the description:
# Site Survey --> Utility Sync --> Regulation Check
# After Regulation Check, Sensor Install and Data Link can be concurrent
# Then Climate Adjust (depends on both Sensor Install and Data Link)
# Crop Scheduling depends on Climate Adjust
# Then Waste Setup and Supply Link can be concurrent
# Then Energy Audit (depends on both Waste Setup and Supply Link)
# Security Setup depends on Energy Audit
# Staff Training depends on Security Setup
# System Test depends on Staff Training
# Performance Review depends on System Test
# Reporting Setup depends on Performance Review

root = StrictPartialOrder(
    nodes=[
        SiteSurvey,
        UtilitySync,
        RegulationCheck,
        SensorInstall,
        DataLink,
        ClimateAdjust,
        CropScheduling,
        WasteSetup,
        SupplyLink,
        EnergyAudit,
        SecuritySetup,
        StaffTraining,
        SystemTest,
        PerformanceReview,
        ReportingSetup
    ]
)

# Add edges representing the partial order
root.order.add_edge(SiteSurvey, UtilitySync)
root.order.add_edge(UtilitySync, RegulationCheck)

# Concurrent after RegulationCheck: SensorInstall and DataLink (both depend on RegulationCheck)
root.order.add_edge(RegulationCheck, SensorInstall)
root.order.add_edge(RegulationCheck, DataLink)

# ClimateAdjust depends on SensorInstall and DataLink
root.order.add_edge(SensorInstall, ClimateAdjust)
root.order.add_edge(DataLink, ClimateAdjust)

# CropScheduling depends on ClimateAdjust
root.order.add_edge(ClimateAdjust, CropScheduling)

# WasteSetup and SupplyLink concurrent after CropScheduling
root.order.add_edge(CropScheduling, WasteSetup)
root.order.add_edge(CropScheduling, SupplyLink)

# EnergyAudit depends on WasteSetup and SupplyLink
root.order.add_edge(WasteSetup, EnergyAudit)
root.order.add_edge(SupplyLink, EnergyAudit)

# SecuritySetup depends on EnergyAudit
root.order.add_edge(EnergyAudit, SecuritySetup)

# StaffTraining depends on SecuritySetup
root.order.add_edge(SecuritySetup, StaffTraining)

# SystemTest depends on StaffTraining
root.order.add_edge(StaffTraining, SystemTest)

# PerformanceReview depends on SystemTest
root.order.add_edge(SystemTest, PerformanceReview)

# ReportingSetup depends on PerformanceReview
root.order.add_edge(PerformanceReview, ReportingSetup)