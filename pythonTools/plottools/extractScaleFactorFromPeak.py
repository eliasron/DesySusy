
from ROOT import TH1, TH1D

import os, sys




def extractScaleFactorFromPeak(histo1,histo2):


    """extracts a scale factor from the ratio of two histograms in the bin with the higher content
    histo1 is the one that is scanned to fix the bin"""

    nbins1=histo1.GetNbinsX()
    nbins2=histo2.GetNbinsX()
    if nbins1 != nbins2:
        print 'nbins1 =',nbins1, 'nbins2 = ',nbins2
        raise NameError(histo1.GetName()+' and '+histo2.GetName()+' have different number of bins ')
    #
    #
    maxbin=-1
    maxquantity=-1
    for bin in range(nbins1):
        if histo1.GetBinContent(bin+1)>maxquantity:
            maxquantity = histo1.GetBinContent(bin+1)
            maxbin=bin+1
        #
    #

    #return the scale factor
    if histo2.GetBinContent(maxbin) != 0:
        scale=histo1.GetBinContent(maxbin)/histo2.GetBinContent(maxbin)
    else:
        scale=1.0
        
    return scale
    #


def getRescaledFromPeak(histo1,histo2):


    scale=extractScaleFactorFromPeak(histo1,histo2)

    newHisto=histo2.Clone()
    newHisto.Scale(scale)
    
    return newHisto


if __name__=='__main__':

    print  'hi from extractScaleFactorFromPeak.py'


