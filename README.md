## Overview
This python project aims to make it easier for MTSU professors to handle zoom breakout rooms. The current, manual method offered by Zoom is quite tedious, especially with larger classes. Using this method, professors only have to write a simple text file that specifies groups and group members (see format below). Then, the script will generate a CSV file that meets Zoom's breakout room specifications, which can be used over and over again throughout the semester.

There is a plan to implement a GUI so that all professors will feel comfortable using this method. 

## Dependencies
**Necessary Python Packages**
  - csv
  - BeautifulSoup4 (bs4)

## Instructions
**Generating CSV for Zoom Breakout Rooms**

1. Write and save a .txt file that specifies groups and members (see below)
    - Save this file as "group.txt" in the same directory as the .py file

*Names **must** be identical to how they appear on D2L classlist.*
*Groups must be separated by a blank line.*

![](https://github.com/hunterkmcgee/zoom-groups/blob/master/img/sample_groups.png)

2. Save classlist website as classlist.html
    - Go to the D2L course page
    - Click on &quot;Communication&quot; drop-down menu
    - Select &quot;Classlist&quot;
    - Right-click on a blank area, and select &quot;Save as&quot;
    - Name the file &quot;classlist.html&quot;, save to same directory as the first .txt file
3. Run python script by typing &quot;python generateGroupsCsv.py&quot; in command line.
4. Open &quot;groups.csv&quot; and make sure everything is saved properly.
    - If a cell looks like &#39;\*\* LastName – FirstName \*\*&#39;, then either the student is not on the course roster or the names do not align between the two files.

**Loading CSV file into Zoom**

![](https://github.com/hunterkmcgee/zoom-groups/blob/master/img/instruct_zoom.png)
