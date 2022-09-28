## Longest-Compound-Words
Impledge Technologies interview challenge 2022
The problem statement can be found in the [Exercise_Fresher_Word_Problem.pdf](https://github.com/SoumadipDey/Longest-Compound-Words/blob/main/Exercise_Fresher_Word_Problem.pdf "Exercise_Fresher_Word_Problem.pdf") file.

## Code Execution Procedure
**Requires Python version 3.7 or newer to be Installed**

 1. Download / Clone the repo into your machine.
 2. Open the `Solution.py` file and scroll to the code segment with the comment 
 `#Change the file path here`.
 3. Enter the relative path of the text file for the input w.r.t the solution file as a parameter to `sol.buildTrie()`.
 4. Execute the file `Solution.py`.


## A brief study of the problem

 - Compounded words are the words formed using one or more of the valid words only in the selected file. 
 - Since the files are already sorted alphabetically and only contain one word per line some of the the valid words that compose the compounded words are bound to come before the compounded word itself.
 - Thus the compounded word can be thought of as the combination of some of the the words that have been already read i.e. -> prefix, and a suffix.
 - If there is a situation where some character which is not the part of any valid word in the file but occours within any position of the word currently being read. Then the word can not be considered as a compounded word.

## Approach and Algorithm

While researching for this problem , many solutions and related problems were observed out of which the **trie based approach** was the most easily understandable , effecient and widely used one. So that particular approach has been selected and modified for solving the given problem

The algorithm for the solution :
> Step 1. Build the trie by reading every word one by one from the selected file.
> 
>  Step 2. While building the trie also build a dequeue which contains `<word,suffix>` pairs if any w.r.t the previously existing valid words in the trie.
>  
> Step 3. Initialize the `longest`, `second_longest`, and `max_length` variables.
>
> Step 4. Repeat untill the queue is empty, POP the `<word,suffix>` pairs from the dequeue.
> 
> > i) Check if the suffix of the word contains any valid word i.e. `prefix` from the trie and if `length (word) > max_length` , set 
> `second_longest = longest` , 
> `longest = word` and 
> `max_length = length(word)`.
> 
> >ii) Else get all the prefixes of the current suffix of the word , and find the new suffixes w.r.t each and every prefix length. Append the new `<word,suffix>` pairs into the deque. 
> 
> Step 5. Return the longest and second_longest words

## Results:
1) Output  for File: Input_01.txt


![Output  for File: Input_01.txt](/Output_1.png)

2) Output  for File: Input_02.txt


![Output  for File: Input_02.txt](/Output_2.png)
