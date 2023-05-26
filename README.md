# bt-visualizer
this is a Python implementation of a binary tree visualizer using the Tkinter library. It allows you to insert nodes into the binary tree and delete nodes from it. The visual representation of the binary tree is drawn on a canvas using circles (ovals) to represent nodes and lines to represent connections between nodes.

The code defines two classes: Node and BinaryTreeVisualizer. The Node class represents a single node in the binary tree, storing a value and references to its left and right children. The BinaryTreeVisualizer class is responsible for creating the GUI, handling user input for inserting and deleting nodes, and drawing the binary tree on the canvas.

The BinaryTreeVisualizer class uses Tkinter to create a window, canvas, and buttons for user interaction. It has methods for inserting and deleting nodes, as well as auxiliary methods for manipulating the binary tree structure. The draw_tree method recursively draws the binary tree on the canvas.
