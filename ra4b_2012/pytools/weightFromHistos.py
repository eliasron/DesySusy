import sys, os
from ROOT import TH1,TH1D,THStack,TRandom,gPad,TDirectory,gDirectory





def GetWeightFromHistos(histo1,histo2,interval):
    '''
    gets the weight from histo1,histo2

    '''

    #
    if len(interval)!=0:
        inf=interval[0]
        sup=interval[1]
        binInf=histo1.FindFixBin(inf)
        binSup=histo1.FindFixBin(sup)        
    else:
        binInf=1
        binSup=histo1.GetNbinsX()
        
    #
    print 'binInf is ',binInf
    print 'binSup is ',binSup
    #
    sum1=0
    sum2=0
    for bin in range(binInf,binSup+1):
        sum1+=histo1.GetBinContent(bin)
        sum2+=histo2.GetBinContent(bin)
        print 'sum1 and sum2',sum1,sum2
        print 'on the the bin ',bin
        #
        #print 'the ratio is ',sum2/sum1
    #
    #
    #
    if sum2 != 0:
        return sum1/sum2
    else:
        return 0.0



def GetWeightFromHistoNames(tdir,histo1, histo2, interval):
    '''
    gets the weight from histo1,histo2
    '''
    #
    print 'tdir is ',tdir 
    h1=tdir.Get(histo1)
    h2=tdir.Get(histo2)
    #
    return GetWeightFromHistos(h1,h2,interval)


def GetWeightFromDicts(dict1, dict2, interval=[]):
    '''
    gets the weight from the ratio of the sum of histograms
    which are fed in with dictionaries
    '''
    #
    histSum1=False
    for key1,value1 in dict1.iteritems():
        if not histSum1:
            histSum1=value1.Clone()
        else:
            sumOK=histSum1.Add(value1)
            if not sumOK:
                print 'the sum did not work'
            #
        #
    #

    histSum2=False
    for key2,value2 in dict2.iteritems():
        if not histSum2:
            histSum2=value2.Clone()
        else:
            sumOK=histSum2.Add(value2)
            if not sumOK:
                print 'the sum did not work'
                #
            #
        #    
    #
    
    return GetWeightFromHistos(histSum1,histSum2,interval)




if __name__=='__main__':

    #
    #
    h1=TH1D("a","a",50,-2.,2.)
    h2=TH1D("b","b",50,-2.,2.)
    h1.FillRandom("gaus",10000)
    h2.FillRandom("gaus",50000)
    h2.Draw()
    gPad.Update()
    raw_input('')
    weight=GetWeightFromHistos(h1,h2,(-0.5,0.5))
    print 'weight is',weight
    #
    #




