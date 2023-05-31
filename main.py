#this is version i worked on long ago 
#I'll be updating the actual webpage for this visualizer soon

import tkinter as tk

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeVisualizer:
    def __init__(self):
        self.root = None

        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack()

        self.insert_button = tk.Button(self.window, text="Insert Node", command=self.insert_node)
        self.insert_button.pack()

        self.delete_button = tk.Button(self.window, text="Delete Node", command=self.delete_node)
        self.delete_button.pack()

        self.window.mainloop()

    def insert_node(self):
        top = tk.Toplevel(self.window)
        top.title("Insert Node")

        label = tk.Label(top, text="Enter the node value:")
        label.pack()

        entry = tk.Entry(top)
        entry.pack()

        ok_button = tk.Button(top, text="OK", command=lambda: self.process_insert_input(top, entry))
        ok_button.pack()

    def process_insert_input(self, top, entry):
        value = int(entry.get())
        self.root = self._insert(self.root, value)
        self.canvas.delete("all")
        self.draw_tree(self.root, 400, 50, 200)
        top.destroy()

    def delete_node(self):
        top = tk.Toplevel(self.window)
        top.title("Delete Node")

        label = tk.Label(top, text="Enter the node value to delete:")
        label.pack()

        entry = tk.Entry(top)
        entry.pack()

        ok_button = tk.Button(top, text="OK", command=lambda: self.process_delete_input(top, entry))
        ok_button.pack()

    def process_delete_input(self, top, entry):
        value = int(entry.get())
        self.root = self._delete(self.root, value)
        self.canvas.delete("all")
        self.draw_tree(self.root, 400, 50, 200)
        top.destroy()

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def _delete(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_minimum(node.right)
                node.value = successor.value
                node.right = self._delete(node.right, successor.value)
        return node

    def _find_minimum(self, node):
        while node.left:
            node = node.left
        return node

    def draw_tree(self, node, x, y, h_gap):
        if node:
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white")
            self.canvas.create_text(x, y, text=str(node.value))
            if node.left:
                x_left = x - h_gap
                y_left = y + 50
                self.canvas.create_line(x, y, x_left, y_left)
                self.draw_tree(node.left, x_left, y_left, h_gap // 2)
            if node.right:
                x_right = x + h_gap
                y_right = y + 50
                self.canvas.create_line(x, y, x_right, y_right)
                self.draw_tree(node.right, x_right, y_right, h_gap // 2)

# Creates an instance of the binary tree visualizer
binary_tree_visualizer = BinaryTreeVisualizer()
