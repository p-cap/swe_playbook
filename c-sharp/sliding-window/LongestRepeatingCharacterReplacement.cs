string s = "ABAB";
int k = 2;
int expected = 4;
// stores char frequency
var counts = new int[26];
int left = 0;
// maxFreq takes the most char count
int maxFreq = 0; 
// returns the maxLength
int maxLength = 0;

for (int right = 0; right < s.Length; right++)
{
    int currentIndex = s[right] - 'A';
    counts[currentIndex]++;
    // checks the char with the highest number of char
    maxFreq = Math.Max(maxFreq, counts[currentIndex]);

    // checks if the window is over k
    while ((right - left + 1) - maxFreq > k)
    {
        counts[s[left] - 'A']--;
        left++;
    }
    maxLength = Math.Max(maxLength, right - left + 1);
}

Console.WriteLine(maxLength);