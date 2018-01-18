# taken from Tyler Ruggles

import ROOT
from array import array
from pileUpVertexCorrections import PUreweight
import math


def addPuWeight( puDict, iFile, iDir, iTree, isData=False ) :
    f = ROOT.TFile( iFile, 'UPDATE' )
    d = f.Get( iDir )
    t = f.Get( iTree )

    print "file:",f
    print "tree:",t
    
    puweight = array('f', [0])
    puweightB = t.Branch('puweight', puweight, 'puweight/F')
    
    count = 0
    for i in range( t.GetEntries() ) :
    	t.GetEntry( i )
    	if(t.nTruePU >0 ):
        	if count % 10000 == 0 : print "Event:",count
        	nTrPu = ( math.floor(t.nTruePU * 10))/10
        	if isData :
                    puweight[0] = 1
                else :
                    puweight[0] = puDict[ nTrPu ]

                puweightB.Fill()
        	count += 1
    
    print "DONE!"
    
    d.cd()
    t.Write('', ROOT.TObject.kOverwrite)
    f.Close()



if '__main__' in __name__ :

    #### Tau Trigger Efficiencies ####
    dataFile = 'DataTemplate_RunBF2017_69p2MinBiasXS_99bins.root'
    puDict = PUreweight( dataFile )

    tName = '/Ntuplizer/TagAndProbe'
    dName = 'Ntuplizer'
    base = '$CMSSW_BASE/src/../../Samples/2018_01_14/'
   
    isData = False
    addPuWeight( puDict, base+'NTuple_RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1_14_01_2018_etst.root', dName, tName, isData )
    
