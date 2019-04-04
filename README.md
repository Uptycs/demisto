# Setting up Demisto

If you are not a Demisto customer already, download and install Demisto Community Edition according to Demisto instructions.

# Configure the Uptycs integration

Go to Settings->Integrations->Servers & Services and search for Uptycs.

Create an instance of your integration and enter in the appropriate Uptycs API information obtained from your uptycs.io account.

Check the Fetches incidents box.

Click the Test button to verify success.

Click the Done button

## Commands
---
You can execute these commands from the Demisto CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.
1. uptycs-get-assets
2. uptycs-run-query
3. uptycs-get-alerts
4. uptycs-get-alert-rules
5. uptycs-get-event-rules
6. uptycs-get-events
7. uptycs-get-process-open-sockets
8. uptycs-get-process-information
9. uptycs-get-process-child-processes
10. uptycs-get-processes
11. uptycs-get-process-open-files
12. uptycs-set-alert-status
13. uptycs-set-asset-tag
14. uptycs-get-user-information
15. uptycs-get-threat-indicators
16. uptycs-get-threat-sources
17. uptycs-get-threat-vendors
18. uptycs-get-parent-information
19. uptycs-post-threat-source
20. uptycs-get-users
21. uptycs-get-asset-groups
22. uptycs-get-user-asset-groups
23. uptycs-get-threat-indicator
24. uptycs-get-threat-source
### uptycs-get-assets
---
return assets enrolled with Uptycs
##### Base Command

`uptycs-get-assets`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| limit | Limit the number of entries returned. | Optional | 
| os | Only return assets with this type of operating system. | Optional | 
| host_name_is | Only return assets with this hostname.  This argument should be in double quotes.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| host_name_like | Only return assets with this string in the hostname.  This argument should be in double quotes.  Use this to find a selection of assets with similar hostnames.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| asset_group_id | Only return assets which are a member of this asset group | Optional | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.Assets.id | string | Uptycs asset id  | 
| Uptycs.Assets.createdAt | date | Time asset was enrolled with Uptycs | 
| Uptycs.Assets.hostName | string | Hostname in Uptycs DB | 
| Uptycs.Assets.os | string | os installed on asset (Windows, Linux, Mac OS X) | 
| Uptycs.Assets.osVersion | string | os version | 
| Uptycs.Assets.lastActivityAt | date | Last activity | 
| Uptycs.Assets.deletedAt | date | Time asset was unenrolled from Uptycs | 
| Uptycs.Assets.osqueryVersion | string | Current version of osquery installed on the asset | 


##### Command Example
`uptycs-get-assets os="Mac OS X/Apple OS X/macOS" limit=1`

##### Context Example
```
{
    "Uptycs.Assets": [
        {
            "status": "active", 
            "last_enrolled_at": "2019-03-06 15:22:05.769", 
            "os_version": "10.14", 
            "osquery_version": "3.2.6.43-Uptycs", 
            "created_at": "2018-09-25 16:38:16.440", 
            "longitude": -97.822, 
            "os_flavor": "darwin", 
            "host_name": "kyle-mbp-work", 
            "latitude": 37.751, 
            "last_activity_at": "2019-03-06 15:42:10.193", 
            "os": "Mac OS X", 
            "id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "location": "United States"
        }
    ]
}
```

##### Human Readable Output
### Uptycs Assets
|id|host_name|os|os_version|osquery_version|last_activity_at|
|---|---|---|---|---|---|
|984d4a7a-9f3a-580a-a3ef-2841a561669b|kyle-mbp-work|Mac OS X|10.14|3.2.6.43-Uptycs|2019-03-06 15:42:10.193|


### uptycs-run-query
---
enter a SQL query to run against the Uptycs database or on your endpoints in real-time.  A list of tables can be found at osquery.io/schema, or by using the query "select * from information_schema.tables"
##### Base Command

`uptycs-run-query`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| query | This is the query that will be run.  Queries should be written for a SQLite database. For example, "SELECT * FROM processes" returns the entire table named "processes".  This argument should be in double quotes. | Required | 
| query_type | The query can be run globally (returns results for entire history stored in Uptycs DB) or real-time (returns results for queries run on endpoints at the time of query execution) | Required | 
| limit | Limit the number of entries returned. | Optional | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.QueryResults | unknown | Results of executed query | 


##### Command Example
`uptycs-run-query query="SELECT * FROM process_open_sockets LIMIT 10" query_type=realtime host_name_like="uptycs-osquery-"`

##### Context Example
```
{
    "Uptycs.QueryResults": [
        {
            "protocol": "6", 
            "socket": "59764565", 
            "family": "2", 
            "local_port": "59752", 
            "remote_port": "443", 
            "pid": "9", 
            "remote_address": "18.213.163.112", 
            "upt_asset_id": "a4991bf9-13e3-026b-7b46-af192746d556", 
            "state": "ESTABLISHED", 
            "fd": "14", 
            "path": "", 
            "local_address": "10.8.0.28", 
            "net_namespace": "4026532943"
        }, 
        {
            "protocol": "6", 
            "socket": "59723589", 
            "family": "2", 
            "local_port": "55386", 
            "remote_port": "443", 
            "pid": "9", 
            "remote_address": "18.213.163.112", 
            "upt_asset_id": "a4991bf9-13e3-026b-7b46-af192746d556", 
            "state": "ESTABLISHED", 
            "fd": "37", 
            "path": "", 
            "local_address": "10.8.0.28", 
            "net_namespace": "4026532943"
        }, 
        {
            "protocol": "6", 
            "socket": "59735105", 
            "family": "2", 
            "local_port": "56532", 
            "remote_port": "443", 
            "pid": "9", 
            "remote_address": "18.213.163.112", 
            "upt_asset_id": "a4991bf9-13e3-026b-7b46-af192746d556", 
            "state": "ESTABLISHED", 
            "fd": "36", 
            "path": "", 
            "local_address": "10.8.0.28", 
            "net_namespace": "4026532943"
        }, 
        {
            "protocol": "0", 
            "socket": "13674642", 
            "family": "1", 
            "local_port": "0", 
            "remote_port": "0", 
            "pid": "9", 
            "remote_address": "", 
            "upt_asset_id": "a4991bf9-13e3-026b-7b46-af192746d556", 
            "state": "", 
            "fd": "11", 
            "path": "/var/osquery/osquery.em", 
            "local_address": "", 
            "net_namespace": "4026532943"
        }, 
        {
            "protocol": "0", 
            "socket": "13674637", 
            "family": "1", 
            "local_port": "0", 
            "remote_port": "0", 
            "pid": "9", 
            "remote_address": "", 
            "upt_asset_id": "a4991bf9-13e3-026b-7b46-af192746d556", 
            "state": "", 
            "fd": "10", 
            "path": "", 
            "local_address": "", 
            "net_namespace": "4026532943"
        }, 
        {
            "protocol": "0", 
            "socket": "13674636", 
            "family": "1", 
            "local_port": "0", 
            "remote_port": "0", 
            "pid": "9", 
            "remote_address": "", 
            "upt_asset_id": "a4991bf9-13e3-026b-7b46-af192746d556", 
            "state": "", 
            "fd": "9", 
            "path": "", 
            "local_address": "", 
            "net_namespace": "4026532943"
        }, 
        {
            "protocol": "0", 
            "socket": "13674635", 
            "family": "1", 
            "local_port": "0", 
            "remote_port": "0", 
            "pid": "9", 
            "remote_address": "", 
            "upt_asset_id": "a4991bf9-13e3-026b-7b46-af192746d556", 
            "state": "", 
            "fd": "8", 
            "path": "", 
            "local_address": "", 
            "net_namespace": "4026532943"
        }, 
        {
            "protocol": "0", 
            "socket": "13674634", 
            "family": "1", 
            "local_port": "0", 
            "remote_port": "0", 
            "pid": "9", 
            "remote_address": "", 
            "upt_asset_id": "a4991bf9-13e3-026b-7b46-af192746d556", 
            "state": "", 
            "fd": "7", 
            "path": "", 
            "local_address": "", 
            "net_namespace": "4026532943"
        }, 
        {
            "protocol": "0", 
            "socket": "13674590", 
            "family": "1", 
            "local_port": "0", 
            "remote_port": "0", 
            "pid": "6", 
            "remote_address": "", 
            "upt_asset_id": "a4991bf9-13e3-026b-7b46-af192746d556", 
            "state": "", 
            "fd": "3", 
            "path": "", 
            "local_address": "", 
            "net_namespace": "4026532943"
        }
    ]
}
```

