import os
import sys
import fileinput

directory = sys.argv[1]

print "PROCESSING: " + directory

pathWords = directory.split("\\")
# print pathWords

numWords = len(pathWords)

roundText = pathWords[numWords-1]
yearText = pathWords[numWords-2]

roundIsValid = roundText.startswith("round")
yearIsValid = yearText.isdigit()

if roundIsValid and yearIsValid:
    # print "Directory structure is valid"

    print "\nMODIFYING HTML FILES"

    textToSearch1 = "<a href=\"http://www.sportident.co.uk\" title=\"SiTiming from SPORTident\" id=\"logo\">"
    textToReplace1 = "<a href=\"https://www.facebook.com/groups/DunedinMTBSummerSeries/\" title=\"Dunedin MTB Summer Series\" id=\"logo\">"

    textToSearch2 = "<span>SiTiming from SPORTident</span>"
    textToReplace2 = "<span>Dunedin MTB Summer Series</span>"

    textToSearch = ""
    textToReplace = ""

    for dname, dirs, files in os.walk(directory):
        isFileHtml = False

        for fname in files:
            fpath = os.path.join(dname, fname)

            numMatches = 0

            isFileHtml = fname.endswith(".html")

            if isFileHtml:
                print "\nSEARCHING:", fname

                fileToSearch = fpath

                tempFile = open( fileToSearch, 'r+' )

                for line in fileinput.input( fileToSearch ):
                    if textToSearch1 in line:
                        numMatches += 1
                        textToSearch = textToSearch1
                        textToReplace = textToReplace1
                    elif textToSearch2 in line:
                        numMatches += 1
                        textToSearch = textToSearch2
                        textToReplace = textToReplace2

                    tempFile.write( line.replace( textToSearch, textToReplace ) )

                tempFile.close()
            else:
                print "\nSKIPPING:", fname
                print "File is not HTML!!"

            if numMatches == 0:
                if isFileHtml == True:
                    print "No Matches Found!!"
            else:
                print numMatches, "Matches Found"


    pathToResultsIndex = directory + "\index.html"
    # print pathToResultsIndex

    fileResultsIndex = open(pathToResultsIndex, 'r')
    # print fileResultsIndex.read()

    for line in fileinput.input(pathToResultsIndex):
        if "<title>" in line:
            resultsTitleString = line
            break

    # print "resultsTitleString = ", resultsTitleString

    titleWords = resultsTitleString.split(" - ")

    courseText = titleWords[1] + " - " + titleWords[2]

    print "\n\nADDING RESULTS ENTRY TO README (" + yearText + " - " + courseText + ")"

    pathToReadme = ""

    for w in pathWords:
        if w == "results":
            break
        else:
            pathToReadme += (w + '\\')

    pathToReadme += "README.md"
    # print "Path to Readme = ", pathToReadme

    fileReadme = open(pathToReadme, 'r+')
    # print fileReadme.read()

    roundEntryExists = False

    for line in fileReadme:
        if roundText in line:
            roundEntryExists = True
            break

    if roundEntryExists == False:
        roundWords = roundText.split('-')
        roundNumber = roundWords[1]

        textToWrite = "* [" + courseText + "](https://dunedinmtbsummerseries.github.io/results/" + yearText + "/" + roundText + "/)\n"
        # print "textToWrite = ", textToWrite

        fileReadme.seek(0,2)
        fileReadme.write(textToWrite)
        fileReadme.close()
        print "SUCCESS"
    else:
        print "SKIPPING! (Entry already exists)"


    publishResults = raw_input("\n\nPublish results to 'DunedinMTBSummerSeries.github.io'? [Y/N]: ")

    if publishResults == 'Y' or publishResults == 'y':
        os.chdir("C:\Users\Admin\Documents\Dunedin MTB Summer Series\DunedinMTBSummerSeries.github.io")

        def sendGitCommand (command):
            exitStatus = os.system(command)
            if exitStatus == 0:
                print "SUCCESS"
            else:
                print "FAIL! (Exit status: ", exitStatus, ")"
            return exitStatus

        print "\n\nADD NEW FILES"
        gitCommandStatus = sendGitCommand("git add .")

        if gitCommandStatus == 0:
            print "\n\nCOMMIT RESULTS FILES"
            commitMessage = raw_input("Commit message: ")
            gitCommand = "git commit -a -m \"" + commitMessage + "\""
            gitCommandStatus = sendGitCommand(gitCommand)

            if gitCommandStatus == 0:
                print"\n\nPUSH REPO TO THE CLOUD"
                gitCommand = "git push -u origin master"
                gitCommandStatus = sendGitCommand(gitCommand)
            else:
                print "Nothing to commmit - skipping push!"
        else:
            print "No files to add - skipping commit and push!"

    else:
        print "Results not published!"

else:
    print "\nERROR!!! - Invalid directory structure"
    print "\nPath must take the form '..\DunedinMTBSummerSeries.github.io\\results\<year>\<round>'"
    print "where: <year>  = 'yyyy' (e.g. 2018)"
    print "       <round> = 'round-x' (e.g. round-1)"

input( '\n\nPress Enter to exit...' )