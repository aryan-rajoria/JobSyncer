# this file has the main server handling calls to the LLM service and feature extracting service.

""" two services with this module
1. LLM service
    a. has a prompt engineer module
    b. has a seperate queue handling
2. Feature Extractor Service
    a. does not have prompt engineering, just generate embedding
    b. store embedding into vector database.
    c. has a seperate queue handling

    all
"""