##### Human Readable Output
### Uptycs Query Result
|protocol|socket|family|local_port|remote_port|pid|remote_address|upt_asset_id|state|fd|path|local_address|net_namespace|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|6|59764565|2|59752|443|9|18.213.163.112|a4991bf9-13e3-026b-7b46-af192746d556|ESTABLISHED|14||10.8.0.28|4026532943|
|6|59723589|2|55386|443|9|18.213.163.112|a4991bf9-13e3-026b-7b46-af192746d556|ESTABLISHED|37||10.8.0.28|4026532943|
|6|59735105|2|56532|443|9|18.213.163.112|a4991bf9-13e3-026b-7b46-af192746d556|ESTABLISHED|36||10.8.0.28|4026532943|
|0|13674642|1|0|0|9||a4991bf9-13e3-026b-7b46-af192746d556||11|/var/osquery/osquery.em||4026532943|
|0|13674637|1|0|0|9||a4991bf9-13e3-026b-7b46-af192746d556||10|||4026532943|
|0|13674636|1|0|0|9||a4991bf9-13e3-026b-7b46-af192746d556||9|||4026532943|
|0|13674635|1|0|0|9||a4991bf9-13e3-026b-7b46-af192746d556||8|||4026532943|
|0|13674634|1|0|0|9||a4991bf9-13e3-026b-7b46-af192746d556||7|||4026532943|
|0|13674590|1|0|0|6||a4991bf9-13e3-026b-7b46-af192746d556||3|||4026532943|


### uptycs-get-alerts
---
return alerts from Uptycs DB
##### Base Command

`uptycs-get-alerts`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| limit | Limit the number of entries returned. | Required | 
| host_name_is | Only return assets with this hostname.  This argument should be in double quotes.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| host_name_like | Only return assets with this string in the hostname. This argument should be in double quotes.  Use this to find a selection of assets with similar hostnames.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| code | Alert code to specify which types of alerts you would like to retrieve | Optional | 
| time_ago | Specifies how far back you want to look.  Format examples: 2 hours, 4 minutes, 6 month, 1 day, etc. | Optional | 
| start_window | Beginning of window to search for open connections.  Format is "YYYY-MM-DD HH:MM:SS.000", for example, March 15, 2019 at 1:52:36 am would be written as "2019-03-15 01:52:36.000".  This argument should be in double quotes. | Optional | 
| end_window | End of window to search for open connections.  Format is "YYYY-MM-DD HH:MM:SS.000", for example, March 15, 2019 at 1:52:36 am would be written as "2019-03-15 01:52:36.000".  This argument should be in double quotes. | Optional | 
| id | Unique Uptycs alert id which will retrieve a specific alert.  Use this argument without any other arguments. | Optional | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.Alerts.description | string | Description of alert | 
| Uptycs.Alerts.upt_asset_id | string | Uptycs asset ID | 
| Uptycs.Alerts.code | string | Alert code in Uptycs DB | 
| Uptycs.Alerts.severity | string | Severity | 
| Uptycs.Alerts.alert_time | date | Time alert was created at | 
| Uptycs.Alerts.value | string | Specific problem which caused an alert.  It may be an IP address, a program that crashed, a file with a file hash known to be malware, etc. | 
| Uptycs.Alerts.host_name | string | Hostname for the asset which fired the alert | 
| Uptycs.Alerts.id | string | unique Uptycs id for a particular alert | 
| Uptycs.Alerts.threat_indicator_id | string | unique Uptycs id that identifies the threat indicator which triggered this alert | 
| Uptycs.Alerts.threat_source_name | string | name of the source of the threat indicator that triggered this alert | 
| Uptycs.Alerts.pid | unknown | pid of the process which was responsible for firing the alert | 


##### Command Example
`uptycs-get-alerts limit=1`

##### Context Example
```
{
    "Uptycs.Alerts": [
        {
            "status": "open", 
            "description": "Outbound Network Connection to threat intel IOC", 
            "threat_source_name": "No threat source for this alert", 
            "severity": "high", 
            "created_at": "2019-03-05 20:08:02.467", 
            "pid": "Not applicable or unknown", 
            "updated_at": "2019-03-05 20:08:04.966", 
            "value": "54.165.17.209", 
            "upt_asset_id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "threat_indicator_id": "No threat indicator for this alert", 
            "alert_time": "2019-03-05 20:07:53.000", 
            "host_name": "kyle-mbp-work", 
            "assigned_to": null, 
            "metadata": "{\"local_address\":\"0.0.0.0\",\"local_port\":20480,\"login_name\":\"kyleschmoll\",\"family\":2,\"remote_address\":\"54.165.17.209\"}", 
            "id": "ce5d1255-df14-4c77-a04b-82a87c74b3df", 
            "grouping": "Compliance"
        }
    ]
}
```

##### Human Readable Output
### Uptycs Alerts: 
|upt_asset_id|host_name|grouping|alert_time|description|value|severity|threat_indicator_id|threat_source_name|
|---|---|---|---|---|---|---|---|---|
|984d4a7a-9f3a-580a-a3ef-2841a561669b|kyle-mbp-work|Compliance|2019-03-05 20:07:53.000|Outbound Network Connection to threat intel IOC|54.165.17.209|high|No threat indicator for this alert|No threat source for this alert|


### uptycs-get-alert-rules
---
retrieve a list of alert rules
##### Base Command

`uptycs-get-alert-rules`
##### Input

There are no input arguments for this command.

##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-get-alert-rules limit=1`

##### Context Example
```

```

##### Human Readable Output
### Uptycs Alert Rules
|name|description|grouping|enabled|updatedAt|code|
|---|---|---|---|---|---|
|Bad Domain Alert|Bad Domain Alert|Critical file|true|2019-02-22T21:04:30.872Z|BAD_DOMAIN|


### uptycs-get-event-rules
---
retrieve a list of event rules
##### Base Command

`uptycs-get-event-rules`
##### Input

There are no input arguments for this command.

##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-get-event-rules limit=1`

##### Context Example
```

```

##### Human Readable Output
### Uptycs Event Rules
|name|description|grouping|enabled|updatedAt|code|
|---|---|---|---|---|---|
|Bad domains|Creates events when a bad domain is resolved|default|true|2019-02-21T17:20:59.825Z|BAD_DOMAIN|


### uptycs-get-events
---
return events from Uptycs DB
##### Base Command

`uptycs-get-events`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| limit | Limit the number of entries returned. | Required | 
| host_name_is | Only return assets with this hostname.  This argument should be in double quotes.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| host_name_like | Only return assets with this string in the hostname. This argument should be in double quotes.  Use this to find a selection of assets with similar hostnames.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| code | Event code to specify which types of events you would like to retrieve | Optional | 
| time_ago | Specifies how far back you want to look.  Format examples: 2 hours, 4 minutes, 6 month, 1 day, etc. | Optional | 
| start_window | Beginning of window to search for open connections.  Format is "YYYY-MM-DD HH:MM:SS.000", for example, March 15, 2019 at 1:52:36 am would be written as "2019-03-15 01:52:36.000".  This argument should be in double quotes. | Optional | 
| end_window | End of window to search for open connections.  Format is "YYYY-MM-DD HH:MM:SS.000", for example, March 15, 2019 at 1:52:36 am would be written as "2019-03-15 01:52:36.000".  This argument should be in double quotes. | Optional | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.Events.description | string | Description of event | 
| Uptycs.Events.assetId | string | Uptycs asset ID | 
| Uptycs.Events.code | string | Event code in Uptycs DB | 
| Uptycs.Events.createdAt | date | Time event was created at | 


##### Command Example
`uptycs-get-events limit=10 time_ago="30 days"`

