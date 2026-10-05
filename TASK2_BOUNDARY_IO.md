# Task 2: System Boundary, User Persona & Input/Output Mapping

## Smart Automated Attendance System

### 1. System Actors / Users
# an actor is someone who interacts with the data i.e., teacher, student, camera, system etc.

| Actor/User       | Role                                                                   |
| ---------------- | ---------------------------------------------------------------------- |
| Student          | Appears in front of the camera and is identified by the system.        |
| Teacher          | Views attendance records and monitors attendance status.               |
| Administrator    | Manages student records, system settings, and the attendance database. |
| Classroom Camera | Provides live video input to the attendance system.                    |

### 2. System Boundary

| Inside the System            | Outside the System    |
| ---------------------------- | --------------------- |
| Face Detection               | Classroom Camera      |
| Face Recognition             | Students              |
| Attendance Processing        | Teacher               |
| Attendance Database          | Administrator         |
| Attendance Record Management | Classroom Environment |

### 3. System Inputs
# input enters the system i.e., the video recording of the students faces

| Input                | Source           | Description                                        |
| -------------------- | ---------------- | -------------------------------------------------- |
| Live Video Stream    | Classroom Camera | Video frames containing students in the classroom. |
| Student Face Images  | Camera           | Facial information used for recognition.           |
| Student Database     | Administrator    | Registered student information and facial records. |
| System Configuration | Administrator    | Attendance and recognition settings.               |

### 4. System Outputs
# output is what the system produces i.e., the attendacne record of a student

| Output                      | Receiver              | Description                                                 |
| --------------------------- | --------------------- | ----------------------------------------------------------- |
| Recognized Student Identity | Teacher/System        | Identifies the student detected by the system.              |
| Attendance Record           | Database              | Stores the student's attendance status and time.            |
| Attendance Report           | Teacher               | Displays attendance information for students.               |
| System Notification         | Teacher/Administrator | Indicates successful attendance marking or system problems. |

### 5. Operational Constraints
# a limitation of the system i.e., memory usage and camera quality

| Constraint        | Description                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------- |
| Processing Speed  | The system should process video with minimal delay.                                       |
| Memory Usage      | The system should operate within the available memory of the processing device.           |
| Network Bandwidth | Video and attendance data transmission should remain within available network bandwidth.  |
| Camera Quality    | The camera should provide sufficient resolution and lighting for reliable face detection. |
| Data Privacy      | Student facial and attendance data must be protected from unauthorized access.            |
