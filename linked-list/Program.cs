using System;

namespace LinkedList {
        public class Node <T> {
              
              // Data
                public T data { get; set; }  

              // Link
                public Node<T> next {get; internal set;}

              // Constructor
                public Node (T data) {
                        this.data = data;
                }
        }

        public class LinkedList {
                // properties
                public Node<T> First {get; private set;}

                public Node<T> Last {get; private set;}

                public int Count {get; private set;}

                // constructor. Not really needed
                public LinkedList() {
                        this.First = null;
                        this.Last = null;
                }
        }
}