##### Context Example
```
{
    "Uptycs.Events": [
        {
            "description": "Bad IP address", 
            "event_time": "2019-03-05 20:09:31.000", 
            "severity": "high", 
            "created_at": "2019-03-05 20:09:33.000", 
            "value": "87.147.254.215", 
            "host_name": "kyle-mbp-work", 
            "metadata": "{\"time\":1551816569,\"path\":\"\",\"pid\":1625}", 
            "id": "cf12af70-2a30-4754-af7b-12251aeb83f6", 
            "grouping": "Bad IP access"
        }, 
        {
            "description": "Bad IP address", 
            "event_time": "2019-03-05 20:09:31.000", 
            "severity": "high", 
            "created_at": "2019-03-05 20:09:33.000", 
            "value": "87.147.254.215", 
            "host_name": "kyle-mbp-work", 
            "metadata": "{\"time\":1551816569,\"path\":\"\",\"pid\":1625}", 
            "id": "d0c9b280-f38e-4f7f-a52a-bfdf0c4578ce", 
            "grouping": "Bad IP access"
        }, 
        {
            "description": "Bad IP address", 
            "event_time": "2019-03-05 20:08:34.000", 
            "severity": "high", 
            "created_at": "2019-03-05 20:08:36.000", 
            "value": "87.147.254.215", 
            "host_name": "kyle-mbp-work", 
            "metadata": "{\"time\":1551816510,\"path\":\"\",\"pid\":1625}", 
            "id": "82f18097-5d46-454c-8449-6868409af639", 
            "grouping": "Bad IP access"
        }, 
        {
            "description": "Bad IP address", 
            "event_time": "2019-03-05 20:08:34.000", 
            "severity": "high", 
            "created_at": "2019-03-05 20:08:36.000", 
            "value": "87.147.254.215", 
            "host_name": "kyle-mbp-work", 
            "metadata": "{\"time\":1551816510,\"path\":\"\",\"pid\":1625}", 
            "id": "7cd6c6b3-b7d4-4404-b0d2-5978caecd706", 
            "grouping": "Bad IP access"
        }, 
        {
            "description": "Outbound Network Connection to threat intel IOC", 
            "event_time": "2019-03-05 20:08:17.000", 
            "severity": "high", 
            "created_at": "2019-03-05 20:08:19.000", 
            "value": "87.147.254.215", 
            "host_name": "kyle-mbp-work", 
            "metadata": "{\"time\":1551816493,\"local_address\":\"0.0.0.0\",\"local_port\":20480,\"login_name\":\"kyleschmoll\",\"family\":2}", 
            "id": "e4a3e70b-cefd-481f-953d-91e7f9a2605e", 
            "grouping": "Compliance"
        }, 
        {
            "description": "Outbound Network Connection to threat intel IOC", 
            "event_time": "2019-03-05 20:08:17.000", 
            "severity": "high", 
            "created_at": "2019-03-05 20:08:19.000", 
            "value": "87.147.254.215", 
            "host_name": "kyle-mbp-work", 
            "metadata": "{\"time\":1551816493,\"local_address\":\"0.0.0.0\",\"local_port\":20480,\"login_name\":\"kyleschmoll\",\"family\":2}", 
            "id": "877497f9-eeff-44ba-8f97-e0f3969e74db", 
            "grouping": "Compliance"
        }, 
        {
            "description": "Outbound Network Connection to threat intel IOC", 
            "event_time": "2019-03-05 20:08:03.000", 
            "severity": "high", 
            "created_at": "2019-03-05 20:08:05.000", 
            "value": "54.165.17.209", 
            "host_name": "kyle-mbp-work", 
            "metadata": "{\"time\":1551816480,\"local_address\":\"0.0.0.0\",\"local_port\":20480,\"login_name\":\"kyleschmoll\",\"family\":2}", 
            "id": "91d28091-8799-404a-a498-03e9e21cd99e", 
            "grouping": "Compliance"
        }, 
        {
            "description": "Outbound Network Connection to threat intel IOC", 
            "event_time": "2019-03-05 20:07:58.000", 
            "severity": "high", 
            "created_at": "2019-03-05 20:08:00.000", 
            "value": "54.165.17.209", 
            "host_name": "kyle-mbp-work", 
            "metadata": "{\"time\":1551816473,\"local_address\":\"0.0.0.0\",\"local_port\":20480,\"login_name\":\"kyleschmoll\",\"family\":2}", 
            "id": "c13a75e6-94de-4f5d-a3f1-6eeedfa2791e", 
            "grouping": "Compliance"
        }, 
        {
            "description": "Bad IP address", 
            "event_time": "2019-03-05 20:07:04.000", 
            "severity": "high", 
            "created_at": "2019-03-05 20:07:06.000", 
            "value": "87.147.254.215", 
            "host_name": "kyle-mbp-work", 
            "metadata": "{\"time\":1551816420,\"path\":\"\",\"pid\":1625}", 
            "id": "1c004f28-60b4-4916-8d99-db706d6fd87f", 
            "grouping": "Bad IP access"
        }, 
        {
            "description": "Outbound Network Connection to threat intel IOC", 
            "event_time": "2019-03-05 20:06:47.000", 
            "severity": "high", 
            "created_at": "2019-03-05 20:06:49.000", 
            "value": "87.147.254.215", 
            "host_name": "kyle-mbp-work", 
            "metadata": "{\"time\":1551816403,\"local_address\":\"0.0.0.0\",\"local_port\":20480,\"login_name\":\"kyleschmoll\",\"family\":2}", 
            "id": "1c7790d3-8b0b-461a-8c1b-ee51da16f9ef", 
            "grouping": "Compliance"
        }
    ]
}
```

##### Human Readable Output
### Uptycs Events
|host_name|grouping|event_time|description|value|severity|
|---|---|---|---|---|---|
|kyle-mbp-work|Bad IP access|2019-03-05 20:09:31.000|Bad IP address|87.147.254.215|high|
|kyle-mbp-work|Bad IP access|2019-03-05 20:09:31.000|Bad IP address|87.147.254.215|high|
|kyle-mbp-work|Bad IP access|2019-03-05 20:08:34.000|Bad IP address|87.147.254.215|high|
|kyle-mbp-work|Bad IP access|2019-03-05 20:08:34.000|Bad IP address|87.147.254.215|high|
|kyle-mbp-work|Compliance|2019-03-05 20:08:17.000|Outbound Network Connection to threat intel IOC|87.147.254.215|high|
|kyle-mbp-work|Compliance|2019-03-05 20:08:17.000|Outbound Network Connection to threat intel IOC|87.147.254.215|high|
|kyle-mbp-work|Compliance|2019-03-05 20:08:03.000|Outbound Network Connection to threat intel IOC|54.165.17.209|high|
|kyle-mbp-work|Compliance|2019-03-05 20:07:58.000|Outbound Network Connection to threat intel IOC|54.165.17.209|high|
|kyle-mbp-work|Bad IP access|2019-03-05 20:07:04.000|Bad IP address|87.147.254.215|high|
|kyle-mbp-work|Compliance|2019-03-05 20:06:47.000|Outbound Network Connection to threat intel IOC|87.147.254.215|high|


### uptycs-get-process-open-sockets
---
find processes which opened a socket
##### Base Command

`uptycs-get-process-open-sockets`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| ip | IP address which process opened a socket to.  This argument should be in double quotes. | Optional | 
| time | Exact time at which the socket was opened.  This argument should be in double quotes. | Optional | 
| host_name_is | Only return assets with this hostname.  This argument should be in double quotes.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| host_name_like | Only return assets with this string in the hostname.  This argument should be in double quotes.  Use this to find a selection of assets with similar hostnames.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| time_ago | Specifies how far back you want to look.  Format examples: 2 hours, 4 minutes, 6 month, 1 day, etc. | Optional | 
| start_window | Beginning of window to search for open sockets.  Format is "YYYY-MM-DD HH:MM:SS.000", for example, March 15, 2019 at 1:52:36 am would be written as "2019-03-15 01:52:36.000".  This argument should be in double quotes. | Optional | 
| end_window | End of window to search for open sockets.  Format is "YYYY-MM-DD HH:MM:SS.000", for example, March 15, 2019 at 1:52:36 am would be written as "2019-03-15 01:52:36.000".  This argument should be in double quotes. | Optional | 
| asset_id | Only return assets with this asset id.  This argument should be in double quotes.  Do not use arguments "asset_id", "host_name_is" or "host_name_like" at the same time. | Optional | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.Sockets.pid | number | pid of process which opened a connection to a specified IP | 
| Uptycs.Sockets.upt_hostname | string | hostname of the asset which ran the specified process | 
| Uptycs.Sockets.upt_time | date | time at which the connection was opened | 
| Uptycs.Sockets.path | string | file path to the process being run | 
| Uptycs.Sockets.local_address | string | local IP for specified connection | 
| Uptycs.Sockets.remote_address | string | remote IP for specified connection | 
| Uptycs.Sockets.local_port | number | local port for specified connection | 
| Uptycs.Sockets.remote_port | number | remote port for specified connection | 
| Uptycs.Sockets.upt_asset_id | string | asset id for asset which ran the specified process | 
| Uptycs.Sockets.parent | unknown | pid for the parent process which spawned the process which opened the connection | 


##### Command Example
`uptycs-get-process-open-sockets limit=1`

##### Context Example
```
{
    "Uptycs.Sockets": [
        {
            "upt_counter": 1584, 
            "protocol": 17, 
            "socket": 9007199254740991, 
            "family": 2, 
            "local_port": 61207, 
            "upt_hash": "a949059d-542e-5d7e-8fc3-3ec1783f7d53", 
            "upt_epoch": 0, 
            "remote_port": 0, 
            "pid": 375, 
            "remote_address": "0.0.0.0", 
            "upt_asset_id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "upt_time": "2019-03-06 15:45:40.000", 
            "state": "", 
            "upt_hostname": "kyle-mbp-work", 
            "fd": 74, 
            "path": "", 
            "local_address": "192.168.86.48", 
            "upt_added": false, 
            "net_namespace": null, 
            "upt_day": 20190306
        }
    ]
}
```

