# create PAT trigger objects using the updated trigger collections
import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.trigTools import *

def customizeConfig(process):

    process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/MINIAODSIM/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/FE203EF9-D824-8547-A809-FAF05F010C3F.root'
        #'file:RelVal_Raw_GRun_MC.root',
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    ),
    secondaryFileNames = cms.untracked.vstring(
     '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/21F5020A-38C2-624C-8FD0-F9F2BF4EBCD5.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/3B8232B3-AB92-314B-8D69-6C3AEF4A744F.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/E601C3AB-62B0-AC49-BBA1-DA169FE76706.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/EA84EB6B-6C7A-8140-AAFE-474359557635.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/366E69BD-AC6C-5A4A-B79D-2BE6E0D33EB0.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/6E18BE60-46AD-EF42-966F-78E985C1D631.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/E3BA14F4-638F-2240-8810-C386FC34A030.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/A61D21F7-2D3C-5341-A96C-907F03ECFFD7.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/C463C9C8-B8EA-FE49-BE4E-60C18AACB9A1.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/D7D09878-B49A-9344-94BB-DB6F899A3DBF.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/7F05653E-D1B0-1543-A7C0-02EFE628479A.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/DB37119E-467A-144D-B3C1-C70AC0E8FB01.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/037A4632-BBEF-3D49-85A5-54A94E005920.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/F25ADFA7-8014-1044-9C65-F2759A128A4E.root',
        '/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/GEN-SIM-RAW/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/50000/24376757-418D-BF4B-A7FD-E22941CB62E0.root'
        )
    )

    del process.dqmOutput
    del process.DQMOutput

    #process.DQMOutput = cms.EndPath( process.dqmOutput )
    process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
        dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
        ),
        fileName = cms.untracked.string('tauHLT_accessingTauDM_customPAT.root'),
        #outputCommands = process.RECOSIMEventContent.outputCommands,
        outputCommands = cms.untracked.vstring(
            "drop *",
            "keep *_TriggerResults_*_*",
            "keep *_genParticles_*_*",
            "keep *_prunedGenParticles_*_*",
            "keep *_slimmedElectrons_*_*",
            "keep *_slimmedMuons_*_*",
            "keep *_slimmedAddPileupInfo_*_*",
            "keep *_slimmedTaus_*_*",
            "keep *_slimmedJets_*_*",
            "keep *_slimmedMETs_*_*",
            "keep *_offlineSlimmedPrimaryVertices_*_*",
            "keep *_packedPFCandidates_*_*",
            "keep *_slimmedPatTrigger_*_*",
            "keep *_caloStage2Digis_*_*",
            "keep *_reducedEgamma_*_*",
            "keep *_offlineBeamSpot_*_*",
            "keep *_fixedGridRhoFastjetAll_*_*",
            "keep *_fixedGridRhoAll_*_*",
            "keep *_hltTriggerSummaryAOD_*_HLT",
            "keep *_hltTriggerSummaryRAW_*_HLT",
            "keep *_hltTriggerSummaryAOD_*_HLTTau",
            "keep *_hltTriggerSummaryRAW_*_HLTTau",
            "keep *_hltPFTaus_*_*",
            "keep *_hltL2TausForPixelIsolation_*_*",
            "keep *_hltL2TausForPixelIsolationL1TauSeeded_*_*",
            "keep *_hltL2TauPixelIsoTagProducer_*_*",
            "keep *_hltL2TauPixelIsoTagProducerL1TauSeeded_*_*",
            "keep *_hltPFTausReg_*_*",
            "keep *_hltHpsPFTauProducerSingleTau_*_*",
            "keep *_hltHpsSelectedPFTausTrackFinding_*_*",
            "keep *_hltPFTaus_*_HLTTau",
            "keep *_hltPFTausReg_*_HLTTau",
            "keep *_hltHpsPFTauProducer_*_HLTTau",
            "keep *_hltHpsPFTauProducerReg_*_HLTTau",

            "keep *_hltHpsCombinatoricRecoTausReg_*_*",
            "keep *_hltHpsPFTauTrack_*_*",
            "keep *_hltHpsPFTau27TrackLooseChargedIso_*_*",
            "keep *_hltHpsPFTau27TrackLooseChargedIsoAgainstMuon_*_*",
            "keep patTriggerObjectStandAlones_patTriggerCustom_*_HLTTau"

            #"keep *_*_*_HLTTau",
            #"keep *_*_*",

        ),
        splitLevel = cms.untracked.int32(0)
    )


    """
    switchOnTriggerStandAlone(
        process                               ,
        path            = 'HLTAnalyzerEndpath',
        triggerProducer = 'patTriggerCustom'  ,
        hltProcess      = 'HLTTau'              ,
        outputModule    = 'RECOSIMoutput'
        )
    """

    process.patTriggerCustom = cms.EDProducer("PATTriggerProducer",
        ReadPrescalesFromFile = cms.bool(False),
        l1GtReadoutRecordInputTag = cms.InputTag("gtDigis"),
        l1GtRecordInputTag = cms.InputTag("gtDigis"),
        l1GtTriggerMenuLiteInputTag = cms.InputTag("gtDigis"),
        l1tAlgBlkInputTag = cms.InputTag("gtStage2Digis"),
        l1tExtBlkInputTag = cms.InputTag("gtStage2Digis"),
        onlyStandAlone = cms.bool(True),
        packTriggerLabels = cms.bool(False),
        processName = cms.string('HLTTau'),
        stageL1Trigger = cms.uint32(2)
        )

    from Configuration.Eras.Modifier_stage2L1Trigger_cff import stage2L1Trigger
    stage2L1Trigger.toModify(process.patTriggerCustom, stageL1Trigger = 2)


    process.slimmedPatTriggerCustom = cms.EDProducer(
        'PATTriggerObjectStandAloneSlimmer',
        cut = cms.string('!filterLabels.empty()'),
        src = cms.InputTag('patTriggerCustom'),
        triggerResults = cms.InputTag('TriggerResults'      , '', "HLTTau"),
        packFilterLabels  = cms.bool(False),
        packP4 = cms.bool(True)
    )


    if not hasattr(process, 'HLTAnalyzerEndpath'):
        process.HLTAnalyzerEndpath = cms.EndPath(process.patTriggerCustom * process.slimmedPatTriggerCustom)
        process.HLTSchedule.append(process.HLTAnalyzerEndpath)
    else:
        process.HLTAnalyzerEndpath += process.patTriggerCustom
        process.HLTAnalyzerEndpath += process.slimmedPatTriggerCustom

    process.patAlgosToolsTask = cms.Task(process.patTriggerCustom)

    process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)


    return process
