# Generated from: 25ac0908-826a-42a7-8f77-08d9a7a4c8af.json
# Description: This process involves the complex migration of a legacy enterprise resource planning (ERP) system to a modern cloud-based architecture. It includes detailed assessment of existing data structures, custom code review, incremental data extraction, transformation, and loading (ETL), parallel system testing, stakeholder training, and phased cutover. Due to the critical nature of the legacy system, thorough risk analysis and rollback planning are essential. The process also requires continuous monitoring post-migration to ensure data integrity and operational stability while minimizing downtime and business disruption across multiple departments and geographic locations.

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ScopeReview = Transition(label='Scope Review')
DataAudit = Transition(label='Data Audit')
CodeScan = Transition(label='Code Scan')
RiskAssess = Transition(label='Risk Assess')
ETLDesign = Transition(label='ETL Design')
ExtractData = Transition(label='Extract Data')
TransformData = Transition(label='Transform Data')
LoadData = Transition(label='Load Data')
UnitTesting = Transition(label='Unit Testing')
IntegrationTest = Transition(label='Integration Test')
UserTraining = Transition(label='User Training')
ParallelRun = Transition(label='Parallel Run')
CutoverPlan = Transition(label='Cutover Plan')
FinalMigration = Transition(label='Final Migration')
PostAudit = Transition(label='Post Audit')
RollbackPrep = Transition(label='Rollback Prep')
SystemMonitor = Transition(label='System Monitor')

# Model ETL as a sequence: Extract -> Transform -> Load
ETL_PO = StrictPartialOrder(nodes=[ExtractData, TransformData, LoadData])
ETL_PO.order.add_edge(ExtractData, TransformData)
ETL_PO.order.add_edge(TransformData, LoadData)

# Risk analysis and rollback planning can be done after code scan in parallel with ETL design
# RiskAssess and RollbackPrep modeled as XOR choice after RiskAssess (loop for rollback possible?), but description suggests "planning", so use XOR for possible rollback planning before proceeding

# Risk and rollback planning loop: do RiskAssess, then either exit or do RollbackPrep then RiskAssess again (loop)
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[RiskAssess, RollbackPrep])

# After ScopeReview -> DataAudit & CodeScan in parallel, both must be done before Risk loop and ETL design
# Model DataAudit and CodeScan as parallel activities (no order between them)
# Then both must finish before next phase

# ETL Design after risk loop and after DataAudit & CodeScan
# So first ScopeReview --> {DataAudit, CodeScan} (concurrent)
# After both, then risk_loop and ETLDesign (parallel), both before ETL_PO

# Model training and parallel system testing in parallel after tests
# UnitTesting -> IntegrationTest (sequence)
testing_PO = StrictPartialOrder(nodes=[UnitTesting, IntegrationTest])
testing_PO.order.add_edge(UnitTesting, IntegrationTest)

# ParallelRun and UserTraining run in parallel after integration test
# So after Testing_PO: both ParallelRun & UserTraining parallel

# CutoverPlan before FinalMigration

# Phased cutover: CutoverPlan -> FinalMigration -> PostAudit

# SystemMonitor continuous after FinalMigration and PostAudit (modeled as partial order with FinalMigration and PostAudit and then SystemMonitor)

# Overall ordering:

# ScopeReview
#  |--> DataAudit and CodeScan (parallel)
#  |--> then risk_loop and ETLDesign in parallel
#  |--> ETL_PO (ExtractData->TransformData->LoadData)
#  |--> testing_PO (UnitTesting->IntegrationTest)
#  |--> parallel: ParallelRun and UserTraining
#  |--> CutoverPlan
#  |--> FinalMigration
#  |--> PostAudit
#  |--> SystemMonitor

# Build partial orders stepwise:

# Step1: DataAudit and CodeScan concurrency (no order)
data_code_PO = StrictPartialOrder(nodes=[DataAudit, CodeScan])

# Step2: risk_loop and ETLDesign parallel
risk_etlDesign_PO = StrictPartialOrder(nodes=[risk_loop, ETLDesign])

# Step3: All nodes after ScopeReview: nodes of data_code_PO + risk_etlDesign_PO + ScopeReview
# We'll put ScopeReview before both DataAudit and CodeScan
# And then ensure risk_etlDesign_PO after data_code_PO

# Step4: ETL_PO after risk_etlDesign_PO

# Step5: testing_PO after ETL_PO

# Step6: ParallelRun and UserTraining parallel after testing_PO

# Step7: CutoverPlan after ParallelRun and UserTraining

# Step8: FinalMigration after CutoverPlan

# Step9: PostAudit after FinalMigration

# Step10: SystemMonitor after PostAudit

# Construct the full POWL model:

nodes = [
    ScopeReview,
    DataAudit,
    CodeScan,
    risk_loop,
    ETLDesign,
    ExtractData,
    TransformData,
    LoadData,
    UnitTesting,
    IntegrationTest,
    ParallelRun,
    UserTraining,
    CutoverPlan,
    FinalMigration,
    PostAudit,
    SystemMonitor,
]

root = StrictPartialOrder(nodes=nodes)

# ScopeReview before DataAudit and CodeScan
root.order.add_edge(ScopeReview, DataAudit)
root.order.add_edge(ScopeReview, CodeScan)

# DataAudit and CodeScan before risk_loop and ETLDesign
root.order.add_edge(DataAudit, risk_loop)
root.order.add_edge(CodeScan, risk_loop)
root.order.add_edge(DataAudit, ETLDesign)
root.order.add_edge(CodeScan, ETLDesign)

# risk_loop and ETLDesign before ETL_PO
root.order.add_edge(risk_loop, ExtractData)
root.order.add_edge(ETLDesign, ExtractData)

# ETL_PO sequence
root.order.add_edge(ExtractData, TransformData)
root.order.add_edge(TransformData, LoadData)

# ETL_PO before testing_PO
root.order.add_edge(LoadData, UnitTesting)

# testing_PO sequence
root.order.add_edge(UnitTesting, IntegrationTest)

# testing_PO before ParallelRun and UserTraining
root.order.add_edge(IntegrationTest, ParallelRun)
root.order.add_edge(IntegrationTest, UserTraining)

# ParallelRun and UserTraining before CutoverPlan
root.order.add_edge(ParallelRun, CutoverPlan)
root.order.add_edge(UserTraining, CutoverPlan)

# CutoverPlan before FinalMigration
root.order.add_edge(CutoverPlan, FinalMigration)

# FinalMigration before PostAudit
root.order.add_edge(FinalMigration, PostAudit)

# PostAudit before SystemMonitor
root.order.add_edge(PostAudit, SystemMonitor)