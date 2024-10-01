Here is an example of a multiagent system built with crewai framework.

Agents and tasks are described in **agents.yaml** and **tasks.yaml** respectively. The files are located in `src > rai_crew > config`.
`rai_crew` folder contains **crew.py** and **main.py** files. **crew.py** contains the definition of the crew itself and the tools used. **main.py** contains code to run the crew and obtain a result.

The pipeline of this example is the following: <br>
•	there is a company (Google for the sake of demonstration), which created a product (described in **product_desc.txt**) and wants to make sure it is aligned perfectly with the company’s values;<br>
•	the company hands its product description to the system;<br>
•	the first agent (with a RAG tool) performs search on the internet to collect more information about the company, scrapes and saves everything available;<br>
•	the second agent analyzes the obtained information and formats it into a table with values and short descriptions for each value;<br>
•	the third agent reads the product description and the set of values provided by the second agent and writes a strategy to align the product with the values.<br>

The result is written to **final_strategy.txt** file (not a necessary step, but it demonstrates the flexibility of the multiagent system).
