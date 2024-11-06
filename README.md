# Timing Tables Comparison

This project contains scripts to extract and compare timing tables from FactoryTalk Optix log files. It can be particularly useful when performing some performances improvements to an application and see if the proiject got better or worse. It can be also used just to extract diagnostics data in a more readable format from the FactoryTalk Optix Runtime

## FactoryTalk Optix Runtime setup

1. Transfer the application to a Linux device (Ubuntu 22.04 in my test)
2. Execute the application by enabling verbose logging and pass the output to a file

```sh
/home/asem/Rockwell_Automation/FactoryTalk_Optix/FTOptixApplication/FTOptixRuntime -c -l VERBOSE2 2>&1 | tee -a /home/asem/outuput.first.txt
```

sample output:

```txt
...
06-11-2024 13:28:52.971 VERBOSE(1) (urn:FTOptix:NativeUI): Delete node begin 9/0b67c9c2e1340747fb2ddaa2341c5a1d
06-11-2024 13:28:52.974 VERBOSE(1) (urn:FTOptix:NativeUI): Remove item begin 9/0b67c9c2e1340747fb2ddaa2341c5a1d, Style
06-11-2024 13:28:52.974 VERBOSE(1) (urn:FTOptix:NativeUI): Dispatch BeforeDeleteUIObject 9/0b67c9c2e1340747fb2ddaa2341c5a1d
06-11-2024 13:28:52.974 VERBOSE(1) (urn:FTOptix:NativeUI): CoreDeleter begin 9/0b67c9c2e1340747fb2ddaa2341c5a1d
06-11-2024 13:28:52.974 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/ScreenBackground_static/TitleGrid/CategoryTitle, nodeId 9/3f159728cddc65476eb4c8ea0034dc3c
06-11-2024 13:28:52.975 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/ScreenBackground_static/TitleGrid/TextSeparator, nodeId 9/48d7dc523bd9503d093c2bfb3214229f
06-11-2024 13:28:52.975 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/ScreenBackground_static/TitleGrid/FeatureTitle, nodeId 9/3342cb5342e36b8261d9ea0a423007fc
06-11-2024 13:28:52.975 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/ScreenBackground_static/TitleGrid, nodeId 9/f4d606dca11d52e0875bc2120b85019d
06-11-2024 13:28:52.975 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/ScreenBackground_static, nodeId 9/bfcceae844eb16d717617821a4082c77
06-11-2024 13:28:52.975 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/WorkspaceArea/Content/Styles/PredefinedStyleSheets/Content/Label1, nodeId 9/7d5f3457a649db4dc8e71426500b42bf
06-11-2024 13:28:52.975 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/WorkspaceArea/Content/Styles/PredefinedStyleSheets/Content/Grid/Default, nodeId 9/f35afc9b0f2491e8ce100c6491bc05d9
06-11-2024 13:28:52.975 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/WorkspaceArea/Content/Styles/PredefinedStyleSheets/Content/Grid/DarkMaterial, nodeId 9/9b93ccb4f7996fa38d2fdd4cab8b20d2
06-11-2024 13:28:52.975 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/WorkspaceArea/Content/Styles/PredefinedStyleSheets/Content/Grid/ISA101, nodeId 9/b66f60f8781c03439632c9d056bcc435
06-11-2024 13:28:52.976 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/WorkspaceArea/Content/Styles/PredefinedStyleSheets/Content/Grid/FriendlyLight, nodeId 9/132351c906ab786dd0bdaac4c3b775f0
06-11-2024 13:28:52.976 VERBOSE(1) (urn:FTOptix:NativeUI): UIGraph: attempt to remove node not already added, node Style/WorkspaceArea/Content/Styles/PredefinedStyleSheets/Content/Grid/FriendlyDark, nodeId 9/a7242c08bcf4ad37c44e3cfa5495fa43
06-11-2024 13:28:52.976 DEBUG (urn:FTOptix:NativeUI): AddItem;86
...
```

3. Save the output files to some place that can be reached by the python code
4. (optional) Apply some changes to the application and run the test again, make sure to save output to a different file name

## Files

- `extract_timing_table.py`: Extracts timing data from a log file and formats it into a table.
- `compare_timing_tables.py`: Compares timing data from two different log files and outputs the comparison in a table format.

## Usage

### Extract Timing Table

To extract timing data from a log file, use the `extract_timing_table.py` script.

1. Place your log file in the `RuntimeLogs` directory.
2. Update the `LOG_FILE` variable in `extract_timing_table.py` to point to your log file.

```python
LOG_FILE = "./RuntimeLogs/your_log_file.txt"
```

3. Run the script and output the `stdout` to a file:

```sh
python extract_timing_table.py > first.txt
```

4. Repeat the process for the second file

### Compare Timing Tables

To compare timing data from two log files, use the `compare_timing_tables.py` script.

1. Place the output of the `extract_timing_table.py` code somewhere in the local machine.
2. Update the `FIRST_FILE` and `SECOND_FILE` variables in `compare_timing_tables.py` to point to your log files.

```python
FIRST_FILE = "./first.txt"
SECOND_FILE = "./second.txt"
```

3. Run the script:

```sh
python compare_timing_tables.py > comparison.txt
```

This will output the comparison table to a txt file that can be investigated manually

## Output Formatting

### Extract Timing Table

The output of `extract_timing_table.py` will be formatted as follows:

```
|--------------------------------|------------------------------------------|------------|------------|------------|
| Page Name                      | Module Name                              | Total      |  Number    |  Items per |
|                                |                                          | load time  |  of items  |  second    |
|--------------------------------|------------------------------------------|------------|------------|------------|
| PageName1                      | ModuleName1                              |     123.45 |       6789 |      12.34 |
|                                |                                          |     234.56 |       7890 |      23.45 |
|--------------------------------|------------------------------------------|------------|------------|------------|
```

### Compare Timing Tables

The output of `compare_timing_tables.py` will be formatted as follows:

```
|--------------------------------|------------------------------------------||--------------------------------------||--------------------------------------||--------------------------------------||
|                                |                                          ||             First file               ||             Second file              ||        First to second ratio         ||
|--------------------------------|------------------------------------------||--------------------------------------||--------------------------------------||--------------------------------------||
| Page Name                      | Module Name                              || Total      |  Number    |  Items per || Total      |  Number    |  Items per || Load time  | items cnt  |   items/s  ||
|                                |                                          || load time  |  of items  |  second    || load time  |  of items  |  second    || improvement| (always 1) | improvement||
|--------------------------------|------------------------------------------||------------|------------|------------||------------|------------|------------||------------|------------|------------||
| PageName1                      | ModuleName1                              ||     123.45 |       6789 |      12.34 ||     234.56 |       7890 |      23.45 ||       0.53 |       0.86 |       0.53 ||
|--------------------------------|------------------------------------------||------------|------------|------------||------------|------------|------------||------------|------------|------------||
```

## Log Files

- Place the log files for extraction in the `RuntimeLogs` directory.
- Place the log files for comparison in the root directory and update the script variables accordingly.
