int[] myArray = [4, 5, 8, 2];

// How does the PriorityQueue work?
// By default, PriorityQueue tracks elements via Min-Priority Queue
PriorityQueue<int,int> _minHeap = new();

// Priority, the second paramter drives the order of the queue
// in this case, the lower the priority, it will come first
foreach (int val in myArray)
{
    _minHeap.Enqueue(val,val);    
}

// The code below will help console the queue 
var sortedSnapshot = _minHeap.UnorderedItems.OrderBy(x => x.Priority);

foreach (var item in sortedSnapshot)
{
    Console.WriteLine($"Priority: {item.Priority} | Value: {item.Element}");
}