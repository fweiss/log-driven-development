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
