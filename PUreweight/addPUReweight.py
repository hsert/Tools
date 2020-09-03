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
        if count % 10000 == 0 : print "Event:",count
        nTrPu = ( math.floor(t.nTruePU * 10))/10
        #print "nTrue", nTrPu
        if(nTrPu > 98):
            nTrPu = 98
        elif(nTrPu < 0):
            nTrPu = 0

        if isData :
            puweight[0] = 1
        else:
           # print "puDict[ nTrPu ]", puDict[ nTrPu ]
            puweight[0] = puDict[ nTrPu ]
            puweightB.Fill()
            count += 1
    
    print "DONE!"
    
    d.cd()
    t.Write('', ROOT.TObject.kOverwrite)
    f.Close()



if '__main__' in __name__ :

    #### Tau Trigger Efficiencies ####
    dataFile = 'DataTemplate_RunBF2017_69p2MinBiasXS_100bins.root'
    puDict = PUreweight( dataFile )

    tName = '/Ntuplizer/TagAndProbe'
    dName = 'Ntuplizer'
    base = '/eos/user/h/hsert/TriggerStudies/ForkedRepo/Samples/12062018/'

    isData = False
    addPuWeight( puDict, base+'NTuple_0WJets_12Apr2018_12062018_PU_1000binMC.root', dName, tName, isData )
    
