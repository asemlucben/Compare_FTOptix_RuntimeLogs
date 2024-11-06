#!/bin/bash
taskset -c 3 /home/asem/Rockwell_Automation/FactoryTalk_Optix/FTOptixApplication/FTOptixRuntime -c -l VERBOSE2 2>&1 | tee -a /home/asem/featuresdemo2.single.txt
