'''Re-structure highlights and notes by grouping by tags.


# Copyright 2016 Guang-zhi XU
#
# This file is distributed under the terms of the
# GPLv3 licence. See the COPYING file for details

Update time: 2016-02-23 23:04:09.
'''

import os
from textwrap import TextWrapper
    




#----------------------------------------
def groupByTags(annodict,verbose=True):
    '''Group highlights and/or notes by tags

    '''
    tags={}

    #----------------Loop through files----------------
    for fii,annoii in annodict.items():

        hlii,ntii=annoii

        try:
            tagsii=['@'+kk for kk in hlii[0].tags]
        except:
            tagsii=['@'+kk for kk in ntii[0].tags]

        try:
            citeii=hlii[0].citationkey
        except:
            citeii=ntii[0].citationkey

        citedict={'highlights': hlii,\
                  'notes': ntii}

        #----------------Loop through tags----------------
        for tagsjj in tagsii:
            if tagsjj in tags:
                tags[tagsjj][citeii]=citedict
            else:
                tags[tagsjj]={citeii:citedict}

    return tags







#--------------Export annotations grouped by tags------------------
def exportAnno(annodict,outdir,action,verbose=True):
    '''Export annotations grouped by tags

    '''

    #-----------Export all to a single file-----------
    if 'm' in action and 'n' not in action:
        fileout='Mendeley_highlights_by_tags.txt'
    elif 'n' in action and 'm' not in action:
        fileout='Mendeley_notes_by_tags.txt'
    elif 'm' in action and 'n' in action:
        fileout='Mendeley_annotations_by_tags.txt'

    abpath_out=os.path.join(outdir,fileout)
    if os.path.isfile(abpath_out):
        os.remove(abpath_out)

    if verbose:
        print('\n# <extracttags>: Exporting all taged annotations to:\n')
        print(abpath_out)

    conv=lambda x:unicode(x)

    wrapper=TextWrapper()
    wrapper.width=70
    wrapper.initial_indent=''
    wrapper.subsequent_indent='\t\t'+int(len('> '))*' '

    wrapper2=TextWrapper()
    wrapper2.width=60
    wrapper2.initial_indent=''
    wrapper2.subsequent_indent='\t\t\t'+int(len('Title: '))*' '

    with open(abpath_out, mode='a') as fout:

        #----------------Loop through tags----------------
        tags=annodict.keys()
        tags.sort()
        for tagii in tags:

            citedictii=annodict[tagii]
            outstr=u'''\n\n{0}\n# {1}'''.format(int(80)*'-', conv(tagii))
            outstr=outstr.encode('ascii','replace')
            fout.write(outstr)

            #--------------Loop through cite keys--------------
            for citejj, annosjj in citedictii.items():
                hljj=annosjj['highlights']
                ntjj=annosjj['notes']

                outstr=u'''\n\n\t@{0}:'''.format(conv(citejj))
                outstr=outstr.encode('ascii','replace')
                fout.write(outstr)

                #-----------------Write highlights-----------------
                if len(hljj)>0:

                    #-------------Loop through highlights-------------
                    for hlkk in hljj:
                        hlstr=wrapper.fill(hlkk.text)
                        title=wrapper2.fill(hlkk.title)
                        outstr=u'''
\n\t\t> {0}

\t\t\t- Title: {1}
\t\t\t- Ctime: {2}'''.format(*map(conv,[hlstr, title,\
                      hlkk.ctime]))

                        outstr=outstr.encode('ascii','replace')
                        fout.write(outstr)

                #-----------------Write notes-----------------
                if len(ntjj)>0:

                    #----------------Loop through notes----------------
                    for ntkk in ntjj:
                        ntstr=wrapper.fill(ntkk.text)
                        title=wrapper2.fill(ntkk.title)
                        outstr=u'''
\n\t\t- {0}

\t\t\t- Title: {1}
\t\t\t- Ctime: {2}'''.format(*map(conv,[ntstr, title,\
                    ntkk.ctime]))

                        outstr=outstr.encode('ascii','replace')
                        fout.write(outstr)

        

    
