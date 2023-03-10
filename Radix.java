import java.util.*;

public class RadixSort {
    public static void radixSort(int[] arr) {
        // Find the maximum number to know the number of digits
        int maxNum = Arrays.stream(arr).max().getAsInt();
 
        // Do counting sort for every digit
        for (int exp = 1; maxNum / exp > 0; exp *= 10) {
            countSort(arr, exp);
        }
    }
 
    public static void countSort(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10];
        Arrays.fill(count, 0);
 
        // Store count of occurrences in count[]
        for (int i = 0; i < n; i++) {
            count[(arr[i] / exp) % 10]++;
        }
 
        // Change count[i] so that count[i] now contains
        // actual position of this digit in output[]
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }
 
        // Build the output array
        for (int i = n - 1; i >= 0; i--) {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }
 
        // Copy the output array to arr[], so that arr[] now
        // contains sorted numbers according to current digit
        for (int i = 0; i < n; i++) {
            arr[i] = output[i];
        }
    }
 
    // Main method to test the implementation
    public static void main(String[] args) {
        int[] arr = { 170, 45, 75, 90, 802, 24, 2, 66 };
 
        System.out.println("Original array: " + Arrays.toString(arr));
        radixSort(arr);
        System.out.println("Sorted array: " + Arrays.toString(arr));
    }
}
