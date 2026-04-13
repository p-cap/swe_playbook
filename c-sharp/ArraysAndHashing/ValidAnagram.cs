string s = "anagram";
string t = "nagaram";

Dictionary<char, int> counts = new();

foreach (char c in s) {
    // TryGetValue(....) receives the parameter and recturns the count if the key has no value
    counts.TryGetValue(c, out int count);
    counts[c] = count + 1;
}

foreach (char c in t) {
    if (!counts.TryGetValue(c, out int currentCount) || currentCount == 0) {
        Console.WriteLine(false);
        break;
    }
    counts[c] = currentCount - 1;
}

Console.WriteLine(true);