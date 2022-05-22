# Assesment Evaluation

Evaluating handwritten assignments of student using various APIs.

Workflow

1. Student submits his handwritten assignment on the portal.
2. The assignment is sent to a S3 buckket for OCR portal for handwritten recognition.
3. The recognized text is then saved in a text file in local storage.
4. The .txt file is then sent to another API for plagarism checking.
5. If the plagarism is below certain threshold, then an evaluation of the assignment is created using ML model and a predefined rubiric.
6. This evaluation is then stored in an SQL database along with other information provided by the student. Eg. Name, Reg No, Email, etc.
