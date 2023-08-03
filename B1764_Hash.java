import java.io.*;
import java.util.*;

public class B1764_Hash {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> map = new HashMap<>();

        for (int i = 0; i < N + M; i++) {
            String name = br.readLine();
            map.put(name, map.getOrDefault(name, 0) + 1);
        }

        ArrayList<String> answer = new ArrayList<>();
        for (HashMap.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() == 2) {
                answer.add(entry.getKey());
            }
        }

        Collections.sort(answer);
        System.out.println(answer.size());
        for (String name : answer) {
            System.out.println(name);
        }
    }
}
