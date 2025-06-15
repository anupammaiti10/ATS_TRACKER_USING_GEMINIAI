# ATS Tracker Using GeminiAI

This project leverages the Gemini AI API to calculate ATS (Applicant Tracking System) scores for resumes, helping job seekers optimize their applications and recruiters streamline the screening process. The tool is built with Python and uses Gemini AI’s powerful language capabilities to compare resumes against job descriptions and provide actionable feedback.

## Features

- Analyze resumes and job descriptions for ATS compatibility.
- Get a detailed ATS score indicating how well a resume matches a job listing.
- Highlight missing keywords and suggest improvements.
- Simple command-line interface for ease of use.
- Built on Python using Gemini AI’s API.

## Requirements

- Python 3.7+
- Gemini AI API key (get one from [Gemini AI](https://ai.google.dev/))
- Required Python packages (see [Installation](#installation))

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/anupammaiti10/ATS_TRACKER_USING_GEMINIAI.git
   cd ATS_TRACKER_USING_GEMINIAI
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your Gemini AI API key:**
   - Obtain your API key from [Gemini AI](https://ai.google.dev/).
   - Create a `.env` file in the project root and add:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

1. **Prepare your files:**
   - Resume (TXT or PDF)
   - Job description (TXT or PDF)

2. **Run the ATS tracker:**
   ```sh
   python ATSTracker.py  
   ```

3. **Output:**
   - The tool prints your ATS score and feedback on how to optimize your resume for the job description.

## Example

```sh
python ats_tracker.py --resume resume.txt --job job.txt
```

**Sample Output:**
```
ATS Score: 78%
Missing Keywords: project management, SQL, agile
Suggestions: Add recent experience with agile teams and SQL technologies.
```

## How It Works

- Reads the resume and job description.
- Sends the content securely to Gemini AI API using your API key.
- Compares relevant skills, experience, and keywords.
- Outputs a score and suggestions for improvement.

## Security

- **Never share your API key publicly.**
- It is recommended to use environment variables or a `.env` file to keep your credentials secure.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for any improvements.

## License

This project is licensed under the MIT License.

## Contact

Created by [anupammaiti10](https://github.com/anupammaiti10)  
For questions, please open an issue or contact via GitHub.
