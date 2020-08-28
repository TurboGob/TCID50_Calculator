# TCID50_Calculator

## What does this calculate?

1. Calculate cumulative infected and uninfected wells adding infected wells totaling everything
under dilution and uninfected wells totaling everything above dilution.

2. Find PD. PD=(A-50)/(A-B)<br />
A=% response above 50%<br />
B=% response below 50%<br />

3. Find TCID 50<br />
Log(10) TCID50 = Dillution giving above 50% response minus PD

4. Take reciprocal of TCID50 and multiply by 100 to get TCID50/mL

5. Multiply by 0.69 to get pfu/mL

6. Output all the aforementioned step results per calculation to be executed.

## How to run a new calculation?

### Input

Input should be a **csv** with the following layout (start and end block per calculation in the file if you want one file to calculate multiple results):
<br /><br />
START<br />
Dilution,Infected,Uninfected<br />
0.00001,8,0<br />
0.000001,5,3<br />
0.0000001,1,7<br />
0.00000001,0,8<br />
END<br />
START<br />
Dilution,Infected,Uninfected<br />
0.00001,8,0<br />
0.000001,5,3<br />
0.0000001,1,7<br />
0.00000001,0,8<br />
END<br />

### How to run?

1. Install python 3.x: https://www.python.org/downloads/

2. Install pip (python package manager): https://pip.pypa.io/en/stable/installing/

3. Install the TCID50 Calculator pip package with the following command: 'TODO'

4. TODO: Execute and profit


### Output

Output will match the same input **csv** in the same directory.<br /><br />
It will have the same name of the provided csv, with **_result** suffixed.<br /><br />
The result file will have additional columns for cumulative totals, Percent_Infected, PD, TCID50, TCID50/mL, and pfu/mL.<br /><br />
START<br />
Dilution,Infected,Uninfected,Cumulative_Infected,Cumulative_Uninfected,Percent_Infected,BLANK_COLUMN,PD,TCID50,TCID50_per_mL,pfu_per_mL<br />
0.00001,8,0,14,0,100,,0.29,0.000000512,0.0000000195,0.0000000134<br />
0.000001,5,3,6,3,66.7<br />
0.0000001,1,7,1,10,9.1<br />
0.00000001,0,8,0,18,0<br />
END<br />
START<br />
Dilution,Infected,Uninfected,Cumulative_Infected,Cumulative_Uninfected,Percent_Infected,BLANK_COLUMN,PD,TCID50,TCID50_per_mL,pfu_per_mL<br />
0.00001,8,0,14,0,100,,0.29,0.000000512,0.0000000195,0.0000000134<br />
0.000001,5,3,6,3,66.7<br />
0.0000001,1,7,1,10,9.1<br />
0.00000001,0,8,0,18,0<br />
END<br />