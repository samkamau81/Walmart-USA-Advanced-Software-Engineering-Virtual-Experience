package org.example;
//time complexity o(n)
//Auxiliary space o(n)
public class Heapify {
        static void heapify(int arr[], int N, int i)
{
                int largest = i; // Initialize largest as root
                int l = 2 * i + 1; // left = 2*i + 1
                int r = 2 * i + 2; // right = 2*i + 2
                // If left child is larger than root
                if (l < N && arr[l] > arr[largest])
                        largest = l;
                // If right child is larger than largest so far
                if (r < N && arr[r] > arr[largest])
                        largest = r;
                // If largest is not root
                if (largest != i) {
                        int swap = arr[i];
                        arr[i] = arr[largest];
                        arr[largest] = swap;
                // Recursively heapify the affected sub-tree
                heapify(arr, N, largest);
                }
}
        static void buildHeap(int arr[], int N)

        {

                // Index of last non-leaf node

                int startIdx = (N / 2) - 1;

                // Perform reverse level order traversal

                // from last non-leaf node and heapify

                // each node
                for (int i = startIdx; i >= 0; i--) {

                heapify(arr, N, i);

        }

} 
        static void printHeap(int arr[], int N)

        {

                System.out.println("Array representation of Heap is:");

                for (int i = 0; i < N; ++i)

                System.out.print(arr[i] + " ");

                System.out.println();

        }



        // Driver Code 

        public static void main(String args[]) 

        {
        int arr[] = {1, 3, 5, 4, 6, 13};

        int N = arr.length;

        buildHeap(arr, N);

        printHeap(arr, N);

        }

}