##### Human Readable Output
### PID for process with open connection
|upt_hostname|pid|local_address|remote_address|upt_time|local_port|remote_port|socket|
|---|---|---|---|---|---|---|---|
|kyle-mbp-work|375|192.168.86.48|0.0.0.0|2019-03-06 15:45:40.000|61207|0|9007199254740991|


### uptycs-get-process-information
---
get information for a particular process
##### Base Command

`uptycs-get-process-information`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| pid | pid for the process. | Required | 
| host_name_is | Hostname for asset which spawned the specified process.  This argument should be in double quotes. | Optional | 
| time | Time that the specified process was spawned.  This argument should be in double quotes. | Required | 
| asset_id | Only return assets with this asset id.  This argument should be in double quotes.  Do not use arguments "asset_id" and "host_name_is" at the same time. | Optional | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.Proc.pid | number | pid for the process | 
| Uptycs.Proc.upt_hostname | string | hostname for asset which spawned the specified process | 
| Uptycs.Proc.upt_asset_id | string | asset id for asset which spawned the specified process | 
| Uptycs.Proc.parent | number | pid for the parent process | 
| Uptycs.Proc.upt_add_time | date | time that the process was spawned | 
| Uptycs.Proc.upt_remove_time | date | time that the process was removed | 


##### Command Example
`uptycs-get-process-information asset_id="984d4a7a-9f3a-580a-a3ef-2841a561669b" pid=5119 time="2019-01-29 17:05:07.000"`

##### Context Example
```
{
    "Uptycs.Proc": [
        {
            "name": "VBoxHeadless", 
            "parent": 484, 
            "upt_add_time": "2019-01-29 16:14:27.000", 
            "pid": 5119, 
            "upt_remove_time": "2019-01-29 19:21:31.000 UTC", 
            "upt_asset_id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "cmdline": "/Applications/VirtualBox.app/Contents/MacOS/VBoxHeadless --comment vagrant_default_1535385658307_92120 --startvm 11742093-a8fa-4189-a88c-afc4cb7c70a6 --vrde config", 
            "upt_hostname": "kyle-mbp-work", 
            "pgroup": 5119, 
            "path": "/Applications/VirtualBox.app/Contents/MacOS/VBoxHeadless", 
            "temp_remove_time": "2019-01-29 19:21:31.000", 
            "cwd": "/Applications"
        }
    ]
}
```

##### Human Readable Output
### Process information
|upt_hostname|parent|pid|name|path|cmdline|
|---|---|---|---|---|---|
|kyle-mbp-work|484|5119|VBoxHeadless|/Applications/VirtualBox.app/Contents/MacOS/VBoxHeadless|/Applications/VirtualBox.app/Contents/MacOS/VBoxHeadless --comment vagrant_default_1535385658307_92120 --startvm 11742093-a8fa-4189-a88c-afc4cb7c70a6 --vrde config|


### uptycs-get-process-child-processes
---
get all the child processes for a given pid
##### Base Command

`uptycs-get-process-child-processes`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| parent | The pid for which all child processes will be found | Required | 
| host_name_is | hostname for the asset which executed these processes.  This argument should be in double quotes. | Optional | 
| limit | Limit the number of entries returned. | Required | 
| asset_id | Only return assets with this asset_id.  This argument should be in double quotes.  Do not use arguments "asset_id" and "host_name_is" at the same time. | Optional | 
| parent_start_time | time at which the parent process was spawned | Optional | 
| parent_end_time | time at which the parent process was killed, if it exists. | Optional | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.Children.pid | number | pid of a daughter process | 
| Uptycs.Children.upt_asset_id | string | asset id for asset which this process was run on | 
| Uptycs.Children.upt_hostname | unknown | hostname for asset which spawned the specified process | 
| Uptycs.Children.upt_add_time | unknown | time that the process was spawned | 
| Uptycs.Children.upt_remove_time | unknown | time that the process was removed | 


##### Command Example
`uptycs-get-process-child-processes asset_id="984d4a7a-9f3a-580a-a3ef-2841a561669b" parent=484 parent_start_time="2019-01-28 14:16:58.000" parent_end_time="2019-01-29 19:21:31.000"`

##### Context Example
```
{
    "Uptycs.Children": [
        {
            "name": "VBoxHeadless", 
            "parent": 484, 
            "upt_add_time": "2019-01-29 16:14:27.000", 
            "pid": 5119, 
            "upt_remove_time": "2019-01-29 19:21:31.000 UTC", 
            "upt_asset_id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "cmdline": "/Applications/VirtualBox.app/Contents/MacOS/VBoxHeadless --comment vagrant_default_1535385658307_92120 --startvm 11742093-a8fa-4189-a88c-afc4cb7c70a6 --vrde config", 
            "upt_hostname": "kyle-mbp-work", 
            "pgroup": 5119, 
            "path": "/Applications/VirtualBox.app/Contents/MacOS/VBoxHeadless", 
            "temp_remove_time": "2019-01-29 19:21:31.000", 
            "cwd": "/Applications"
        }, 
        {
            "name": "VirtualBoxVM", 
            "parent": 484, 
            "upt_add_time": "2019-01-29 16:00:17.000", 
            "pid": 5008, 
            "upt_remove_time": "2019-01-29 16:13:55.000 UTC", 
            "upt_asset_id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "cmdline": "/Applications/VirtualBox.app/Contents/Resources/VirtualBoxVM.app/Contents/MacOS/VirtualBoxVM --comment vagrant_default_1535385658307_92120 --startvm 11742093-a8fa-4189-a88c-afc4cb7c70a6 --no-startvm-errormsgbox", 
            "upt_hostname": "kyle-mbp-work", 
            "pgroup": 5008, 
            "path": "/Applications/VirtualBox.app/Contents/MacOS/VirtualBoxVM", 
            "temp_remove_time": "2019-01-29 16:13:55.000", 
            "cwd": "/Applications"
        }, 
        {
            "name": "VirtualBoxVM", 
            "parent": 484, 
            "upt_add_time": "2019-01-29 15:58:10.000", 
            "pid": 5002, 
            "upt_remove_time": "2019-01-29 16:00:17.000 UTC", 
            "upt_asset_id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "cmdline": "/Applications/VirtualBox.app/Contents/Resources/VirtualBoxVM.app/Contents/MacOS/VirtualBoxVM --comment basevm_centos_7_orig --startvm 58264539-0e7a-418f-91be-365aa0f20854 --no-startvm-errormsgbox", 
            "upt_hostname": "kyle-mbp-work", 
            "pgroup": 5002, 
            "path": "/Applications/VirtualBox.app/Contents/MacOS/VirtualBoxVM", 
            "temp_remove_time": "2019-01-29 16:00:17.000", 
            "cwd": "/Applications"
        }, 
        {
            "name": "VirtualBoxVM", 
            "parent": 484, 
            "upt_add_time": "2019-01-29 15:55:32.000", 
            "pid": 4994, 
            "upt_remove_time": "2019-01-29 15:57:38.000 UTC", 
            "upt_asset_id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "cmdline": "/Applications/VirtualBox.app/Contents/Resources/VirtualBoxVM.app/Contents/MacOS/VirtualBoxVM --comment vagrant_default_1535385658307_92120 --startvm 11742093-a8fa-4189-a88c-afc4cb7c70a6 --no-startvm-errormsgbox", 
            "upt_hostname": "kyle-mbp-work", 
            "pgroup": 4994, 
            "path": "/Applications/VirtualBox.app/Contents/MacOS/VirtualBoxVM", 
            "temp_remove_time": "2019-01-29 15:57:38.000", 
            "cwd": "/Applications"
        }, 
        {
            "name": "VirtualBoxVM", 
            "parent": 484, 
            "upt_add_time": "2019-01-28 17:00:39.000", 
            "pid": 3448, 
            "upt_remove_time": "2019-01-28 22:27:17.000 UTC", 
            "upt_asset_id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "cmdline": "/Applications/VirtualBox.app/Contents/Resources/VirtualBoxVM.app/Contents/MacOS/VirtualBoxVM --comment ova-31822- --startvm d7414d11-5764-4583-aeb6-94e5527c851c --no-startvm-errormsgbox", 
            "upt_hostname": "kyle-mbp-work", 
            "pgroup": 3448, 
            "path": "/Applications/VirtualBox.app/Contents/MacOS/VirtualBoxVM", 
            "temp_remove_time": "2019-01-28 22:27:17.000", 
            "cwd": "/Applications"
        }
    ]
}
```

