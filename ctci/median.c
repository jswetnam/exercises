// Find the running median of a list of numbers.

// First thought: keep a sorted list, and return the median when requested.
// I'll use HeapSort since the optimal solution uses a Min and max heap,
// and I can reuse the implementation.

// Tags: Heaps, Sorting


#include <stdlib.h>
#include <stdio.h>

#define MAX_HEAP_SIZE 100

typedef struct {
int* values;
int size; // Number of elements currently in the heap.
} MinHeap;

MinHeap* NewMinHeap() {
  MinHeap* new_heap = malloc(sizeof(MinHeap));
  new_heap->values = malloc(sizeof(int) * MAX_HEAP_SIZE);
  return new_heap;
}

// Return the index of the parent of the element at index i.
int Parent(int i) { return i / 2; }

// Return the index of the left child of the element at index i
int LeftChild(int i) { return 2 * i; }

// Return the index of the right child of the element at index i
int RightChild(int i) { return 2 * i + 1; }

// Push a new element onto the heap.
void Push(MinHeap* heap, int new_element) {
  heap->values[heap->size] = new_element;
  heap->size++;
  // Preserve the MinHeap property.
  // While A[i]'s parent is > A[i], swap A[i] with its parent.
  for (int i = heap->size - 1;
       i > 0 && heap->values[Parent(i)] > heap->values[i];
       i = Parent(i)) {
    int tmp = heap->values[Parent(i)];
    heap->values[Parent(i)] = heap->values[i];
    heap->values[i] = tmp;
  }
}

void MinHeapify(MinHeap* heap, int root) {
  if (root > heap->size - 1) { return; }
  if (heap->values[root] > heap->values[LeftChild(root)]) {
    int tmp = heap->values[root];
    heap->values[root] = heap->values[LeftChild(root)];
    heap->values[LeftChild(root)] = tmp;
    MinHeapify(heap, LeftChild(root));
  }
  if (heap->values[root] > heap->values[RightChild(root)]) {
    int tmp = heap->values[root];
    heap->values[root] = heap->values[RightChild(root)];
    heap->values[RightChild(root)] = tmp;
    MinHeapify(heap, RightChild(root));
  }
}

int RemoveMin(MinHeap* heap) {
  int min = heap->values[0];
  heap->values[0] = heap->values[heap->size - 1];
  heap->size--;
  MinHeapify(heap, 0);
  return min;
}

// Return the Minimum value of the heap.
int MinValue(MinHeap* heap) {
  return heap->values[0];
}

int main() {
  MinHeap* heap = NewMinHeap();
  for (int i = 10; i > 0; --i) {
    Push(heap, i);
    printf("Min Value: %d\n", MinValue(heap));
  }
  while (heap->size > 0) {
    int min = RemoveMin(heap);
    printf("Removed min value: %d.  Size is now %d.", min, heap->size);
  }
}

