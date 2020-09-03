
#Step 1
#edmProvDump root://xrootd-cms.infn.it//store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/FEF559B1-95DF-E811-9528-D4AE52900EF9.root | sed -n '/^Processing History/,/^----/p'

# The output
#Processing History:
#  LHE '' '"CMSSW_7_1_20_patch2"' [1]  (8793131d8750c177285c8434000be34a)
#    SIM '' '"CMSSW_7_1_20_patch3"' [1]  (2480552d3a4cb91ebeaa106488712ec9)
#      HLT '' '"CMSSW_8_0_21"' [1]  (16ca0fac1b892ff3c3d45d801745cbbf)
#        RECO '' '"CMSSW_8_0_21"' [1]  (b1a4edca9adfa7a2e4059536bf605cd7)
#          PAT '' '"CMSSW_9_4_9"' [1]  (bd3e7bcff6c9bcad356ea4ed7e4f08b4)
#---------Producers with data in file---------

#Step 2
#edmProvDump root://xrootd-cms.infn.it//store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/120000/FEF559B1-95DF-E811-9528-D4AE52900EF9.root -i 16ca0fac1b892ff3c3d45d801745cbbf | grep tableName


#For 2018
edmProvDump root://xrootd-cms.infn.it//store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FA553171-E5E9-5346-B634-6A64D6DEB64C.root  | sed -n '/^\
Processing History/,/^----/p' 

#/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FA553171-E5E9-5346-B634-6A64D6DEB64C.root