##### Human Readable Output
### PIDs for child processes of a specified pid
|upt_hostname|pid|name|path|cmdline|upt_add_time|
|---|---|---|---|---|---|
|kyle-mbp-work|5119|VBoxHeadless|/Applications/VirtualBox.app/Contents/MacOS/VBoxHeadless|/Applications/VirtualBox.app/Contents/MacOS/VBoxHeadless --comment vagrant_default_1535385658307_92120 --startvm 11742093-a8fa-4189-a88c-afc4cb7c70a6 --vrde config|2019-01-29 16:14:27.000|
|kyle-mbp-work|5008|VirtualBoxVM|/Applications/VirtualBox.app/Contents/MacOS/VirtualBoxVM|/Applications/VirtualBox.app/Contents/Resources/VirtualBoxVM.app/Contents/MacOS/VirtualBoxVM --comment vagrant_default_1535385658307_92120 --startvm 11742093-a8fa-4189-a88c-afc4cb7c70a6 --no-startvm-errormsgbox|2019-01-29 16:00:17.000|
|kyle-mbp-work|5002|VirtualBoxVM|/Applications/VirtualBox.app/Contents/MacOS/VirtualBoxVM|/Applications/VirtualBox.app/Contents/Resources/VirtualBoxVM.app/Contents/MacOS/VirtualBoxVM --comment basevm_centos_7_orig --startvm 58264539-0e7a-418f-91be-365aa0f20854 --no-startvm-errormsgbox|2019-01-29 15:58:10.000|
|kyle-mbp-work|4994|VirtualBoxVM|/Applications/VirtualBox.app/Contents/MacOS/VirtualBoxVM|/Applications/VirtualBox.app/Contents/Resources/VirtualBoxVM.app/Contents/MacOS/VirtualBoxVM --comment vagrant_default_1535385658307_92120 --startvm 11742093-a8fa-4189-a88c-afc4cb7c70a6 --no-startvm-errormsgbox|2019-01-29 15:55:32.000|
|kyle-mbp-work|3448|VirtualBoxVM|/Applications/VirtualBox.app/Contents/MacOS/VirtualBoxVM|/Applications/VirtualBox.app/Contents/Resources/VirtualBoxVM.app/Contents/MacOS/VirtualBoxVM --comment ova-31822- --startvm d7414d11-5764-4583-aeb6-94e5527c851c --no-startvm-errormsgbox|2019-01-28 17:00:39.000|


### uptycs-get-processes
---
find processes which are running or have run on a registered Uptycs assert
##### Base Command

`uptycs-get-processes`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| time | Exact time at which the process was spawned.  This argument should be in double quotes. | Optional | 
| host_name_is | Only return assets with this hostname.  This argument should be in double quotes.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| host_name_like | Only return assets with this string in the hostname.  This argument should be in double quotes.  Use this to find a selection of assets with similar hostnames.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| time_ago | Specifies how far back you want to look.  Format examples: 2 hours, 4 minutes, 6 month, 1 day, etc. | Optional | 
| start_window | Beginning of window to search for open connections.  Format is "YYYY-MM-DD HH:MM:SS.000", for example, March 15, 2019 at 1:52:36 am would be written as "2019-03-15 01:52:36.000".  This argument should be in double quotes. | Optional | 
| end_window | End of window to search for open connections.  Format is "YYYY-MM-DD HH:MM:SS.000", for example, March 15, 2019 at 1:52:36 am would be written as "2019-03-15 01:52:36.000".  This argument should be in double quotes. | Optional | 
| asset_id | Only return assets with this asset id.  This argument should be in double quotes.  Do not use arguments "asset_id", "host_name_is" or "host_name_like" at the same time. | Optional | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.Process.pid | number | pid for a particular process | 
| Uptycs.Process.parent | number | pid for the parent of a particular process | 
| Uptycs.Process.upt_asset_id | string | uptycs asset id for the asset which is running (or ran) the process | 
| Uptycs.Process.upt_hostname | string | host name for the asset which is running (or ran) the process | 
| Uptycs.Process.upt_time | unknown | time at which the process was spawned | 


##### Command Example
`uptycs-get-processes limit=1`

##### Context Example
```
{
    "Uptycs.Process": [
        {
            "uid": 501, 
            "upt_counter": 1763, 
            "pid": 2375, 
            "upt_epoch": 0, 
            "upt_asset_id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "resident_size": null, 
            "upt_hostname": "kyle-mbp-work", 
            "sgid": 20, 
            "suid": 501, 
            "total_size": null, 
            "upt_hash": "2010e1dc-1c9e-5f80-b66b-fa10a292bba4", 
            "euid": 501, 
            "state": null, 
            "gid": 20, 
            "upt_time": "2019-03-06 15:46:40.000", 
            "upt_added": false, 
            "cwd": "/private/tmp", 
            "user_time": null, 
            "nice": 0, 
            "parent": 1, 
            "cgroup_namespace": "", 
            "start_time": null, 
            "uts_namespace": "", 
            "threads": null, 
            "mnt_namespace": "", 
            "pgroup": 2375, 
            "path": "/System/Library/Frameworks/QuickLook.framework/Versions/A/Resources/quicklookd.app/Contents/MacOS/quicklookd", 
            "user_namespace": "", 
            "upt_day": 20190306, 
            "system_time": null, 
            "name": "quicklookd", 
            "cmdline": "/System/Library/Frameworks/QuickLook.framework/Resources/quicklookd.app/Contents/MacOS/quicklookd", 
            "net_namespace": "", 
            "pid_namespace": "", 
            "disk_bytes_written": null, 
            "is_elevated_token": 0, 
            "egid": 20, 
            "wired_size": null, 
            "ipc_namespace": "", 
            "root": "", 
            "on_disk": 1, 
            "disk_bytes_read": null
        }
    ]
}
```

##### Human Readable Output
### Processes
|upt_hostname|pid|name|path|upt_time|parent|cmdline|
|---|---|---|---|---|---|---|
|kyle-mbp-work|2375|quicklookd|/System/Library/Frameworks/QuickLook.framework/Versions/A/Resources/quicklookd.app/Contents/MacOS/quicklookd|2019-03-06 15:46:40.000|1|/System/Library/Frameworks/QuickLook.framework/Resources/quicklookd.app/Contents/MacOS/quicklookd|


### uptycs-get-process-open-files
---
find processes which have opened files
##### Base Command

`uptycs-get-process-open-files`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| time | Exact time at which the process was spawned.  This argument should be in double quotes. | Optional | 
| host_name_is | Only return assets with this hostname.  This argument should be in double quotes.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| host_name_like | Only return assets with this string in the hostname.  This argument should be in double quotes.  Use this to find a selection of assets with similar hostnames.  Do not use arguments "host_name_is" and "host_name_like" at the same time. | Optional | 
| time_ago | Specifies how far back you want to look.  Format examples: 2 hours, 4 minutes, 6 month, 1 day, etc. | Optional | 
| start_window | Beginning of window to search for open connections.  Format is "YYYY-MM-DD HH:MM:SS.000", for example, March 15, 2019 at 1:52:36 am would be written as "2019-03-15 01:52:36.000".  This argument should be in double quotes. | Optional | 
| end_window | End of window to search for open connections.  Format is "YYYY-MM-DD HH:MM:SS.000", for example, March 15, 2019 at 1:52:36 am would be written as "2019-03-15 01:52:36.000".  This argument should be in double quotes. | Optional | 
| asset_id | Only return assets with this asset id.  This argument should be in double quotes.  Do not use arguments "asset_id", "host_name_is" or "host_name_like" at the same time. | Optional | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.Files.pid | number | pid for the process which opened a file | 
| Uptycs.Files.fd | number | process specific file descriptor number | 
| Uptycs.Files.upt_asset_id | string | Uptycs asset id for the the asset on which the file was opened | 
| Uptycs.Files.upt_hostname | string | Host name for the asset on which the file was opened | 
| Uptycs.Files.upt_time | date | time at which the file was opened | 


##### Command Example
`uptycs-get-process-open-files limit=1`

##### Context Example
```
{
    "Uptycs.Files": [
        {
            "path": "/var/osquery/osquery.db/058345.sst", 
            "pid": 9, 
            "upt_hostname": "uptycs-osquery-vmfk7", 
            "fd": 23, 
            "upt_time": "2019-03-06 15:46:54.000"
        }
    ]
}
```

