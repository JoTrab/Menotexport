# Menotexport

**Menotexport (Mendeley-Note-Export) extracts highlights and notes from your Mendeley database**

## What does this do?

Menotexport.py is a simple python solution to help extracts annotations (highlighted
texts and sticky notes) you made in the build-in PDF reader of Mendeley.

*Mendeley is a desktop and web program for managing and sharing research
papers.* It offers free desktop clients for Windows, OSX and Linux. But the
software is not open source, and their support team has been real slow in responding
to customers feature requests, some of which has been proposed by many for YEARS.
This tool aims at solving the following:

### 1. Bulk export annotated PDFs.

Annotations (highlights and notes) made inside Mendeley are saved not directly onto
the relevant PDFs, but to a separate database file. Therefore these annotations can
not be viewered in another PDF reader other than Mendeley itself.

The native but awkward solution to export a PDF with its annotations is: in
Mendeley, open that PDF in the Mendeley PDF reader, go to Files -> Export PDF
with annotations. However to export all your collections, this has to be repeated
manually for each individual PDF in your library. 

This script can bulk export all PDFs with annotations to a given folder, and
the annotations are readable by other PDF softwares. NOTE that PDFs with no annotations
are not exported.

### 2. Extract annotation texts.

To extract texts from the highlights and sticky notes in a PDF, other than
Copy-n-Paste one by one, some softwares offer an automated solution.

*skim* on OSX has the functionality to produce a summary of all annotations.

Some versions of *Foxit Reader* can do that (on windows, not on the Linux version, not sure about Mac).

Pro versions of *Adobe Reader* **may** have that too.

Most of the PDF readers in Linux do not have that functionality. (Let me know if you find one).

This tool could extract the texts from the highlights and notes in the PDFs in Mendeley
to a plain text file, and format the information in a sensible structure.


## Installation

- Command line or GUI usage on Linux or Mac or Win, download the zip and unzip to any folder. Make sure you have all the dependencies listed below and Python 2.7.

- For Windows specific GUI, only need to get the `Menotexport-win64.zip` file. Download from dropbox: https://www.dropbox.com/s/64267kqvmlemaz8/menotexport-win64.rar?dl=0



## Usage

### Command line

```
python menotexport.py [-h] [-e] [-m] [-n] [-w] [-s] [-f folder] dbfile outputdir
```

where

- `-h`: Show help messages.
- `-e`: Bulk export PDFs to a folder given by `outputdir`.
- `-m`: Extract markups (highlighted texts).
- `-n`: Extract notes.
- `-w`: Do not overwrite existing files in `outputdir`. Default to overwrite.
- `-s`: Save extracted texts to a separate txt file for each PDF. Default to
      save all texts to a single file.
- `-f`: Select to process only a Mendeley folder. Note this is case sensitive and match has to be literal.
- `dbfile`: Absolute path to the Mendeley database file. In Linux systems default location is
  `~/.local/share/data/Mendeley\ Ltd./Mendeley\ Desktop/your_email@www.mendeley.com.sqlite`
- `outputdir`: folder to save outputs.

- If `-s`, texts for each PDF is saved to `Anno_PDFTITLE.txt` (if both `-m` and
`-n` are given), or to `Highlights_PDFTITLE.txt` or `Notes_PDFTITLE.txt` (if
either `-m` or `-n` is given).

- If not `-s`, save extracted texts from all PDFs to `Mendeley_annotations.txt`
(if both `-m` and `-n` are given), or to `Mendeley_highlights.txt` or
`Mendeley_notes.txt` (if either `-m` or `-n` is given). 

- If not `-s`, also generate another txt `Mendeley_annotations_by_tags.txt` where
information is grouped by tags.

Example:

To bulk export, extract and save to separate txt files:

```
python menotexport.py -emns dbfile outputdir
```
To bulk export all PDFs and extract all annotations in Mendeley folder "Tropical_Cyclones" and save extracted annotations to a single file: 

```
python menotexport.py -emn -f "Tropical_Cyclones" dbfile outputdir
```

### GUI

Launch `menotexport-gui.exe`, select the Mendeley database file and an output folder. Select the actions to perform (see above), then *start*. 


## Caveats and further notes

- The bulk PDF export works with **quite good** accuracy, most highlights and notes are
  reproduced as they should be.
- Note extraction works with **quite good** accruacy.
- **Highlight extraction accuracy is compromised**, due to the inherent nature of the PDF
  format. Not all texts are correctly extracted, and the order they appear in the output
  may not be exactly the same as in the PDFs (top-down, left-right). DO proof read afterwards.
- Highlighted texts from a single "block" of texts are treated as one record/entry. A "block" of
  texts is a continuous chunk of texts in the PDF, could be a whole paragraph, a single
  line separated from others, or a single isolated word. This ambiguity is again due to the inherent
  nature of PDF format. Again proof read the results.
- Citationkeys and tags are added to the extracted texts to facilitate further information
  processes, both can be editted in Mendeley.
- If choose to save all annotations to a single file, the programme also re-structure the extracted texts
  and organize them by their tags before saving to a separate file. Pieces of texts from a PDF that isn't taged are given a tag of @None.
- Sometimes your edits inside Mendeley may not be saved immediately to the database file. In such cases just reboot Mendeley. No needed to reboot Menotexport (if you are using the GUI) though, as each time you press the "start" button it will issue a new connection to the database.
- Possible follow-ups one can do: re-format the extracted txts to PDFs, docs or sync into
  your Evernote account, will probably implement these in a later version.
- To batch upload to **Evernote**, check out this repo: [txt2evernote](https://github.com/Xunius/txt2evernote).
- If you encounter an error `from pdfminer.pdfdocument import PDFDocument
ImportError: No module named pdfdocument`, make sure the *pdfminer* module version is 2014+ and try again.


## Dependencies

Developed in python2.7. **NOT** compatible with python3+ (*pdfminer* doesn't support python3).

It requires the following packages:
- PyPDF2
- sqlite3
- pandas
- pdfminer (version 2014 or later. Note that 2013 version does not work).
- numpy

It further incorporate (with minor adjustments) the pdfannotation.py file from
the [Menextract2pdf](https://github.com/cycomanic/Menextract2pdf) project.


## Platform/OS

The software is tested on Linux and Windows 10. Should also run on Mac.

## Versions

* 0.1 first release
* 1.0 added GUI and Windows version


## Licence

The script is distributed under the GPLv3. The pdfannotations.py file is
LGPLv3. 

## Related projects

* [Mendeley2Zotero](https://github.com/flinz/mendeley2zotero)
* [Adios_Mendeley](https://github.com/rdiaz02/Adios_Mendeley)
* [Menextract2pdf](https://github.com/cycomanic/Menextract2pdf)
* [txt2evernote](https://github.com/Xunius/txt2evernote)
* [tagextract](https://github.com/Xunius/tagextract)

