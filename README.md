**Generating CSV for Zoom Breakout Rooms**

1. Write and save a .txt file that specifies groups and members (see below)
  1. Save this file as group.txt in the same directory as the .py file

 ![](RackMultipart20200908-4-1bjbpy6_html_a4987fd3db44a33c.gif)

**Names must be identical to how they appear on D2L classlist.**

![](RackMultipart20200908-4-1bjbpy6_html_946f47daf08a1ae.png)

1. Save classlist website as classlist.html
  1. Go to the D2L course page
  2. Click on &quot;Communication&quot; drop-down menu
  3. Select &quot;Classlist&quot;
  4. Right-click on a blank area, and select &quot;Save as&quot;
  5. Name the file &quot;classlist.html&quot;, save to same directory as the first .txt file
2. Run python script by typing &quot;python generateGroupsCsv.py&quot; in command line.
3. Open &quot;groups.csv&quot; and make sure everything is saved properly.
  1. If a cell looks like &#39;\*\* LastName – FirstName \*\*&#39;, then either the student is not on the course roster or the names do not align between the two files.

![](RackMultipart20200908-4-1bjbpy6_html_e73302458183a93b.png)