##### Human Readable Output
### PID for process which has opened a file
|upt_hostname|pid|path|fd|upt_time|
|---|---|---|---|---|
|uptycs-osquery-vmfk7|9|/var/osquery/osquery.db/058345.sst|23|2019-03-06 15:46:54.000|


### uptycs-set-alert-status
---
Set the status of an alert to new, assigned, resolved, or closed
##### Base Command

`uptycs-set-alert-status`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| id | Uptycs alert id used to identify a particular alert | Required | 
| status | Status of the alert can be new, assigned, resolved, or closed | Required | 


##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-set-alert-status alert_id="9cb18abd-2c9a-43a8-988a-0601e9140f6c" status=assigned`

##### Context Example
```
{
    "Uptycs.AlertStatus": {
        "status": "assigned", 
        "code": "OUTBOUND_CONNECTION_TO_THREAT_IOC", 
        "updatedAt": "2019-03-06T15:48:08.196Z", 
        "updatedByEmail": "bschmoll@uptycs.com", 
        "updatedByAdmin": true, 
        "updatedBy": "B schmoll", 
        "id": "9cb18abd-2c9a-43a8-988a-0601e9140f6c", 
        "createdAt": "2019-02-22T21:13:21.238Z"
    }
}
```

##### Human Readable Output
### Uptycs Alert Status
|id|code|status|createdAt|updatedAt|
|---|---|---|---|---|
|9cb18abd-2c9a-43a8-988a-0601e9140f6c|OUTBOUND_CONNECTION_TO_THREAT_IOC|assigned|2019-02-22T21:13:21.238Z|2019-03-06T15:48:08.196Z|


### uptycs-set-asset-tag
---
Sets a tag on a particular asset
##### Base Command

`uptycs-set-asset-tag`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| asset_id | Uptycs asset id for the asset that the tag should be set on | Required | 
| tag | Tag that will be set on the asset | Required | 


##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-set-asset-tag asset_id="984d4a7a-9f3a-580a-a3ef-2841a561669b" tag_key="owner" tag_value="Uptycs office"`

##### Context Example
```
{
    "Uptycs.AssetTags": {
        "hostName": "kyle-mbp-work", 
        "tags": [
            "network=low", 
            "Uptycs=work laptop", 
            "owner=Uptycs office", 
            "cpu=unknown", 
            "memory=unknown", 
            "disk=high"
        ]
    }
}
```

##### Human Readable Output
### Uptycs Asset Tag
|hostName|tags|
|---|---|
|kyle-mbp-work|network=low,<br>Uptycs=work laptop,<br>owner=Uptycs office,<br>cpu=unknown,<br>memory=unknown,<br>disk=high|


### uptycs-get-user-information
---
get info for an Uptycs user
##### Base Command

`uptycs-get-user-information`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| user_id | Unique Uptycs id for the user | Required | 


##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-get-user-information user_id="33436e24-f30f-42d0-8438-d948be12b5af"`

##### Context Example
```
{
    "Uptycs.UserInfo": {
        "userObjectGroups": [
            {
                "userId": "33436e24-f30f-42d0-8438-d948be12b5af", 
                "updatedBy": null, 
                "objectGroupId": "106eef5e-c3a6-44eb-bb3d-1a2087cded3d", 
                "customerId": "e8213ef3-ef92-460e-a542-46dccd700c16", 
                "object_group_id": "106eef5e-c3a6-44eb-bb3d-1a2087cded3d", 
                "createdBy": null, 
                "updatedAt": "2018-09-24T17:24:45.606Z", 
                "id": "e10d6fbb-366c-4b89-86b3-89a1cd4ee83c", 
                "createdAt": "2018-09-24T17:24:45.606Z"
            }
        ], 
        "userRoles": {
            "admin": {
                "description": "Default admin role", 
                "updatedBy": null, 
                "custom": false, 
                "createdBy": null, 
                "updatedAt": "2019-02-21T17:20:13.070Z", 
                "id": "01b8ce5d-c93a-41a6-ba63-2e26c7d2cd79", 
                "hidden": false, 
                "permissions": [
                    "ALERT:READ", 
                    "ALERT_RULE:READ", 
                    "ASSET:READ", 
                    "CUSTOMER:READ", 
                    "DESTINATION:READ", 
                    "EVENT:READ", 
                    "EVENT_RULE:READ", 
                    "EXCEPTION:READ", 
                    "FIM:READ", 
                    "FLAG:READ", 
                    "OBJECT_GROUP:READ", 
                    "PROFILE:READ", 
                    "PROMETHEUS_TARGET:READ", 
                    "QUERY:READ", 
                    "QUERY_PACK:READ", 
                    "REPORT:READ", 
                    "REPORT_RUN:READ", 
                    "SCHEMA:READ", 
                    "SCHEDULED_GROUP:READ", 
                    "SCHEDULED_QUERY:READ", 
                    "SNAPSHOT:READ", 
                    "TAG:READ", 
                    "TAG_RULE:READ", 
                    "TEMPLATE:READ", 
                    "THREAT:READ", 
                    "USER:READ", 
                    "USER_ROLE:READ", 
                    "CURRENT_USER:UPDATE", 
                    "CUSTOMER:QUERY", 
                    "ASSET:QUERY", 
                    "OSQUERY:DOWNLOAD", 
                    "OSQUERY:READ", 
                    "FEATURE_SET:READ", 
                    "DASHBOARD:READ", 
                    "CURRENT_USER_PREFERENCE:READ", 
                    "CURRENT_USER_PREFERENCE:CREATE", 
                    "CURRENT_USER_PREFERENCE:UPDATE", 
                    "CURRENT_USER_PREFERENCE:DELETE", 
                    "CURRENT_USER_REPORT_SCHEDULE:CREATE", 
                    "CURRENT_USER_REPORT_SCHEDULE:READ", 
                    "CURRENT_USER_REPORT_SCHEDULE:UPDATE", 
                    "CURRENT_USER_REPORT_SCHEDULE:DELETE", 
                    "COMPLIANCE_FAILURE:READ", 
                    "COMPLIANCE_FAILURE:UPDATE", 
                    "CUSTOM_PROFILE:READ", 
                    "QUERY_JOB:CREATE", 
                    "QUERY_JOB:READ", 
                    "QUERY_JOB:UPDATE", 
                    "QUERY_JOB:DELETE", 
                    "EVENT_EXCLUDE_PROFILE:READ", 
                    "ATC_QUERY:READ", 
                    "ALERT:CREATE", 
                    "ALERT:UPDATE", 
                    "ALERT:DELETE", 
                    "ALERT_RULE:CREATE", 
                    "ALERT_RULE:UPDATE", 
                    "ALERT_RULE:DELETE", 
                    "API_KEY:CREATE", 
                    "API_KEY:READ", 
                    "API_KEY:UPDATE", 
                    "API_KEY:DELETE", 
                    "ASSET:UPDATE", 
                    "ASSET:DELETE", 
                    "ASSET_GROUP_RULE:CREATE", 
                    "ASSET_GROUP_RULE:READ", 
                    "ASSET_GROUP_RULE:UPDATE", 
                    "ASSET_GROUP_RULE:DELETE", 
                    "CUSTOMER:UPDATE", 
                    "DESTINATION:CREATE", 
                    "DESTINATION:UPDATE", 
                    "DESTINATION:DELETE", 
                    "EVENT:CREATE", 
                    "EVENT:UPDATE", 
                    "EVENT:DELETE", 
                    "EVENT_RULE:CREATE", 
                    "EVENT_RULE:UPDATE", 
                    "EVENT_RULE:DELETE", 
                    "EXCEPTION:CREATE", 
                    "EXCEPTION:UPDATE", 
                    "EXCEPTION:DELETE", 
                    "FIM:CREATE", 
                    "FIM:UPDATE", 
                    "FIM:DELETE", 
                    "FLAG:CREATE", 
                    "FLAG:UPDATE", 
                    "FLAG:DELETE", 
                    "OBJECT_GROUP:CREATE", 
                    "OBJECT_GROUP:UPDATE", 
                    "OBJECT_GROUP:DELETE", 
                    "PROMETHEUS_TARGET:CREATE", 
                    "PROMETHEUS_TARGET:UPDATE", 
                    "PROMETHEUS_TARGET:DELETE", 
                    "QUERY:CREATE", 
                    "QUERY:UPDATE", 
                    "QUERY:DELETE", 
                    "QUERY_PACK:CREATE", 
                    "QUERY_PACK:UPDATE", 
                    "QUERY_PACK:DELETE", 
                    "REPORT:CREATE", 
                    "REPORT:UPDATE", 
                    "REPORT:DELETE", 
                    "REPORT_RUN:CREATE", 
                    "REPORT_RUN:UPDATE", 
                    "REPORT_RUN:DELETE", 
                    "SCHEDULED_GROUP:UPDATE", 
                    "SCHEDULED_GROUP:DELETE", 
                    "SCHEDULED_QUERY:CREATE", 
                    "SCHEDULED_QUERY:UPDATE", 
                    "SCHEDULED_QUERY:DELETE", 
                    "SNAPSHOT:CREATE", 
                    "SNAPSHOT:UPDATE", 
                    "SNAPSHOT:DELETE", 
                    "TAG:CREATE", 
                    "TAG:UPDATE", 
                    "TAG:DELETE", 
                    "TAG_RULE:CREATE", 
                    "TAG_RULE:UPDATE", 
                    "TAG_RULE:DELETE", 
                    "TEMPLATE:CREATE", 
                    "TEMPLATE:UPDATE", 
                    "TEMPLATE:DELETE", 
                    "THREAT:CREATE", 
                    "THREAT:UPDATE", 
                    "THREAT:DELETE", 
                    "USER:CREATE", 
                    "USER:UPDATE", 
                    "USER:DELETE", 
                    "USER_ROLE:CREATE", 
                    "USER_ROLE:UPDATE", 
                    "USER_ROLE:DELETE", 
                    "CURRENT_USER:READ", 
                    "CURRENT_USER:UPDATE", 
                    "CUSTOMER_FEATURE_SET:UPDATE", 
                    "USER_PREFERENCE:CREATE", 
                    "USER_PREFERENCE:READ", 
                    "USER_PREFERENCE:UPDATE", 
                    "USER_PREFERENCE:DELETE", 
                    "REPORT_SCHEDULE:CREATE", 
                    "REPORT_SCHEDULE:READ", 
                    "REPORT_SCHEDULE:UPDATE", 
                    "REPORT_SCHEDULE:DELETE", 
                    "AUDIT_LOGS:READ", 
                    "CUSTOM_PROFILE:CREATE", 
                    "CUSTOM_PROFILE:UPDATE", 
                    "CUSTOM_PROFILE:DELETE", 
                    "EVENT_EXCLUDE_PROFILE:CREATE", 
                    "EVENT_EXCLUDE_PROFILE:UPDATE", 
                    "EVENT_EXCLUDE_PROFILE:DELETE", 
                    "ATC_QUERY:CREATE", 
                    "ATC_QUERY:UPDATE", 
                    "ATC_QUERY:DELETE"
                ], 
                "customerId": "e8213ef3-ef92-460e-a542-46dccd700c16", 
                "createdAt": "2018-09-24T17:24:41.194Z", 
                "name": "admin"
            }
        }, 
        "email": "bschmoll@uptycs.com", 
        "name": "B schmoll", 
        "id": "33436e24-f30f-42d0-8438-d948be12b5af"
    }
}
```

