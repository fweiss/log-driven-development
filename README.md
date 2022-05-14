# Log Driven Development
Explore ways of using log file to describe the operation of an application

## Process meta-model
"a sequence of steps leading to an end"

- sequence: linear, non-linear (branching), parallel
- step: state, action, transition, event
- leading to: path, causality
- end: result, output, final state, goal

## Ideas
- basic log filtering
- "trace" log level
- filter by module
- extract module
- module meta-data?
- tagging process "ends"
- how to infer "initial state"
- nesting, drill down

## Apps
### open-log-viewer
- node/electron
- open source
- simplistic
- may be good start for LDD

#### Customize
- FileViewer.vue
- FileSettings.setLogLevelsToShow()
- written partly in Vue

## syslogng
- uses PatternDB
- can define filters in .conf DSK files
- can enrich by interpolating external data

## Links and references

[IBM RSVP annotated and nestedlog file](https://www.ibm.com/docs/en/zos/2.2.0?topic=problems-example-log-file)

### LAKE - Logs as Knowledge Bases
[Other uses for log files](https://www.researchgate.net/publication/273760856_Using_Log_Files_Recorded_During_Program_Execution)

coding to debugging vs logging to observation 

"This  idea  can  be  expanded to include tuning logs so that logs serves as a knowledge base of program execution that con-tains precise, concise, and critical information for  software  developers to  better understand how the software runs"

"logging is mainly used for debug-ging"

push statistics calculation cheaply into the running program

"Thereafter,  a software  program  is  obligated  to  reveal  its nontrivial  execution  details with  appropriate density in an easy-to-follow way."

It looked like it was going to get into what I was looking for, but then focused on debugging.
