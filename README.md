# interviewschedule
Scheduling interviews is a burden in most of the companies. When you want to schedule multiple interviews in a single day, It depends on the availability of the interviewer and candidate. This application help user to register their interview slot and the interviewer can get the available time slots

# API List
create/update/delete interviewer or candidate http://127.0.0.1:8000/api/user
create/update/delete interview slot http://127.0.0.1:8000/api/interview-slots

List spefic interview slots http://127.0.0.1:8000/api/active-slots?interviewer_id=1&candidate_id=2

Create interview slots
Avilable slot choices
10AM-11AM, 11AM-12PM, 12PM-1PM, 1PM-2PM, 2PM-3PM, 3PM-4PM, 4PM-5PM, 5PM-6PM

Date format
Year-Month-Date, ex: 2022-4-4

To get the specific interview slots
1.Pass interviewer_id and candidate_id as query parameters

Sample output
{ "2020-5-6": [ "11AM-12PM", "1PM-2PM" ], "2020-12-02": [ "1PM-2PM" ] }
