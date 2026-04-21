// https://learn.microsoft.com/en-us/dotnet/csharp/linq/
int[] scores = [97, 92, 81, 60];

// never used IEnumerable before
// I can use LINQ within Enumerable instance???
IEnumerable<int> scoreQuery = from score in scores where score > 80 select score;

foreach (var i in scoreQuery)
{
    Console.Write(i + " ");
}

List<int> numbers = [];

foreach (int i in Enumerable.Range(1,6))
{
    numbers.Add(i);
}

Console.WriteLine(numbers.Select(row -> Console));