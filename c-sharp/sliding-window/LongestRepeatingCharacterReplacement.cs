int[] s = "ABAB";
int k = 2;
int expected = 4;
var counts = new int[26];
int left = 0;

// determine the purpose of maxFreq and maxLength in the context of sliding window
int maxFeq = 0, maxLength = 0;

for (int right = 0; right < s.Length; right++)
{
    // this is the currentIndex based on the counts array
    int currentIndex = s[right] - 'A';
    counts[currentIndex]++;

    // why maxFreq?
    maxFeq = Math.Max(maxFeq, counts[currentIndex]);

    while ((right - left + 1) - maxFeq > k)
    {
        counts[s[left] - 'A']--;
        left++;       
    }


}