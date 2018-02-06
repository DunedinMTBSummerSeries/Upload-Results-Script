import os
import sys
import fileinput

textToSearch1 = "<a href=\"http://www.sportident.co.uk\" title=\"SiTiming from SPORTident\" id=\"logo\">"
textToReplace1 = "<a href=\"https://www.facebook.com/groups/DunedinMTBSummerSeries/\" title=\"Dunedin MTB Summer Series\" id=\"logo\">"

textToSearch2 = "<span>SiTiming from SPORTident</span>"
textToReplace2 = "<span>Dunedin MTB Summer Series</span>"

directory = sys.argv[1]

print "Directory: ", directory, "\n"

textToSearch = ""
textToReplace = ""

for dname, dirs, files in os.walk(directory):
    isFileHtml = False

    for fname in files:
        fpath = os.path.join(dname, fname)

        numMatches = 0

        isFileHtml = fname.endswith(".html")

        if isFileHtml:
            print "SEARCHING:", fname

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
            print "SKIPPING:", fname
            print "File is not HTML!!\n"

        if numMatches == 0:
            if isFileHtml == True:
                print "No Matches Found!!\n"
        else:
            print numMatches, "Matches Found\n"

publishResults = raw_input("\nPublish results to 'DunedinMTBSummerSeries.github.io'? [Y/N]: ")

if publishResults == 'Y' or publishResults == 'y':
    os.chdir("C:\Users\cjensen\Documents\Dunedin MTB Summer Series\ResultsTest")

    def sendGitCommand (command):
        exitStatus = os.system(command)
        if exitStatus == 0:
            print "SUCCESS"
        else:
            print "FAIL! (Exit status: ", exitStatus, ")"
        return exitStatus

    print "\nADD NEW FILES"
    gitCommandStatus = sendGitCommand("git add .")
    # gitCommand = "git add -A"
    # exitStatus = os.system(gitCommand)
    # if exitStatus == 0:
    #     print SUCCESS
    # else
    #     print "FAIL! (Exit status: ", exitStatus

    if gitCommandStatus == 0:
        print "\nCOMMIT RESULTS FILES"
        commitMessage = raw_input("Commit message: ")
        gitCommand = "git commit -a -m \"" + commitMessage + "\""
        gitCommandStatus = sendGitCommand(gitCommand)
        # exitStatus = os.system(gitCommand)
        # print "Exit status = ", exitStatus

        if gitCommandStatus == 0:
            print"\nPUSH REPO TO THE CLOUD"
            gitCommand = "git push -u origin master"
            gitCommandStatus = sendGitCommand(gitCommand)
            # os.system(gitCommand)
            # print "Exit status = ", exitStatus

            # if exitStatus != 0:
            #     print "Nothing pushed!"
        else:
            print "Nothing to commmit - skipping push!"
    else:
        print "No files to add - skipping commit and push!"

else:
    print "Results not published!"

input( '\n\n Press Enter to exit...' )