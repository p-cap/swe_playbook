int[][] intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]];
int[] newInterval = [4,8];
List<int[]> result = [];

int i = 0;
int n = intervals.Length;

// Add all intervals before newInterval
while (i < n && intervals[i][1] < newInterval[0])
{
    result.Add(intervals[i]);
    i++;
}



// Merge newInterval and intervals comparing their elements
while (i < n && intervals[i][0] <= newInterval[1])
{
    newInterval[0] = Math.Min(newInterval[0], intervals[i][0]);
    newInterval[1] = Math.Min(newInterval[1], intervals[i][1]);
    i++;
}

result.Add(newInterval);

while (i < n)
{
    result.Add(intervals[i]);
    i++;
}

// let's use LINQ
var output = string.Join(", ", result.Select(row => string.Join(", ", row)));
Console.WriteLine(output);