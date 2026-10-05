# Task 3: Data-Flow Diagram (DFD)

## AI Object Detection and Analytics System

### Level 0 — Context Diagram

The Level 0 DFD represents the complete AI object detection and analytics system as a single process and shows its interaction with external entities.

```mermaid
flowchart LR

    Camera[Camera / Video Source]
    Operator[Security Operator]
    Alert[Alert System]
    Database[(Analytics Database)]

    System((AI Object Detection & Analytics System))

    Camera -->|Raw Video Stream| System
    System -->|Detection Results| Operator
    System -->|Alert Notifications| Alert
    System -->|Analytics Data| Database
```

---

## Level 1 — Detailed Data-Flow Diagram

The Level 1 DFD decomposes the AI object detection and analytics system into its major processing stages.

```mermaid
flowchart LR

    Camera[Camera / Video Source]

    P1[1. Data Ingestion]
    P2[2. Image Preprocessing]
    P3[3. Model Inference]
    P4[4. Post-Processing]
    P5[5. Storage & Alert Management]

    DB[(Analytics Database)]
    Operator[Security Operator]
    Alert[Alert System]

    Camera -->|Raw Video Stream| P1
    P1 -->|Video Frames| P2
    P2 -->|Preprocessed Frames| P3
    P3 -->|Raw Detection Results| P4
    P4 -->|Processed Detection Results| P5

    P5 -->|Analytics Data| DB
    P5 -->|Detection Results| Operator
    P5 -->|Alert Notifications| Alert
```

### Data Flow Description

| Data Flow                   | Description                                                     |
| --------------------------- | --------------------------------------------------------------- |
| Raw Video           | Video received.                 |
| Video Frames                | Individual frames extracted     |
| Preprocessed Frames         | Frames prepared for model inference.                         |
| Detection Results       | Objects detected by the model.                               |
| Processed Detection Results | Filtered, organized detection results.                       |
| Analytics Data              | Detection information stored                |
| Alert Notifications         | Notifications generated during alerts |