##### Human Readable Output
### Uptycs User Information
|name|email|id|
|---|---|---|
|B schmoll|bschmoll@uptycs.com|33436e24-f30f-42d0-8438-d948be12b5af|


### uptycs-get-threat-indicators
---
get Uptycs threat indicators
##### Base Command

`uptycs-get-threat-indicators`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| indicator | the specific indicator you wish to search for.  This can be an IP address, a Bad Domain, etc. as well ass any indicators you have added. | Optional | 


##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-get-threat-indicators limit=1`

##### Context Example
```
{
    "Uptycs.ThreatIndicators": [
        {
            "indicator": "54.165.17.209", 
            "description": "malware.com", 
            "threatId": "9528e9a6-b948-4681-b4f3-bffb41ea691b", 
            "indicatorType": "IPv4", 
            "createdAt": "2019-03-06T15:41:38.096Z", 
            "id": "c32c2b71-e364-4846-9e7c-902f903a18db", 
            "isActive": true
        }
    ]
}
```

##### Human Readable Output
### Uptycs Threat Indicators
|id|indicator|description|indicatorType|createdAt|isActive|threatId|
|---|---|---|---|---|---|---|
|c32c2b71-e364-4846-9e7c-902f903a18db|54.165.17.209|malware.com|IPv4|2019-03-06T15:41:38.096Z|true|9528e9a6-b948-4681-b4f3-bffb41ea691b|


### uptycs-get-threat-sources
---
get Uptycs threat sources
##### Base Command

`uptycs-get-threat-sources`
##### Input

There are no input arguments for this command.

##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-get-threat-sources limit=1`

##### Context Example
```
{
    "Uptycs.ThreatSources": [
        {
            "name": "AlienVault Open Threat Exchange Malicious Domains and IPs", 
            "url": "4533da856e43f06ee00bb5f1adf170a0ce5cacaca5992ab1279733c2bdd0a88c", 
            "enabled": true, 
            "custom": false, 
            "lastDownload": "2019-03-06T01:00:06.767Z", 
            "createdAt": "2019-03-03T01:00:47.056Z", 
            "description": "A feed of malicious domains and IP addresses"
        }
    ]
}
```

##### Human Readable Output
### Uptycs Threat Sources
|name|description|url|enabled|custom|createdAt|lastDownload|
|---|---|---|---|---|---|---|
|AlienVault Open Threat Exchange Malicious Domains and IPs|A feed of malicious domains and IP addresses|4533da856e43f06ee00bb5f1adf170a0ce5cacaca5992ab1279733c2bdd0a88c|true|false|2019-03-03T01:00:47.056Z|2019-03-06T01:00:06.767Z|


### uptycs-get-threat-vendors
---
get Uptycs threat vendors
##### Base Command

`uptycs-get-threat-vendors`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| threat_vendor_id | unique Uptycs id which identifies the vendor of this specific threat source | Optional | 


##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-get-threat-vendors `

##### Context Example
```
{
    "Uptycs.ThreatVendors": [
        {
            "name": "Bschmoll Inc.-Threats", 
            "url": null, 
            "updatedAt": "2018-11-20T19:15:05.611Z", 
            "customerId": "e8213ef3-ef92-460e-a542-46dccd700c16", 
            "numThreats": null, 
            "numIocs": null, 
            "lastDownload": null, 
            "id": "42b9220c-7e29-4fd8-9cf7-9f811e851f8e", 
            "createdAt": "2018-11-20T19:15:05.611Z", 
            "description": null
        }
    ]
}
```

##### Human Readable Output
### Uptycs Threat Vendors
|description|url|updatedAt|customerId|numIocs|numThreats|lastDownload|id|createdAt|name|
|---|---|---|---|---|---|---|---|---|---|
|||2018-11-20T19:15:05.611Z|e8213ef3-ef92-460e-a542-46dccd700c16||||42b9220c-7e29-4fd8-9cf7-9f811e851f8e|2018-11-20T19:15:05.611Z|Bschmoll Inc.-Threats|


### uptycs-get-parent-information
---
get the parent process information for a particular child process
##### Base Command

`uptycs-get-parent-information`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| parent | pid for the parent process. | Required | 
| host_name_is | Hostname for asset which spawned the specified process.  This argument should be in double quotes. | Optional | 
| child_add_time | Time that the specified process was spawned.  This argument should be in double quotes. | Required | 
| asset_id | Only return assets with this asset id.  This argument should be in double quotes.  Do not use arguments "asset_id" and "host_name_is" at the same time. | Optional | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.Parent.pid | number | pid of the process (this is the same number as the input argument 'parent') | 
| Uptycs.Parent.upt_hostname | string | hostname for asset which spawned the specified process | 
| Uptycs.Parent.upt_asset_id | string | asset id for asset which spawned the specified process | 
| Uptycs.Parent.parent | number | pid for the parent process (this is the parent of the input argument 'parent') | 
| Uptycs.Parent.upt_add_time | date | time that the process was spawned | 
| Uptycs.Parent.upt_remove_time | date | time that the process was removed | 


##### Command Example
`uptycs-get-parent-information asset_id="984d4a7a-9f3a-580a-a3ef-2841a561669b" child_add_time="2019-01-29 16:14:27.000" parent=484`

##### Context Example
```
{
    "Uptycs.Parent": [
        {
            "name": "VBoxSVC", 
            "parent": 1, 
            "upt_add_time": "2019-01-28 14:16:58.000", 
            "pid": 484, 
            "upt_remove_time": "2019-01-29 19:21:31.000 UTC", 
            "upt_asset_id": "984d4a7a-9f3a-580a-a3ef-2841a561669b", 
            "cmdline": "/Applications/VirtualBox.app/Contents/MacOS/VBoxSVC --auto-shutdown", 
            "upt_hostname": "kyle-mbp-work", 
            "pgroup": 484, 
            "path": "/Applications/VirtualBox.app/Contents/MacOS/VBoxSVC", 
            "temp_remove_time": "2019-01-29 19:21:31.000", 
            "cwd": "/Applications"
        }
    ]
}
```

