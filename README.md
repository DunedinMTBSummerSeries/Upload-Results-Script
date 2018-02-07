# Upload-Results-Script
A script that modifies the HTML results output from SiTiming, automatically adds a results entry to the readme file and pushes files to the GitHub pages repo 'DunedinMTBSummerSeries.github.io' 

# What the Script Modifies
The script replaces the following strings:

| Description | Replaces | With |
| ----------- | -------- | ---- |
| Banner image link | ```<a href="http://www.sportident.co.uk" title="SiTiming from SPORTident" id="logo">``` | ```<a href="https://www.facebook.com/groups/DunedinMTBSummerSeries/" title="Dunedin MTB Summer Series" id="logo">``` |
| Banner text | ```<span>SiTiming from SPORTident</span>``` | ```<span>Dunedin MTB Summer Series</span>``` |

# Structure of the Website
```
https://dunedinmtbsummerseries.github.io
  |--results
       |--2018
            |--round-1
            |--round-2
       |--2017
            |--round-1
```
README.md is the root index page for the website - https://dunedinmtbsummerseries.github.io.

# How to Use the Script
It should be obvious, but just in case :) - Internet access is required for the results to be published.
1. Using SiTiming, save the HTML results for the round to the respective folder in the DunedinMTBSummerSeries.github.io repo (e.g. results/2018/round-1).
2. Using Windows Explorer, drag the folder where the HTML results were saved onto the 'modify-and-upload-results.py' script file to run the script on that round's results.
3. At the prompt, type 'Y' then Enter if you wish to publish the results to DunedinMTBSummerSeries.github.io.
4. At the prompt, enter a commit message (e.g. "Results for Round 2.").
5. Hopefully everything has worked and you can press Enter to exit the script.
6. Check the results at [dunedinmtbsummerseries.github.io/results\/\<year\>/\<round\>](https://dunedinmtbsummerseries.github.io/results/2018/round-1).
