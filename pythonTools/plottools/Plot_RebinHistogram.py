
from ROOT import TH1,TH1F,TH1D,TH2D
from array import *


#
def Getxbins(histo):
    #
    axis=histo.GetXaxis()
    mylist=[]

    #get an array with GetNbins+1 values
    for bin in range(1,axis.GetNbins()+2 ):
        mylist.append(axis.GetBinLowEdge(bin))
        #print 'doing it ',bin
    #print 'length of the array is ',len(array('d',mylist))
    return array('d',mylist)

def MergeLastBins(histo,Properties):

    howManyBins=Properties.get('rebin_howManyBins')
    if howManyBins==None:
        print 'you are trying to merge the last bins but didnt specify how many'
        assert False
        
    #
    #print 'the histo has ',histo.GetNbinsX(),' bins'
    oldxbins=Getxbins(histo)
    newxbins=[]
    for num,i in enumerate(oldxbins):

        #print 'num and i ',num,i
        #copy the first entries
        if num+1 <= histo.GetNbinsX()+1 - howManyBins:
            #print 'appending ',i
            newxbins.append(i)
            #
        else:
            #copy the last onw
            newxbins.append(oldxbins[-1])
            break
        #
        #
    newxbins=array('d',newxbins)
    #=====check
    if( len(newxbins) != histo.GetNbinsX()-howManyBins+2):
        #print 'the size of the new low edges is not correct'
        #print 'len(newxbins) = ',len(newxbins)
        #print 'histo size = ',histo.GetNbinsX()
        #print 'howManyBins ' ,howManyBins
        return 0
    else:
        return newxbins


#def RebinAll(histo,Properties):
#    '''rebin all bins'''
#    newName=Properties.get('rebin_newName',histo.GetName()+'_rebin')        
#    rebinngroup=Properties.get('rebin_ngroup',1)
#    histo.Rebin(rebinngroup,histo.GetName()+'_'+newname)
    
def Rebin(histo,Properties):


    #PARAMETERS OF REBIN
    #ngroup=Properties.get('rebin_ngroup')
    newName=Properties.get('rebin_newName',histo.GetName()+'_rebin')    

    rebinMode=Properties.get('rebin_rebinMode','rebin')
    if rebinMode=='mergeLastBins':
        xbins=MergeLastBins(histo,Properties)
        ngroup=histo.GetNbinsX()-Properties.get('rebin_howManyBins') +1
    elif rebinMode=='rebin':

        #REBINS ALL BINS BY A FACTOR OF NGROUP
        ngroup=Properties.get('rebin_ngroup',2)
        xbins=Properties.get('rebin_xbins',0)

    #
    #
    #DO IT
    #print 'ngroup is ',ngroup
    #print 'low edges size ',len(xbins)
    #print xbins
    #
    h=histo.Rebin(ngroup,histo.GetName()+'_'+newName,xbins)
    return h







