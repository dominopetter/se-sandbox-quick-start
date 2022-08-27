/* X-Axis &amp; Y-Axis Title */
proc sgplot data=sashelp.cars;
    vbar type;
    xaxis label="Type of Vehicle";
    yaxis label="Frequency of Vehicle Type";
run;