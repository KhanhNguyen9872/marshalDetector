# marshalDetector

A powerful, native Python hook designed to detect and monitor `marshal.loads` calls. This project provides a security-focused mechanism to audit or intercept serialized Python objects during the unmarshalling process.

## Features

- **Native Hooks**: Implemented as high-performance C-extensions (`.pyd`).
- **Seamless Integration**: Simply import `marshalDetector` to activate the detection hook.
- **Wide Compatibility**: Pre-built binaries for Windows (x64) across Python versions 3.9 up to 3.15.
- **Auditing**: Ideal for detecting potentially malicious payloads in `marshal` data.

## Usage

To integrate the detector into your workflow, simply import it at the beginning of your script:

```python
## modify your marshal.loads here



## let's detect it
import marshalDetector
```

## Supported Versions

This repository includes pre-built binaries for the following Python versions on Windows x64:

- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14
- Python 3.15

## Installation

Ensure you have the appropriate `.pyd` file for your Python version in your project directory or `PYTHONPATH`.

---
*Built with security and performance in mind.*