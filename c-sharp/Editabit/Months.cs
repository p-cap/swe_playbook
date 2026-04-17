

Console.Write("Please enter base: ");
int myBase = Convert.ToInt32(Console.ReadLine());
Console.Write("Please enter expornent: ");
int myExpoenent = Convert.ToInt32(Console.ReadLine());
int myResult = 1;

for (int i = 0; i < myExpoenent; i++)
{
    myResult *= myBase;
}
Console.WriteLine($"The result is: {myResult}");


static void Edabit2()
{
    Random rand = new();
    int myArrayLength = 10;
    int[] myArray = new int[myArrayLength];

    for (int i = 0; i < myArrayLength; i++)
    {
        myArray[i] = rand.Next(1, 100);
        Console.Write($"{myArray[i]}, ");
    }
    Console.WriteLine();
    Array.Sort(myArray);
    foreach (int i in myArray)
    {
        Console.Write($"{i}, ");
    }
    // Console.WriteLine();
    Console.WriteLine($"\nThe smallest number in the {myArray} is {myArray[0]}");
    Console.WriteLine($"The largest number in the {myArray} is {myArray[myArrayLength - 1]}");

}

static void Edabit()
{
    Dictionary<int, string> numToMonths = new();
    string[] months = { "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" };
    for (int i = 1; i < 13; i++)
    {
        numToMonths[i] = months[i - 1];
    }

    Console.Write("Enter a number month: ");
    if (int.TryParse(Console.ReadLine(), out int selectedNumber))
    {
        Console.WriteLine(numToMonths[selectedNumber]);
    }
    else
    {
        Console.WriteLine("Please enter values 1 through 12");
    }
}