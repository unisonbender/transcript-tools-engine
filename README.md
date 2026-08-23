# Transcript Tools Engine

A Python engine for converting vtt caption files into clean, customizable text transcripts.

## Project Goals

The initial goal is to build a WebVTT parser using Python's standard library.

The engine will eventually be able to:

- Read WebVTT caption files
- Extract spoken text from caption data
- Remove timestamps and caption metadata
- Clean and normalize transcript text
- Generate readable paragraphs
- Allow configurable paragraph length limits
- Return transcript text for use by web-based tools

## Why This Project Exists

Transcript and caption files are useful for accessibility, but they are not always convenient to read or reuse as ordinary text.
This tool aims to make it easy to convert caption data into clean, readable transcripts without requiring specialized software. The resulting transcripts can then be used by end users for further editing, publishing, or production.

This project is also being built as a computer science and Python learning project. The core parsing and text-processing functionality will be implemented using Python's built-in features rather than third-party caption-processing libraries.

## Current Status

Early development.

The first milestone is a standalone Python program that can read a WebVTT file and extract its caption text.

## Planned Development

The project will be developed incrementally, beginning with basic WebVTT parsing and expanding into transcript cleaning, paragraph formatting, testing, additional caption formats, and eventual integration into broader applications toolsets.

## License

This project is licensed under the MIT License.