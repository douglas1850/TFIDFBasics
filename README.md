# TFIDFBasics
Created program based on a blog post about using Term Frequency-Inverse Document Frequency to determine which words are most imoportant

The basic premise of Term Frequency-Inverse Document Frequency is to observe the frequency of words/terms in a document and then see how often those terms occur in other documents. Words like "the", "is", etc will occur in most documents so they will be weighted less.

This will help determine which terms are most important to that document. Words that appear in multiple documents are scaled down. Words that appear in a single document are scaled up. 
