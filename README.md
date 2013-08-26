
<h1>LR0 Prasing tool</h1>
<hr>

<p>
	<p>A project that implements the stages in a typical <b>LR(0)</b>
	<br>parser take a input grammar and parse the input for the grammar </p>
	<p>This is done as a part of Compiler design course.
	A parser typically parse a input string and check whether the input belongs to the grammer.
	
	LR(0) parser - left to right scanning of the input and rightmost derivation of grammar symbols.
	</p>
	
	<h3>LR(0) parser composed of five stages.</h3>
	 <ul>
	 	<li> finding the FIRST set of grammar symbols. </li>
	 	<li>  finding the FOLLOW set of grammar symbols. </li>
	 	<li> from initial state apply the closure rule to find all the possible input states. </li>
	 	<li>  construct a parsing table from states obtained by applying closure. </li>
	 	<li> parse the input string by using the parsing table.</li>
	 </ul>
	
	All the above stages are implemented and the GUI is provided making it as a tool for learning the<b> LR(0) </b>parsing. 
	
	<br>
	Each of the above stage outputs can be seen at a click of corresponding button.
	
	language used: python 2.7 and PyQt4 frame work.
	<h3>To execute </h3>
	<b>$ python Gui_mai.py</b>
	<hr>
	<h2> Tool </h2>
	<img src="https://dl.dropboxusercontent.com/u/109288873/LR0.png">
</p>