##### Human Readable Output
### Parent process information
|upt_hostname|parent|pid|name|path|cmdline|
|---|---|---|---|---|---|
|kyle-mbp-work|1|484|VBoxSVC|/Applications/VirtualBox.app/Contents/MacOS/VBoxSVC|/Applications/VirtualBox.app/Contents/MacOS/VBoxSVC --auto-shutdown|


### uptycs-post-threat-source
---
post a new threat source to your threat sources in Uptycs
##### Base Command

`uptycs-post-threat-source`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| name | The name for the threat source | Required | 
| filepath | path to the file containing threat information which will be uploaded | Required | 
| description | A short description for the threat source | Required | 


##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-post-threat-source  name="testThreatSources" description="testing Uptycs API" entry_id="4322@27d41dbb-9676-4408-88bf-51193334caf7" filename="threatSourcesTest.csv"`

##### Context Example
```

```

##### Human Readable Output
Uptycs Posted Threat Source

### uptycs-get-users
---
get a list of Uptycs users
##### Base Command

`uptycs-get-users`
##### Input

There are no input arguments for this command.

##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| id | string | unique Uptycs id for the user | 


##### Command Example
`uptycs-get-users limit=1`

##### Context Example
```
{
    "Uptycs.Users": [
        {
            "name": "B schmoll", 
            "admin": true, 
            "id": "33436e24-f30f-42d0-8438-d948be12b5af", 
            "updatedAt": "2018-09-25T16:10:28.140Z", 
            "active": true, 
            "email": "bschmoll@uptycs.com", 
            "createdAt": "2018-09-24T17:24:38.635Z"
        }
    ]
}
```

##### Human Readable Output
### Uptycs Users
|name|email|id|admin|active|createdAt|updatedAt|
|---|---|---|---|---|---|---|
|B schmoll|bschmoll@uptycs.com|33436e24-f30f-42d0-8438-d948be12b5af|true|true|2018-09-24T17:24:38.635Z|2018-09-25T16:10:28.140Z|


### uptycs-get-asset-groups
---
get Uptycs asset groups
##### Base Command

`uptycs-get-asset-groups`
##### Input

There are no input arguments for this command.

##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.AssetGroups.id | string | unique Uptycs id for a particular object group | 


##### Command Example
`uptycs-get-asset-groups `

##### Context Example
```
{
    "Uptycs.AssetGroups": [
        {
            "name": "assets", 
            "description": "Default asset group", 
            "custom": false, 
            "updatedAt": "2018-09-24T17:24:45.604Z", 
            "id": "106eef5e-c3a6-44eb-bb3d-1a2087cded3d", 
            "createdAt": "2018-09-24T17:24:45.604Z", 
            "objectType": "ASSET"
        }, 
        {
            "name": "enrolling", 
            "description": "Enrolling asset group", 
            "custom": false, 
            "updatedAt": "2018-09-24T17:24:45.601Z", 
            "id": "a73353c1-1b27-4eea-9a7c-d2f946cca030", 
            "createdAt": "2018-09-24T17:24:45.601Z", 
            "objectType": "ASSET"
        }
    ]
}
```

##### Human Readable Output
### Uptycs Users
|id|name|description|objectType|custom|createdAt|updatedAt|
|---|---|---|---|---|---|---|
|106eef5e-c3a6-44eb-bb3d-1a2087cded3d|assets|Default asset group|ASSET|false|2018-09-24T17:24:45.604Z|2018-09-24T17:24:45.604Z|
|a73353c1-1b27-4eea-9a7c-d2f946cca030|enrolling|Enrolling asset group|ASSET|false|2018-09-24T17:24:45.601Z|2018-09-24T17:24:45.601Z|


### uptycs-get-user-asset-groups
---
get a list of users in a particular asset group
##### Base Command

`uptycs-get-user-asset-groups`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| asset_group_id | return a list of users with access to this asset group | Required | 


##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-get-user-asset-groups asset_group_id="106eef5e-c3a6-44eb-bb3d-1a2087cded3d"`

##### Context Example
```
{
    "Uptycs.UserGroups": {
        "B schmoll": {
            "email": "bschmoll@uptycs.com", 
            "id": "33436e24-f30f-42d0-8438-d948be12b5af"
        }, 
        "Milan Shah": {
            "email": "milans100@gmail.com", 
            "id": "89d26aa4-f0a8-48d9-a174-ce5285d9dd60"
        }
    }
}
```

##### Human Readable Output
### Uptycs User Asset Groups
|B schmoll|Milan Shah|
|---|---|
|email: bschmoll@uptycs.com<br>id: 33436e24-f30f-42d0-8438-d948be12b5af|email: milans100@gmail.com<br>id: 89d26aa4-f0a8-48d9-a174-ce5285d9dd60|


### uptycs-get-threat-indicator
---
retrieve information about a specific threat indicator using a unique threat indicator id
##### Base Command

`uptycs-get-threat-indicator`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| indicator_id | unique Uptycs id which identifies a specific threat indicator | Required | 


##### Context Output

| **Path** | **Type** | **Description** |
| --- | --- | --- |
| Uptycs.ThreatIndicator.threat_source_id | string | unique Uptycs id which identifies the source of this specific threat indicator | 
| Uptycs.ThreatIndicator.threat_vendor_id | string | unique Uptycs id which identifies the vendor of this specific threat source | 


##### Command Example
`uptycs-get-threat-indicator indicator_id="0ab619bb-cfe0-4db0-8a31-0a71fcc2a362"`

##### Context Example
```
{
    "Uptycs.ThreatIndicator": {
        "indicator": "92.242.140.21", 
        "description": "nishant.uptycs.io", 
        "threatId": "60e2e9eb-f756-4a4d-a85d-55aa8167d59d", 
        "threat_source_name": "test-bad-ips", 
        "threat_vendor_id": "42b9220c-7e29-4fd8-9cf7-9f811e851f8e", 
        "indicatorType": "IPv4", 
        "threat_source_id": "c67d0821-f2f2-44ee-b3a8-a0bae5b04e55", 
        "id": "0ab619bb-cfe0-4db0-8a31-0a71fcc2a362", 
        "createdAt": "2019-01-10T21:25:49.280Z"
    }
}
```

##### Human Readable Output
### Uptycs Threat Indicator
|id|indicator|description|indicatorType|createdAt|isActive|threatId|
|---|---|---|---|---|---|---|
|0ab619bb-cfe0-4db0-8a31-0a71fcc2a362|92.242.140.21|nishant.uptycs.io|IPv4|2019-01-10T21:25:49.280Z|true|60e2e9eb-f756-4a4d-a85d-55aa8167d59d|


### uptycs-get-threat-source
---
retrieve information about a specific threat source
##### Base Command

`uptycs-get-threat-source`
##### Input

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| threat_source_id | unique Uptycs id for the threat source you wish to retrive | Required | 


##### Context Output

There is no context output for this command.

##### Command Example
`uptycs-get-threat-source threat_source_id="20ee2177-4fdc-4070-a046-945048373dd1"`

##### Context Example
```
{
    "Uptycs.ThreatSources": {
        "name": "Debian Linux vulnerabilities", 
        "url": "https://vulners.com/api/v3/archive/collection/?type=debian", 
        "enabled": true, 
        "custom": false, 
        "lastDownload": null, 
        "createdAt": "2018-09-14T18:43:54.832Z", 
        "description": "Debian Linux vulnerabilities"
    }
}
```

##### Human Readable Output
### Uptycs Threat Sources
|name|description|url|enabled|custom|createdAt|lastDownload|
|---|---|---|---|---|---|---|
|Debian Linux vulnerabilities|Debian Linux vulnerabilities|https://vulners.com/api/v3/archive/collection/?type=debian|true|false|2018-09-14T18:43:54.832Z||


## Additional Information
---

In order to create an instance of the integration, a user API key and secret must be downloaded from the users Uptycs account.  After signing in, navigate to Configuration->Users.  At the bottom left of the screen you will see a window labeled "User API key".  Click download.  The downloaded file will have all the information necessary to create the instance.

## Known Limitations
---

While the Demisto-Uptycs integration provides multiple commands with which to access the Uptycs backend, not all features are supported.  In particular, configuration changes are best made using the Uptycs UI.  Many of the commands have a limit set to reduce the number of rows returned from a query or api call.  The limit can be raised, or turned off, however, this may cause the queries take longer to return and potentially return large numbers of rows.  When writing queries, it can sometimes be easier to test using the Uptycs UI rather than the integration.


##  Kill a process on an endpoint with demisto

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
