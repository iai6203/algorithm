package baekjoon_9461;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class Main {
  public static void main(String[] args) throws Exception {

    System.setIn(new FileInputStream("src/baekjoon_9461/input.txt"));
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int cases = Integer.parseInt(br.readLine());

    for (int test_case = 1; test_case <= cases; test_case++) {
      int n = Integer.parseInt(br.readLine());
      long[] cache = new long[Math.max(n + 1, 5 + 1)];

      cache[1] = 1;
      cache[2] = 1;
      cache[3] = 1;
      cache[4] = 2;
      cache[5] = 2;

      for (int i = 6; i <= n; i++) {
        cache[i] = cache[i - 1] + cache[i - 5];
      }

      System.out.println(cache[n]);
    }
  }
}
