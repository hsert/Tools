
import ROOT
from array import array
import math


def addTauESshift(iFile, iDir, iTree, isData=False ) :
    f = ROOT.TFile( iFile, 'UPDATE' )
    d = f.Get( iDir )
    t = f.Get( iTree )

    print "file:",f
    print "tree:",t
    
    tauPt_ESshifted = array('f', [0])
    tauPt_ESshiftedB = t.Branch('tauPt_ESshifted', tauPt_ESshifted, 'tauPt_ESshifted/F')

    count = 0
    for i in range( t.GetEntries() ) :
    	t.GetEntry( i )
        #if count % 10000 == 0 : print "Event:", count
        tauPt = t.tauPt
        tauDM = t.tauDM
        tauPt_ESshift = -1
		
        if (tauDM == 0):
            tauPt_ESshift = 1.007*tauPt
        elif (tauDM == 1):
            tauPt_ESshift = 0.998*tauPt
        elif(tauDM ==10):
            tauPt_ESshift = 1.001*tauPt
        
       # print "tauPt", tauPt, "tauDM", tauDM , "tauptcorrected", tauPt_ESshifted


        if isData :
            tauPt_ESshifted[0] = tauPt
        else:
           # print "puDict[ nTrPu ]", puDict[ nTrPu ]
            tauPt_ESshifted[0] = tauPt_ESshift

        tauPt_ESshiftedB.Fill()
        count += 1
    
    print "DONE!"
    
    d.cd()
    t.Write('', ROOT.TObject.kOverwrite)
    f.Close()



if '__main__' in __name__ :

    #### Tau Trigger Efficiencies ####
    dataFile = 'DataTemplate_RunBF2017_69p2MinBiasXS_100bins.root'

    tName = '/Ntuplizer/TagAndProbe'
    dName = 'Ntuplizer'
    base = '/eos/user/h/hsert/TriggerStudies/ForkedRepo/Samples/12062018/'

    isData = False
    addTauESshift(base+'NTuple_DYJetsToLL_12Apr2018_v1Andext1v1_12062018_PU_1000binMC_tauESshift.root', dName, tName, isData )
    
