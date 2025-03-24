# TRE-Backend

---

### Key Endpoints
1. **Fetch Course Details**
   - **URL**: `/api/course_details`
   - **Method**: `GET`
   - **Description**: Retrieves a list of all courses along with their subjects, exam patterns, and related content.
2. **Get a PDF File**
   - **URL**: `/api/get_pdf`
   - **Method**: `POST`
   - **Description**: Downloads a PDF file based on the provided `pdf_link`. 
3. **Fetch Course PYQs**
   - **URL**: `/api/course_pyqs`
   - **Method**: `GET`
   - **Description**: Fetches available previous year question papers (PYQs) for all courses.
4. **Get a PYQ File**
   - **URL**: `/api/get_pyq`
   - **Method**: `POST`
   - **Description**: Retrieves a specific previous year question paper (PYQ) based on the provided `pdf_link`.

---

## Example Usage

### Fetch Course Details
**Endpoint**: `GET /api/course_details`

**Response**:
```json
[
    {
        "id": 1,
        "title": "BPSC TRE",
        "description": "BPSC Bihar Computer Science Teacher Syllabus 2023 is released by Education Department of Bihar. Candidates must access the BPSC Bihar Computer Science Teacher Syllabus from the article below.",
        "banner": "/media/banners/compsci.jpg",
        "subjects": [
            {
                "id": 1,
                "title": "PGT(11-12)",
                "description": "The Bihar Computer Science Teacher Recruitment 2023 is conducted by the Education Department of Bihar. The candidates must refer to the following table for more information on the Bihar Computer Science Teacher Syllabus.",
                "pdf_link": "/media/pdfs/data.pdf",
                "exam_patterns": [
                    {
                        "topics": "TreesLanguage (Qualifying)",
                        "sub_topics": ["Part - 1 English", " Part - 2 Hindi / Urdu / Bengali"],
                        "total_questions": [25, 75],
                        "total_marks": [25, 75],
                        "duration": 2
                    }
                ],
                "subject_contents": [
                    {
                        "title": "Bihar Computer Science Teacher Syllabus PDF.",
                        "description": "The direct link to download Bihar Computer Science Teacher Syllabus Pdf has been given below. Candidate can download through the below link Bihar CS Teacher Syllabus PDF section wise.",
                        "reference_links": ["https://example.com/trees"]
                    }
                ]
            }
        ]
    }
]
```

### Get a PDF File
**Endpoint**: `POST /api/get_pdf`

**Payload**:
```json
{
    "pdf_link": "/media/pdfs/sample.pdf"
}
```

**Response**: 
Returns the requested PDF file if found else returns an error.
```json
{
    "error": "File not found"
}
```

### Fetch Course PYQs
**Endpoint**: `GET /api/course_pyqs`

**Response**:
```json
{
    "BPSC TRE": [
        "/media/pyqs/PDF_to_Teach.pdf",
        "/media/pyqs/PDF_to_Teach.pdf"
    ],
    "BIHAR STET":[
        "/media/pyqs/PDF_to_Teach.pdf"
    ]
}
```

### Get a PYQ File
**Endpoint**: `POST /api/get_pyq`

**Payload**:
```json
{
    "pdf_link": "/media/pyqs/sample_pyq.pdf"
}
```

**Response**: Returns the requested PDF file if found else returns an error.
```json
{
    "error": "File not found"
}
```
