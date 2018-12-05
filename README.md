# Setting up Demisto

Download and install Demisto Community Edition according to Demisto instructions

# Upload docker image to demisto server.

Use Dockerfile to create docker image and put into a public repository.

# Build your own integration

Go to Settings->Integrations->Servers & Services.

Click the +BYOI button.

Delete sample code and copy in demisto_uptycs.py.

In the integration settings fill in the following:

```sh
        Basic:
                Integration name:<choose a name>
                Description:<choose a description>
                Type: Analytics & SIEM
                Fetches Incidents: checked
        Parameters:
                Parameter name: key
                Mandatory: checked
                Display name: apifile key

                Parameter name: secret
                Mandatory: checked
                Display name: apifile secret

                Parameter name: domain
                Mandatory: checked
                Display name: apifile domain

                Parameter name: customerId
                Mandatory: checked
                Display name: apifile customerId

        Commands:
                Command name: post-query
                Description: query Uptycs DB
                Arguments:
                        Argument: method
                        Mandatory: checked
                        Description: http methods
                        List options: GET,POST

                        Argument: api_call
                        Mandatory: checked
                        Description: uri to connect to

                        Argument: query
                        Mandatory: checked
                        Description: query to run

                        Argument: queryType
                        Mandatory: checked
                        Description: type of query to run
                        List options: global,realtime

                Outputs:
                        Context Path: TestUptycsKey.items
                        Description: query result
                        Type: Unknown

        Script:
                Language type: Python
                Docker image name: bkschmolluptycs/demisto_uptycs:latest or use the repository you uploaded the image to above.
                Run on seperate container: checked
```
Click the Save icon.

Create an instance of your integration and enter in the appropriate Uptycs API information obtained from your uptycs.io account.

Check the Fetches incidents box.

Click the Test button to verify success.

Click the Done button

After your instance has pulled a few incidents, click the settings wheel and uncheck the Fetches incidents box.

Click the Done button.

# Create SharedAgent instance

Go to Settings->Integrations->Servers & Services.

Type 'shared agent' into the search bar.

Click 'Add instance'.

Fill in the following:
```sh
        Name:<choose a name for the endpoint>
        Credentials:<valid username on endpoint>
        Password:<corresponding password>
        Default Hostname or IP Address:<valid IP for endpoint>
        Target Architecture: amd64
        Target Operation System:<os of the endpoint>
```

Click the Test button to verify success.

Click the Done button.

# Add your script

Compress killProcess.sh into a .zip file.

Go to Settings->Integrations->Agent Tools.

Click the +Add Tool button.

Navigate to the directory with your zipped up script and upload it.

# Create Demisto Automation to run your script

Go to Automation.

Click the +New Script button.

Delete sample code and paste in killProcess.js.

In the script settings, fill in the following:
```sh
        Basic:
                Name:killProcess
                Type: JavaScript
        Arguments:
                Argument: upt_pid
                Mandatory: checked
                Description: pid for process to be killed
        Advanced:
        Run On: D2 Agent
```

Click the Save icon.

# Create Demisto Playbook to run automations

Go to Playbooks.

Click the +New Playbook button. Give the playbook a name.

Click the +Create Task button. Give the task a name.

Click 'Choose automation' and type in the name of your integration command, in this case, 'post-query'.

Fill in the following:
```sh
        method: POST
        api_call: /query
        query: SELECT json_extract(metadata, '$.pid') AS upt_pid FROM upt_alerts WHERE description = 'Bad IP address' ORDER BY alert_time DESC LIMIT 1
        queryType: global
```

Click the green OK button.

Click the +Create Task button. Give the task a name.

Click 'Choose automation' and type in the name of your integration command, in this case, 'D2ExecuteCommand'.

Fill in the following:
```sh
        commandName: D2Drop
        arguments:
                {
                "destpath":"<path of where to save the script on the endpoint>",
                "files":"killProcess/killProcess.sh",
                "using":"<name of your SharedAgent instance from above>"
                }
```

Click the green OK button.

Click the +Create Task button. Give the task a name.

Click 'Choose automation' and type in the name of your integration command, in this case, 'D2ExecuteCommand'.

Fill in the following:
```sh
        commandName: killProcess
        arguments: {"upt_pid":${UptycsKey.items.upt_pid}}
```

Click the green OK button

Click the Save icon.

Now connect the nodes of the task boxes to create a workflow, starting with the query, followed by dropping the script on the endpoint, and finally executing the script to kill the process.

Save the playbook.

# Add endpoint to an incident

Click on one of the incidents and go to the Work Plan.

Follow demisto instructions to install a D2 Agent on the desired endpoint.

Use the system_add command to add an endpoint to the incident.

```sh
/system_add host=<ip of endpoint> arch=amd64 name=<name for endpoint in UI> os=<os of endpoint> password=<Will-Prompt-After-Enter> user=<valid user on endpoint>
```
