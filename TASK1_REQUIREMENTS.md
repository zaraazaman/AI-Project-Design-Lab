# Task 1: Functional & Non-Functional Requirements

## Smart Automated Attendance System

### Functional Requirements

| ID    | Functional Requirement                                                     |
| ----- | -------------------------------------------------------------------------- |
| FR-01 | The system shall capture video from the classroom camera.                  |
| FR-02 | The system shall detect and recognize students' faces from the video.      |
| FR-03 | The system shall automatically mark attendance for recognized students.    |
| FR-04 | The system shall store attendance records in a database.                   |
| FR-05 | The system shall synchronize attendance records with the central database. |

### Non-Functional Requirements

| ID     | Non-Functional Requirement                                                                        |
| ------ | ------------------------------------------------------------------------------------------------- |
| NFR-01 | The system shall recognize students with at least 95% accuracy under normal classroom conditions. |
| NFR-02 | Face detection should be completed within 1 second of receiving a video frame.                    |
| NFR-03 | The system should process at least 15 frames per second.                                          |
| NFR-04 | Student attendance and facial data shall be protected from unauthorized access.                   |
| NFR-05 | The system should minimize power and memory usage on the edge device.                             |